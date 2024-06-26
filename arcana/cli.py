from arcanalib import Filter, triplets, invert, lift
from arcana import templates
from openai import OpenAI
import re
import time
import os
import json
from tqdm import tqdm
from collections import Counter


def remove_java_comments(java_source):
	# Regular expression to match Java comments (both single-line and multi-line)
	pattern = r"(//.*?$)|(/\*.*?\*/)"

	# Remove comments using the regular expression
	java_source_without_comments = re.sub(
		pattern, 
		"", 
		java_source, 
		flags=re.MULTILINE | re.DOTALL
	)

	return java_source_without_comments.strip()


def sentence(s):
	'''
	Capitalize the first letter of a string `s` and ensures that the string
	ends with a period (if it's not already a sentence-ending punctuation).
	'''
	t = s.strip()
	if t[-1] in '.?!…~–—':
		return f'{t[0].upper()}{t[1:]}'
	else:
		return f'{t[0].upper()}{t[1:]}.'


def lower1(s):
	if not s:
		return s
	return s[0].lower() + s[1:]



def prettify_json(obj):
	pretty_json = json.dumps(obj, indent='\t')
	return pretty_json




class MetricsFilter(Filter):
	def process(self, data):
		parents = {e['source']:e['target'] for e in invert(data.edges['contains'])}
		dependency_profiles = dict()
		if 'calls' in data.edges:
			calls = data.edges['calls']
		else:
			calls = lift(data.edges['hasScript'], data.edges['invokes'], 'calls')
		for edge in calls:

			source_id = edge['source']
			target_id = edge['target']

			if not source_id in dependency_profiles:
				dependency_profiles[source_id] = list()
			if not target_id in dependency_profiles:
				dependency_profiles[target_id] = list()
			
			if parents[source_id] != parents[target_id]:
				dependency_profiles[source_id].append('out')
				dependency_profiles[target_id].append('in')

		dependency_profiles = {id:Counter(profile) for id, profile in dependency_profiles.items()}
  
		def dependency_profile_category(inn,out):
			if inn==0 and out>0:
				return "outbound"
			elif inn>0 and out==0:
				return "inbound"
			elif inn>0 and out>0:
				return "transit"
			else:
				return "hidden"

		for id, profile in dependency_profiles.items():
			data.nodes[id]['properties']['dependencyProfile'] = dependency_profile_category(profile['in'],profile['out']) 
		
		return data

class LLMFilter(Filter):
	def process(self, data):

				
		def describe(node):
			keys = 'description,reason,howToUse,howItWorks,assertions,roleStereotype,layer'.split(',')
			desc = ''
			for key in keys:
				if key in node['properties']:
					desc += f"**{key}**: {str(node['properties'][key])}. "
			return desc


		project_name = self.config['project']['name']
		project_desc = self.config['project']['desc']

		openai_client_args = dict()

		if 'apikey' in self.config['openai']:
			openai_client_args['api_key'] = self.config['openai']['apikey']
		if 'apibase' in self.config['openai']:
			openai_client_args['base_url'] = self.config['openai']['apibase']
		if 'model' in self.config['openai']:
			model = self.config['openai']['model']
		else:
			model = "gpt-3.5-turbo"

		client = OpenAI(**openai_client_args)

		methods = sorted(triplets(data.edges['contains'], data.edges['hasScript']))
		classes = sorted({(pkg, clz) for pkg, clz, _ in methods})
		packages = sorted({pkg for pkg, _ in classes})

		hierarchy = {
			pkg_id: {
				cls_id: [
					met_id for _, c, met_id in methods if c == cls_id
				] for p, cls_id in classes if p == pkg_id
			} for pkg_id in packages
		}

		timestr = time.strftime("%Y%m%d-%H%M%S")

		with open(f'arcana-{timestr}.jsonl', 'a', encoding="utf-8") as file:

			try:
				for pkg_id, pkg_data in tqdm(hierarchy.items(), desc="Processing packages", position=0):
					# file.write(f'# {pkg_id}\n')
					package = data.nodes[pkg_id]

					for cls_id, cls_data in tqdm(pkg_data.items(), desc="Processing classes", position=1, leave=False):
						# file.write(f'\t* {cls_id}\n')
						clasz = data.nodes[cls_id]

						class_name = clasz['properties']['qualifiedName']
						class_kind = clasz['properties']['kind']
						if class_kind == 'enumeration':
							class_kind = 'enum'
						elif class_kind == 'abstract':
							class_kind = 'abstract class'

						for met_id in tqdm(cls_data, desc='Processing methods', position=2, leave=False):

							if 'description' not in data.nodes[met_id]['properties'] \
									or not data.nodes[met_id]['properties']['description']:

								# file.write(f'\t\t- {met_id}\n')

								method = data.nodes[met_id]

								method_name = method['properties']['simpleName']
								method_src = remove_java_comments(method['properties']['sourceText'])

								prompt = templates.script_analysis.format(
									op_name=method_name,
									struct_kind=class_kind,
									struct_name=class_name,
									op_src=method_src)
								# file.write('\t\t\t' + prompt.replace('\n', '\n\t\t\t') + "\n")
								# file.write("\n")
								if self.config.dry_run:
									pass
								else:
									response = None
									try:
										response = client.chat.completions.create(
											model=model,
											response_format={"type": "json_object"},
											messages=[
												{"role": "user", "content": prompt},
												# {"role": "assistant","content": '{ "What": "'}
											],
											max_tokens=1024,  # stop=[". "],
											temperature=0)
										description = response.choices[0].message.content
									except:
										description = '{}'
										print(response)

									try:
										description = json.loads(description)
									except:
										description = dict()
		
									file.write(json.dumps({'data': {'id': method['id'], 'labels': method['labels'], 'properties': description}}))

									# file.write('\t\t\t' + prettify_json(description).replace('\n', '\n\t\t\t') + "\n")
									# file.write("\n")
									for key in description:
										if key.endswith('Reason'):
											pass
										elif lower1(key) == 'parameters':
											for parameter in description[key]:
												param_id = method['id'] + '.' + parameter['name']
												if param_id in data.nodes:
													data.nodes[param_id]['properties']['description'] = parameter.get(
														'description', None)
										else:
											method['properties'][lower1(key)] = description[key]

							if os.path.exists('stop'):
								raise StopIteration

						ancestors = {
							edge['target']
							for edge in data.edges['specializes']
							if edge['source'] == cls_id
						}
						fields = {
							edge['target']
							for edge in data.edges['hasVariable']
							if edge['source'] == cls_id
						}
						fields = [
							' '.join(remove_java_comments(data.nodes[field]['properties']['sourceText']).split())
							for field in fields
						]

						prompt = templates.structure_analysis.format(
							struct_type=class_kind,
							struct_name=class_name,
							ancestors="\n".join([
								f"- `{ancestor}`"
								for ancestor in ancestors
							]) if ancestors else "(none)",
							fields="\n".join([
								f"- `{field}`"
								for field in fields
							]) if fields else "(none)",
							methods="\n".join([
								f"- `{data.nodes[met_id]['properties']['simpleName']}`: {describe(data.nodes[met_id])}"
								for met_id in cls_data
							])) if cls_data else "(none)"

						# file.write('\t\t' + prompt.replace('\n', '\n\t\t') + "\n")
						# file.write("\n")
						if self.config.dry_run:
							pass
						else:
							response = None
							try:
								# file.write(prompt + "\n")
								response = client.chat.completions.create(
									model=model,
									response_format={"type": "json_object"},
									messages=[
										{"role": "user", "content": prompt},
										# {"role": "assistant", "content": "{"}
									],
									max_tokens=1024,
									# stop=[". "],
									temperature=0
								)
								description = response.choices[0].message.content
							except:
								description = "{}"
								# file.write(str(response) + "\n")

							try:
								description = json.loads(description)
							except:
								description = dict()
	
							file.write(json.dumps({'data': {'id': clasz['id'], 'labels': clasz['labels'], 'properties': description}}))

							# file.write('\t\t' + prettify_json(description).replace('\n', '\n\t\t') + "\n")
							# file.write("\n")
							for key in description:
								if key.endswith('Reason'):
									pass
								else:
									clasz['properties'][lower1(key)] = description[key]

						file.flush()
						if os.path.exists('stop'):
							raise StopIteration

					prompt = templates.component_analysis.format(
						pkg_name=package['properties']['qualifiedName'],
						classes="\n".join([
							f"- {data.nodes[cls_id]['properties']['kind']} `{data.nodes[cls_id]['properties']['qualifiedName']}`: "
							f"{describe(data.nodes[cls_id])}"
							for cls_id, _ in pkg_data.items()
						])
					)

					# file.write('\t' + prompt.replace('\n', '\n\t') + "\n")
					# file.write("\n")
					if self.config.dry_run:
						pass
					else:
						response = None
						try:
							response = client.chat.completions.create(
								model=model,
								response_format={"type": "json_object"},
								messages=[
									{"role": "user", "content": prompt},
									# {"role": "assistant", "content": f"The package `{package_name}` is a package that"}
								],
								max_tokens=1024,
								# stop=[". "],
								temperature=0)
							description = response.choices[0].message.content
						except:
							description = '{}'
							# file.write(f'{str(response)}\n')

						try:
							description = json.loads(description)
						except:
							description = dict()
	
						file.write(json.dumps({'data': {'id': package['id'], 'labels': package['labels'], 'properties': description}}))

						# file.write('\t' + prettify_json(description).replace('\n', '\n\t') + "\n")
						# file.write("\n")
						for key in description:
							if not key.endswith('Reason'):
								package['properties'][lower1(key)] = description[key]
					if os.path.exists('stop'):
						raise StopIteration

			except StopIteration:
				pass

		return data
