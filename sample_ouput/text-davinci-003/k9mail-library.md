# package `com.fsck.k9.mail`

This package  provides an interface for accessing and manipulating email messages stored on a mail server.

This package contains the following class(es):

## class `com.fsck.k9.mail.MessagingException`

This class  provides utility methods for determining whether an email message failed permanently or not.

This class contains the following public method(s):

- `isPermanentFailure()`  returns whether a MessagingException is a permanent failure or not.
- `setPermanentFailure(boolean)`  sets a flag indicating whether the exception is a permanent failure.

## interface `com.fsck.k9.mail.K9MailLib$DebugStatus`

This interface  "provides methods to check the status of debugging sensitive information".

This class contains the following public method(s):

- `debugSensitive()`  returns whether debugging sensitive information is enabled or not.
- `enabled()`  checks if debugging is enabled.

## class `com.fsck.k9.mail.K9MailLib$DefaultDebugStatus`

This class  "facilitates debugging by providing methods to control the enabled state and sensitivity of debug output."

This class contains the following public method(s):

- `debugSensitive()`  returns a boolean value based on the value of the variable `sensitive`.
- `enabled()`  returns a boolean indicating whether debugging is enabled or not.
- `setEnabled(boolean)`  sets the enabled state of an object.
- `setSensitive(boolean)`  sets the sensitivity of a debug status to a specified value.

## interface `com.fsck.k9.mail.Part`

This interface  provides methods to write, access, and modify email parts.

This class contains the following public method(s):

- `getContentType()`  returns the content type of the message part.
- `getBody()`  "retrieves the proper body for the Part object".
- `setServerExtra(java.lang.String)`  sets the server's extra information associated with the mail part.
- `getHeader(java.lang.String)`  returns a String array of headers with a given name.
- `getServerExtra()`  returns a string representing any information sent with the part from the server.
- `addHeader(java.lang.String,java.lang.String)`  adds a header to the outgoing message with a specified name and value.
- `getContentId()`  returns the content ID of the part.
- `setBody(com.fsck.k9.mail.Body)`  sets the body of the mail Part object.
- `getDisposition()`  returns the MIME Content-Disposition header of the part in question.
- `addRawHeader(java.lang.String,java.lang.String)`  adds a raw header to an email part.
- `setHeader(java.lang.String,java.lang.String)`  sets a specified header and value pair for a given email part.
- `writeTo(java.io.OutputStream)`  writes the contents of an email partition to an output stream.
- `removeHeader(java.lang.String)`  removes the given header from the Part.
- `isMimeType(java.lang.String)`  checks if the given MIME type is the MIME type of the Part object.
- `getMimeType()`  returns the MIME type of the email part.
- `writeHeaderTo(java.io.OutputStream)`  writes the header of a message to an `OutputStream`.

## abstract class `com.fsck.k9.mail.Transport`

This abstract class  provides a set of methods to open, close, and send a message via the transport layer of the K-9 Mail Android app.

This class contains the following public method(s):

- `open()`  opens a connection for the transport.
- `close()`  closes the transport connection.
- `sendMessage(com.fsck.k9.mail.Message)`  sends a given message via the transport layer of the K-9 Mail Android app.

## abstract class `com.fsck.k9.mail.Store`

This abstract class  provides methods for checking email store settings, getting folders, sending and copying messages, and checking push and seen flag support.

This class contains the following public method(s):

- `isCopyCapable()`  returns whether copying is supported by the Store.
- `getFolder(java.lang.String)`  gets a `com.fsck.k9.mail.Folder` object based on a provided folder name.
- `isExpungeCapable()`  returns whether the store is capable of expunging messages.
- `getPusher(com.fsck.k9.mail.PushReceiver)`  returns a `Pusher` object associated with the given `PushReceiver` object.
- `isSendCapable()`  returns `false`.
- `isSeenFlagSupported()`  returns a boolean indicating whether the seen flag is supported.
- `getPersonalNamespaces(boolean)`  retrieves a list of personal folders on the mail store.
- `sendMessages(java.util.List)`  allows users to send a list of messages.
- `checkSettings()`  checks the settings of the mail store.
- `isMoveCapable()`  returns `false` to indicate that the store is not capable of moving messages.
- `isPushCapable()`  returns whether push capability is enabled or not.

## class `com.fsck.k9.mail.Address`

This class  provides methods to parse, encode, pack, unpack, and manipulate email addresses and associated personal details.

This class contains the following public method(s):

- `pack(com.fsck.k9.mail.Address[])`  packs an array of addresses into a string in a specific format for easy reading and parsing.
- `parse(java.lang.String)`  takes a String of comma-separated addresses in RFC-822 format and returns an array of Address objects representing each address.
- `toEncodedString(com.fsck.k9.mail.Address[])`  creates a single string of comma separated encoded strings from a given array of `Address` objects.
- `hashCode()`  calculates a unique identifier (the hash code) for the given address that is based on its address and personal values.
- `getHostname()`  returns the hostname from an email address by extracting it from the string after an "@" character.
- `quoteAtoms(java.lang.String)`  checks if a given string consists of atoms, and if so, returns it, otherwise, it returns the string as a quoted string.
- `getPersonal()`  returns the personal portion of an email address.
- `equals(java.lang.Object)`  checks if two `Address` objects are equal by comparing their personal and address fields.
- `toString(com.fsck.k9.mail.Address[])`  takes an array of `com.fsck.k9.mail.Address` objects and returns a `String` of all of the addresses separated by commas.
- `getAddress()`  gets the address.
- `unpack(java.lang.String)`  parses a string that contains a list of email address and personal details and returns an array of `com.fsck.k9.mail.Address` objects representing each email address.
- `parseUnencoded(java.lang.String)`  turns a comma separated list of readable email addresses into an array of encoded RFC-822 addresses.
- `toString()`  returns a String representation of the object which contains the personal name and address if they exist, or only the address otherwise.
- `toEncodedString()`  returns an encoded version of the mailbox address if personal name is provided, otherwise it just returns the address.
- `setPersonal(java.lang.String)`  sets the `mPersonal` parameter of the `Address` object to the value of the `newPersonal` parameter or `null` if `newPersonal` is an empty string.
- `setAddress(java.lang.String)`  sets the address of an Address object.

## class `com.fsck.k9.mail.Authentication`

This class  provides various authentication methods, including XOAUTH, CRAM-MD5, and base64 encoding.

This class contains the following public method(s):

- `computeXoauth(java.lang.String,java.lang.String)`  computes an XOAUTH authentication string from a username and an authToken, and returns it as a Base64-encoded string.
- `computeCramMd5Bytes(java.lang.String,java.lang.String,byte[])`  encodes a username, password and nonce in CRAM-MD5 and returns the encoded credentials as a base64 byte array.
- `computeCramMd5(java.lang.String,java.lang.String,java.lang.String)`  uses the given username, password, and nonce to generate a CRAM-MD5 response.

## interface `com.fsck.k9.mail.Body`

This interface  provides methods for writing, retrieving, and setting the content transfer encoding for an email message body.

This class contains the following public method(s):

- `writeTo(java.io.OutputStream)`  writes the body's data to a given output stream in a transfer-encoded form.
- `getInputStream()`  retrieves the raw data of the body without any applied transfer encoding.
- `setEncoding(java.lang.String)`  sets the content transfer encoding for a body of an email message.

## class `com.fsck.k9.mail.CertificateValidationException`

This class  provides methods for handling exceptions related to the validation of digital certificates.

This class contains the following public method(s):

- `getAlias()`  retrieves a stored alias.
- `needsUserAttention()`  returns a boolean value indicating whether or not the user needs to take action on the certificate validation exception.
- `getReason()`  returns a value of the `Reason` field from the `CertificateValidationException` class.
- `getCertChain()`  returns the certificate chain (as an array of X509Certificates) associated with a CertificateValidationException.

## class `com.fsck.k9.mail.BoundaryGenerator`

This class  generates random strings to be used as boundaries in emails.

This class contains the following public method(s):

- `generateBoundary()`  generates a string of random characters to be used as a boundary for emails.
- `getInstance()`  returns an instance of the `BoundaryGenerator` class.

## abstract class `com.fsck.k9.mail.BodyPart`

This abstract class  provides an abstract representation of an email body part which can be used to set and get its encoding, parent, and extra information from the server.

This class contains the following public method(s):

- `setEncoding(java.lang.String)`  sets the encoding of a body part.
- `setParent(com.fsck.k9.mail.Multipart)`  assigns a given `Multipart` object to the `BodyPart` instance as its parent.
- `getParent()`  "returns the parent MultiPart of the BodyPart".
- `setServerExtra(java.lang.String)`  sets the extra information from the server.
- `getServerExtra()`  returns a string containing extra information from the server.

## class `com.fsck.k9.mail.TransportUris`

This class 
"converts between transport-specific URIs and ServerSettings objects."

This class contains the following public method(s):

- `decodeTransportUri(java.lang.String)`  decodes the given transport-specific URI into a ServerSettings object.
- `createTransportUri(com.fsck.k9.mail.ServerSettings)`  creates a transport URI from the information provided in a given ServerSettings object.

## class `com.fsck.k9.mail.DefaultBodyFactory`

This class  creates a Body instance from an InputStream with a content transfer encoding and content type.

This class contains the following public method(s):

- `createBody(java.lang.String,java.lang.String,java.io.InputStream)`  creates a Body instance from an InputStream with a content transfer encoding and content type.

## interface `com.fsck.k9.mail.MessageRetrievalListener`

This interface  allows any class implementing the interface to be notified upon the completion of retrieving and/or starting to retrieve messages from a mail server.

This class contains the following public method(s):

- `messageFinished(com.fsck.k9.mail.Message,int,int)`  notifies the listener that retrieval of a single message has completed.
- `messagesFinished(int)`  indicates when retrieval of messages has finished.
- `messageStarted(java.lang.String,int,int)`  notifies the listener of the start of a message retrieval from the specified UID.

## interface `com.fsck.k9.mail.BodyFactory`

This interface  creates a `com.fsck.k9.mail.Body` object from given content transfer encoding, content type, and input stream.

This class contains the following public method(s):

- `createBody(java.lang.String,java.lang.String,java.io.InputStream)`  creates and returns a `com.fsck.k9.mail.Body` object based on the given content transfer encoding, content type, and input stream.

## interface `com.fsck.k9.mail.Pusher`

This interface  provides an interface for performing periodic synchronization of email folders for push services.

This class contains the following public method(s):

- `getLastRefresh()`  "retrieves the last time the Pusher was refreshed".
- `setLastRefresh(long)`  sets the time of the last refresh operation for this Pusher.
- `getRefreshInterval()`  returns the number of milliseconds required for a refresh interval.
- `stop()`  stops the operation of the Pusher interface.
- `refresh()`  refreshes the data associated with a Pusher.
- `start(java.util.List)`  begins the periodic synchronization of specific folders for push services.

## class `com.fsck.k9.mail.K9MailLib`

This class 
allows users to control the debug status and debug-sensitive information display of an email client.

This class contains the following public method(s):

- `setDebugStatus(com.fsck.k9.mail.K9MailLib$DebugStatus)`  sets the current debug status.
- `isDebug()`  checks if the debug status is enabled.
- `setDebugSensitive(boolean)`  sets a flag indicating whether debug-sensitive information should be displayed.
- `isDebugSensitive()`  returns a boolean value based on the current debug status of the K9MailLib class.
- `setDebug(boolean)`  enables or disables the debugging status of the K9MailLib library.

## class `com.fsck.k9.mail.ServerSettings`

This class  provides a set of methods for storing and manipulating information about server settings.

This class contains the following public method(s):

- `getExtra()`  returns a map of extra settings associated with a particular server.
- `newClientCertificateAlias(java.lang.String)`  creates and returns a new `ServerSettings` object initialized with the given `newAlias`, while keeping all the other fields the same.
- `newPassword(java.lang.String)`  creates a new ServerSettings instance with the same parameters except for the new password.
- `equals(java.lang.Object)`  checks to see if two `ServerSettings` objects are equal by comparing their various attributes.

## interface `com.fsck.k9.mail.K9MailLib$WritableDebugStatus`

This interface  "allows a client to control the sensitivity and enabled state of a `K9MailLib$WritableDebugStatus` object".

This class contains the following public method(s):

- `setSensitive(boolean)`  sets whether the debug status is sensitive or not.
- `setEnabled(boolean)`  sets the enabled state of the `K9MailLib$WritableDebugStatus` object.

## class `com.fsck.k9.mail.TransportProvider`

This class  provides several methods for creating and accessing transport-related objects.

This class contains the following public method(s):

- `getInstance()`  returns the static transport provider instance.
- `getTransport(android.content.Context,com.fsck.k9.mail.store.StoreConfig)`  creates a transport related to the given StoreConfig object based on the type of URI provided.

## interface `com.fsck.k9.mail.PushReceiver`

This interface  provides methods to update, synchronize, and receive push notifications for a given folder.

This class contains the following public method(s):

- `messagesRemoved(com.fsck.k9.mail.Folder,java.util.List)`  removes a given list of messages from a folder.
- `messagesFlagsChanged(com.fsck.k9.mail.Folder,java.util.List)`  updates the flags on a list of messages in a given folder.
- `syncFolder(com.fsck.k9.mail.Folder)`  synchronizes a given folder.
- `authenticationFailed()`  informs the receiver that authentication has failed.
- `getContext()`  returns the Android context of the associated receiver.
- `messagesArrived(com.fsck.k9.mail.Folder,java.util.List)`  notifies the receiver of an arrival of messages in a given folder.
- `setPushActive(java.lang.String,boolean)`  "enables or disables push notifications for the specified folder".
- `getPushState(java.lang.String)`  returns the state of a push connection for the specified folder.
- `sleep(com.fsck.k9.mail.power.TracingPowerManager$TracingWakeLock,long)`  acquires the given wake lock and puts the thread to sleep for the specified number of milliseconds.
- `pushError(java.lang.String,java.lang.Exception)`  logs an error message and associated exception.

## enum `com.fsck.k9.mail.NetworkType`

This enum  defines a set of constants for different types of Internet network connections.

This class contains the following public method(s):

- `fromConnectivityManagerType(int)`  returns an instance of NetworkType based on a given connectivity manager type.

## abstract class `com.fsck.k9.mail.Multipart`

This abstract class  provides an interface for constructing MIME-formatted messages composed of multiple parts.

This class contains the following public method(s):

- `getMimeType()`  returns a string containing the MIME type of the multipart.
- `getEpilogue()`  gets the epilogue of the Multipart as a byte array.
- `addBodyPart(com.fsck.k9.mail.BodyPart)`  adds a `BodyPart` object to a `Multipart` object and sets the `Parent` attribute of the `BodyPart` object to the `Multipart` object.
- `getBodyParts()`  returns an unmodifiable list of `com.fsck.k9.mail.BodyPart` objects.
- `getCount()`  returns the total number of parts contained in the Multipart object.
- `getBodyPart(int)`  retrieves the body part at a given index from a `Multipart` object.
- `getParent()`  retrieves the parent part for the multipart.
- `getPreamble()`  returns a byte array of the preamble data from a multipart message.
- `getBoundary()`  returns a boundary string for a multipart instance.
- `setEncoding(java.lang.String)`  sets the encoding of the `Multipart` body to either 7bit or 8bit while throwing an exception if the encoding does not match those standards.
- `setParent(com.fsck.k9.mail.Part)`  sets the parent object of the `Multipart` instance.
- `setCharset(java.lang.String)`  sets the given charset to the first body part of the multipart.

## abstract class `com.fsck.k9.mail.Message`

This abstract class  provides methods for setting and retrieving data from a mail message, such as the body, flags, headers, and the sender/recipient information.

This class contains the following public method(s):

- `setFlags(java.util.Set,boolean)`  sets one or more flags to either true or false.
- `getInternalDate()`  returns the `mInternalDate` field of a `Message` object.
- `setFlag(com.fsck.k9.mail.Flag,boolean)`  adds or removes a Flag from the message flags.
- `getSize()`  returns the size of a Message object.
- `delete(java.lang.String)`  deletes a message from a specified trash folder.
- `getFrom()`  returns an array of addresses from the message.
- `clone()`  creates a new `Message` object with the same content as the original object.
- `setSubject(java.lang.String)`  sets the subject of a message.
- `setInReplyTo(java.lang.String)`  sets the "In-Reply-To" field of the message.
- `setFrom(com.fsck.k9.mail.Address)`  sets the email sender's address.
- `setReplyTo(com.fsck.k9.mail.Address[])`  sets the "Reply-To" addresses for an email message.
- `getRecipients(com.fsck.k9.mail.Message$RecipientType)`  returns an array of `com.fsck.k9.mail.Address` objects that represent the specified `RecipientType` in the message.
- `getSentDate()`  returns the date when the message was sent.
- `setBody(com.fsck.k9.mail.Body)`  sets the message's body to the provided body.
- `setReferences(java.lang.String)`  sets the message's references.
- `setInternalDate(java.util.Date)`  sets the internal date of a Message object.
- `addRawHeader(java.lang.String,java.lang.String)`  adds a header to a message with the given name and raw value.
- `setRecipient(com.fsck.k9.mail.Message$RecipientType,com.fsck.k9.mail.Address)`  assigns a single address as the type of recipient specified.
- `calculateSize()`  calculates the size of the message by writing to an output stream and using a counting output stream to return the size.
- `setSentDate(java.util.Date,boolean)`  sets the sent date of the message based on the argument.
- `addHeader(java.lang.String,java.lang.String)`  adds a header with the specified name and value to the message.
- `hasAttachments()`  checks if a message has attachments.
- `setEncoding(java.lang.String)`  sets the encoding of the message.
- `getHeaderNames()`  gets the names of the headers of the mail message.
- `setCharset(java.lang.String)`  sets the character set of a message.
- `getReferences()`  retrieves the references of a message.
- `getSubject()`  retrieves the subject of the message.
- `isSet(com.fsck.k9.mail.Flag)`  checks whether the specified flag is set for this message.
- `getFlags()`  returns an unmodifiable set of the message's flags.
- `getSender()`  is used to retrieve an array of addresses representing the sender of a message.
- `setUid(java.lang.String)`  sets the message UID to the given UID.
- `getReplyTo()`  returns the addresses to use when replying to the message.
- `getHeader(java.lang.String)`  returns an array of strings containing the headers of the given name associated with the message.
- `setHeader(java.lang.String,java.lang.String)`  sets the header of a message with a given name and value.
- `getFolder()`  returns the instance of com.fsck.k9.mail.Folder stored in the Message instance.
- `destroy()`  destroys a message.
- `equals(java.lang.Object)`  returns `true` if the `UID` and folder name of two `Message` objects is the same.
- `setSender(com.fsck.k9.mail.Address)`  sets the sender address of a `Message` object.
- `setRecipients(com.fsck.k9.mail.Message$RecipientType,com.fsck.k9.mail.Address[])`  sets the supplied type of recipient (e.g. TO, CC, BCC, etc.) using the provided list of addresses.
- `hashCode()`  computes a hash code based on the name of its `mFolder` and its `mUid` fields.
- `removeHeader(java.lang.String)`  removes a specified header from the message.
- `getMessageId()`  gets a string representing an ID of the message.
- `getBody()`  returns the body of the message.
- `getUid()`  retrieves the UID of the message.
- `olderThan(java.util.Date)`  determines whether the message was sent before a given date.

## class `com.fsck.k9.mail.CertificateChainException`

This class  "provides a way to store and access an X509Certificate chain".

This class contains the following public method(s):

- `getCertChain()`  returns an array of `X509Certificate`s.
- `setCertChain(java.security.cert.X509Certificate[])`  sets the X509Certificate chain for the CertificateChainException.

## abstract class `com.fsck.k9.mail.Folder`

This abstract class  provides methods for manipulating mail providers, folders, messages, and their properties.

This class contains the following public method(s):

- `moveMessages(java.util.List,com.fsck.k9.mail.Folder)`  moves multiple messages from one folder to another.
- `areMoreMessagesAvailable(int,java.util.Date)`  checks to see if there are more messages available in the folder given an index of the oldest message and a earliest date.
- `delete(boolean)`  deletes a folder with an option to recursively delete any subfolders.
- `fetch(java.util.List,com.fsck.k9.mail.FetchProfile,com.fsck.k9.mail.MessageRetrievalListener)`  downloads one or more certain types of content from a mailbox, such as headers, body, or flags, for a list of messages and notifies a listener as it does so.
- `setFlags(java.util.Set,boolean)`  sets a given set of flags to the specified boolean value.
- `setLastPush(long)`  sets the `lastPush` field of the `Folder` instance to the given parameter value.
- `getSyncClass()`  returns the FolderClass object associated with the Folder instance.
- `open(int)`  opens the mail provider with the given access mode.
- `isInTopGroup()`  returns a boolean value indicating whether or not the folder is in the top group.
- `close()`  closes the MailProvider, so that any further access will try to reopen it.
- `create(com.fsck.k9.mail.Folder$FolderType,int)`  creates a new folder with a specified display limit.
- `create(com.fsck.k9.mail.Folder$FolderType)`  attempts to create a new folder of a certain type.
- `fetchPart(com.fsck.k9.mail.Message,com.fsck.k9.mail.Part,com.fsck.k9.mail.MessageRetrievalListener,com.fsck.k9.mail.BodyFactory)`  logs a message to indicate that the fetchPart() method is not implemented.
- `search(java.lang.String,java.util.Set,java.util.Set)`  throws a MessagingException indicating that K-9 does not support searches on this folder type.
- `getNewPushState(java.lang.String,com.fsck.k9.mail.Message)`  returns a value that serves either to clear or preserve the old push state of a mail message.
- `getStatus()`  returns the value of the `status` variable.
- `isFlagSupported(com.fsck.k9.mail.Flag)`  returns `true` if a flag is supported.
- `expunge()`  removes any messages marked for deletion in the folder.
- `getLastPush()`  returns the timestamp of the last push for a folder.
- `appendMessages(java.util.List)`  appends a list of messages to an existing folder.
- `getName()`  returns the name of a mail folder.
- `exists()`  checks whether a folder exists or not.
- `getLastChecked()`  returns the timestamp of when the folder was last checked.
- `setStatus(java.lang.String)`  sets the status of the folder.
- `getMessages(int,int,java.util.Date,com.fsck.k9.mail.MessageRetrievalListener)`  retrieves the shells of messages within a given UID range and after a specified date.
- `setFlags(java.util.List,java.util.Set,boolean)`  sets flags for a list of messages to a specified value.
- `getFlaggedMessageCount()`  returns the number of flagged messages in a folder.
- `getLastUpdate()`  returns the latest timestamp of the last check or push for a given folder.
- `getMessage(java.lang.String)`  retrieves a message based on its UID.
- `supportsFetchingFlags()`  returns whether a folder supports fetching flags.
- `getMessageCount()`  returns the count of the messages in the selected folder.
- `setLastChecked(long)`  sets the "last checked" time to a specified time.
- `copyMessages(java.util.List,com.fsck.k9.mail.Folder)`  copies a list of messages from one folder to another.
- `isOpen()`  determines if the current folder connection is already open.
- `getMode()`  returns the mode in which the folder was opened.
- `getDisplayClass()`  returns a `FolderClass` constant representing the display class of the folder.
- `toString()`  returns the `name` of the Folder.
- `delete(java.util.List,java.lang.String)`  deletes a given list of messages by moving them to the specified trash folder.
- `getUnreadMessageCount()`  retrieves the number of unread messages in a folder.
- `getUidFromMessageId(com.fsck.k9.mail.Message)`  retrieves the unique identifier of a message from its Message object.
- `getPushClass()`  returns the same value as the `getSyncClass()` method.


# package `com.fsck.k9.mail.filter`

This package  provides classes for encoding, decoding, and manipulating data from streams in various formats.

This package contains the following class(es):

## class `com.fsck.k9.mail.filter.Base64OutputStream`

This class  allows the encoding and decoding of data in Base64 format.

This class contains the following public method(s):

- `flush()`  forces any buffered output bytes to be written out to the stream.
- `write(int)`  writes a single byte to the output stream.
- `close()`  notifies the encoder or decoder of End Of File (-1) and flushes the underlying stream.
- `write(byte[],int,int)`  writes a given number of bytes from the provided byte array, starting at the specified offset, to the output stream, throwing an exception if the arguments are invalid.

## class `com.fsck.k9.mail.filter.SmtpDataStuffing`

This class  copies input bytes to an output stream, doubling any dots that follow a carriage return.

This class contains the following public method(s):

- `write(int)`  writes the given byte to the output stream, and if the byte follows a carriage return and is a dot then it writes an additional dot.

## class `com.fsck.k9.mail.filter.LineWrapOutputStream`

This class :

"Wraps lines of text and writes them to an output stream, flushing the buffered characters when needed."

This class contains the following public method(s):

- `write(int)`  breaks a line at word boundaries, outputting the line to the output stream, and storing excess character in a buffer.
- `flush()`  outputs the contents of the buffer up to the current position and flushes the output stream.

## enum `com.fsck.k9.mail.filter.SignSafeOutputStream$State`

This enum  allows for tracking and transitioning between different states of a SignSafeOutputStream stream.

This class contains the following public method(s):

- `nextState(int)`  takes an integer as an argument and returns the next state of the SignSafeOutputStream enum.

## class `com.fsck.k9.mail.filter.Hex`

This class 
provides a method to convert an array of bytes to an array of characters representing the hexadecimal values of each byte.

This class contains the following public method(s):

- `encodeHex(byte[])`  converts an array of bytes into an array of characters representing the hexadecimal values of each byte in order.

## class `com.fsck.k9.mail.filter.CountingOutputStream`

This class  counts the number of bytes that have been written to an output stream.

This class contains the following public method(s):

- `write(byte[],int,int)`  updates a total count by adding the length of the provided array.
- `write(byte[])`  increases the counter by the length of the given byte array.
- `write(int)`  increments the value of the `mCount` variable by one.
- `getCount()`  returns the total number of bytes that have been written to the stream.

## class `com.fsck.k9.mail.filter.Base64`

This class  provides a set of methods which can be used to encode and decode data in the base64 format.

This class contains the following public method(s):

- `decode(java.lang.Object)`  takes an object as an argument and decodes it using the base64 algorithm if the object is of type byte[], otherwise, it throws a DecoderException.
- `decode(byte[])`  converts a byte array containing Base64 encoded characters into a byte array of binary data.
- `encodeBase64(byte[],boolean)`  encodes binary data into the Base64 algorithm, possibly chunking the output into 76 character blocks.
- `decodeBase64(byte[])`  decodes a byte array containing Base64 data into octets.
- `decode(java.lang.String)`  takes a String which is encoded in Base64 as a parameter and returns the same string in decoded form.
- `encodeInteger(java.math.BigInteger)`  encodes a Big Integer to a byte 64-encoded integer using XML-Signature crypto standards.
- `encode(java.lang.Object)`  encodes a byte array using the base64 algorithm and throws an EncoderException if the supplied object is not of type byte[].
- `encodeBase64Chunked(byte[])`  encodes a provided array of binary data into Base64 characters chunked into 76 character blocks.
- `isArrayByteBase64(byte[])`  tests a given byte array to see if it contains only valid characters in the Base64 alphabet.
- `isBase64(byte)`  checks whether or not the given byte is in the Base64 alphabet.
- `encode(byte[])`  encodes a byte array containing binary data into a byte array of Base64 characters.
- `encodeBase64(byte[])`  takes a binary array as input and returns the array encoded using the base64 algorithm.
- `encode(java.lang.String)`  takes a String as an argument and returns its Base64 encoded version.
- `decodeInteger(byte[])`  decodes a base64-encoded integer and returns a BigInteger object.

## class `com.fsck.k9.mail.filter.PeekableInputStream`

This class  provides an input stream class that allows for peeking at the next byte without advancing the pointer.

This class contains the following public method(s):

- `peek()`  reads the next byte from the input stream and stores it without advancing the pointer.
- `read(byte[],int,int)`  reads in bytes from an input stream and stores them in a buffer.
- `read(byte[])`  reads a given byte array into a buffer.
- `toString()`  returns a string representation of an instance of the `PeekableInputStream` class.
- `read()`  reads the next byte from the wrapped input stream or the most-recently peeked byte if one was present.

## class `com.fsck.k9.mail.filter.EOLConvertingOutputStream`

This class  converts any Windows-style line endings (CR+LF) to single Unix line endings (LF) and flushes the output stream.

This class contains the following public method(s):

- `endWithCrLfAndFlush()`  outputs a new line (CR + LF) and flushes the output stream.
- `flush()`  completes any pending [carriage return/line feed] sequence and flushes the underlying output stream.
- `write(int)`  converts any Windows-style line endings (CR+LF) to single Unix line endings (LF).

## class `com.fsck.k9.mail.filter.FixedLengthInputStream`

This class  provides methods for reading and skipping bytes from a given input stream.

This class contains the following public method(s):

- `read(byte[])`  reads a byte array from an InputStream.
- `skip(long)`  skips a certain number of bytes in the stream up to the maximum amount of available bytes.
- `toString()`  returns a String representation of the FixedLengthInputStream object.
- `read(byte[],int,int)`  reads a number of bytes from an input stream to a buffer, with a maximum of the number specified by the input parameters.
- `read()`  reads a single byte from the input stream and increments a counter.
- `available()`  returns the remaining number of bytes that can be read from the stream.
- `skipRemaining()`  skips all the remaining available bytes in the input stream.

## class `com.fsck.k9.mail.filter.SignSafeOutputStream`

This class  provides an output stream used to safely encode and write data to another output stream.

This class contains the following public method(s):

- `flush()`  flushes buffered output and then flushes the underlying output stream.
- `write(byte[],int,int)`  encodes byte data contained within the given byte array and writes it to an output stream.
- `close()`  closes the output stream and ensures all data is flushed before the stream is closed.
- `encode(byte)`  takes a byte and either write the byte to the buffer or writes three escaped-space characters to the buffer depending on the state of the stream.
- `write(int)`  writes the given integer to the stream, or throws an exception if the stream is closed.


# package `com.fsck.k9.mail.helper`

This package  provides methods to encode and decode strings in UTF-8 format.

This package contains the following class(es):

## class `com.fsck.k9.mail.helper.UrlEncodingHelper`

This class  provides methods that can encode and decode strings in UTF-8 format.

This class contains the following public method(s):

- `encodeUtf8(java.lang.String)`  encodes a String in UTF-8 format.
- `decodeUtf8(java.lang.String)`  takes a string and decodes it using the UTF-8 encoding.


# package `com.fsck.k9.mail.internet`

This package  provides classes for manipulating, encoding, decoding, and extracting data and text from MIME messages and parts.

This package contains the following class(es):

## class `com.fsck.k9.mail.internet.ListHeaders`

This class  extracts list post addresses from a given Message object.

This class contains the following public method(s):

- `getListPostAddresses(com.fsck.k9.mail.Message)`  gets an array of list post addresses from a given Message object.

## class `com.fsck.k9.mail.internet.BinaryTempFileBody`

This class  provides methods for writing and reading data from a binary file in a temporary directory.

This class contains the following public method(s):

- `getEncoding()`  returns the encoding of the `BinaryTempFileBody` object.
- `getFile()`  returns a `File` object.
- `getInputStream()`  returns an input stream from a file.
- `getTempDirectory()`  returns the temporary file directory.
- `getSize()`  returns the length of the underlying file.
- `setTempDirectory(java.io.File)`  sets a static temp directory for use by BinaryTempFileBody objects.
- `setEncoding(java.lang.String)`  reads the body from an `InputStream` using the current encoding, converts it to a new encoding, and then writes it to a new file.
- `getOutputStream()`  creates a temporary file and returns an output stream for it.
- `writeTo(java.io.OutputStream)`  copies the data from the input stream to the given output stream.

## class `com.fsck.k9.mail.internet.CharsetSupport`

This class  enables users to set the character set for a mail part and also looks for a variant of a JIS encoded address and returns the corresponding shift_jis-2007 charset if it exists, or UTF-8 if it doesn't.

This class contains the following public method(s):

- `setCharset(java.lang.String,com.fsck.k9.mail.Part)`  sets the given charset for the given mail part.
- `getCharsetFromAddress(java.lang.String)`  looks for a variant of a JIS encoded address and returns the corresponding shift_jis-2007 charset if it exists, or UTF-8 if it doesn't.

## class `com.fsck.k9.mail.internet.EncoderUtil`

This class  encodes text into an encoded word or a sequence of encoded words with a suitable charset.

This class contains the following public method(s):

- `encodeEncodedWord(java.lang.String,java.nio.charset.Charset)`  encodes a text into an encoded word or a sequence of encoded words with a suitable charset.

## class `com.fsck.k9.mail.internet.JisSupport`

This class  provides methods to detect the JIS variant of an email address or a message.

This class contains the following public method(s):

- `getJisVariantFromAddress(java.lang.String)`  determines a JIS variant of an email address based on its domain.
- `getJisVariantFromMessage(com.fsck.k9.mail.Message)`  extracts the JIS variant from either the received headers, the from headers, or the mailer headers from the given message.
- `isShiftJis(java.lang.String)`  checks if a given String is a Shift JIS character encoding.

## class `com.fsck.k9.mail.internet.MimeHeader`

This class  allows users to manipulate headers in a MIME message.

This class contains the following public method(s):

- `setCharset(java.lang.String)`  sets the character set of a MimeHeader object.
- `removeHeader(java.lang.String)`  removes all matching header fields from the given name.
- `clone()`  creates a clone of the `MimeHeader` object.
- `addHeader(java.lang.String,java.lang.String)`  adds a new header to the MimeHeader object, with the specified name and value.
- `writeTo(java.io.OutputStream)`  writes a list of field objects to an OutputStream.
- `getFirstHeader(java.lang.String)`  returns the value of the first header with the specified name.
- `getHeaderNames()`  returns a set of strings containing the names of the MimeHeader's fields.
- `getHeader(java.lang.String)`  returns an array of strings containing all values of a certain named MIME header field.
- `clear()`  empties a list of fields maintained by the MimeHeader class.
- `toString()`  takes the MIME header fields and creates a raw MIME header string.
- `setHeader(java.lang.String,java.lang.String)`  adds or modifies an existing header in a MIME message based on a given name and value.

## class `com.fsck.k9.mail.internet.Iso2022JpToShiftJisInputStream`

This class  reads and converts ISO 2022 Japanese text to Shift-JIS character encoding.

This class contains the following public method(s):

- `read()`  reads and converts ISO 2022 Japanese text into Shift-JIS, which is an 8-bit character encoding.

## class `com.fsck.k9.mail.internet.BinaryTempFileBody$BinaryTempFileBodyInputStream`

This class  provides an input stream implementation for body parts backed by a temporarily created file that can be closed without deleting it.

This class contains the following public method(s):

- `closeWithoutDeleting()`  closes a file without deleting it.
- `close()`  closes the underlying stream, logs information about deleting a temporary file, and then deletes the temporary file.

## abstract class `com.fsck.k9.mail.internet.Viewable$Textual`

This abstract class  provides a way to access the underlying internet `Part` associated with a `Textual` instance.

This class contains the following public method(s):

- `getPart()`  returns the `Part` associated with the `Textual` instance.

## class `com.fsck.k9.mail.internet.MimeMessage$MimeMessageBuilder`

This class  builds a MimeMessage object from header-fields, bodies, and content-types.

This class contains the following public method(s):

- `body(org.apache.james.mime4j.stream.BodyDescriptor,java.io.InputStream)`  sets the Body attribute of the current peek of the stack to a given Body created from a given BodyDescriptor and an InputStream.
- `endHeader()`  sets the expected class type to `Part.class`.
- `endMessage()`  removes the first element from the stack when a MimeMessage object is expected.
- `preamble(java.io.InputStream)`  assigns a preamble to the MimeMultipart at the top of the stack.
- `raw(java.io.InputStream)`  throws an UnsupportedOperationException when called.
- `endBodyPart()`  removes the first element of the stack when the class `BodyPart` is expected.
- `endMultipart()`  removes the `Multipart` instance from the stack and updates the `Part` instance accordingly if the `Multipart` instance has no body parts of epilogue.
- `startHeader()`  expects a `Part.class` before starting to build a MimeMessage.
- `field(org.apache.james.mime4j.stream.Field)`  adds a header with the given name and raw value to the top part on the stack.
- `startMultipart(org.apache.james.mime4j.stream.BodyDescriptor)`  sets the body of the part on the top of the stack to a new MimeMultipart object created from the given mime type and boundary.
- `epilogue(java.io.InputStream)`  sets the epilogue of the top stack element in a MimeMultipart object to the contents of a given InputStream.
- `startMessage()`  adds a new `MimeMessage` as the body of the `Part` at the top of the stack.
- `startBodyPart()`  adds a new MimeBodyPart to the already existing MimeMultipart.

## class `com.fsck.k9.mail.internet.MessageIdGenerator`

This class  provides a static method for generating a message ID based on the hostname of the sender for a given message.

This class contains the following public method(s):

- `getInstance()`  "Creates and returns a new instance of the MessageIdGenerator class".
- `generateMessageId(com.fsck.k9.mail.Message)`  generates a message ID for the provided message based on the hostname of the sender.

## class `com.fsck.k9.mail.internet.MessageExtractor`

This class  helps extract text from email messages as well as viewable files and attachment parts.

This class contains the following public method(s):

- `getTextFromPart(com.fsck.k9.mail.Part)`  extracts text from a mail Part object without size limit.
- `findViewablesAndAttachments(com.fsck.k9.mail.Part,java.util.List,java.util.List)`  extracts viewable parts from a MIME message and stores them in two separate lists.
- `hasMissingParts(com.fsck.k9.mail.Part)`  checks whether a given part of an email message has any missing parts.
- `collectAttachments(com.fsck.k9.mail.Message)`  collects attachment parts of a message into a list.
- `getTextParts(com.fsck.k9.mail.Part)`  extracts and returns the text parts from the given part object.
- `collectTextParts(com.fsck.k9.mail.Message)`  collects the viewable textual parts of a message.
- `getTextFromPart(com.fsck.k9.mail.Part,long)`  extracts text from a given email message part and returns it as a string.

## class `com.fsck.k9.mail.internet.MimeBodyPart`

This class  provides methods to access, set, and write header information, body content, and content types for MimeBodyPart objects.

This class contains the following public method(s):

- `getHeader(java.lang.String)`  gets all headers with the given name from a MimeBodyPart object.
- `setHeader(java.lang.String,java.lang.String)`  sets a header name and value.
- `writeTo(java.io.OutputStream)`  writes the MimeMessage data in MIME format to an output stream.
- `removeHeader(java.lang.String)`  removes a specified header from the MimeBodyPart.
- `writeHeaderTo(java.io.OutputStream)`  writes the header of a MimeBodyPart object to an OutputStream.
- `getDisposition()`  returns the value of the header `Content-Disposition`.
- `getBody()`  returns the body of the MimeBodyPart.
- `getMimeType()`  returns the MIME type of the body part.
- `addHeader(java.lang.String,java.lang.String)`  adds a header and its value to a MimeBodyPart object.
- `setEncoding(java.lang.String)`  sets a content transfer encoding for a MimeBodyPart to the specified encoding.
- `setBody(com.fsck.k9.mail.Body)`  sets the body for the MimeBodyPart object.
- `addRawHeader(java.lang.String,java.lang.String)`  adds a raw header to the MimeBodyPart.
- `isMimeType(java.lang.String)`  compares a given string to the most recent MIME type of the object and returns true if they match.
- `getContentType()`  returns the content type of a MIME body part as a string.
- `getContentId()`  gets the content ID string from the first header of a MimeBodyPart, and returns it with any angle brackets removed.

## class `com.fsck.k9.mail.internet.DecoderUtil`

This class  decodes encoded words in strings according to RFC 2047.

This class contains the following public method(s):

- `decodeEncodedWords(java.lang.String,com.fsck.k9.mail.Message)`  decodes encoded words in strings according to RFC 2047.

## class `com.fsck.k9.mail.internet.MimeUtility`

This class  provides methods for decoding, encoding, and manipulating MIME types and associated data.

This class contains the following public method(s):

- `decodeBody(com.fsck.k9.mail.Body)`  takes a `Body` parameter and returns its decoded contents as an `InputStream` based on the encoding set for it.
- `getEncodingforType(java.lang.String)`  returns a default content-transfer-encoding based on the given type.
- `unfoldAndDecode(java.lang.String,com.fsck.k9.mail.Message)`  takes a string, unfolds it, then decodes it using a message.
- `unfoldAndDecode(java.lang.String)`  decodes a string using the MIME utility.
- `getAllHeaderParameters(java.lang.String)`  splits a given string header value by ';' and '=' to generate a map of key-value pairs.
- `foldAndEncode(java.lang.String)`  returns a string without any modifications.
- `unfold(java.lang.String)`  removes all newline and carriage return characters from a given String.
- `isMultipart(java.lang.String)`  checks if a given String mimeType is a multipart type or not.
- `getMimeTypeByExtension(java.lang.String)`  returns the MIME type of the provided file name.
- `isSameMimeType(java.lang.String,java.lang.String)`  checks whether the two specified MIME types are the same.
- `findFirstPartByMimeType(com.fsck.k9.mail.Part,java.lang.String)`  takes a Part and a MIME type as parameters, and returns the first part contained in the Part with the given MIME type.
- `isDefaultMimeType(java.lang.String)`  checks if a given mime type is the same as the default attachment MIME type.
- `isMessage(java.lang.String)`  checks if the given MIME type is "message/rfc822".
- `closeInputStreamWithoutDeletingTemporaryFiles(java.io.InputStream)`  closes an input stream, omitting the deletion of any associated temporary files.
- `mimeTypeMatches(java.lang.String,java.lang.String)`  checks if a given MIME type matches a given MIME type specification.
- `getHeaderParameter(java.lang.String,java.lang.String)`  returns the named parameter of a header field provided the header value and the parameter name.
- `getExtensionByMimeType(java.lang.String)`  takes a MIME type as a String and returns the file extension associated with it, if any.

## class `com.fsck.k9.mail.internet.MimeHeader$Field`

This class  creates and stores MimeHeader fields with names and values, and can generate toString representations of them.

This class contains the following public method(s):

- `getValue()`  "returns the value of the MimeHeader's raw field, after trimming any whitespace that follows the delimiter."
- `newNameValueField(java.lang.String,java.lang.String)`  creates a `MimeHeader` field with a given name and value.
- `getName()`  returns the name of the MimeHeader field.
- `getRaw()`  returns the raw String of the MimeHeader's Field.
- `hasRawData()`  checks if this MimeHeader Field object has raw data.
- `toString()`  returns either the raw data of the field or the name and value of the field as a single string.
- `newRawField(java.lang.String,java.lang.String)`  creates and returns a new MimeHeader.Field object based on a given name and raw value.

## class `com.fsck.k9.mail.internet.MimeMessage`

This class  provides a set of methods for manipulating and retrieving data from a MIME message.

This class contains the following public method(s):

- `getSentDate()`  returns the sent date of a MimeMessage stored in the mSentDate field.
- `setSubject(java.lang.String)`  sets a header in the MimeMessage with the given subject.
- `writeHeaderTo(java.io.OutputStream)`  writes a MIME message's header to an output stream.
- `setRecipients(com.fsck.k9.mail.Message$RecipientType,com.fsck.k9.mail.Address[])`  sets the recipients of a MimeMessage based on the given recipient type and addresses.
- `setInternalSentDate(java.util.Date)`  sets the internal sent date of the MimeMessage object.
- `setReferences(java.lang.String)`  sets a References header on the email message to a value that will not exceed the maximum header line length.
- `setFrom(com.fsck.k9.mail.Address)`  sets the sender's address of the MimeMessage object.
- `setServerExtra(java.lang.String)`  sets the specified extra data for the server.
- `setReplyTo(com.fsck.k9.mail.Address[])`  sets a specified reply-to address for the email message.
- `getReferences()`  returns the "References" header of the MimeMessage object it's called on.
- `setHeader(java.lang.String,java.lang.String)`  sets the given name and value as a header in a MimeMessage object.
- `setInReplyTo(java.lang.String)`  sets the "In-Reply-To" header of a MimeMessage object to the specified string.
- `getContentType()`  returns the content type of a MIME message.
- `parse(java.io.InputStream)`  parses an InputStream using Apache Mime4J to build a MimeMessage without recursing through nested bodyparts.
- `getContentId()`  returns a string identifier for a MIME message.
- `getSize()`  returns the size of a MimeMessage.
- `getFrom()`  returns the address of the sender of the MimeMessage.
- `getSubject()`  retrieves and decodes the value of the `Subject` header in a MIME message.
- `setCharset(java.lang.String)`  sets the charset of this MimeMessage and its contents.
- `getServerExtra()`  returns a string containing extra server information from the MimeMessage.
- `getDisposition()`  gets the content disposition from the first header of a MIME message.
- `setSentDate(java.util.Date,boolean)`  adds the sent date to the message and removes any existing 'date' header.
- `clone()`  creates and returns a new instance of MimeMessage, which is a copy of the original message.
- `getHeaderNames()`  returns the set of all header names in the Mime message.
- `getHeader(java.lang.String)`  returns the header value for a given header name from an instance of the MimeMessage class.
- `getRecipients(com.fsck.k9.mail.Message$RecipientType)`  returns a list of given recipient type from the message based on the recipient type all specified in the header.
- `getBody()`  "returns the mBody of the MimeMessage".
- `writeTo(java.io.OutputStream)`  writes the header and body of a MimeMessage to an OutputStream.
- `getMimeType()`  retrieves the mime type of the MimeMessage.
- `getInputStream()`  throws an UnsupportedOperationException.
- `getSender()`  retrieves the sender's address from a MIME Message.
- `setMessageId(java.lang.String)`  sets the "Message-ID" header of a MimeMessage object to the given message ID.
- `setBody(com.fsck.k9.mail.Body)`  assigns a body for the MimeMessage.
- `toBodyPart()`  takes a top-level message and returns a body part without any inappropriate headers.
- `addRawHeader(java.lang.String,java.lang.String)`  adds a raw header to the MimeMessage object.
- `getReplyTo()`  returns the address(es) in "Reply-to" header of a MIME message.
- `setEncoding(java.lang.String)`  sets the encoding of the body and header of the MimeMessage.
- `removeHeader(java.lang.String)`  removes the header with the specified name from the MimeMessage.
- `parseMimeMessage(java.io.InputStream,boolean)`  parses a MIME message from an input stream and returns a `MimeMessage` instance.
- `hasAttachments()`  checks whether a MimeMessage has any attachments.
- `addHeader(java.lang.String,java.lang.String)`  adds a header to the MimeMessage object.
- `addSentDate(java.util.Date,boolean)`  adds a 'Date' header to the MimeMessage object using the specified date and time information, while also setting the sent date object member for performance reasons.
- `getMessageId()`  returns the value of the "Message-ID" header from the MimeMessage object.
- `setSender(com.fsck.k9.mail.Address)`  sets the header of the message with the encoded string of the sender address, and also updates the sender field of the message.
- `isMimeType(java.lang.String)`  checks if the content type of the MIME message is equal to the given string, ignoring the case.

## class `com.fsck.k9.mail.internet.Viewable$Alternative`

This class  provides methods to retrieve text, HTML and alternative Viewable objects.

This class contains the following public method(s):

- `getText()`  returns a list of Viewable objects.
- `getHtml()`  returns a list of Viewable objects.

## class `com.fsck.k9.mail.internet.MimeMessageHelper`

This class  provides methods to modify Part objects by setting their encoding and body.

This class contains the following public method(s):

- `setEncoding(com.fsck.k9.mail.Part,java.lang.String)`  sets the specified encoding on the given part.
- `setBody(com.fsck.k9.mail.Part,com.fsck.k9.mail.Body)`  sets the body and some related headers on the given Part.

## class `com.fsck.k9.mail.internet.Viewable$Flowed`

This class  provides a way to get the value of the `delSp` field.

This class contains the following public method(s):

- `isDelSp()`  returns the value of the `delSp` field.

## class `com.fsck.k9.mail.internet.BinaryTempFileMessageBody`

This class  allows users to set the content-transfer-encoding for a message/rfc822 body.

This class contains the following public method(s):

- `setEncoding(java.lang.String)`  sets the content-transfer-encoding for a message/rfc822 body, and throws an exception if the encoding is incompatible.

## interface `com.fsck.k9.mail.internet.RawDataBody`

This interface  
provides a method to retrieve the encoding of raw data contained in a body of an email message.

This class contains the following public method(s):

- `getEncoding()`  returns the encoding of the raw data body.

## class `com.fsck.k9.mail.internet.MimeMultipart`

This class  creates MIME multipart objects, with various operations for setting the preamble, boundary, subtype, and epilogue of the object.

This class contains the following public method(s):

- `getPreamble()`  returns the preamble stored in the class instance.
- `getInputStream()`  throws an exception indicating that it does not support the `getInputStream()` operation.
- `writeTo(java.io.OutputStream)`  writes the contents of a MimeMultipart to an OutputStream.
- `setPreamble(byte[])`  sets the preamble of a MimeMultipart object.
- `newInstance()`  creates a new instance of the `MimeMultipart` class with a randomly-generated boundary.
- `getEpilogue()`  returns the epilogue of a MimeMultipart.
- `getBoundary()`  returns the boundary of the MIME multipart object.
- `getMimeType()`  returns the MIME type of the MimeMultipart object.
- `setEpilogue(byte[])`  sets the epilogue of a MimeMultipart object.
- `setSubType(java.lang.String)`  sets the subtype of a MIME multipart to a given string.

## interface `com.fsck.k9.mail.internet.SizeAware`

This interface  provides functionality to determine the size of an object.

This class contains the following public method(s):

- `getSize()`  returns the size of the object.

## class `com.fsck.k9.mail.internet.TextBody`

This class  provides methods that allow users to manipulate text bodies, such as setting the encoding, retrieving raw text, or getting the size.

This class contains the following public method(s):

- `getEncoding()`  retrieves the value of the `encoding` field.
- `setCharset(java.lang.String)`  sets the character set of a TextBody object.
- `getComposedMessageLength()`  returns an Integer that represents the length of the composed message.
- `getInputStream()`  returns an `InputStream` from the given `text`.
- `getComposedMessageOffset()`  retrieves the composed message offset.
- `setComposedMessageLength(java.lang.Integer)`  sets the composed message length of a text body to a specified integer.
- `getSize()`  calculates the size of text body based on given charset and encoding.
- `getRawText()`  returns the raw text stored in the TextBody object.
- `writeTo(java.io.OutputStream)`  takes in an OutputStream and writes the text in it specified by the encoding in the class variables.
- `setEncoding(java.lang.String)`  sets the encoding of the text body provided it is supported by the MimeUtil class.
- `setComposedMessageOffset(java.lang.Integer)`  sets an offset value for a composed message.

## class `com.fsck.k9.mail.internet.Viewable$MessageHeader`

This class  "provides methods to get the associated message and the container part of the Viewable."

This class contains the following public method(s):

- `getMessage()`  returns the message associated with the Viewable.
- `getContainerPart()`  returns the `mContainerPart` object.


# package `com.fsck.k9.mail.message`

This package  provides classes for parsing and handling raw message headers and body parts for use in a message receiver.

This package contains the following class(es):

## class `com.fsck.k9.mail.message.MessageHeaderParser$MessageHeaderParserContentHandler`

This class  handles the raw message headers and body parts for use in a message receiver.

This class contains the following public method(s):

- `raw(java.io.InputStream)`  does nothing when given an input stream.
- `endHeader()`  does nothing when the header is finished.
- `endMultipart()`  does nothing.
- `body(org.apache.james.mime4j.stream.BodyDescriptor,java.io.InputStream)`  does nothing.
- `endBodyPart()`  does nothing when the end of a body part is reached.
- `startMultipart(org.apache.james.mime4j.stream.BodyDescriptor)`  does nothing.
- `preamble(java.io.InputStream)`  does nothing.
- `endMessage()`  does nothing when the end of the message is reached.
- `startHeader()`  does nothing when a header section starts.
- `startMessage()`  does nothing when the start of a message is encountered.
- `field(org.apache.james.mime4j.stream.Field)`  adds a raw header with the given name to the current part.
- `epilogue(java.io.InputStream)`  does nothing.
- `startBodyPart()`  does nothing.

## class `com.fsck.k9.mail.message.MessageHeaderParser`

This class  parses and assigns expected headers to a given mail message part.

This class contains the following public method(s):

- `parse(com.fsck.k9.mail.Part,java.io.InputStream)`  parses the headers from the given input stream and assigns them to the given part.


# package `com.fsck.k9.mail.oauth`

This package  provides interfaces and a class for supporting OAuth 2.0 authentication for API access.

This package contains the following class(es):

## class `com.fsck.k9.mail.oauth.XOAuth2ChallengeParser`

This class  parses an OAuth2 challenge response and determines if a retry is needed.

This class contains the following public method(s):

- `shouldRetry(java.lang.String,java.lang.String)`  checks if a response from an OAuth2 challenge requires retrying or not.

## interface `com.fsck.k9.mail.oauth.OAuth2TokenProvider`

This interface  provides methods for authorizing API access, getting accounts suitable for OAuth 2.0 token provision, getting tokens with a time limit before expiry, and invalidating previously saved tokens for a given username.

This class contains the following public method(s):

- `authorizeApi(java.lang.String,android.app.Activity,com.fsck.k9.mail.oauth.OAuth2TokenProvider$OAuth2TokenProviderAuthCallback)`  requests API authorization for a given username using a given Activity, and passes a callback to process the asynchronous response.
- `getAccounts()`  returns a list of strings containing accounts suitable for OAuth 2.0 token provision.
- `getToken(java.lang.String,long)`  returns an OAuth2 token for the given user name, with a given time limit before the token expires.
- `invalidateToken(java.lang.String)`  invalidates previously saved tokens for a given username.

## interface `com.fsck.k9.mail.oauth.OAuth2TokenProvider$OAuth2TokenProviderAuthCallback`

This interface  provides a callback for OAuth 2.0 authentication, which either succeeds or fails.

This class contains the following public method(s):

- `success()`  indicates that the OAuth authentication process was successful.
- `failure(com.fsck.k9.mail.oauth.AuthorizationException)`  notifies the caller of a failed authorization.


# package `com.fsck.k9.mail.power`

This package  provides an interface for creating and acquiring wake locks with logging and notification to monitor the acquire and release of the locks.

This package contains the following class(es):

## class `com.fsck.k9.mail.power.TracingPowerManager$TracingWakeLock`

This class  provides a wake lock with logging and notification to monitor the acquire and release of the lock.

This class contains the following public method(s):

- `acquire()`  acquires a wake lock and raises a notification, then logs a warning if in debug mode and sets the start time if it hasn't already been set.
- `setReferenceCounted(boolean)`  sets whether or not a WakeLock object's reference count will be tracked.
- `acquire(long)`  acquires a wake Lock with a specified timeout, logs a Timber message, raises a notification, and stores the timeout and the start time.
- `release()`  releases the wake lock associated with the TracingPowerManager object and logs relevant information depending on the debug mode.

## class `com.fsck.k9.mail.power.TracingPowerManager`

This class  provides an interface to create and acquire wake locks for tracking power management operations.

This class contains the following public method(s):

- `newWakeLock(int,java.lang.String)`  creates and returns a new instance of type `TracingWakeLock` with the specified flags and tag.
- `getPowerManager(android.content.Context)`  creates an instance of the TracingPowerManager class and stores it when called, or returns the stored instance if one exists.


# package `com.fsck.k9.mail.ssl`

This package  provides utilities for creating a secure and trusted connection to send and receive emails using SSL/TLS network connections.

This package contains the following class(es):

## class `com.fsck.k9.mail.ssl.DefaultTrustedSocketFactory`

This class  creates a secure and trusted socket connection for sending and receiving emails.

This class contains the following public method(s):

- `createSocket(java.net.Socket,java.lang.String,int,java.lang.String)`  creates an SSL/TLS-secured socket connection with optional client certificate authentication.
- `setSniHost(javax.net.ssl.SSLSocketFactory,javax.net.ssl.SSLSocket,java.lang.String)`  sets the hostname of an SSLSocketFactory and SSLSocket using either the SSLCertificateSocketFactory API or a setHostnameViaReflection method.

## class `com.fsck.k9.mail.ssl.TrustManagerFactory$SecureX509TrustManager`

This class  provides an implementation of the X509TrustManager interface to verify server certificates and determine if they should be trusted.

This class contains the following public method(s):

- `checkClientTrusted(java.security.cert.X509Certificate[],java.lang.String)`  checks if the X509 certificates provided by the client are trusted.
- `checkServerTrusted(java.security.cert.X509Certificate[],java.lang.String)`  verifies the server's certificate by checking a global key store and local key store and throws an exception in case the certificate is invalid.
- `getAcceptedIssuers()`  returns the accepted issuers of the default trust manager.
- `getInstance(java.lang.String,int)`  creates a new `SecureX509TrustManager` instance if one isn't already stored for the specified host and port, or it returns the existing instance if one is stored.

## class `com.fsck.k9.mail.ssl.LocalKeyStore`

This class  provides an API for managing a local SSL certificate key store.

This class contains the following public method(s):

- `deleteCertificate(java.lang.String,int)`  deletes an existing certificate from the local key store.
- `addCertificate(java.lang.String,int,java.security.cert.X509Certificate)`  adds a given SSL certificate to the local key store, then writes the certificate file.
- `isValidCertificate(java.security.cert.Certificate,java.lang.String,int)`  checks if a provided certificate is valid by comparing it to a stored certificate.
- `setKeyStoreLocation(java.lang.String)`  sets the directory for the local key store.
- `setKeyStoreFile(java.io.File)`  sets or resets a local KeyStore using a file provided by the caller.
- `getInstance()`  returns an instance of the `LocalKeyStore` class.

## class `com.fsck.k9.mail.ssl.KeyChainKeyManager`

This class  provides alias-based key selection and management methods for working with a key chain in an SSL/TLS network connection.

This class contains the following public method(s):

- `chooseEngineServerAlias(java.lang.String,java.security.Principal[],javax.net.ssl.SSLEngine)`  returns a server alias for the given SSL engine based on the given key type and list of issuers.
- `chooseClientAlias(java.lang.String[],java.security.Principal[],java.net.Socket)`  chooses an alias based on the given key types and issuers.
- `getServerAliases(java.lang.String,java.security.Principal[])`  chooses an alias and returns a single-element array containing the chosen alias.
- `chooseEngineClientAlias(java.lang.String[],java.security.Principal[],javax.net.ssl.SSLEngine)`  returns an alias for a client's SSLEngine based on the given key types and issuers.
- `chooseServerAlias(java.lang.String,java.security.Principal[],java.net.Socket)`  selects an alias from the key chain for the specified key type and issuers.
- `getClientAliases(java.lang.String,java.security.Principal[])`  returns the client aliases associated with the given key type and issuers.
- `getPrivateKey(java.lang.String)`  returns the private key associated with the given alias.
- `getCertificateChain(java.lang.String)`  returns the certificate chain associated with the given alias.

## interface `com.fsck.k9.mail.ssl.TrustedSocketFactory`

This interface  provides a secure socket for communication to a specific host on a given port using a specific client certificate alias.

This class contains the following public method(s):

- `createSocket(java.net.Socket,java.lang.String,int,java.lang.String)`  creates a secure socket for communication to a specific host on a given port using a specific client certificate alias.

## class `com.fsck.k9.mail.ssl.TrustManagerFactory`

This class  generates a SecureX509TrustManager instance based on the specified host and port.

This class contains the following public method(s):

- `get(java.lang.String,int)`  returns a SecureX509TrustManager instance configured with the specified host and port.


# package `com.fsck.k9.mail.store.imap`

This package  provides classes and interfaces which allow users to connect to an IMAP server and manipulate the emails contained within by parsing responses, setting flags, and more.

This package contains the following class(es):

## class `com.fsck.k9.mail.store.imap.PermanentFlagsResponse`

This class  parses an ImapResponse and creates a set of flags that indicates whether keywords can be created or not.

This class contains the following public method(s):

- `canCreateKeywords()`  returns whether creating keywords is allowed or not.
- `parse(com.fsck.k9.mail.store.imap.ImapResponse)`  parses an ImapResponse and creates a PermanentFlagsResponse.
- `getFlags()`  returns a set of flags.

## class `com.fsck.k9.mail.store.imap.ImapMessage`

This class  provides methods for manipulating an IMAP message, such as setting flags and deleting it.

This class contains the following public method(s):

- `setFlagInternal(com.fsck.k9.mail.Flag,boolean)`  sets a flag on a message internally.
- `setSize(int)`  sets the size value of an `ImapMessage` object.
- `setFlag(com.fsck.k9.mail.Flag,boolean)`  sets a flag for the given message in the message's containing folder.
- `delete(java.lang.String)`  deletes the ImapMessage from the current folder into a specified trash folder.

## class `com.fsck.k9.mail.store.imap.ImapStoreSettings`

This class  stores settings for the ImapStore in order to establish a connection with an IMAP server.

This class contains the following public method(s):

- `getExtra()`  creates a map with the auto-detect namespace and path prefix key/value pairs from the ImapStoreSettings object and returns it.
- `newPassword(java.lang.String)`  returns an ImapStoreSettings object based on the given String parameter for the new password.

## class `com.fsck.k9.mail.store.imap.SearchResponse`

This class :

Parses IMAP SEARCH responses and returns a list of numbers.

This class contains the following public method(s):

- `getNumbers()`  returns a list of numbers from the SEARCH response.
- `parse(java.util.List)`  takes a list of `ImapResponse` objects, then parses the responses and returns a new `SearchResponse` object containing the parsed numbers.

## interface `com.fsck.k9.mail.store.imap.ImapResponseCallback`

This interface  enables users to parse IMAP responses and return an object with the literal string found therein.

This class contains the following public method(s):

- `foundLiteral(com.fsck.k9.mail.store.imap.ImapResponse,com.fsck.k9.mail.filter.FixedLengthInputStream)`  provides a callback to parse an IMAP response and return an object with the literal string that has been found.

## class `com.fsck.k9.mail.store.imap.ImapResponseParser`

This class  reads an IMAP response from an input stream and provides a callback object for handling the response.

This class contains the following public method(s):

- `readResponse(com.fsck.k9.mail.store.imap.ImapResponseCallback)`  reads the next response available on a stream and returns an ImapResponse object that represents it.
- `readResponse()`  reads an IMAP response from the input stream.

## class `com.fsck.k9.mail.store.imap.ImapPushState`

This class  provides a way to parse a push state string and obtain an ImapPushState object.

This class contains the following public method(s):

- `parse(java.lang.String)`  parses a push state string and returns a valid ImapPushState object.
- `toString()`  returns a string containing the value of `uidNext`.

## class `com.fsck.k9.mail.store.imap.ImapStoreUriCreator`

This class  creates an ImapStore URI based on the supplied server settings.

This class contains the following public method(s):

- `create(com.fsck.k9.mail.ServerSettings)`  creates an ImapStore URI based on the supplied server settings.

## class `com.fsck.k9.mail.store.imap.NamespaceResponse`

This class  "parses IMAP namespace responses and provides getter methods to retrieve its namespace prefix and hierarchy delimiter".

This class contains the following public method(s):

- `getPrefix()`  returns the prefix.
- `getHierarchyDelimiter()`  returns the hierarchy delimiter for an IMAP namespace.
- `parse(java.util.List)`  finds and returns the NamespaceResponse object from a list of ImapResponse objects.

## class `com.fsck.k9.mail.store.imap.ResponseCodeExtractor`

This class  extracts an IMAP response code from an `ImapResponse` object.

This class contains the following public method(s):

- `getResponseCode(com.fsck.k9.mail.store.imap.ImapResponse)`  extracts the response code of an ImapResponse object.

## class `com.fsck.k9.mail.store.imap.ImapConnection`

This class  enables users to connect to an IMAP server, send commands, read responses, and close connections.

This class contains the following public method(s):

- `open()`  establishes a connection to the IMAP server and authenticates the user.
- `executeSimpleCommand(java.lang.String)`  executes a given command and returns the response from the server.
- `sendContinuation(java.lang.String)`  sends a given string to the output stream with a line break at the end.
- `readResponse()`  reads a response from an IMAP connection and returns it.
- `sendCommand(java.lang.String,boolean)`  sends a command to an IMAP connection, logging it if specified.
- `readResponse(com.fsck.k9.mail.store.imap.ImapResponseCallback)`  reads an ImapResponse from the responseParser and logs it with Timber if K9MailLib debugging is enabled.
- `executeSimpleCommand(java.lang.String,boolean)`  sends a command to an ImapConnection and then reads the status response.
- `close()`  sets the open field to `false` and closes any attached I/O streams and the socket.
- `getOutputStream()`  returns an output stream.
- `sendSaslIrCommand(java.lang.String,java.lang.String,boolean)`  sends an SASL IR command to an IMAP connection and returns the command tag for the command.
- `readStatusResponse(java.lang.String,java.lang.String,com.fsck.k9.mail.store.imap.UntaggedHandler)`  reads an IMAP status response associated with a given tag, command and untaggedHandler.
- `isConnected()`  checks if the ImapConnection is connected and returns a Boolean value.

## class `com.fsck.k9.mail.store.imap.SelectOrExamineResponse`

This class  parses an IMAP response and returns an instance indicating whether the current mode is read-only or read-write.

This class contains the following public method(s):

- `getOpenMode()`  "returns the open mode of the command based on whether it is read-write or read-only".
- `parse(com.fsck.k9.mail.store.imap.ImapResponse)`  parses an IMAP response returning either an instance of the SelectOrExamineResponse class indicating whether the current mode is read-only or read-write, or null if the response is not valid.
- `hasOpenMode()`  returns whether or not the response has an open mode.

## class `com.fsck.k9.mail.store.imap.ImapUtility`

This class  provides utility methods for dealing with IMAP protocol operations.

This class contains the following public method(s):

- `getImapRangeValues(java.lang.String)`  expands a given number range to a list of individual numbers.
- `getImapSequenceValues(java.lang.String)`  takes a sequence set in the form of a string, splits the elements into individual numbers and ranges, and returns a list of those numbers as strings.
- `encodeString(java.lang.String)`  takes a string as an input and returns a quoted (IMAP) version of the same string.
- `getLastResponse(java.util.List)`  "retrieves the last ImapResponse from a List of ImapResponses."

## interface `com.fsck.k9.mail.store.imap.ImapSettings`

This interface  allows users to define the connection and authentication settings for an IMAP server connection.

This class contains the following public method(s):

- `getUsername()`  gets the username associated with an IMAP account.
- `getPassword()`  retrieves the password associated with an IMAP connection.
- `getConnectionSecurity()`  retrieves the connection security settings for an IMAP server.
- `setCombinedPrefix(java.lang.String)`  sets the prefix for combined IMAP folders.
- `getClientCertificateAlias()`  returns a client certificate alias from the IMAP settings.
- `getPort()`  "returns the port for the IMAP connection".
- `setPathDelimiter(java.lang.String)`  sets the path delimiter used to separate folder names in the IMAP server.
- `getPathDelimiter()`  returns the character used to separate folders in an IMAP message store.
- `setPathPrefix(java.lang.String)`  sets a sub-directory for the ImapSettings object.
- `getPathPrefix()`  returns the prefix of the IMAP mail folder path as a String.
- `getHost()`  returns the host as a String.
- `getCombinedPrefix()`  returns the combined prefix for an IMAP server.
- `useCompression(com.fsck.k9.mail.NetworkType)`  checks if compression should be used based on the given network type.
- `getAuthType()`  gets the authentication type associated with ImapSettings.

## class `com.fsck.k9.mail.store.imap.ImapResponse`

This class  provides a class that stores response tags, command continuation requests, and callback handlers for handling IMAP server responses.

This class contains the following public method(s):

- `newTaggedResponse(com.fsck.k9.mail.store.imap.ImapResponseCallback,java.lang.String)`  creates a new Tagged ImapResponse with the supplied tag and associated with the given response callback.
- `getTag()`  "returns the tag of the ImapResponse object".
- `toString()`  returns a string representation of the tag, command continuation request, and the super class's string representation.
- `setCallback(com.fsck.k9.mail.store.imap.ImapResponseCallback)`  sets an ImapResponseCallback for an ImapResponse.
- `newContinuationRequest(com.fsck.k9.mail.store.imap.ImapResponseCallback)`  creates a new ImapResponse with a callback and signals that this request requires a continuation.
- `getCallback()`  returns the specified `ImapResponseCallback`.
- `isTagged()`  checks if the `tag` field is not null.
- `isContinuationRequested()`  checks if the IMAP response signals a continuation request.
- `newUntaggedResponse(com.fsck.k9.mail.store.imap.ImapResponseCallback)`  creates an untagged ImapResponse with a provided callback handler.

## class `com.fsck.k9.mail.store.imap.FetchPartCallback`

This class  provides a way to process and store IMAP data, such as content types and transfer encodings, into a Body object.

This class contains the following public method(s):

- `foundLiteral(com.fsck.k9.mail.store.imap.ImapResponse,com.fsck.k9.mail.filter.FixedLengthInputStream)`  takes an ImapResponse and a FixedLengthInputStream, and it creates a Body object from the content transfer encoding and content type information in the ImapResponse.

## class `com.fsck.k9.mail.store.imap.ImapStore$StoreImapSettings`

This class  provides access to the settings associated with an IMAP store, such as the port, host, username, password, connection security type, authentication type, and path delimiter.

This class contains the following public method(s):

- `getPort()`  returns the port number.
- `getHost()`  returns the host string.
- `getConnectionSecurity()`  gets the connection security type of an IMAP store.
- `getUsername()`  returns the username.
- `setPathPrefix(java.lang.String)`  sets the IMAP path prefix.
- `getPathPrefix()`  returns the path prefix.
- `setCombinedPrefix(java.lang.String)`  sets the combined prefix for the ImapStore object.
- `getClientCertificateAlias()`  returns the alias of the client certificate associated with the ImapStore object.
- `setPathDelimiter(java.lang.String)`  sets the path delimiter for an IMAP store.
- `getAuthType()`  returns the authentication type specified in the ImapStore's StoreImapSettings.
- `getPathDelimiter()`  returns the character used as a delimiter for folder paths.
- `useCompression(com.fsck.k9.mail.NetworkType)`  checks the store configuration provided to determine if compression should be used for a specified network type.
- `getCombinedPrefix()`  returns the stored combined prefix value.
- `getPassword()`  returns the password stored in the ImapStore$StoreImapSettings object.

## class `com.fsck.k9.mail.store.imap.ImapFolderPusher`

This class  provides an automated way to push emails to an IMAP folder.

This class contains the following public method(s):

- `start()`  creates and starts a new thread responsible for pushing emails to an IMAP folder.
- `stop()`  stops any connections and threads for the `ImapFolderPusher` class.
- `refresh()`  stops the idle process for ImapFolderPusher.

## class `com.fsck.k9.mail.store.imap.ImapStoreUriDecoder`

This class  parses ImapStore URIs and converts them into ImapStoreSettings.

This class contains the following public method(s):

- `decode(java.lang.String)`  decodes an ImapStore URI into ImapStoreSettings.

## class `com.fsck.k9.mail.store.imap.FetchBodyCallback`

This class  stores the message associated with a given UID by parsing the ImapResponse and the FixedLengthInputStream.

This class contains the following public method(s):

- `foundLiteral(com.fsck.k9.mail.store.imap.ImapResponse,com.fsck.k9.mail.filter.FixedLengthInputStream)`  takes an ImapResponse and a FixedLengthInputStream and uses them to parse and store the message associated with the UID contained in the ImapResponse.

## class `com.fsck.k9.mail.store.imap.ImapPusher`

This class  handles and manages automatic refreshes of IMAP folders.

This class contains the following public method(s):

- `getRefreshInterval()`  gets the refresh interval set in the store configuration in milliseconds.
- `start(java.util.List)`  creates several `ImapFolderPusher` objects and starts them.
- `setLastRefresh(long)`  sets the last refresh time for the IMAP Pusher.
- `stop()`  requests a stop of all IMAP folder pushers and then clears the list of folder pushers.
- `refresh()`  refreshes the folder pushers for a given ImapPusher.
- `getLastRefresh()`  returns the last refresh time.

## class `com.fsck.k9.mail.store.imap.ImapFolderPusher$IdleStopper`

This class  stops the idle process of an IMAP folder pusher by setting the `acceptDoneContinuation` flag to false and sending a done signal.

This class contains the following public method(s):

- `stopAcceptingDoneContinuation()`  sets the value of the `acceptDoneContinuation` field to `false` and sets the `imapConnection` field to `null`.
- `startAcceptingDoneContinuation(com.fsck.k9.mail.store.imap.ImapConnection)`  starts an action to accept a Done continuation, given an IMAP connection.
- `stopIdle()`  stops the idle process of an IMAP folder pusher by setting the `acceptDoneContinuation` flag to false and sending a done signal.

## class `com.fsck.k9.mail.store.imap.NegativeImapResponseException`

This class  "provides a means for capturing an IMAP error response from the server and accessing the last response and associated alert text".

This class contains the following public method(s):

- `getLastResponse()`  retrieves the last ImapResponse from the `responses` List.
- `wasByeResponseReceived()`  determines whether the server responded with a "BYE" tag.
- `getAlertText()`  obtains the alert text from the last IMAP response.

## class `com.fsck.k9.mail.store.imap.FolderNameCodec`

This class  provides a way to encode and decode folder names from and to a modified UTF-7 charset.

This class contains the following public method(s):

- `decode(java.lang.String)`  decodes an encoded folder name from a modified UTF-7 charset to a string.
- `newInstance()`  creates a new instance of the `FolderNameCodec` class.
- `encode(java.lang.String)`  converts a given string to modified UTF-7 encoding using an ASCII character set.

## class `com.fsck.k9.mail.store.imap.CapabilityResponse`

This class  parses IMAP responses and provides the capabilities of the IMAP server.

This class contains the following public method(s):

- `parse(java.util.List)`  parses a list of IMAP responses and returns a `CapabilityResponse` object if valid in the response.
- `getCapabilities()`  returns a set of String containing all the capabilities of the IMAP server.

## interface `com.fsck.k9.mail.store.imap.ImapSearcher`

This interface  provides a method for searching an IMAP server and returning a list of search results.

This class contains the following public method(s):

- `search()`  searches an IMAP server and returns a list of ImapResponse objects.

## class `com.fsck.k9.mail.store.imap.AlertResponse`

This class  provides a method to extract an alert message from an IMAP response.

This class contains the following public method(s):

- `getAlertText(com.fsck.k9.mail.store.imap.ImapResponse)`  extracts a string containing an alert message from an IMAP response.

## class `com.fsck.k9.mail.store.imap.ImapList`

This class  provides methods to access, retrieve, and manipulate data from an ImapList object.

This class contains the following public method(s):

- `getList(int)`  returns the ImapList object located at the specified index.
- `getKeyedString(java.lang.String)`  returns the value associated with the provided key from the ImapList as a String.
- `getKeyedNumber(java.lang.String)`  parses a string into an integer and returns it.
- `isString(int)`  checks if the specified index contains a string object.
- `containsKey(java.lang.String)`  checks if a given key is present in the list.
- `getKeyedValue(java.lang.String)`  takes a String as an argument and returns the associated Object from the list.
- `getObject(int)`  returns the item at the specified index in the list.
- `getKeyedDate(java.lang.String)`  returns a Date object based on the string retrieved by the specified key.
- `getNumber(int)`  parses a string to an integer at the specified index.
- `getKeyIndex(java.lang.String)`  returns the index of an element in a collection that matches a given key.
- `getDate(int)`  retrieves the date at the specified index from the ImapList.
- `getString(int)`  returns the string stored in the given index.
- `isList(int)`  checks if the provided index is within range and returns a boolean value to indicate if the element at the index is an instance of `ImapList`.
- `getLong(int)`  parses a String representation of a long integer number and returns the long integer value.
- `getKeyedList(java.lang.String)`  retrieves a `com.fsck.k9.mail.store.imap.ImapList` object from a given key.

## interface `com.fsck.k9.mail.store.imap.UntaggedHandler`

This interface  provides a callback for asynchronous handling of untagged IMAP responses.

This class contains the following public method(s):

- `handleAsyncUntaggedResponse(com.fsck.k9.mail.store.imap.ImapResponse)`  handles an untagged IMAP response asynchronously.

## class `com.fsck.k9.mail.store.imap.ImapFolder`

This class  provides methods to access and manipulate an IMAP folder.

This class contains the following public method(s):

- `setFlags(java.util.Set,boolean)`  sets the specified flags of all messages in the IMAP folder to the specified value.
- `exists()`  checks if an IMAP folder exists by making a STATUS query to the IMAP server.
- `getMode()`  returns the value of the `mode` field.
- `setFlags(java.util.List,java.util.Set,boolean)`  sets the given flags for the given messages on the IMAP server.
- `moveMessages(java.util.List,com.fsck.k9.mail.Folder)`  copies a list of messages to another folder and sets the `DELETED` flag for each one.
- `search(java.lang.String,java.util.Set,java.util.Set)`  searches a remote ImapFolder according to the given query string, required flags, and forbidden flags specified, and returns a List of messages found.
- `getMessageCount()`  returns the total number of messages in the IMAP folder.
- `isOpen()`  "checks if an IMAP folder is open".
- `hashCode()`  returns a hash code for the ImapFolder object's name.
- `expunge()`  deletes all messages marked for deletion in the ImapFolder.
- `getNewPushState(java.lang.String,com.fsck.k9.mail.Message)`  updates a push state associated with a message given an old serialized push state.
- `delete(boolean)`  throws an error because it has not yet been implemented.
- `equals(java.lang.Object)`  checks if two ImapFolder objects have the same name (regardless of case) and returns a Boolean.
- `create(com.fsck.k9.mail.Folder$FolderType)`  creates a new folder by encoding and escaping the folder name provided and sending a CREATE command over an IMAP connection.
- `getFlaggedMessageCount()`  retrieves the number of flagged but undeleted messages in the remote ImapFolder.
- `getUidFromMessageId(com.fsck.k9.mail.Message)`  gets the UID of a message based on the Message-ID header.
- `getUnreadMessageCount()`  retrieves the number of unread messages in the folder.
- `copyMessages(java.util.List,com.fsck.k9.mail.Folder)`  copies a list of messages identified by their UIDs to the specified folder.
- `close()`  closes the folder connection.
- `getName()`  retrieves the folder name of an IMAP folder.
- `areMoreMessagesAvailable(int,java.util.Date)`  checks whether more messages are available in an IMAP folder given the index of the oldest message and the earliest date.
- `open(int)`  open an IMAP folder and throws a `MessagingException` if the message count is not found.
- `fetch(java.util.List,com.fsck.k9.mail.FetchProfile,com.fsck.k9.mail.MessageRetrievalListener)`  fetches the specified messages with the given FetchProfile and MessageRetrievalListener.
- `getMessage(java.lang.String)`  creates a new instance of the ImapMessage class with the given UID and the current ImapFolder instance.
- `delete(java.util.List,java.lang.String)`  moves messages to a specified folder, or sets the DELETED flag for the messages if the specified folder is the folder the messages are in.
- `appendMessages(java.util.List)`  appends the given messages to the selected folder, and determines the new UIDs of the given messages on the IMAP server.
- `fetchPart(com.fsck.k9.mail.Message,com.fsck.k9.mail.Part,com.fsck.k9.mail.MessageRetrievalListener,com.fsck.k9.mail.BodyFactory)`  fetches a part of a message in an IMAP folder and sets the body of the specified part to be used for the message.
- `getMessages(int,int,java.util.Date,com.fsck.k9.mail.MessageRetrievalListener)`  retrieves a list of ImapMessages in a specified range using the specified MessageRetrievalListener.

## class `com.fsck.k9.mail.store.imap.ImapStore`

This class  provides a connection to an IMAP server and enables the manipulation of its associated folders.

This class contains the following public method(s):

- `isCopyCapable()`  returns a boolean value indicating whether copying is supported by the ImapStore.
- `createUri(com.fsck.k9.mail.ServerSettings)`  creates an IMAP store URI from server settings.
- `getPusher(com.fsck.k9.mail.PushReceiver)`  returns a new ImapPusher object that provides push functionality for the associated PushReceiver.
- `getFolder(java.lang.String)`  creates a new ImapFolder object and adds it to the folderCache when one does not already exist for the given name.
- `isMoveCapable()`  returns a boolean value that indicates if the ImapStore is move capable or not.
- `checkSettings()`  creates a connection to an IMAP server and configures the folders accordingly.
- `getPersonalNamespaces(boolean)`  gets the personal namespaces from the IMAP store based on whether subscribed folders only is enabled or not.
- `isPushCapable()`  returns `true` to indicate that the ImapStore is push capable.
- `isExpungeCapable()`  returns a boolean indicating whether the IMAP store is expunge capable.
- `decodeUri(java.lang.String)`  decodes an IMAP store URI and returns an ImapStoreSettings instance.

## class `com.fsck.k9.mail.store.imap.ImapFolderPusher$PushRunnable`

This class  handles asynchronous responses from an IMAP server and sends out notifications while looping and allowing for repetitive errors.

This class contains the following public method(s):

- `handleAsyncUntaggedResponse(com.fsck.k9.mail.store.imap.ImapResponse)`  handles an asynchronous response from an IMAP server and wakes up the connection if necessary.
- `run()`  runs a loop that acquires a wake lock, checks for new messages, and sends out notifications while allowing for repetitive errors before stopping.

## class `com.fsck.k9.mail.store.imap.CopyUidResponse`

This class  parses a provided ImapResponse object and returns a mapping of source UIDs to destination UIDs.

This class contains the following public method(s):

- `parse(com.fsck.k9.mail.store.imap.ImapResponse)`  takes in an ImapResponse object as an argument and returns a CopyUidResponse object containing a mapping of source UIDs to destination UIDs.
- `getUidMapping()`  returns a map of source UIDs to target UIDs.

## class `com.fsck.k9.mail.store.imap.ListResponse`

This class  parses a list of ImapResponses and returns a list of ListResponses with associated hierarchy delimiter and attributes.

This class contains the following public method(s):

- `getHierarchyDelimiter()`  returns the hierarchy delimiter associated with a ListResponse.
- `parseList(java.util.List)`  parses a list of ImapResponse objects into a list of ListResponse objects.
- `getName()`  returns the name of the ListResponse object.
- `parseLsub(java.util.List)`  parses a list of ImapResponses and returns a list of ListResponses.
- `getAttributes()`  retrieves a list of strings corresponding to the attributes of the ListResponse object.
- `hasAttribute(java.lang.String)`  checks if the given attribute is in the list of attributes.


# package `com.fsck.k9.mail.store.pop3`

This package  provides the necessary methods for interacting with a POP3 email server, including generating a formatted string of enabled POP3 features, reading characters from an input stream, creating and decoding a Pop3Store URI, retrieving messages, creating folders, deleting messages, and manipulating Pop3 mail messages.

This package contains the following class(es):

## class `com.fsck.k9.mail.store.pop3.Pop3Store$Pop3Capabilities`

This class  
generates a formatted string of the enabled POP3 features for a given server.

This class contains the following public method(s):

- `toString()`  returns a formatted string of the Pop3Capabilities' enabled features.

## class `com.fsck.k9.mail.store.pop3.Pop3Store$Pop3ResponseInputStream`

This class :

Reads characters from an input stream and checks whether the end of the line has been reached.

This class contains the following public method(s):

- `read()`  reads a character from the input stream and checks if it is the end of line (EOL) character.

## class `com.fsck.k9.mail.store.pop3.Pop3Store`

This class  provides methods for creating, decoding and checking an encoded Pop3Store URI, as well as getting a Pop3Folder and a list of Folder objects that contain the inbox folder name.

This class contains the following public method(s):

- `isSeenFlagSupported()`  determines whether the seen flag is supported by the POP3 store.
- `createUri(com.fsck.k9.mail.ServerSettings)`  creates a Pop3Store URI string based on the supplied server settings.
- `decodeUri(java.lang.String)`  takes an encoded Pop3Store URI as a parameter and decodes it into a `ServerSettings` object.
- `getFolder(java.lang.String)`  returns a Pop3Folder object based on a given name from the mFolders map.
- `getPersonalNamespaces(boolean)`  returns a list of `Folder` objects that contain the inbox folder name.
- `checkSettings()`  checks for the capability to use UIDL commands on the pop3 server, and throws a MessagingException if it is not supported.

## class `com.fsck.k9.mail.store.pop3.Pop3Store$Pop3Message`

This class  provides methods to manipulate Pop3 mail messages.

This class contains the following public method(s):

- `setFlag(com.fsck.k9.mail.Flag,boolean)`  sets the specified flag for the current message and also sets flags in the folder.
- `delete(java.lang.String)`  marks a message as deleted.
- `setSize(int)`  sets the size of the Pop3Message.

## class `com.fsck.k9.mail.store.pop3.Pop3Store$Pop3Folder`

This class  provides methods for interacting with a POP3 email folder, such as retrieving messages, creating folders, deleting messages, etc.

This class contains the following public method(s):

- `setFlags(java.util.Set,boolean)`  throws an UnsupportedOperationException if an attempt is made to use the setFlags(java.util.Set,boolean) method on a Pop3Folder instance.
- `getMessage(java.lang.String)`  retrieves a corresponding Pop3Message object for a given UID.
- `equals(java.lang.Object)`  compares the given object `o` to the `Pop3Folder` of which it is a member, and returns whether they are equal.
- `getName()`  returns the name of the Pop3Folder object.
- `close()`  sends a QUIT command to the server and closes the input and output streams.
- `getUnreadMessageCount()`  returns the number of unread messages in the associated folder.
- `delete(java.util.List,java.lang.String)`  sets the "DELETED" Flag on an provided list of messages.
- `supportsFetchingFlags()`  returns a boolean value indicating whether flag fetching is supported.
- `getMessages(int,int,java.util.Date,com.fsck.k9.mail.MessageRetrievalListener)`  returns a List of Pop3Message objects that are between two specified indices, and optionally calls specified MessageRetrievalListeners for each message.
- `areMoreMessagesAvailable(int,java.util.Date)`  checks if there are more messages available than the index of the oldest message.
- `getUidFromMessageId(com.fsck.k9.mail.Message)`  gets a UID from a given message ID.
- `getMode()`  returns the read-write open mode of a POP3 folder.
- `appendMessages(java.util.List)`  adds one or more messages to a POP3 email folder and returns a mapping of the message UIDs.
- `open(int)`  opens a connection to the POP3 server and authenticates the user, if necessary.
- `isOpen()`  checks if the pop3 folder is open.
- `create(com.fsck.k9.mail.Folder$FolderType)`  returns a boolean value indicating whether it successfully created a folder of the specified type.
- `isFlagSupported(com.fsck.k9.mail.Flag)`  checks if a given flag is supported by the Pop3Folder class.
- `getMessageCount()`  returns the total number of messages in the folder.
- `delete(boolean)`  allows the deletion of a POP3 folder.
- `fetch(java.util.List,com.fsck.k9.mail.FetchProfile,com.fsck.k9.mail.MessageRetrievalListener)`  fetches items specified by a fetch profile into a given set of messages in the most efficient way.
- `exists()`  checks whether the folder exists by comparing the current folder name to the inbox folder name.
- `getFlaggedMessageCount()`  returns -1 for the count of flagged messages.
- `hashCode()`  calculates a numerical hash code for the `Pop3Folder` object based on its name.
- `setFlags(java.util.List,java.util.Set,boolean)`  sets the Deleted flag to true for a list of messages provided as arguments.


# package `com.fsck.k9.mail.store.webdav`

This package  provides classes which enable users to access and manipulate messages stored in a webDAV mail store.

This package contains the following class(es):

## class `com.fsck.k9.mail.store.webdav.DataSet`

This class  "provides methods to manage message data covers such as Message UIDs, URLs, special folder names and Read Status".

This class contains the following public method(s):

- `getUids()`  returns a list of all message UIDs from a Dataset.
- `getHrefs()`  returns an array of URLs stored in a `DataSet` object.
- `getMessageEnvelopes()`  creates a map of message UIDs and an associated ParsedMessageEnvelope by extracting data from the mData field.
- `getSpecialFolderToUrl()`  creates a map of special folder names to special folder URLs.
- `getUidToRead()`  returns a HashMap associating Message UIDs with their Read Status.
- `finish()`  adds a temporary data item and its unique ID to the main data set, and then creates a new hashmap for the temporary data items.
- `getMessageCount()`  returns the total message count of the mailbox as it was retrieved.
- `addValue(java.lang.String,java.lang.String)`  adds the specified value to a tag name, either appending it to an existing tag or creating a new one in a map.
- `getUidToUrl()`  creates a map of message UIDs and their URLs.

## class `com.fsck.k9.mail.store.webdav.WebDavHttpClient`

This class  modifies and executes HttpUriRequests with the ability to accept and decode gzipped responses.

This class contains the following public method(s):

- `executeOverride(org.apache.http.client.methods.HttpUriRequest,org.apache.http.protocol.HttpContext)`  modifies a given HttpUriRequest to accept Gzip responses, and then executes it using the parent class.
- `modifyRequestToAcceptGzipResponse(org.apache.http.HttpRequest)`  adds a header to the `HttpRequest` object to accept gzip-encoded responses.
- `getUngzippedContent(org.apache.http.HttpEntity)`  decodes the response stream from a compressed gzipped format, if necessary, and returns an ungzipped response stream.

## class `com.fsck.k9.mail.store.webdav.WebDavHttpClient$WebDavHttpClientFactory`

This class  provides a factory for creating instances of the `WebDavHttpClient` class.

This class contains the following public method(s):

- `create()`  creates an instance of the `WebDavHttpClient` class.

## class `com.fsck.k9.mail.store.webdav.WebDavStoreSettings`

This class  provides methods for creating and getting information from a WebDavStoreSettings object, which stores data related to a WebDav-based mail store.

This class contains the following public method(s):

- `getExtra()`  returns a map of Strings, which contains aliased, path, authorized path and mailbox path as key-value pairs.
- `newPassword(java.lang.String)`  creates a new WebDavStoreSettings object, populated with the same data as the original object except for the new password passed as parameter.

## class `com.fsck.k9.mail.store.webdav.WebDavHandler`

This class  "parses and stores webDAV requests and responses".

This class contains the following public method(s):

- `getDataSet()`  returns the `DataSet` instance associated with `WebDavHandler`.
- `endElement(java.lang.String,java.lang.String,java.lang.String)`  finishes the data set and removes the first element from the list of open tags.
- `startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)`  adds a local name to the top of an open tags list.
- `endDocument()`  does nothing.
- `startDocument()`  initializes a new `DataSet` instance.
- `characters(char[],int,int)`  takes a character array, start index and length, and adds the corresponding substring of the character array to the current top of the open tags stack.

## class `com.fsck.k9.mail.store.webdav.WebDavStoreUriCreator`

This class  creates a WebDavStore URI based on the server settings provided.

This class contains the following public method(s):

- `create(com.fsck.k9.mail.ServerSettings)`  creates a WebDavStore URI using the supplied settings from the input parameter `ServerSettings` object.

## class `com.fsck.k9.mail.store.webdav.WebDavStoreUriDecoder`

This class  provides a mechanism to parse and decode WebDavStore URIs into an object (`WebDavStoreSettings`) containing all relevant information.

This class contains the following public method(s):

- `decode(java.lang.String)`  decodes a WebDavStore URI and returns a WebDavStoreSettings object containing all relevant info.

## class `com.fsck.k9.mail.store.webdav.HttpGeneric`

This class  provides a utility to generate and set HTTP request methods.

This class contains the following public method(s):

- `getMethod()`  returns a string that contains the HTTP request method name for the HTTPGeneric class.
- `setMethod(java.lang.String)`  sets the METHOD_NAME field of the class to the given parameter.

## class `com.fsck.k9.mail.store.webdav.WebDavMessage`

This class  enables the manipulation and storage of messages in a WebDAV store.

This class contains the following public method(s):

- `setFlagInternal(com.fsck.k9.mail.Flag,boolean)`  sets a flag for a message in a webDAV store.
- `setSize(int)`  sets the size of the `WebDavMessage` object.
- `setFlag(com.fsck.k9.mail.Flag,boolean)`  sets the requested flag to a specified value for the current message.
- `setUrl(java.lang.String)`  takes a URL as an argument and creates a properly encoded URL built from the given URL using the folder's URL.
- `delete(java.lang.String)`  moves the message to a trash folder.
- `setNewHeaders(com.fsck.k9.mail.store.webdav.ParsedMessageEnvelope)`  parses envelope headers and adds them to the message headers of the WebDavMessage object.
- `getUrl()`  returns a String representing the URL of a WebDavMessage.

## class `com.fsck.k9.mail.store.webdav.ParsedMessageEnvelope`

This class  provides methods for getting, setting, and adding message headers to a parsed message envelope.

This class contains the following public method(s):

- `getMessageHeaders()`  returns the map of message headers.
- `addHeader(java.lang.String,java.lang.String)`  adds a header field and value to be included in a parsed message envelope.
- `setReadStatus(boolean)`  sets the read status of the `ParsedMessageEnvelope` to the value of the `status` parameter.
- `setUid(java.lang.String)`  sets the UID for the current `ParsedMessageEnvelope` object.
- `getHeaderList()`  retrieves the list of headers in the specified message envelope as a string array.
- `getUid()`  returns the unique identifier of the message envelope.
- `getReadStatus()`  returns the read status of the `ParsedMessageEnvelope` object.

## class `com.fsck.k9.mail.store.webdav.WebDavFolder`

This class  provides the ability to retrieve messages, append messages, create a folder, get the URL, delete messages, move or copy messages, and open the WebDAV folder in a specified mode with the `HttpClient`.

This class contains the following public method(s):

- `getMessages(int,int,java.util.Date,com.fsck.k9.mail.MessageRetrievalListener)`  gets a list of WebDavMessages from a WebDavFolder within a given range and a given date.
- `appendMessages(java.util.List)`  appends the given list of messages to a WebDav folder.
- `create(com.fsck.k9.mail.Folder$FolderType)`  creates a folder of the given type.
- `getUrl()`  returns the URL of the WebDavFolder.
- `isOpen()`  checks whether the folder is open or not.
- `delete(java.util.List,java.lang.String)`  moves or copies a list of messages to a trash folder.
- `moveMessages(java.util.List,com.fsck.k9.mail.Folder)`  moves the given messages in the passed folder.
- `exists()`  returns `true` to indicate that the folder exists.
- `appendWebDavMessages(java.util.List)`  uploads the given messages to the webDAV folder and returns added messages as a list.
- `setUrl(java.lang.String)`  sets the folder URL for the WebDavFolder object.
- `delete(boolean)`  throws an `Error` when it is called as it is not yet implemented.
- `areMoreMessagesAvailable(int,java.util.Date)`  returns whether there are more messages available than the one with the given index that were sent before the given date.
- `copyMessages(java.util.List,com.fsck.k9.mail.Folder)`  copies a list of messages to a given folder.
- `equals(java.lang.Object)`  checks if the given object is an instance of a `WebDavFolder`, and if so, determines if the object's name is equal to the name of the object in which this method is called on.
- `getName()`  returns the name of the WebDavFolder object.
- `getMode()`  returns the open mode of the folder as read/write access (`OPEN_MODE_RW`).
- `setFlags(java.util.Set,boolean)`  logs an error message for unimplemented functionality when trying to call the methods `markAllMessagesAsRead` and `EmptyTrash`.
- `getFlaggedMessageCount()`  returns -1 as the flagged message count.
- `close()`  sets the message count, unread message count, and open status of a WebDavFolder to 0 and false, respectively.
- `getUidFromMessageId(com.fsck.k9.mail.Message)`  throws a timber log Timber.e message to alert of an unimplemented method, and it returns null.
- `getUnreadMessageCount()`  opens the folder in read/write mode and retrieves the number of unread messages.
- `getMessageCount()`  opens this WebDavFolder using read-write mode, stores the number of messages in this folder in the mMessageCount property, and then returns the mMessageCount.
- `setFlags(java.util.List,java.util.Set,boolean)`  sets flags (such as seen or deleted) for multiple messages based on the the given boolean value.
- `fetch(java.util.List,com.fsck.k9.mail.FetchProfile,com.fsck.k9.mail.MessageRetrievalListener)`  fetches envelope, flags, body, and/or bodies of messages in a specified list from a WebDAV folder given a certain fetch profile.
- `getMessage(java.lang.String)`  returns a WebDavMessage object given the UID.
- `open(int)`  opens the `WebDavFolder` with the given mode, allowing the `HttpClient` to be used.

## class `com.fsck.k9.mail.store.webdav.WebDavSocketFactory`

This class  provides methods for creating an SSL socket and for connecting it to a host using specified parameters.

This class contains the following public method(s):

- `createSocket(java.net.Socket,java.lang.String,int,boolean)`  creates an SSL socket from an existing socket using the specified host, port, and auto close value.
- `createSocket()`  creates a socket using the internal `mSocketFactory` object.
- `isSecure(java.net.Socket)`  checks if a given socket is secure.
- `connectSocket(java.net.Socket,java.lang.String,int,java.net.InetAddress,int,org.apache.http.params.HttpParams)`  connects a socket to a host at a specified port, using a given socket, InetAddress, port, and HttpParams.

## class `com.fsck.k9.mail.store.webdav.WebDavStore`

This class  provides methods for authentication, decoding, sending, and retrieving folders, as well as other operations related to webdav communications.

This class contains the following public method(s):

- `createUri(com.fsck.k9.mail.ServerSettings)`  creates and returns a uniform resource identifier (URI).
- `sendMessages(java.util.List)`  takes a list of messages, appends them to a drafts folder, and then moves them to a send spool folder.
- `getAuthCookies()`  returns the `authCookies` cookie store.
- `getAuthString()`  retrieves the authentication string for the WebDavStore.
- `isCopyCapable()`  returns a boolean value indicating whether the WebDavStore is capable of copying objects.
- `isMoveCapable()`  returns a boolean value indicating whether the WebDavStore is capable of performing moves.
- `getFolder(java.lang.String)`  retrieves a WebDav folder based on the inputted name.
- `isSendCapable()`  checks if the WebDavStore is capable of sending messages.
- `getUrl()`  returns the base URL of a WebDavStore.
- `checkSettings()`  authenticates the WebDavStore.
- `getAlias()`  returns the value of the `alias` field.
- `getPersonalNamespaces(boolean)`  gets a list of folders by validating the authentication and collecting data from PROPFIND and SEARCH requests.
- `decodeUri(java.lang.String)`  decodes a given URI to a `WebDavStoreSettings` object.
- `getHttpClient()`  creates, configures, and returns an `httpClient` object.


# package `com.fsck.k9.mail.store`

This package  provides an abstract class and an interface to enable applications to manage remote mail stores and their associated credentials.

This package contains the following class(es):

## abstract class `com.fsck.k9.mail.store.RemoteStore`

This abstract class  provides an interface that enables applications to manage remote mail stores and their associated credentials.

This class contains the following public method(s):

- `removeInstance(com.fsck.k9.mail.store.StoreConfig)`  removes the reference to a remote mail store instance based on the StoreConfig instance that is supplied.
- `decodeStoreUri(java.lang.String)`  decodes a store-specific URI and makes a ServerSettings object with the newly decoded contents.
- `getInstance(android.content.Context,com.fsck.k9.mail.store.StoreConfig)`  gets an instance of a remote mail store based on the given URI and context.
- `createStoreUri(com.fsck.k9.mail.ServerSettings)`  creates a store URI from the information contained in a `com.fsck.k9.mail.ServerSettings` object.

## interface `com.fsck.k9.mail.store.StoreConfig`

This interface  provides methods to configure different elements of a mail store.

This class contains the following public method(s):

- `setSentFolderName(java.lang.String)`  sets the name of the sent folder for a store configuration.
- `getMaximumAutoDownloadMessageSize()`  requests the maximum size of an email message that can be auto-downloaded.
- `isPushPollOnConnect()`  checks if a push poll is enabled on connect.
- `setArchiveFolderName(java.lang.String)`  sets the name of the folder used for archiving emails.
- `setInboxFolderName(java.lang.String)`  sets the name of the inbox folder of the store configuration.
- `subscribedFoldersOnly()`  returns whether the store should only return subscribed folders.
- `setTrashFolderName(java.lang.String)`  sets the name of the trash folder in a StoreConfig object.
- `allowRemoteSearch()`  checks if remote search is allowed.
- `getStoreUri()`  returns the store's Uniform Resource Identifier (URI).
- `getIdleRefreshMinutes()`  **returns the idle refresh minutes** set in the store configuration.
- `setAutoExpandFolderName(java.lang.String)`  sets the name of the folder to be automatically expanded by the store config.
- `setSpamFolderName(java.lang.String)`  lets the user set a name for a Spam folder.
- `isRemoteSearchFullText()`  checks whether remote searches should use full text.
- `getInboxFolderName()`  returns the name of the Inbox folder for the mail store.
- `getOutboxFolderName()`  returns the folder name of the outbox used for outgoing messages.
- `setDraftsFolderName(java.lang.String)`  sets the name of the drafts folder in the store configuration.
- `getDisplayCount()`  "gets the display count for the given store configuration."
- `getDraftsFolderName()`  returns a String containing the name of the folder for drafts.
- `useCompression(com.fsck.k9.mail.NetworkType)`  checks whether compression should be used for the given network type.
- `getTransportUri()`  returns a URI used for connecting to the mail server's transport service.


