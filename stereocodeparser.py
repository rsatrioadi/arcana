import xml.etree.ElementTree as ET
import sys
import json

def get_parameter_types(parameter_list_element, namespaces):
    types = []
    for parameter in parameter_list_element.findall('src:parameter/src:decl/src:type/src:name', namespaces):
        types.append(''.join(parameter.itertext()).split('<')[0])
    return ','.join(types)

def parse_class_element(class_element, current_package_name, parent_class_id, namespaces, result):
    class_name_element = class_element.find('src:name', namespaces)
    if class_name_element is not None:
        class_name = class_name_element.text
        if parent_class_id:
            class_id = f"{parent_class_id}${class_name}"
        else:
            class_id = f"{current_package_name}.{class_name}"

        result[class_id] = {
            "id": class_id,
            "labels": ["Structure"],
            "properties": {
                "stereotypes": []
            }
        }

        # Extract class stereotypes
        class_stereotype = class_element.get('{http://www.srcML.org/srcML/stereotype}stereotype')
        if class_stereotype:
            result[class_id]["properties"]["stereotypes"].append(class_stereotype)

        # Extract functions directly under class/block
        block_element = class_element.find('src:block', namespaces)
        if block_element is not None:
            for function_element in block_element.findall('src:function', namespaces):
                func_name_element = function_element.find('src:name', namespaces)
                param_list_element = function_element.find('src:parameter_list', namespaces)
                if func_name_element is not None and param_list_element is not None:
                    func_name = func_name_element.text + '(' + get_parameter_types(param_list_element, namespaces) + ')'
                    func_id = f"{class_id}.{func_name}"
                    result[func_id] = {
                        "id": func_id,
                        "labels": ["Operation"],
                        "properties": {
                            "stereotypes": []
                        }
                    }

                    # Extract function stereotypes
                    func_stereotype = function_element.get('{http://www.srcML.org/srcML/stereotype}stereotype')
                    if func_stereotype:
                        result[func_id]["properties"]["stereotypes"].extend(func_stereotype.split())

            # Extract constructors directly under class/block
            for constructor_element in block_element.findall('src:constructor', namespaces):
                param_list_element = constructor_element.find('src:parameter_list', namespaces)
                if param_list_element is not None:
                    constr_signature = '(' + get_parameter_types(param_list_element, namespaces) + ')'
                    constr_id = f"{class_id}{constr_signature}"
                    result[constr_id] = {
                        "id": constr_id,
                        "labels": ["Constructor"],
                        "properties": {
                            "stereotypes": []
                        }
                    }

                    # Extract constructor stereotypes
                    constr_stereotype = constructor_element.get('{http://www.srcML.org/srcML/stereotype}stereotype')
                    if constr_stereotype:
                        result[constr_id]["properties"]["stereotypes"].extend(constr_stereotype.split())

        # Recursively process nested classes within this class
        for nested_class_element in block_element.findall('src:class', namespaces):
            parse_class_element(nested_class_element, current_package_name, class_id, namespaces, result)


def parse_xml(xml_content):
    # Register namespaces to handle them properly
    namespaces = {
        'src': 'http://www.srcML.org/srcML/src',
        'st': 'http://www.srcML.org/srcML/stereotype'
    }

    tree = ET.ElementTree(ET.fromstring(xml_content))
    root = tree.getroot()

    result = {}

    # Iterate over each <unit> element
    for unit_element in root.findall('src:unit', namespaces):
        package_element = unit_element.find('.//src:package/src:name', namespaces)
        if package_element is not None:
            package_name = ''.join(package_element.itertext())

            # Extract top-level class information within this unit
            for class_element in unit_element.findall('src:class', namespaces):
                parse_class_element(class_element, package_name, None, namespaces, result)

    return result

def main():
    xml_content = sys.stdin.read()
    result = parse_xml(xml_content)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
