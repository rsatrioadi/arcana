# package `com.fsck.k9.mail`

This package provides classes and interfaces for handling email messaging, including sending and receiving emails, managing email stores, and handling authentication and certificate validation.

This package contains the following class(es):

## class `com.fsck.k9.mail.MessagingException`

This class handles exceptions related to email messaging in a Java program.

This class contains the following public method(s):

- `isPermanentFailure()` returns a boolean value indicating whether the messaging exception is a permanent failure or not.
- `setPermanentFailure(boolean)` (no description)

## interface `com.fsck.k9.mail.K9MailLib$DebugStatus`

This interface provides methods to check if debugging is enabled and if sensitive debugging information is enabled in K9MailLib.

This class contains the following public method(s):

- `debugSensitive()` returns a boolean value indicating whether sensitive debugging information is enabled or not.
- `enabled()` returns a boolean value indicating whether debugging is currently enabled in the K9MailLib.

## class `com.fsck.k9.mail.K9MailLib$DefaultDebugStatus`

This class provides methods for managing the debug status and sensitivity of the K9MailLib mail library.

This class contains the following public method(s):

- `debugSensitive()` returns a boolean value indicating whether sensitive debugging information should be displayed.
- `enabled()` returns a boolean value indicating whether debugging is enabled or not in the K9MailLib library's default debug status.
- `setEnabled(boolean)` sets the enabled status of the debug status in K9MailLib to a given boolean value.
- `setSensitive(boolean)` sets the sensitivity status of a default debug status object in the K9MailLib mail library.

## interface `com.fsck.k9.mail.Part`

This interface provides methods to access and manipulate various properties and contents of an email message part.

This class contains the following public method(s):

- `getContentType()` returns the content type of a mail part.
- `getBody()` returns the body of an email message as a com.fsck.k9.mail.Body object in Java.
- `setServerExtra(java.lang.String)` sets a string representing extra data associated with the email part on the server.
- `getHeader(java.lang.String)` returns an array of headers with the given name.
- `getServerExtra()` returns the extra server-specific information of an email message part.
- `addHeader(java.lang.String,java.lang.String)` adds a header with a specified name and value to a mail part.
- `getContentId()` returns the content ID of the email part.
- `setBody(com.fsck.k9.mail.Body)` sets the body of the email message.
- `getDisposition()` returns the disposition of the email part.
- `addRawHeader(java.lang.String,java.lang.String)` adds a raw header with the specified name and value to the Part.
- `setHeader(java.lang.String,java.lang.String)` sets the value of a specified header in an email part.
- `writeTo(java.io.OutputStream)` writes the contents of the email part to an output stream.
- `removeHeader(java.lang.String)` removes a header with the given name from the Part.
- `isMimeType(java.lang.String)` checks if the MIME type of the email part matches the specified MIME type.
- `getMimeType()` returns the MIME type of the email message part.
- `writeHeaderTo(java.io.OutputStream)` writes the header of the email part to an output stream.

## abstract class `com.fsck.k9.mail.Transport`

This abstract class defines the methods required to establish a connection to a mail server and send email messages.

This class contains the following public method(s):

- `open()` opens a connection to a mail server and throws a messaging exception if there is a problem.
- `close()` closes the connection used by the email transport.
- `sendMessage(com.fsck.k9.mail.Message)` sends a mail message using the specified transport.

## abstract class `com.fsck.k9.mail.Store`

This abstract class defines a set of methods that allow interactions with a mail store, including retrieving and manipulating email messages, sending email, and checking mail settings.

This class contains the following public method(s):

- `isCopyCapable()` returns a boolean value representing whether the Store is capable of copying emails or not.
- `getFolder(java.lang.String)` returns a mail folder with the given name, containing messages of a certain type.
- `isExpungeCapable()` returns a boolean value indicating whether the mail store is capable of expunging (permanently deleting) messages.
- `getPusher(com.fsck.k9.mail.PushReceiver)` returns a null `Pusher` object when given a `PushReceiver` object.
- `isSendCapable()` returns whether the mail store is capable of sending email or not.
- `isSeenFlagSupported()` returns a boolean value indicating whether the email client supports the "seen" flag for marking emails as read.
- `getPersonalNamespaces(boolean)` gets the list of personal email folders for the current user, with an option to forcefully reload all folder list.
- `sendMessages(java.util.List)` sends a list of email messages using the K-9 mail library.
- `checkSettings()` checks the settings of a mail store implementation and throws a `MessagingException` if there are any issues.
- `isMoveCapable()` returns a boolean value indicating whether the Store implementation is capable of moving messages between folders.
- `isPushCapable()` checks whether the email store is capable of pushing email notifications, and returns a boolean value accordingly.

## class `com.fsck.k9.mail.Address`

This class provides methods to handle parsing, encoding, and manipulation of email addresses and personal names.

This class contains the following public method(s):

- `pack(com.fsck.k9.mail.Address[])` packs an array of email addresses into a String that is easy to read and parse.
- `parse(java.lang.String)` parses a comma separated list of email addresses in RFC-822 format and returns an array of Address objects.
- `toEncodedString(com.fsck.k9.mail.Address[])` takes an array of email addresses and returns a string representation of those addresses, encoded for transmission over the internet.
- `hashCode()` calculates a hash code for an email address object based on its email address and personal name, if available.
- `getHostname()` returns the hostname part of an email address stored in the `mAddress` variable of an instance of the `Address` class.
- `quoteAtoms(java.lang.String)` quotes a string based on the definition of an "atom" as specified in RFC2822.
- `getPersonal()` returns the personal name associated with the email address.
- `equals(java.lang.Object)` checks whether two email `Address` objects are equal based on their email addresses and personal names.
- `toString(com.fsck.k9.mail.Address[])` takes an array of email addresses and returns a concatenated string representation of those addresses separated by commas.
- `getAddress()` returns the email address associated with a `com.fsck.k9.mail.Address` object.
- `unpack(java.lang.String)` unpacks a packed address list and returns an array of email addresses.
- `parseUnencoded(java.lang.String)` parses a comma separated list of human readable email addresses and returns an array of corresponding Address objects encoded according to the RFC-822 standard.
- `toString()` returns a string representation of an email address, including the personal name if available.
- `toEncodedString()` returns an encoded string representation of an email Address object, including the personal name if it is present.
- `setPersonal(java.lang.String)` sets the "personal" name associated with an email address while handling empty or null inputs.
- `setAddress(java.lang.String)` sets the email address of an instance of the `Address` class.

## class `com.fsck.k9.mail.Authentication`

This class provides methods to compute and handle authentication for email accounts.

This class contains the following public method(s):

- `computeXoauth(java.lang.String,java.lang.String)` computes an XOAuth authentication string using a given username and authentication token and returns it as a base64-encoded string.
- `computeCramMd5Bytes(java.lang.String,java.lang.String,byte[])` calculates the response for CRAM-MD5 authentication by taking in the user credentials and server-provided nonce.
- `computeCramMd5(java.lang.String,java.lang.String,java.lang.String)` computes the response for CRAM-MD5 authentication mechanism given the user credentials and server-provided nonce.

## interface `com.fsck.k9.mail.Body`

This interface provides methods to handle different transfer encodings for the body of an email message.

This class contains the following public method(s):

- `writeTo(java.io.OutputStream)` writes the body's data to an OutputStream with transfer encoding (such as Base64).
- `getInputStream()` returns the raw data of the body without any encoding applied.
- `setEncoding(java.lang.String)` sets the content transfer encoding for the body of an email message.

## class `com.fsck.k9.mail.CertificateValidationException`

This class represents an exception that occurs during certificate validation in email communication.

This class contains the following public method(s):

- `getAlias()` returns the alias of the certificate that caused the validation exception.
- `needsUserAttention()` returns a boolean value indicating whether the certificate validation exception needs user attention or not.
- `getReason()` returns the reason for a certificate validation exception in the form of a `Reason` object.
- `getCertChain()` returns the X509Certificate chain if it is available, otherwise it returns null.

## class `com.fsck.k9.mail.BoundaryGenerator`

This class generates a unique boundary string for use in email messages.

This class contains the following public method(s):

- `generateBoundary()` generates a random boundary string for use in email messages.
- `getInstance()` returns the instance of the `BoundaryGenerator` class.

## abstract class `com.fsck.k9.mail.BodyPart`

This abstract class represents a part of an email message and provides methods for setting and retrieving its encoding, parent, and serverExtra fields.

This class contains the following public method(s):

- `setEncoding(java.lang.String)` sets the encoding for the body part content of an email message.
- `setParent(com.fsck.k9.mail.Multipart)` sets the parent `Multipart` of the current `BodyPart`.
- `getParent()` returns the `Multipart` parent of the `BodyPart`.
- `setServerExtra(java.lang.String)` sets the serverExtra field value in a BodyPart object.
- `getServerExtra()` returns the serverExtra string variable of the BodyPart object.

## class `com.fsck.k9.mail.TransportUris`

This class provides methods for decoding and creating transport-specific URIs and ServerSettings objects in Java.

This class contains the following public method(s):

- `decodeTransportUri(java.lang.String)` decodes transport-specific URIs into a ServerSettings object.
- `createTransportUri(com.fsck.k9.mail.ServerSettings)` creates a transport URI from the information provided in a ServerSettings object.

## class `com.fsck.k9.mail.DefaultBodyFactory`

This class creates a mail body object from an input stream and content transfer encoding and content type parameters.

This class contains the following public method(s):

- `createBody(java.lang.String,java.lang.String,java.io.InputStream)` creates a mail body object from an input stream and content transfer encoding and content type parameters.

## interface `com.fsck.k9.mail.MessageRetrievalListener`

This interface provides callbacks for events related to the retrieval of email messages.

This class contains the following public method(s):

- `messageFinished(com.fsck.k9.mail.Message,int,int)` notifies the listener that a message has been fully retrieved and provides information about its position in the sequence of retrieved messages.
- `messagesFinished(int)` notifies the listener that all messages have been retrieved and provides the total number of messages retrieved.
- `messageStarted(java.lang.String,int,int)` notifies the listener that a message has started downloading, providing details such as the message UID, its position within the message list and the total number of messages.

## interface `com.fsck.k9.mail.BodyFactory`

This interface provides a method to create a mail body with specified characteristics.

This class contains the following public method(s):

- `createBody(java.lang.String,java.lang.String,java.io.InputStream)` creates a mail body with the specified content transfer encoding, content type, and input stream.

## interface `com.fsck.k9.mail.Pusher`

This interface provides methods for managing and controlling push notification services for email communication.

This class contains the following public method(s):

- `getLastRefresh()` returns the timestamp of the last refresh made by the mail pusher.
- `setLastRefresh(long)` sets the timestamp for the last refresh of the Pusher.
- `getRefreshInterval()` returns the required refresh interval in milliseconds for a push service.
- `stop()` stops the pushing of email notifications.
- `refresh()` triggers a refresh operation for the underlying email server.
- `start(java.util.List)` starts the push service for a list of folder names in email communication.

## class `com.fsck.k9.mail.K9MailLib`

This class provides methods for setting and checking the debug status of the K9MailLib Java class.

This class contains the following public method(s):

- `setDebugStatus(com.fsck.k9.mail.K9MailLib$DebugStatus)` sets the debug status for the K9MailLib Java class.
- `isDebug()` returns whether debug mode is enabled in the K9MailLib Java class.
- `setDebugSensitive(boolean)` sets the debug sensitive flag to true or false depending on the value passed as a parameter.
- `isDebugSensitive()` returns whether the K9MailLib debugging mode is set to sensitive.
- `setDebug(boolean)` sets the debug status of the K9MailLib library to the specified boolean value.

## class `com.fsck.k9.mail.ServerSettings`

This class provides settings for storing and transporting emails and includes methods for creating new instances with updated certificate alias or password and comparing equality between instances.

This class contains the following public method(s):

- `getExtra()` returns additional settings as a key/value pair specific to either storing or transporting emails.
- `newClientCertificateAlias(java.lang.String)` creates a new instance of ServerSettings with a new certificate alias.
- `newPassword(java.lang.String)` creates a new `ServerSettings` object with a new password and returns it.
- `equals(java.lang.Object)` compares two ServerSettings objects to see if they are equal.

## interface `com.fsck.k9.mail.K9MailLib$WritableDebugStatus`

This interface provides methods to control and modify the debug status of the K9MailLib library.

This class contains the following public method(s):

- `setSensitive(boolean)` sets whether the debug status is sensitive or not.
- `setEnabled(boolean)` enables or disables the debug status of the K9MailLib.

## class `com.fsck.k9.mail.TransportProvider`

This class provides a way to get a mail transport object based on the provided store configuration using SMTP and WebDav protocols.

This class contains the following public method(s):

- `getInstance()` returns the instance of the TransportProvider class.
- `getTransport(android.content.Context,com.fsck.k9.mail.store.StoreConfig)` returns a mail transport object based on the provided store configuration, with support for SMTP and WebDav protocols.

## interface `com.fsck.k9.mail.PushReceiver`

This interface provides methods for handling push notifications in an email messaging system.

This class contains the following public method(s):

- `messagesRemoved(com.fsck.k9.mail.Folder,java.util.List)` notifies the receiver that messages have been removed from a specific folder.
- `messagesFlagsChanged(com.fsck.k9.mail.Folder,java.util.List)` notifies the push receiver that the flags of one or more messages in a certain folder have changed.
- `syncFolder(com.fsck.k9.mail.Folder)` synchronizes the specified email folder with the remote email server.
- `authenticationFailed()` notifies that authentication has failed in a push email receiver.
- `getContext()` returns the Android context associated with the PushReceiver interface.
- `messagesArrived(com.fsck.k9.mail.Folder,java.util.List)` notifies the push receiver that new messages have arrived in a certain folder.
- `setPushActive(java.lang.String,boolean)` enables or disables push notifications for a specific email folder.
- `getPushState(java.lang.String)` returns the push state for a given email folder.
- `sleep(com.fsck.k9.mail.power.TracingPowerManager$TracingWakeLock,long)` puts the thread to sleep for the specified amount of time while holding the provided wake lock.
- `pushError(java.lang.String,java.lang.Exception)` is used for reporting errors that occur during push messaging.

## enum `com.fsck.k9.mail.NetworkType`

This enum provides a mapping between Android ConnectivityManager network types and K-9 Mail network types.

This class contains the following public method(s):

- `fromConnectivityManagerType(int)` converts an integer representing a type of network connectivity from the Android ConnectivityManager class to a corresponding network type in the K-9 Mail app.

## abstract class `com.fsck.k9.mail.Multipart`

This abstract class provides methods for handling multipart MIME messages in Java.

This class contains the following public method(s):

- `getMimeType()` returns the MIME type of the multipart message.
- `getEpilogue()` returns the epilogue of the MIME multipart message as an array of bytes.
- `addBodyPart(com.fsck.k9.mail.BodyPart)` adds a new body part to the existing multipart email message and sets the parent of the new body part as the current multipart message.
- `getBodyParts()` returns an immutable list of BodyPart objects that make up this Multipart object.
- `getCount()` returns the number of parts in the multipart message.
- `getBodyPart(int)` returns the `BodyPart` located at the specified index of the `Multipart`.
- `getParent()` returns the parent `Part` object of the current `Multipart` object.
- `getPreamble()` returns the preamble of a multipart email message as a byte array.
- `getBoundary()` returns the boundary string used to separate each part of the multipart message.
- `setEncoding(java.lang.String)` sets the encoding for a multipart email message and ensures it is compatible with the content-transfer-encoding for a multipart/* body.
- `setParent(com.fsck.k9.mail.Part)` sets the parent part of a multipart email.
- `setCharset(java.lang.String)` sets the character encoding of the multipart message's text body.

## abstract class `com.fsck.k9.mail.Message`

This abstract class provides methods to manipulate and retrieve various properties of an email message.

This class contains the following public method(s):

- `setFlags(java.util.Set,boolean)` sets the specified flags to the message.
- `getInternalDate()` returns the internal date of a message.
- `setFlag(com.fsck.k9.mail.Flag,boolean)` adds or removes a flag to or from a message.
- `getSize()` returns the size of the message.
- `delete(java.lang.String)` deletes a message and moves it to the specified trash folder.
- `getFrom()` returns an array of email addresses that the message is from.
- `clone()` creates a new Message object with the same content as the current object.
- `setSubject(java.lang.String)` sets the subject of a mail message.
- `setInReplyTo(java.lang.String)` sets the ID of the message being replied to in the In-Reply-To message header.
- `setFrom(com.fsck.k9.mail.Address)` sets the sender address of the email message.
- `setReplyTo(com.fsck.k9.mail.Address[])` sets the reply-to address(es) for the email message.
- `getRecipients(com.fsck.k9.mail.Message$RecipientType)` returns an array of email addresses for the specified recipient type in an email message.
- `getSentDate()` returns the date and time when the message was originally sent.
- `setBody(com.fsck.k9.mail.Body)` sets the message body for an email message.
- `setReferences(java.lang.String)` sets the references for the message.
- `setInternalDate(java.util.Date)` sets the internal date of a message to a specified date.
- `addRawHeader(java.lang.String,java.lang.String)` adds a raw header with the provided name and string value to the email message.
- `setRecipient(com.fsck.k9.mail.Message$RecipientType,com.fsck.k9.mail.Address)` sets a single recipient of a specific type for the email message.
- `calculateSize()` calculates the size of an email message.
- `setSentDate(java.util.Date,boolean)` sets the sent date of the email message with an option to hide the time zone information.
- `addHeader(java.lang.String,java.lang.String)` adds a header with given name and value to the message.
- `hasAttachments()` checks if the email message has any attachments.
- `setEncoding(java.lang.String)` sets the encoding of the message.
- `getHeaderNames()` returns a set of all the header names for the email message.
- `setCharset(java.lang.String)` sets the character set for the message content.
- `getReferences()` gets the unique identifiers of messages that are referenced in the current message.
- `getSubject()` returns the subject of the email message.
- `isSet(com.fsck.k9.mail.Flag)` checks if the specified flag is set for the message.
- `getFlags()` returns an unmodifiable set of flags associated with the email message.
- `getSender()` returns the sender(s) of the email message.
- `setUid(java.lang.String)` sets the unique identifier of the email message.
- `getReplyTo()` returns an array of email addresses to reply to for the email message.
- `getHeader(java.lang.String)` returns an array of Strings containing the header values for the specified header name of the email message.
- `setHeader(java.lang.String,java.lang.String)` sets a header with a specified name and value for the email message.
- `getFolder()` returns the folder that the message belongs to.
- `destroy()` throws a messaging exception but has no actual implementation or action.
- `equals(java.lang.Object)` checks if the given object is equal to the current Message object based on its UID and Folder name.
- `setSender(com.fsck.k9.mail.Address)` Sets the sender address of the email message.
- `setRecipients(com.fsck.k9.mail.Message$RecipientType,com.fsck.k9.mail.Address[])` sets the recipients of a mail message with the specified recipient type and address(es).
- `hashCode()` calculates a unique hash code for a `Message` object based on its folder name and UID.
- `removeHeader(java.lang.String)` removes a header with the given name from the message.
- `getMessageId()` returns the message ID of the email message.
- `getBody()` returns the body of an email message of the `com.fsck.k9.mail.Message` class.
- `getUid()` returns the unique identifier of a mail message.
- `olderThan(java.util.Date)` checks if the message's sent date or internal date is earlier than a given date.

## class `com.fsck.k9.mail.CertificateChainException`

This class represents an exception that occurs when there is an issue with a certificate chain in email messages sent and received by the K-9 Mail app.

This class contains the following public method(s):

- `getCertChain()` returns the X.509 certificate chain associated with a CertificateChainException in Java.
- `setCertChain(java.security.cert.X509Certificate[])` sets the certificate chain for the CertificateChainException object.

## abstract class `com.fsck.k9.mail.Folder`

This abstract class provides a set of methods for manipulating and retrieving emails within a mail folder.

This class contains the following public method(s):

- `moveMessages(java.util.List,com.fsck.k9.mail.Folder)` moves a list of email messages to a specified folder and returns a map of message IDs to their new folder IDs.
- `areMoreMessagesAvailable(int,java.util.Date)` checks if there are more messages available in the email folder beyond the specified index and date.
- `delete(boolean)` deletes the folder and all its contents if `recurse` is `true`, or only the folder if `recurse` is `false`.
- `fetch(java.util.List,com.fsck.k9.mail.FetchProfile,com.fsck.k9.mail.MessageRetrievalListener)` populates a list of messages based on a `FetchProfile` and notifies a listener as it fetches the messages.
- `setFlags(java.util.Set,boolean)` sets the specified set of email flags to the given boolean value for this mail folder.
- `setLastPush(long)` sets the time of the last push notification for a mail folder.
- `getSyncClass()` returns the sync class of the mail folder, which is equal to its display class.
- `open(int)` opens a mail provider for reading or writing, but only if it is not already open.
- `isInTopGroup()` returns a boolean value indicating whether the folder is in the top group.
- `close()` forces the closure of the MailProvider and any further access will attempt to reopen it.
- `create(com.fsck.k9.mail.Folder$FolderType,int)` creates a new folder with a specified display limit.
- `create(com.fsck.k9.mail.Folder$FolderType)` creates a folder of the specified type.
- `fetchPart(com.fsck.k9.mail.Message,com.fsck.k9.mail.Part,com.fsck.k9.mail.MessageRetrievalListener,com.fsck.k9.mail.BodyFactory)` fetches a specific part of a message and logs a message indicating that it is not implemented.
- `search(java.lang.String,java.util.Set,java.util.Set)` throws a messaging exception as K-9 does not support searches on this folder type.
- `getNewPushState(java.lang.String,com.fsck.k9.mail.Message)` returns a new push state for the folder.
- `getStatus()` returns the status of the email folder represented by the `Folder` object.
- `isFlagSupported(com.fsck.k9.mail.Flag)` always returns `true` for any given mail flag.
- `expunge()` deletes all messages in the mailbox marked as "deleted".
- `getLastPush()` returns the timestamp of the last push event for this email folder.
- `appendMessages(java.util.List)` appends a list of email messages to the folder and returns a map containing unique identifiers for each message.
- `getName()` returns the name of the folder as a String.
- `exists()` checks if the folder exists on the mail server.
- `getLastChecked()` returns the timestamp of when the folder was last checked.
- `setStatus(java.lang.String)` sets the status of the email folder.
- `getMessages(int,int,java.util.Date,com.fsck.k9.mail.MessageRetrievalListener)` fetches a list of messages within a specified UID range and after a given date, notifying a listener during the download process.
- `setFlags(java.util.List,java.util.Set,boolean)` sets or removes specified flags on a list of messages in a mail folder.
- `getFlaggedMessageCount()` returns the count of flagged messages in a mail folder.
- `getLastUpdate()` returns the maximum value between the time the folder was last checked and the time it was last pushed.
- `getMessage(java.lang.String)` returns a message with a given UID from the folder.
- `supportsFetchingFlags()` determines if the email server supports fetching flags.
- `getMessageCount()` returns the number of messages in the selected email folder.
- `setLastChecked(long)` sets the time when the folder was last checked for new messages.
- `copyMessages(java.util.List,com.fsck.k9.mail.Folder)` copies a list of email messages to another folder within the email service.
- `isOpen()` returns a boolean value indicating whether the connection to the folder is already open or not.
- `getMode()` returns the mode the folder was opened with.
- `getDisplayClass()` returns the display class of the folder, which in this case is set to NO_CLASS.
- `toString()` returns the name of the folder as a string.
- `delete(java.util.List,java.lang.String)` deletes a list of messages from a folder and moves them to a specified trash folder.
- `getUnreadMessageCount()` returns the number of unread messages in the mailbox folder.
- `getUidFromMessageId(com.fsck.k9.mail.Message)` gets the UID (unique identifier) of a message from its message ID in the email folder.
- `getPushClass()` returns the synchronization class of a mail folder used for push notifications.


# package `com.fsck.k9.mail.filter`

This package provides classes for encoding, decoding, manipulating, and counting data streams in the context of email filters.

This package contains the following class(es):

## class `com.fsck.k9.mail.filter.Base64OutputStream`

This class encodes byte data into Base64 format and writes it to an output stream.

This class contains the following public method(s):

- `flush()` flushes the output stream and writes any buffered output bytes to the stream.
- `write(int)` writes a single byte to the output stream in Base64 encoding.
- `close()` closes the output stream, flushing any remaining bytes that must be encoded or decoded and notifying the encoder of end of file.
- `write(byte[],int,int)` writes a specified number of bytes from a source byte array to an output stream, encoding or decoding the bytes using base64 if specified.

## class `com.fsck.k9.mail.filter.SmtpDataStuffing`

This class provides a method for writing bytes to an output stream with SMTP data stuffing to prevent message delimiter collision.

This class contains the following public method(s):

- `write(int)` writes bytes to an output stream while performing SMTP data stuffing to avoid message delimiter collision.

## class `com.fsck.k9.mail.filter.LineWrapOutputStream`

This class (no description)

This class contains the following public method(s):

- `write(int)` implements a line-wrapping algorithm by buffering and breaking long lines of text at word boundaries.
- `flush()` flushes any remaining data in the buffer and the underlying output stream.

## enum `com.fsck.k9.mail.filter.SignSafeOutputStream$State`

This enum provides a mechanism for transitioning between different states based on an input parameter in the context of signing and encryption for email filters.

This class contains the following public method(s):

- `nextState(int)` returns the next state based on the input parameter `b`.

## class `com.fsck.k9.mail.filter.Hex`

This class encodes an array of bytes into a string of lower-case hexadecimal characters.

This class contains the following public method(s):

- `encodeHex(byte[])` converts an array of bytes into a string of lower-case hexadecimal characters.

## class `com.fsck.k9.mail.filter.CountingOutputStream`

This class counts the number of bytes written to an output stream.

This class contains the following public method(s):

- `write(byte[],int,int)` increments a counter by the length of some data being written to an output stream.
- `write(byte[])` increments the count variable by the length of the byte array passed as a parameter.
- `write(int)` increments the count of bytes written to the output stream by 1.
- `getCount()` returns the count of bytes written to the output stream.

## class `com.fsck.k9.mail.filter.Base64`

This class provides methods for encoding and decoding data using the Base64 algorithm, as well as for checking whether a given byte array or byte is part of the Base64 alphabet.

This class contains the following public method(s):

- `decode(java.lang.Object)` decodes a `byte[]` object using the base64 algorithm.
- `decode(byte[])` decodes a byte array containing characters in the Base64 alphabet into binary data.
- `encodeBase64(byte[],boolean)` encodes binary data using base64 algorithm and optionally chunks the output into 76 character blocks.
- `decodeBase64(byte[])` decodes Base64 encoded data into octets (decoding a byte array of Base64 data into a new byte array of decoded data).
- `decode(java.lang.String)` decodes a Base64-encoded string into its original format.
- `encodeInteger(java.math.BigInteger)` encodes a BigInteger to a byte64-encoded integer according to crypto standards such as W3C's XML-Signature.
- `encode(java.lang.Object)` encodes an object using the base64 algorithm.
- `encodeBase64Chunked(byte[])` encodes binary data using the base64 algorithm and chunks the encoded output into 76 character blocks.
- `isArrayByteBase64(byte[])` checks if a given byte array contains only characters within the Base64 alphabet or is empty.
- `isBase64(byte)` checks if a given byte is part of the Base64 alphabet.
- `encode(byte[])` encodes a byte array of binary data into a byte array containing characters in the Base64 alphabet.
- `encodeBase64(byte[])` encodes binary data using the base64 algorithm without chunking the output.
- `encode(java.lang.String)` encodes a given string using Base64 encoding.
- `decodeInteger(byte[])` decodes a byte64-encoded integer according to crypto standards such as W3C's XML-Signature and returns it as a BigInteger.

## class `com.fsck.k9.mail.filter.PeekableInputStream`

This class provides the ability to peek at and potentially reuse upcoming bytes in an input stream while maintaining state information.

This class contains the following public method(s):

- `peek()` returns the next byte of data from the input stream without actually consuming it, by peeking ahead at the next available byte.
- `read(byte[],int,int)` reads bytes from the input stream, potentially using a previously peeked byte.
- `read(byte[])` reads bytes from the input stream and stores them in the given buffer.
- `toString()` returns a string representation of the PeekableInputStream object, including information about its current state (if it has peeked bytes or not).
- `read()` reads a single byte from the input stream either by calling the `in.read()` method or returning the byte previously peeked at.

## class `com.fsck.k9.mail.filter.EOLConvertingOutputStream`

This class converts and flushes line endings in an output stream.

This class contains the following public method(s):

- `endWithCrLfAndFlush()` adds a CRLF sequence to the end of the output stream and flushes the stream.
- `flush()` flushes any buffered output to the underlying stream after ensuring that any incomplete carriage return line feed (CR LF) pairs have been completed.
- `write(int)` converts line endings in the output by replacing LF with CR and/or adding a LF after a CR.

## class `com.fsck.k9.mail.filter.FixedLengthInputStream`

This class provides methods for reading a fixed length of bytes from an input stream, skipping specified number of bytes, and discarding any remaining bytes.

This class contains the following public method(s):

- `read(byte[])` reads a fixed length of bytes from the input stream into the byte array.
- `skip(long)` skips a specified number of bytes from the input stream while also keeping track of the number of bytes skipped.
- `toString()` returns a string representation of the `FixedLengthInputStream` object, showing the input stream and length.
- `read(byte[],int,int)` reads a specified number of bytes from an input stream into a byte array with a specified offset and length.
- `read()` reads a single byte from an input stream and tracks if a specified length has been reached.
- `available()` returns the number of bytes remaining to be read from the input stream.
- `skipRemaining()` skips over and discards any remaining bytes in the input stream.

## class `com.fsck.k9.mail.filter.SignSafeOutputStream`

This class provides methods to encode and write bytes to an output stream while ensuring its safe closure.

This class contains the following public method(s):

- `flush()` flushes the output for a SignSafeOutputStream Java class by calling both its own `flushOutput()` method and the `flush()` method of the underlying output stream (`out`).
- `write(byte[],int,int)` writes the specified portion of a byte array to the output stream, encoding each byte using a certain algorithm, while also checking if the stream has been closed.
- `close()` closes the output stream, flushing its contents before setting the "closed" flag to true.
- `encode(byte)` encodes a byte using a specific algorithm in a SignSafeOutputStream class.
- `write(int)` writes a single byte to the output stream while checking if the stream has been closed and encodes the byte.


# package `com.fsck.k9.mail.helper`

This package provides a helper class for encoding and decoding URLs.

This package contains the following class(es):

## class `com.fsck.k9.mail.helper.UrlEncodingHelper`

This class provides methods for encoding and decoding UTF-8 strings for use in URLs.

This class contains the following public method(s):

- `encodeUtf8(java.lang.String)` encodes a given string using UTF-8 encoding and returns the encoded string.
- `decodeUtf8(java.lang.String)` decodes a URL-encoded UTF-8 string.


# package `com.fsck.k9.mail.internet`

This package provides classes for handling and manipulating email messages and their content in the MIME format.

This package contains the following class(es):

## class `com.fsck.k9.mail.internet.ListHeaders`

This class extracts list post addresses from an email message.

This class contains the following public method(s):

- `getListPostAddresses(com.fsck.k9.mail.Message)` returns the list post addresses extracted from the given email message.

## class `com.fsck.k9.mail.internet.BinaryTempFileBody`

This class provides methods for handling binary temporary files associated with the content of an email message.

This class contains the following public method(s):

- `getEncoding()` returns the encoding used for the binary temp file body content.
- `getFile()` returns the binary temporary file associated with the email body.
- `getInputStream()` returns an InputStream that reads the content of a binary temp file associated with this BinaryTempFileBody object.
- `getTempDirectory()` returns the temporary directory used by the `BinaryTempFileBody` class.
- `getSize()` returns the length (in bytes) of a file associated with the BinaryTempFileBody object.
- `setTempDirectory(java.io.File)` sets the temporary directory where BinaryTempFileBody will store its temporary files.
- `setEncoding(java.lang.String)` changes the encoding of the body of an email message and converts it to the specified encoding.
- `getOutputStream()` returns an OutputStream to write data to a temporary file with a given prefix, which subsequently will be deleted on exit.
- `writeTo(java.io.OutputStream)` writes the contents of an input stream to an output stream using the Apache Commons IO library.

## class `com.fsck.k9.mail.internet.CharsetSupport`

This class supports character encoding operations for email parts and addresses.

This class contains the following public method(s):

- `setCharset(java.lang.String,com.fsck.k9.mail.Part)` sets the character encoding for a specific email part.
- `getCharsetFromAddress(java.lang.String)` determines the character encoding charset to be used based on the given email address.

## class `com.fsck.k9.mail.internet.EncoderUtil`

This class provides a method to encode a given text into an encoded word or a sequence of encoded words separated by space.

This class contains the following public method(s):

- `encodeEncodedWord(java.lang.String,java.nio.charset.Charset)` encodes a given text into an encoded word or a sequence of encoded words separated by space.

## class `com.fsck.k9.mail.internet.JisSupport`

This class provides methods for handling JIS variants and checking character encoding in emails.

This class contains the following public method(s):

- `getJisVariantFromAddress(java.lang.String)` determines the JIS variant (docomo, softbank, or kddi) based on the given email address.
- `getJisVariantFromMessage(com.fsck.k9.mail.Message)` returns the JIS variant of a given email message by checking its received, from, and mailer headers.
- `isShiftJis(java.lang.String)` checks if a given string represents the Shift JIS character encoding.

## class `com.fsck.k9.mail.internet.MimeHeader`

This class manages and manipulates MimeHeaders in email messages.

This class contains the following public method(s):

- `setCharset(java.lang.String)` sets the character encoding of the MimeHeader.
- `removeHeader(java.lang.String)` removes all headers with a specified name from the MimeHeader object.
- `clone()` creates a clone of the MimeHeader object with a new ArrayList of fields.
- `addHeader(java.lang.String,java.lang.String)` adds a new header field with given name and value to a list of MIME headers.
- `writeTo(java.io.OutputStream)` writes the MIME header fields to an output stream.
- `getFirstHeader(java.lang.String)` returns the first header value of a specific name in a MimeHeader object.
- `getHeaderNames()` returns a set of all the header names in the MIME header.
- `getHeader(java.lang.String)` returns an array of strings containing the values of the specified header attribute.
- `clear()` clears all the fields in the MimeHeader object.
- `toString()` builds a string representation of the MIME headers by iterating through the fields and formatting them as name-value pairs or appending raw data.
- `setHeader(java.lang.String,java.lang.String)` sets a value for a specified header name while removing any existing headers with the same name.

## class `com.fsck.k9.mail.internet.Iso2022JpToShiftJisInputStream`

This class converts ISO-2022-JP encoded characters to Shift-JIS encoding.

This class contains the following public method(s):

- `read()` reads input from a stream of characters encoded in the ISO-2022-JP format, converts them to Shift-JIS encoding, and returns the resulting characters one by one.

## class `com.fsck.k9.mail.internet.BinaryTempFileBody$BinaryTempFileBodyInputStream`

This class provides an input stream for a binary temporary file and allows the file to be closed and deleted or closed without deletion.

This class contains the following public method(s):

- `closeWithoutDeleting()` closes the input stream without deleting the underlying binary temp file.
- `close()` closes the input stream and deletes the associated temporary binary file.

## abstract class `com.fsck.k9.mail.internet.Viewable$Textual`

This abstract class provides functionality to access the Part associated with a textual message in an email.

This class contains the following public method(s):

- `getPart()` returns the Part associated with the Viewable$Textual instance.

## class `com.fsck.k9.mail.internet.MimeMessage$MimeMessageBuilder`

This class builds and constructs a MIME message with various methods for setting the header, body, preamble, epilogue, and body parts of the message.

This class contains the following public method(s):

- `body(org.apache.james.mime4j.stream.BodyDescriptor,java.io.InputStream)` sets the body of a MIME message with content from a given input stream and body descriptor.
- `endHeader()` ends the header of a MIME message being built and expects the class to be `com.fsck.k9.mail.Part`.
- `endMessage()` removes the current `com.fsck.k9.mail.internet.MimeMessage` instance from the stack.
- `preamble(java.io.InputStream)` sets the preamble of a MimeMultipart object with the content of an InputStream.
- `raw(java.io.InputStream)` throws an exception indicating that this method is not supported.
- `endBodyPart()` removes the first element from a stack if it is of type `com.fsck.k9.mail.BodyPart`.
- `endMultipart()` ends a multi-part message and checks if it has any body parts or an epilogue, and if not, sets its content to null.
- `startHeader()` starts constructing the header of a MIME message by setting the expected class type.
- `field(org.apache.james.mime4j.stream.Field)` adds the parsed field to the current MimeMessage's header.
- `startMultipart(org.apache.james.mime4j.stream.BodyDescriptor)` starts a multipart section of a MIME message, sets the body of the current part to a new MimeMultipart object, and pushes it onto a stack.
- `epilogue(java.io.InputStream)` sets the epilogue of a MIME multipart message based on the given input stream.
- `startMessage()` starts building a MIME message by adding it as the body of a part in a stack.
- `startBodyPart()` starts a new body part in a MIME message and adds it to a MIME multipart object.

## class `com.fsck.k9.mail.internet.MessageIdGenerator`

This class generates unique message IDs for email messages.

This class contains the following public method(s):

- `getInstance()` returns a new instance of the `MessageIdGenerator` class.
- `generateMessageId(com.fsck.k9.mail.Message)` generates a unique message ID for a given email message using the sender or reply-to address's hostname and a randomly generated UUID.

## class `com.fsck.k9.mail.internet.MessageExtractor`

This class provides methods for extracting text content, viewable parts, attachments, and text parts from email messages.

This class contains the following public method(s):

- `getTextFromPart(com.fsck.k9.mail.Part)` returns the text content from a given email message part.
- `findViewablesAndAttachments(com.fsck.k9.mail.Part,java.util.List,java.util.List)` traverses the MIME tree of an email message and extracts viewable parts and attachments.
- `hasMissingParts(com.fsck.k9.mail.Part)` checks whether a given email message part has any missing components.
- `collectAttachments(com.fsck.k9.mail.Message)` collects attachment parts from a given email message.
- `getTextParts(com.fsck.k9.mail.Part)` extracts and returns all the text parts from a given email message part.
- `collectTextParts(com.fsck.k9.mail.Message)` collects the viewable textual parts of a given email message.
- `getTextFromPart(com.fsck.k9.mail.Part,long)` extracts the text content from a given email message part up until a specified size limit.

## class `com.fsck.k9.mail.internet.MimeBodyPart`

This class manages and manipulates the content and headers of a MIME body part in an email message.

This class contains the following public method(s):

- `getHeader(java.lang.String)` returns an array of the values associated with the specified header name for a MimeBodyPart object.
- `setHeader(java.lang.String,java.lang.String)` sets the value of a specified header in the MIME body part.
- `writeTo(java.io.OutputStream)` writes a MimeMessage to an OutputStream in MIME format.
- `removeHeader(java.lang.String)` removes a particular header from the MimeBodyPart.
- `writeHeaderTo(java.io.OutputStream)` writes the header of a MimeBodyPart to an OutputStream.
- `getDisposition()` returns the value of the "Content-Disposition" header for a MIME body part.
- `getBody()` returns the body of a MimeBodyPart object.
- `getMimeType()` returns the MIME type of the body part.
- `addHeader(java.lang.String,java.lang.String)` adds a header with the specified name and value to the MIME body part.
- `setEncoding(java.lang.String)` sets the encoding of a MIME body part and updates the associated header.
- `setBody(com.fsck.k9.mail.Body)` sets the body of the MIME body part with the given body.
- `addRawHeader(java.lang.String,java.lang.String)` adds a raw header with a specified name and value to the MimeBodyPart object's header.
- `isMimeType(java.lang.String)` checks whether the MIME type of the body part is equal to the specified MIME type string in a case-insensitive manner.
- `getContentType()` gets the content type of a MIME body part, and if it's null, determines the content type based on its parent MIME type or defaults to "text/plain".
- `getContentId()` returns the unique identifier of the MIME body part within the message, extracted from the "Content-ID" header if present.

## class `com.fsck.k9.mail.internet.DecoderUtil`

This class can decode a string containing encoded words as defined by RFC 2047.

This class contains the following public method(s):

- `decodeEncodedWords(java.lang.String,com.fsck.k9.mail.Message)` decodes a string containing encoded words as defined by RFC 2047.

## class `com.fsck.k9.mail.internet.MimeUtility`

This class provides a set of utilities for working with MIME messages, including decoding and encoding, retrieving MIME types based on file extensions, and parsing header fields.

This class contains the following public method(s):

- `decodeBody(com.fsck.k9.mail.Body)` decodes the contents of a body by retrieving the input stream and using different decoding methods based on the body's encoding type.
- `getEncodingforType(java.lang.String)` returns a default content-transfer-encoding based on a MIME content-type.
- `unfoldAndDecode(java.lang.String,com.fsck.k9.mail.Message)` unfolds and decodes a given string using the `MimeUtility` class in the `com.fsck.k9.mail.internet` package, with a reference to a `Message`.
- `unfoldAndDecode(java.lang.String)` unfolds and decodes a given MIME message header field value.
- `getAllHeaderParameters(java.lang.String)` parses a given header value and returns a map of all parameter name-value pairs found within it.
- `foldAndEncode(java.lang.String)` simply returns the input string without any modifications or encoding.
- `unfold(java.lang.String)` removes line breaks from a given string.
- `isMultipart(java.lang.String)` checks whether a given MIME type is a multipart type or not.
- `getMimeTypeByExtension(java.lang.String)` returns the MIME type of a given file, based on its extension, and tries to determine the correct MIME type if the user's mailer set it as application/octet-stream.
- `isSameMimeType(java.lang.String,java.lang.String)` checks if two MIME types are the same, ignoring case sensitivity.
- `findFirstPartByMimeType(com.fsck.k9.mail.Part,java.lang.String)` finds the first part of a MIME message with a specified MIME type.
- `isDefaultMimeType(java.lang.String)` checks if a given MIME type is the default attachment MIME type used by the email client.
- `isMessage(java.lang.String)` checks if the given MIME type is a message/rfc822.
- `closeInputStreamWithoutDeletingTemporaryFiles(java.io.InputStream)` closes an input stream without deleting any temporary files associated with it, if it is a binary temp file body input stream.
- `mimeTypeMatches(java.lang.String,java.lang.String)` determines if a given MIME type matches a specified pattern which may include wildcards.
- `getHeaderParameter(java.lang.String,java.lang.String)` returns the value of a named parameter in a header field, or the first parameter if no name is specified, in a case insensitive fashion.
- `getExtensionByMimeType(java.lang.String)` returns the file extension for a given MIME type.

## class `com.fsck.k9.mail.internet.MimeHeader$Field`

This class represents a MIME header field and provides methods to get and set its value and name.

This class contains the following public method(s):

- `getValue()` returns the value of a MIME header field by splitting the raw field into the header name and value and returning the value portion after trimming it.
- `newNameValueField(java.lang.String,java.lang.String)` creates a new Field object with the specified name and value for use in a MIME header.
- `getName()` returns the name of the MimeHeader Field object.
- `getRaw()` returns the raw string value of a MimeHeader field.
- `hasRawData()` checks if there is a raw data present in the MimeHeader field.
- `toString()` returns the string representation of the MimeHeader field, either using the raw data or the field's name and value.
- `newRawField(java.lang.String,java.lang.String)` creates a new instance of the `MimeHeader.Field` class with a given name and raw value.

## class `com.fsck.k9.mail.internet.MimeMessage`

This class represents a MIME email message and provides methods to manipulate its headers, content, recipients, and other properties.

This class contains the following public method(s):

- `getSentDate()` returns the sent date of the email message if available, otherwise it parses the date from the email headers and returns it.
- `setSubject(java.lang.String)` sets the subject of the MIME message by adding a "Subject" header with the specified subject string.
- `writeHeaderTo(java.io.OutputStream)` writes the header of a MimeMessage to an OutputStream.
- `setRecipients(com.fsck.k9.mail.Message$RecipientType,com.fsck.k9.mail.Address[])` sets the recipients of the email message based on the provided type and array of addresses.
- `setInternalSentDate(java.util.Date)` sets the internal sent date of a MIME message in a Java program.
- `setReferences(java.lang.String)` sets the "References" header of a MimeMessage object, ensuring that it doesn't exceed a certain length and won't cause issues with certain email clients.
- `setFrom(com.fsck.k9.mail.Address)` sets the From address of a MIME message and saves it as an array of addresses.
- `setServerExtra(java.lang.String)` sets the server extra information for the MimeMessage object.
- `setReplyTo(com.fsck.k9.mail.Address[])` sets the "Reply-to" header of a MimeMessage with the provided array of email addresses, or removes the header if the array is empty or null.
- `getReferences()` returns an array of references extracted from the "References" header of the MIME message.
- `setHeader(java.lang.String,java.lang.String)` sets a header with a given name and value in the MimeMessage object.
- `setInReplyTo(java.lang.String)` (no description)
- `getContentType()` returns the content type of a MIME message, defaulting to "text/plain" if none is specified.
- `parse(java.io.InputStream)` parses a MIME message from an input stream using Apache Mime4J, without recursively parsing nested body parts.
- `getContentId()` returns the content ID of the MimeMessage, or null if there is none.
- `getSize()` returns the size of a MimeMessage object.
- `getFrom()` returns an array of email addresses in the "From" or "Sender" header of a MimeMessage, parsing it if necessary.
- `getSubject()` returns the decoded and unfolded value of the Subject header of a MIME email message.
- `setCharset(java.lang.String)` sets the character encoding of the MIME message and its body if applicable.
- `getServerExtra()` returns the server extra string of a MIME message.
- `getDisposition()` gets the value of the Content-Disposition header from a MIME message.
- `setSentDate(java.util.Date,boolean)` sets the sent date of a MimeMessage object while potentially hiding the time zone information.
- `clone()` creates a new instance of `MimeMessage` and copies all the properties of the current instance into it before returning the new instance.
- `getHeaderNames()` returns a set of header names for the MIME message.
- `getHeader(java.lang.String)` returns an array of header values associated with a specific name in a MimeMessage object.
- `getRecipients(com.fsck.k9.mail.Message$RecipientType)` returns an array of email addresses for a specific recipient type included in a MimeMessage object, such as TO, CC or BCC.
- `getBody()` returns the body of a MimeMessage object.
- `writeTo(java.io.OutputStream)` writes the contents of the MimeMessage, including its header and body, to the specified output stream.
- `getMimeType()` returns the MIME type of the email message.
- `getInputStream()` throws an UnsupportedOperationException when called.
- `getSender()` gets the sender address(es) of the MIME message.
- `setMessageId(java.lang.String)` sets the Message-ID header and updates the mMessageId field with the provided value.
- `setBody(com.fsck.k9.mail.Body)` sets the body of a MimeMessage object to the provided Body object.
- `toBodyPart()` converts a top level message into a bodypart by extracting appropriate headers and creating a new `MimeBodyPart` object with those headers and the body of the original message.
- `addRawHeader(java.lang.String,java.lang.String)` adds a raw header to the MimeMessage object with the specified name and value.
- `getReplyTo()` returns the address(es) specified in the "Reply-To" header of a MIME message.
- `setEncoding(java.lang.String)` sets the encoding of the message body and the content transfer encoding header in a MIME message.
- `removeHeader(java.lang.String)` removes a header with the given name from the MimeMessage.
- `parseMimeMessage(java.io.InputStream,boolean)` parses a MIME message from an input stream and returns a representation of it as a MimeMessage object.
- `hasAttachments()` returns false if the email message does not have any attachments, and true otherwise.
- `addHeader(java.lang.String,java.lang.String)` adds a header to the current MimeMessage with the specified name and value.
- `addSentDate(java.util.Date,boolean)` adds a 'Date' header to the MIME message with the given sent date and hides the time zone if specified.
- `getMessageId()` returns the message ID of the MimeMessage, and if it is null, it obtains it from the first header.
- `setSender(com.fsck.k9.mail.Address)` sets the sender address for a MimeMessage object and updates its corresponding header.
- `isMimeType(java.lang.String)` checks if the message's MIME type is equal to the specified MIME type.

## class `com.fsck.k9.mail.internet.Viewable$Alternative`

This class provides methods to retrieve viewable content and HTML content from an email message.

This class contains the following public method(s):

- `getText()` returns a list of viewable content from an email message.
- `getHtml()` returns a list of viewable HTML content from an instance of the `Viewable$Alternative` class in the Java class `com.fsck.k9.mail.internet`.

## class `com.fsck.k9.mail.internet.MimeMessageHelper`

This class provides methods to manipulate and set properties of MIME message parts.

This class contains the following public method(s):

- `setEncoding(com.fsck.k9.mail.Part,java.lang.String)` sets the encoding of a specified mail Part and its content transfer header.
- `setBody(com.fsck.k9.mail.Part,com.fsck.k9.mail.Body)` sets the body and header of a MIME message part.

## class `com.fsck.k9.mail.internet.Viewable$Flowed`

This class provides the functionality to check the value of the `delSp` boolean variable.

This class contains the following public method(s):

- `isDelSp()` returns the value of the `delSp` boolean variable.

## class `com.fsck.k9.mail.internet.BinaryTempFileMessageBody`

This class manages the encoding of binary message bodies.

This class contains the following public method(s):

- `setEncoding(java.lang.String)` sets the encoding of a BinaryTempFileMessageBody object and throws an exception if the encoding is not compatible.

## interface `com.fsck.k9.mail.internet.RawDataBody`

This interface provides a method to retrieve the encoding type of a raw data body in Java.

This class contains the following public method(s):

- `getEncoding()` returns the encoding type of the raw data body.

## class `com.fsck.k9.mail.internet.MimeMultipart`

This class handles MIME multipart messages, including setting and retrieving the preamble, epilogue, boundary, and body parts.

This class contains the following public method(s):

- `getPreamble()` returns the preamble of a MIME multipart message as a byte array.
- `getInputStream()` throws an UnsupportedOperationException when called.
- `writeTo(java.io.OutputStream)` writes the MimeMultipart to an OutputStream, along with its preamble, body parts, and epilogue.
- `setPreamble(byte[])` sets the preamble of the MIME multipart to the given byte array.
- `newInstance()` creates a new instance of a MimeMultipart object with a generated boundary.
- `getEpilogue()` returns the epilogue of the MimeMultipart object as a byte array.
- `getBoundary()` returns the boundary of a MimeMultipart object in string format.
- `getMimeType()` returns the MIME type of the MimeMultipart object.
- `setEpilogue(byte[])` sets the epilogue (closing text) of the MIME multipart.
- `setSubType(java.lang.String)` sets the subtype of the MIME multipart content type.

## interface `com.fsck.k9.mail.internet.SizeAware`

This interface provides a method to retrieve the size of an object in bytes.

This class contains the following public method(s):

- `getSize()` returns the size of an object that implements the `SizeAware` interface in bytes.

## class `com.fsck.k9.mail.internet.TextBody`

This class provides methods for getting, setting, and manipulating the encoding, size, and content of text bodies in emails.

This class contains the following public method(s):

- `getEncoding()` returns the encoding of the text in the TextBody object.
- `setCharset(java.lang.String)` sets the character encoding of the text body in the email.
- `getComposedMessageLength()` returns the length of the composed message as an Integer, if it exists.
- `getInputStream()` returns an input stream to read the contents of the TextBody object.
- `getComposedMessageOffset()` returns the offset of the composed message.
- `setComposedMessageLength(java.lang.Integer)` sets the length of the composed message in a TextBody object.
- `getSize()` returns the size of the text body, taking into account the encoding type and quoted-printable encoding.
- `getRawText()` returns the raw text of the email body.
- `writeTo(java.io.OutputStream)` writes the content of a TextBody to an output stream using a specified encoding.
- `setEncoding(java.lang.String)` sets the encoding of the text body, but throws an exception if the encoding type is not supported.
- `setComposedMessageOffset(java.lang.Integer)` sets the offset of the composed message for a TextBody object in Java.

## class `com.fsck.k9.mail.internet.Viewable$MessageHeader`

This class provides methods to access the message and container part of an email header.

This class contains the following public method(s):

- `getMessage()` returns the message associated with the `Viewable$MessageHeader` object.
- `getContainerPart()` returns the container part of a message header.


# package `com.fsck.k9.mail.message`

This package contains classes for parsing and handling the headers of email messages in the K-9 mail app.

This package contains the following class(es):

## class `com.fsck.k9.mail.message.MessageHeaderParser$MessageHeaderParserContentHandler`

This class parses the header of a MIME message in K-9 mail and provides methods for handling different parts of the header.

This class contains the following public method(s):

- `raw(java.io.InputStream)` does nothing with the input stream parameter passed to it.
- `endHeader()` does nothing because it is simply an override of the superclass method.
- `endMultipart()` does nothing when the end of a multipart message is reached during parsing.
- `body(org.apache.james.mime4j.stream.BodyDescriptor,java.io.InputStream)` does nothing.
- `endBodyPart()` does nothing and simply overrides the same method in its superclass.
- `startMultipart(org.apache.james.mime4j.stream.BodyDescriptor)` does nothing when starting a multipart body in a MIME message.
- `preamble(java.io.InputStream)` does nothing with the input stream provided as a parameter.
- `endMessage()` does nothing when the end of the message is reached during parsing of a message header in K-9 mail.
- `startHeader()` does nothing.
- `startMessage()` does nothing as it overrides the `startMessage()` method from the parent class but does not add any new functionality.
- `field(org.apache.james.mime4j.stream.Field)` adds a raw header to the current message part being parsed.
- `epilogue(java.io.InputStream)` does nothing.
- `startBodyPart()` overrides the `startBodyPart()` method of the `ContentHandler` interface and doesn't do anything when it is invoked.

## class `com.fsck.k9.mail.message.MessageHeaderParser`

This class parses the headers of a mail message's part.

This class contains the following public method(s):

- `parse(com.fsck.k9.mail.Part,java.io.InputStream)` parses the headers of a mail message's part using the Apache James Mime4j parser.


# package `com.fsck.k9.mail.oauth`

This package provides classes and interfaces for OAuth2 authentication in email communication in Java.

This package contains the following class(es):

## class `com.fsck.k9.mail.oauth.XOAuth2ChallengeParser`

This class parses challenge requests for OAuth2 authentication and determines if a response should be retried based on the parsed status.

This class contains the following public method(s):

- `shouldRetry(java.lang.String,java.lang.String)` checks if the response from a challenge request should be retried based on the status parsed from a JSON object.

## interface `com.fsck.k9.mail.oauth.OAuth2TokenProvider`

This interface provides methods for requesting API authorization, fetching and invalidating OAuth2 tokens for specific usernames, and getting a list of accounts suitable for OAuth 2.0 token provision.

This class contains the following public method(s):

- `authorizeApi(java.lang.String,android.app.Activity,com.fsck.k9.mail.oauth.OAuth2TokenProvider$OAuth2TokenProviderAuthCallback)` requests API authorization and provides a callback for asynchronous response processing.
- `getAccounts()` returns a list of accounts that are suitable for OAuth 2.0 token provision.
- `getToken(java.lang.String,long)` fetches an OAuth2 token for a specified username with a specified timeout.
- `invalidateToken(java.lang.String)` invalidates the token associated with a specific username.

## interface `com.fsck.k9.mail.oauth.OAuth2TokenProvider$OAuth2TokenProviderAuthCallback`

This interface defines callback methods for handling the success or failure of OAuth2 authentication.

This class contains the following public method(s):

- `success()` executes code when the OAuth2 authentication process succeeds.
- `failure(com.fsck.k9.mail.oauth.AuthorizationException)` handles the failure of obtaining an OAuth2 token by taking in an AuthorizationException as input parameter.


# package `com.fsck.k9.mail.power`

This package contains classes for managing power-related functionalities in email applications, including a tracing power manager.

This package contains the following class(es):

## class `com.fsck.k9.mail.power.TracingPowerManager$TracingWakeLock`

This class (no description)

This class contains the following public method(s):

- `acquire()` acquires a wake lock, raises a notification, and logs a warning if K9MailLib is in debug mode.
- `setReferenceCounted(boolean)` sets whether the wake lock should be reference counted or not.
- `acquire(long)` acquires a wake lock and raises a notification with specified timeout.
- `release()` releases a tracing wake lock, cancels any notifications associated with it, and logs information about its release time if in debug mode.

## class `com.fsck.k9.mail.power.TracingPowerManager`

This class provides a tracing power manager for managing power-related functionalities in email applications.

This class contains the following public method(s):

- `newWakeLock(int,java.lang.String)` creates a new instance of a TracingWakeLock object with the specified flags and tag.
- `getPowerManager(android.content.Context)` returns a TracingPowerManager for a given context, creating it if it does not already exist.


# package `com.fsck.k9.mail.ssl`

This package provides SSL/TLS functionality and related security management for the K9 mail client.

This package contains the following class(es):

## class `com.fsck.k9.mail.ssl.DefaultTrustedSocketFactory`

This class creates SSL/TLS sockets with trusted SSL certificates and provides methods to set client certificate properties and set the hostname for the SSL socket.

This class contains the following public method(s):

- `createSocket(java.net.Socket,java.lang.String,int,java.lang.String)` creates a SSL/TLS socket with a trusted SSL certificate and sets optional client certificate properties.
- `setSniHost(javax.net.ssl.SSLSocketFactory,javax.net.ssl.SSLSocket,java.lang.String)` sets the hostname for a given SSL socket using either the Android SSLCertificateSocketFactory or reflection.

## class `com.fsck.k9.mail.ssl.TrustManagerFactory$SecureX509TrustManager`

This class implements a custom X509TrustManager for SSL/TLS connections in the K9 mail client that checks client and server certificates for validity and manages trusted issuers.

This class contains the following public method(s):

- `checkClientTrusted(java.security.cert.X509Certificate[],java.lang.String)` checks if the client's X509 certificate is trusted.
- `checkServerTrusted(java.security.cert.X509Certificate[],java.lang.String)` checks the server's X.509 certificate chain for validity and throws a CertificateChainException if it cannot be validated using either the global or local key store.
- `getAcceptedIssuers()` returns an array of X509 certificates that are accepted issuers by the default trust manager.
- `getInstance(java.lang.String,int)` returns a synchronized instance of `javax.net.ssl.X509TrustManager` based on the host and port parameters, creating a new one if it does not exist already in the `mTrustManager` map.

## class `com.fsck.k9.mail.ssl.LocalKeyStore`

This class provides methods to manage and validate X509 certificates for a given host and port in a local key store.

This class contains the following public method(s):

- `deleteCertificate(java.lang.String,int)` deletes a certificate from the local key store using the host and port provided.
- `addCertificate(java.lang.String,int,java.security.cert.X509Certificate)` adds a new X509 certificate to the local key store associated with a given host and port.
- `isValidCertificate(java.security.cert.Certificate,java.lang.String,int)` checks if a given certificate is valid and matches the stored certificate for a given hostname and port.
- `setKeyStoreLocation(java.lang.String)` sets the directory location for the LocalKeyStore.
- `setKeyStoreFile(java.io.File)` reinitializes the local key store with certificates from a specified file or defaults to a default file location if null.
- `getInstance()` returns the instance of the LocalKeyStore class.

## class `com.fsck.k9.mail.ssl.KeyChainKeyManager`

This class manages SSL/TLS key chains for server and client authentication.

This class contains the following public method(s):

- `chooseEngineServerAlias(java.lang.String,java.security.Principal[],javax.net.ssl.SSLEngine)` chooses a server alias for an SSL engine based on the provided key type and issuers.
- `chooseClientAlias(java.lang.String[],java.security.Principal[],java.net.Socket)` chooses a client alias based on the given key types and issuers for SSL/TLS authentication.
- `getServerAliases(java.lang.String,java.security.Principal[])` returns an array of server aliases based on the specified key type and issuers.
- `chooseEngineClientAlias(java.lang.String[],java.security.Principal[],javax.net.ssl.SSLEngine)` chooses a client alias from a specified list of key types and issuers for the given SSL engine.
- `chooseServerAlias(java.lang.String,java.security.Principal[],java.net.Socket)` chooses the server alias based on the provided parameters.
- `getClientAliases(java.lang.String,java.security.Principal[])` returns an array of client aliases for a given key type and array of issuers.
- `getPrivateKey(java.lang.String)` retrieves the private key associated with the given alias if it matches the key manager's alias, otherwise it returns null.
- `getCertificateChain(java.lang.String)` returns the X.509 certificate chain associated with the given alias if it matches the instance's alias, or null otherwise.

## interface `com.fsck.k9.mail.ssl.TrustedSocketFactory`

This interface creates SSL/TLS sockets with client certificate alias for a given host and port.

This class contains the following public method(s):

- `createSocket(java.net.Socket,java.lang.String,int,java.lang.String)` creates a new SSL/TLS socket using an existing socket, a host address, a port number, and a client certificate alias.

## class `com.fsck.k9.mail.ssl.TrustManagerFactory`

This class provides a way to obtain an instance of X509TrustManager for a specified host and port.

This class contains the following public method(s):

- `get(java.lang.String,int)` returns an instance of X509TrustManager for the specified host and port.


# package `com.fsck.k9.mail.store.imap`

This package provides classes and interfaces for interacting with and manipulating email messages and folders stored on an IMAP email server.

This package contains the following class(es):

## class `com.fsck.k9.mail.store.imap.PermanentFlagsResponse`

This class provides methods to parse and retrieve permanent mailbox flags and whether new keyword creation is allowed for an IMAP mailbox.

This class contains the following public method(s):

- `canCreateKeywords()` returns a boolean value indicating if creating keywords is allowed.
- `parse(com.fsck.k9.mail.store.imap.ImapResponse)` parses an IMAP response to obtain the set of permanent mailbox flags and whether new keywords can be created.
- `getFlags()` returns a Java Set collection of `com.fsck.k9.mail.Flag` objects representing the permanent flags associated with an IMAP mailbox.

## class `com.fsck.k9.mail.store.imap.ImapMessage`

This class provides methods for managing and manipulating email messages in an IMAP email store.

This class contains the following public method(s):

- `setFlagInternal(com.fsck.k9.mail.Flag,boolean)` sets a flag for an email message internally.
- `setSize(int)` sets the size of a message in bytes in an IMAP email store.
- `setFlag(com.fsck.k9.mail.Flag,boolean)` sets or removes a flag from an email message and updates the flag’s status in the corresponding IMAP folder.
- `delete(java.lang.String)` deletes the current email message and moves it to the specified trash folder.

## class `com.fsck.k9.mail.store.imap.ImapStoreSettings`

This class provides settings for connecting to an IMAP email store and allows for the creation of new instances with updated authentication details.

This class contains the following public method(s):

- `getExtra()` returns a map with extra settings for an IMAP email store, including autodetect namespace and path prefix if they are set.
- `newPassword(java.lang.String)` creates a new instance of `ImapStoreSettings` with the inputted new password for authentication.

## class `com.fsck.k9.mail.store.imap.SearchResponse`

This class provides methods for parsing and retrieving a list of message numbers from IMAP SEARCH responses.

This class contains the following public method(s):

- `getNumbers()` returns a mutable list of numbers from the SEARCH response(s) belonging to the Java class `com.fsck.k9.mail.store.imap.SearchResponse`.
- `parse(java.util.List)` parses a list of IMAP responses to construct a search response containing a list of matching message numbers.

## interface `com.fsck.k9.mail.store.imap.ImapResponseCallback`

This interface handles callbacks for when a literal string is found in an IMAP response during parsing.

This class contains the following public method(s):

- `foundLiteral(com.fsck.k9.mail.store.imap.ImapResponse,com.fsck.k9.mail.filter.FixedLengthInputStream)` handles the callback for when a literal string is found in an IMAP response during parsing.

## class `com.fsck.k9.mail.store.imap.ImapResponseParser`

This class parses IMAP responses from a server and returns them as an ImapResponse object.

This class contains the following public method(s):

- `readResponse(com.fsck.k9.mail.store.imap.ImapResponseCallback)` reads the next response available on the input stream and returns an ImapResponse object that represents it, based on whether it's a continuation request, untagged response, or tagged response.
- `readResponse()` reads and returns an IMAP response from a server.

## class `com.fsck.k9.mail.store.imap.ImapPushState`

This class represents the state of an IMAP mailbox for push notifications and provides methods for parsing and converting the state to a string representation.

This class contains the following public method(s):

- `parse(java.lang.String)` parses a string into an ImapPushState object, returning a default state if the string is invalid.
- `toString()` returns a string representation of the `uidNext` value in the `ImapPushState` class.

## class `com.fsck.k9.mail.store.imap.ImapStoreUriCreator`

This class creates an ImapStore URI using server settings.

This class contains the following public method(s):

- `create(com.fsck.k9.mail.ServerSettings)` creates an ImapStore URI with the supplied server settings.

## class `com.fsck.k9.mail.store.imap.NamespaceResponse`

This class provides methods for retrieving the prefix and hierarchy delimiter of a mailbox namespace, as well as parsing a list of IMAP responses for the first namespace response.

This class contains the following public method(s):

- `getPrefix()` returns the prefix of a namespace response in the form of a string.
- `getHierarchyDelimiter()` returns the hierarchy delimiter used by the IMAP server for a given mailbox namespace.
- `parse(java.util.List)` parses a list of IMAP responses and returns the first namespace response.

## class `com.fsck.k9.mail.store.imap.ResponseCodeExtractor`

This class extracts response codes from IMAP server responses.

This class contains the following public method(s):

- `getResponseCode(com.fsck.k9.mail.store.imap.ImapResponse)` extracts the response code from an IMAP server response.

## class `com.fsck.k9.mail.store.imap.ImapConnection`

This class provides methods for establishing and managing connections to an IMAP server.

This class contains the following public method(s):

- `open()` opens a connection to an IMAP server and performs necessary authentication and configuration.
- `executeSimpleCommand(java.lang.String)` executes a simple IMAP command with the option to specify whether to fetch the response immediately.
- `sendContinuation(java.lang.String)` sends a continuation command in the IMAP protocol and logs it if debugging is enabled.
- `readResponse()` reads an IMAP server response.
- `sendCommand(java.lang.String,boolean)` sends a command to an IMAP server and logs the command if debugging is enabled.
- `readResponse(com.fsck.k9.mail.store.imap.ImapResponseCallback)` reads and returns an IMAP response from the server and logs it, while also handling any IO exceptions and closing the connection if necessary.
- `executeSimpleCommand(java.lang.String,boolean)` executes a simple IMAP command while optionally redacting sensitive information from the command for logging purposes.
- `close()` closes the IMAP connection and its input/output streams while also setting the open status to false.
- `getOutputStream()` returns the output stream of the IMAP connection.
- `sendSaslIrCommand(java.lang.String,java.lang.String,boolean)` sends a SASL initial response command over an IMAP connection and returns a unique tag for the command.
- `readStatusResponse(java.lang.String,java.lang.String,com.fsck.k9.mail.store.imap.UntaggedHandler)` reads and parses a status response from an IMAP server with the provided tag and command, and handles any untagged events with the given handler.
- `isConnected()` checks if the input and output streams and socket are not null and connected, and that the socket is not closed, and returns a boolean value representing whether the connection is currently active.

## class `com.fsck.k9.mail.store.imap.SelectOrExamineResponse`

This class provides functionality to parse and determine the open mode of an IMAP mailbox.

This class contains the following public method(s):

- `getOpenMode()` returns the open mode of an IMAP mailbox either in read-only or read-write mode.
- `parse(com.fsck.k9.mail.store.imap.ImapResponse)` parses an IMAP response to determine the open mode of a mailbox.
- `hasOpenMode()` checks if the mailbox has been opened in read-write mode or not.

## class `com.fsck.k9.mail.store.imap.ImapUtility`

This class provides utility methods to work with IMAP servers in email communication.

This class contains the following public method(s):

- `getImapRangeValues(java.lang.String)` expands a given number range into a list of individual numbers in a valid format for an IMAP server response.
- `getImapSequenceValues(java.lang.String)` parses a string of sequence sets received from an IMAP server and returns a list of individual numbers, expanding any ranges specified in the input.
- `encodeString(java.lang.String)` encodes a string to make it usable in an IMAP command.
- `getLastResponse(java.util.List)` returns the last element of a list of IMAP response objects.

## interface `com.fsck.k9.mail.store.imap.ImapSettings`

This interface provides methods to get and set various IMAP email account settings, such as username, password, connection security, port number, authentication type, and mailbox folder paths.

This class contains the following public method(s):

- `getUsername()` returns the username associated with the IMAP settings.
- `getPassword()` returns a string representing the password for the IMAP email account.
- `getConnectionSecurity()` returns the type of security used for the IMAP connection.
- `setCombinedPrefix(java.lang.String)` sets a common prefix for the mailbox folder path in IMAP email settings.
- `getClientCertificateAlias()` returns the alias of the client certificate used for authentication in an IMAP email server connection.
- `getPort()` returns the port number specified in the IMAP settings.
- `setPathDelimiter(java.lang.String)` sets the path delimiter used in an IMAP mailbox.
- `getPathDelimiter()` returns the path delimiter used by an IMAP server.
- `setPathPrefix(java.lang.String)` sets the path prefix for IMAP settings in the K9 mail client.
- `getPathPrefix()` returns the path prefix used in the IMAP server for the inbox folder.
- `getHost()` returns the host address of the IMAP server.
- `getCombinedPrefix()` gets the combined prefix for IMAP folders.
- `useCompression(com.fsck.k9.mail.NetworkType)` checks whether compression should be used for a specific network type in an IMAP email server.
- `getAuthType()` returns the authentication type used for an IMAP mail store.

## class `com.fsck.k9.mail.store.imap.ImapResponse`

This class handles and represents responses received from an IMAP server, including tagged and untagged responses, continuation requests, and associated callbacks.

This class contains the following public method(s):

- `newTaggedResponse(com.fsck.k9.mail.store.imap.ImapResponseCallback,java.lang.String)` creates a new tagged response object for an IMAP server with a specified callback and tag value.
- `getTag()` returns the tag value of the current ImapResponse object.
- `toString()` returns a string representation of an IMAP response object, including its tag and command continuation status.
- `setCallback(com.fsck.k9.mail.store.imap.ImapResponseCallback)` sets the callback for handling responses from an IMAP server.
- `newContinuationRequest(com.fsck.k9.mail.store.imap.ImapResponseCallback)` returns a new `ImapResponse` object with a callback and a flag indicating it is a continuation request.
- `getCallback()` returns the callback object associated with an instance of the ImapResponse class.
- `isTagged()` checks if the IMAP response has a tag associated with it.
- `isContinuationRequested()` returns a boolean value indicating whether a continuation has been requested for an IMAP command.
- `newUntaggedResponse(com.fsck.k9.mail.store.imap.ImapResponseCallback)` creates a new untagged response object with a specified callback.

## class `com.fsck.k9.mail.store.imap.FetchPartCallback`

This class provides a method for parsing IMAP responses and creating MimeBodyPart objects.

This class contains the following public method(s):

- `foundLiteral(com.fsck.k9.mail.store.imap.ImapResponse,com.fsck.k9.mail.filter.FixedLengthInputStream)` parses an IMAP response and creates a MimeBodyPart object from the response's literal.

## class `com.fsck.k9.mail.store.imap.ImapStore$StoreImapSettings`

This class stores the settings and credentials for accessing an IMAP email server.

This class contains the following public method(s):

- `getPort()` returns the value of the port variable in the `StoreImapSettings` class of the `ImapStore`.
- `getHost()` returns the host value stored in the `ImapStore$StoreImapSettings` class.
- `getConnectionSecurity()` returns the connection security of an IMAP email server.
- `getUsername()` returns the username for accessing an IMAP mail server.
- `setPathPrefix(java.lang.String)` sets the path prefix for a IMAP store's settings.
- `getPathPrefix()` returns the path prefix of an IMAP store's settings.
- `setCombinedPrefix(java.lang.String)` sets the combined prefix of a store's IMAP settings.
- `getClientCertificateAlias()` returns the client certificate alias of an IMAP store's settings.
- `setPathDelimiter(java.lang.String)` sets the path delimiter for a particular IMAP store.
- `getAuthType()` returns the authentication type used for an IMAP email store.
- `getPathDelimiter()` returns the path delimiter used by the IMAP server for this email store.
- `useCompression(com.fsck.k9.mail.NetworkType)` returns a boolean value indicating whether compression should be used for a given network type in an IMAP email store configuration.
- `getCombinedPrefix()` returns the combined prefix used by the current instance of the ImapStore class.
- `getPassword()` returns the password of an IMAP email account stored in an instance of the `ImapStore$StoreImapSettings` class.

## class `com.fsck.k9.mail.store.imap.ImapFolderPusher`

This class pushes new messages from an IMAP folder to a device in real-time.

This class contains the following public method(s):

- `start()` starts a new thread to execute the `PushRunnable()` method, throwing an exception if `start()` is called twice.
- `stop()` stops the listening thread and closes the IMAP connection to stop pushing for a particular folder.
- `refresh()` stops the idling process and acquires a wake lock before refreshing the IMAP folder.

## class `com.fsck.k9.mail.store.imap.ImapStoreUriDecoder`

This class decodes an ImapStore URI into an object of type `com.fsck.k9.mail.store.imap.ImapStoreSettings`.

This class contains the following public method(s):

- `decode(java.lang.String)` decodes an ImapStore URI into an object of type `com.fsck.k9.mail.store.imap.ImapStoreSettings`.

## class `com.fsck.k9.mail.store.imap.FetchBodyCallback`

This class parses literal message bodies from an IMAP server response and returns placeholder objects.

This class contains the following public method(s):

- `foundLiteral(com.fsck.k9.mail.store.imap.ImapResponse,com.fsck.k9.mail.filter.FixedLengthInputStream)` parses a literal message body from an IMAP server response and returns a placeholder object.

## class `com.fsck.k9.mail.store.imap.ImapPusher`

This class implements functionality for pushing new email messages to a client's mailbox through synchronization and refresh intervals.

This class contains the following public method(s):

- `getRefreshInterval()` returns the refresh interval for an IMAP push email service, calculated based on the `IdleRefreshMinutes` property of the store configuration.
- `start(java.util.List)` starts folder pushers for the given list of folder names in a synchronized manner.
- `setLastRefresh(long)` sets the last refresh time for an IMAP email account in the K9 email client.
- `stop()` stops the IMAP pusher and all associated folder pushers.
- `refresh()` calls the `refresh()` method on all the `ImapFolderPusher` objects in the `folderPushers` list while handling any exceptions that occur during the process.
- `getLastRefresh()` returns the timestamp of the last refresh of an IMAP mailbox.

## class `com.fsck.k9.mail.store.imap.ImapFolderPusher$IdleStopper`

This class manages the idle mode and acceptance of "done continuation" commands for an IMAP folder pusher.

This class contains the following public method(s):

- `stopAcceptingDoneContinuation()` stops accepting "done continuation" commands and sets the IMAP connection to null.
- `startAcceptingDoneContinuation(com.fsck.k9.mail.store.imap.ImapConnection)` sets a flag to start accepting Done continuation responses from an IMAP connection and sets the IMAP connection object.
- `stopIdle()` stops the idle mode of an IMAP folder pusher if it is currently in that mode.

## class `com.fsck.k9.mail.store.imap.NegativeImapResponseException`

This class throws an exception when an unexpected or negative response is received during an IMAP transaction and provides methods to retrieve information about the response.

This class contains the following public method(s):

- `getLastResponse()` returns the last response received during an IMAP transaction.
- `wasByeResponseReceived()` checks if a BYE response was received in the responses list of an IMAP server.
- `getAlertText()` returns the alert text from an IMAP response, or retrieves it from the last response if it has not been set yet.

## class `com.fsck.k9.mail.store.imap.FolderNameCodec`

This class encodes and decodes folder names using a modified UTF-7 charset.

This class contains the following public method(s):

- `decode(java.lang.String)` decodes an encoded folder name using a modified UTF-7 charset.
- `newInstance()` creates a new instance of the `FolderNameCodec` class.
- `encode(java.lang.String)` encodes a given folder name using modified UTF-7 encoding and returns the encoded string using ASCII encoding.

## class `com.fsck.k9.mail.store.imap.CapabilityResponse`

This class parses and retrieves the capabilities of an IMAP mail store.

This class contains the following public method(s):

- `parse(java.util.List)` parses a list of IMAP responses into a CapabilityResponse object.
- `getCapabilities()` returns a set of capabilities for the IMAP mail store.

## interface `com.fsck.k9.mail.store.imap.ImapSearcher`

This interface provides a method to search for emails in an IMAP mailbox and return a list of IMAP responses.

This class contains the following public method(s):

- `search()` searches for emails in an IMAP mailbox and returns a list of IMAP responses.

## class `com.fsck.k9.mail.store.imap.AlertResponse`

This class provides a method to extract alert text from an IMAP response.

This class contains the following public method(s):

- `getAlertText(com.fsck.k9.mail.store.imap.ImapResponse)` returns the alert text from an IMAP response, or null if it does not contain the proper code.

## class `com.fsck.k9.mail.store.imap.ImapList`

This class provides methods to manipulate and retrieve values from an IMAP list.

This class contains the following public method(s):

- `getList(int)` gets an `ImapList` object at the specified index from a list.
- `getKeyedString(java.lang.String)` returns the value associated with the given key as a string.
- `getKeyedNumber(java.lang.String)` returns an integer value of a string value that corresponds to a given key.
- `isString(int)` checks if the object at a specified index in an ImapList is a Java string.
- `containsKey(java.lang.String)` checks if a given string key exists in the list of strings.
- `getKeyedValue(java.lang.String)` searches for a specific key in the list and returns its corresponding value, or null if the key cannot be found.
- `getObject(int)` returns an object at a specified index of an ImapList.
- `getKeyedDate(java.lang.String)` returns a Date object associated with a specified key in the ImapList.
- `getNumber(int)` returns the integer value of the string at the specified index within the ImapList.
- `getKeyIndex(java.lang.String)` returns the index of a given key in the collection or throws an exception if the key is not found.
- `getDate(int)` returns a Date object for a specified index by converting the result of getString method.
- `getString(int)` returns a String value at the given index position in the ImapList.
- `isList(int)` checks if the object at the given index in the ImapList is an instance of ImapList.
- `getLong(int)` returns the long value of the string at the specified index in an ImapList.
- `getKeyedList(java.lang.String)` gets a specified value from an IMAP list using a key.

## interface `com.fsck.k9.mail.store.imap.UntaggedHandler`

This interface provides a method for handling asynchronous untagged responses received from an IMAP server.

This class contains the following public method(s):

- `handleAsyncUntaggedResponse(com.fsck.k9.mail.store.imap.ImapResponse)` handles an untagged response received from an IMAP server in an asynchronous manner.

## class `com.fsck.k9.mail.store.imap.ImapFolder`

This class provides methods for managing and manipulating email folders stored on an IMAP server.

This class contains the following public method(s):

- `setFlags(java.util.Set,boolean)` sets the flags of the IMAP folder using a UID STORE command.
- `exists()` checks if the folder exists on the IMAP server.
- `getMode()` returns the mode of the IMAP folder.
- `setFlags(java.util.List,java.util.Set,boolean)` sets flags for a list of email messages in an IMAP folder.
- `moveMessages(java.util.List,com.fsck.k9.mail.Folder)` moves messages from one folder to another and sets the DELETED flag on the original messages.
- `search(java.lang.String,java.util.Set,java.util.Set)` searches for messages in a remote IMAP folder based on a query string and specified flag criteria, returning a list of matching messages.
- `getMessageCount()` returns the total number of messages in the IMAP folder.
- `isOpen()` checks if the connection to the IMAP server is open or not.
- `hashCode()` computes a hash value based on the name of the email folder.
- `expunge()` performs an "EXPUNGE" command on an open IMAP folder to permanently remove deleted emails.
- `getNewPushState(java.lang.String,com.fsck.k9.mail.Message)` updates the push state of an email message in an IMAP folder and returns the new push state.
- `delete(boolean)` throws an error as it has not been implemented yet.
- `equals(java.lang.Object)` checks if another ImapFolder object is equal to this object based on their names (ignoring case).
- `create(com.fsck.k9.mail.Folder$FolderType)` creates a folder of a specified type in an IMAP mail account.
- `getFlaggedMessageCount()` returns the number of messages in an IMAP folder that are flagged but not deleted.
- `getUidFromMessageId(com.fsck.k9.mail.Message)` extracts the UID of a message from its Message-ID header in an IMAP folder.
- `getUnreadMessageCount()` returns the number of unread messages in an IMAP email folder.
- `copyMessages(java.util.List,com.fsck.k9.mail.Folder)` copies the given messages to a specified folder and returns a mapping of original message UIDs to the new server UIDs.
- `close()` closes the IMAP folder, sets the message count to -1, releases the connection, and potentially shuts down the connection if a search was aborted.
- `getName()` returns the name of an email folder in an IMAP email account.
- `areMoreMessagesAvailable(int,java.util.Date)` checks if there are more messages available in the IMAP folder newer than a specified date and before the oldest message currently displayed.
- `open(int)` opens a folder in a specified mode and throws an exception if the message count is not found.
- `fetch(java.util.List,com.fsck.k9.mail.FetchProfile,com.fsck.k9.mail.MessageRetrievalListener)` fetches a list of messages from an IMAP server according to a specified fetch profile and notifies a listener about the retrieval progress.
- `getMessage(java.lang.String)` returns an instance of `ImapMessage` with the given UID and folder reference.
- `delete(java.util.List,java.lang.String)` deletes a list of messages from an IMAP folder, either moving them to a specified trash folder or marking them as deleted if no trash folder is specified.
- `appendMessages(java.util.List)` appends a list of messages to an IMAP folder while also determining and changing their UIDs on the server.
- `fetchPart(com.fsck.k9.mail.Message,com.fsck.k9.mail.Part,com.fsck.k9.mail.MessageRetrievalListener,com.fsck.k9.mail.BodyFactory)` fetches a specified part of a message using the IMAP protocol and passes it to the given message retrieval listener with the help of a body factory.
- `getMessages(int,int,java.util.Date,com.fsck.k9.mail.MessageRetrievalListener)` retrieves a list of IMAP messages within a specified range and earliest date, with support for a retrieval listener.

## class `com.fsck.k9.mail.store.imap.ImapStore`

This class provides methods to interact with an IMAP email server, such as creating URIs, getting folders, checking settings, and supporting push notifications.

This class contains the following public method(s):

- `isCopyCapable()` returns a boolean value indicating whether the `ImapStore` class is capable of copying email messages.
- `createUri(com.fsck.k9.mail.ServerSettings)` creates an IMAP URI string using server settings.
- `getPusher(com.fsck.k9.mail.PushReceiver)` returns a new instance of the class `ImapPusher` with the given `ImapStore` and `PushReceiver` parameters.
- `getFolder(java.lang.String)` returns an instance of an IMAP folder with the given name, creating it if it doesn't already exist in the folder cache.
- `isMoveCapable()` returns a boolean value indicating whether or not the ImapStore class is capable of moving messages.
- `checkSettings()` checks the IMAP connection settings by creating an IMAP connection, autoconfiguring folders, and catching any errors that arise.
- `getPersonalNamespaces(boolean)` returns a list of personal namespaces/folders in an IMAP store and filters them based on whether they are subscribed to or not.
- `isPushCapable()` returns a boolean indicating whether the ImapStore is capable of supporting push notifications.
- `isExpungeCapable()` returns a boolean value indicating whether or not the ImapStore is capable of expunging messages.
- `decodeUri(java.lang.String)` decodes a given URI string into an `ImapStoreSettings` object using the `ImapStoreUriDecoder` class.

## class `com.fsck.k9.mail.store.imap.ImapFolderPusher$PushRunnable`

This class handles pushing new email messages to an IMAP folder in an email client's folder pusher and handles exceptions that may occur during that process.

This class contains the following public method(s):

- `handleAsyncUntaggedResponse(com.fsck.k9.mail.store.imap.ImapResponse)` handles an asynchronous untagged response from an IMAP server in an email client's folder pusher.
- `run()` implements the logic for pushing new email messages to an IMAP folder and handles exceptions that may occur during that process.

## class `com.fsck.k9.mail.store.imap.CopyUidResponse`

This class parses IMAP responses and provides UID mappings for copied messages.

This class contains the following public method(s):

- `parse(com.fsck.k9.mail.store.imap.ImapResponse)` parses an IMAP response to get the UID mapping for copied messages.
- `getUidMapping()` returns a `Map` object containing UID mappings as key-value pairs between source and destination mailboxes.

## class `com.fsck.k9.mail.store.imap.ListResponse`

This class provides methods for parsing and accessing information about IMAP mailbox listings.

This class contains the following public method(s):

- `getHierarchyDelimiter()` returns the hierarchy delimiter used in the response of an IMAP LIST command.
- `parseList(java.util.List)` parses a list of IMAP responses into a list of `ListResponse` objects.
- `getName()` returns the name attribute of an instance of the `ListResponse` Java class as a String.
- `parseLsub(java.util.List)` parses a List of ImapResponse objects and returns a List of ListResponse objects using the LSUB response type.
- `getAttributes()` returns a list of attributes of an IMAP mailbox as strings.
- `hasAttribute(java.lang.String)` checks if a given attribute exists in a list of attributes and returns a boolean value accordingly.


# package `com.fsck.k9.mail.store.pop3`

This package provides classes and functionalities for interacting with a POP3 email server in Java.

This package contains the following class(es):

## class `com.fsck.k9.mail.store.pop3.Pop3Store$Pop3Capabilities`

This class provides information on the capabilities and features supported by a POP3 email server.

This class contains the following public method(s):

- `toString()` returns a formatted string containing the available capabilities of a POP3 email store, including authentication methods and supported commands.

## class `com.fsck.k9.mail.store.pop3.Pop3Store$Pop3ResponseInputStream`

This class reads bytes from an input stream for a POP3 response.

This class contains the following public method(s):

- `read()` reads bytes from an input stream, checks for the end of a line and end of the response and returns the bytes read.

## class `com.fsck.k9.mail.store.pop3.Pop3Store`

This class provides methods to interact with a POP3 email server and manage email folders and settings.

This class contains the following public method(s):

- `isSeenFlagSupported()` returns a boolean value indicating whether the POP3 server supports the "seen" flag feature.
- `createUri(com.fsck.k9.mail.ServerSettings)` creates a Pop3Store URI based on the server settings provided.
- `decodeUri(java.lang.String)` decodes a Pop3Store URI into a ServerSettings object containing information such as the host, port, connection security, authentication type, username, and password.
- `getFolder(java.lang.String)` returns a Folder object with the given name, creating a new one if it does not already exist.
- `getPersonalNamespaces(boolean)` returns a list of personal namespaces (in this case, only the inbox folder) from a POP3 email server.
- `checkSettings()` checks the settings for a Pop3Store and verifies whether UIDL is supported by the server.

## class `com.fsck.k9.mail.store.pop3.Pop3Store$Pop3Message`

This class handles operations on POP3 email messages including setting and updating flags, marking as deleted, and setting message size.

This class contains the following public method(s):

- `setFlag(com.fsck.k9.mail.Flag,boolean)` sets a flag on a POP3 email message and updates the flag status for the corresponding folder.
- `delete(java.lang.String)` marks a Pop3Message as deleted by setting the `Flag.DELETED` flag to true.
- `setSize(int)` sets the size of a Pop3Message object.

## class `com.fsck.k9.mail.store.pop3.Pop3Store$Pop3Folder`

This class represents a POP3 email folder in a Java email client and provides methods to interact with the server, fetch and delete messages, and manage flags.

This class contains the following public method(s):

- `setFlags(java.util.Set,boolean)` throws an exception as it does not support setting flags in the POP3 protocol.
- `getMessage(java.lang.String)` returns a Pop3Message object with the given unique identifier or creates a new one if it does not exist in the map.
- `equals(java.lang.Object)` compares whether two `Pop3Folder` objects have the same name.
- `getName()` returns the name of a Pop3 folder in a Java email client.
- `close()` closes the connection to the POP3 server and releases resources.
- `getUnreadMessageCount()` returns -1 and throws a messaging exception when attempting to get the unread message count for a POP3 folder.
- `delete(java.util.List,java.lang.String)` marks the given list of email messages as deleted by setting the DELETED flag.
- `supportsFetchingFlags()` returns a boolean value indicating whether the Pop3Folder supports fetching flags or not.
- `getMessages(int,int,java.util.Date,com.fsck.k9.mail.MessageRetrievalListener)` retrieves a range of messages from a POP3 server and returns them as a list.
- `areMoreMessagesAvailable(int,java.util.Date)` checks if there are more messages available for retrieval in a POP3 email folder based on the index of the oldest message and earliest date provided.
- `getUidFromMessageId(com.fsck.k9.mail.Message)` returns null as it does not implement the functionality to retrieve a UID from the message ID.
- `getMode()` returns the open mode of the POP3 email folder as read-write.
- `appendMessages(java.util.List)` appends a list of messages to a Pop3 folder in a mail store but currently returns null.
- `open(int)` opens a POP3 folder and establishes a connection to the server, authenticates the user using the specified authentication method, and retrieves the number of messages in the folder.
- `isOpen()` checks if the Pop3 folder connection is open.
- `create(com.fsck.k9.mail.Folder$FolderType)` returns `false` when trying to create a folder of a specified `FolderType` in a `Pop3Folder` of the `Pop3Store`.
- `isFlagSupported(com.fsck.k9.mail.Flag)` checks whether the given flag (in this case, the "DELETED" flag) is supported by the POP3 email server.
- `getMessageCount()` returns the message count of a POP3 email folder.
- `delete(boolean)` deletes emails from a POP3 server folder, with an option to recursively delete sub-folders.
- `fetch(java.util.List,com.fsck.k9.mail.FetchProfile,com.fsck.k9.mail.MessageRetrievalListener)` fetches and populates the given list of messages with the requested content based on the specified FetchProfile.
- `exists()` checks if the given Pop3 folder exists by comparing its name with the name of the inbox folder in the email store configuration.
- `getFlaggedMessageCount()` returns -1 as the flagged message count for a POP3 folder in a mail store.
- `hashCode()` returns the hash code of the name of the Pop3Store folder.
- `setFlags(java.util.List,java.util.Set,boolean)` sets the "Deleted" flag for a list of messages in a POP3 email account.


# package `com.fsck.k9.mail.store.webdav`

This package provides functionality for accessing and managing email messages in a WebDAV email store through various classes.

This package contains the following class(es):

## class `com.fsck.k9.mail.store.webdav.DataSet`

This class provides various methods to manipulate and retrieve data related to mailbox messages, URLs and their attributes in a WebDAV store.

This class contains the following public method(s):

- `getUids()` returns an array of all Message UIDs that were received.
- `getHrefs()` returns an array of all hrefs (urls) that were received by iterating over a list of data using a for loop.
- `getMessageEnvelopes()` returns a mapping of message UIDs to parsed message envelopes.
- `getSpecialFolderToUrl()` returns a hashmap of special folder name and their corresponding URLs.
- `getUidToRead()` returns a HashMap of message UIDs and their corresponding read statuses.
- `finish()` saves temporary data into the final data map with a given UID or handles lost data if there is no UID provided, then resets the temporary data and UID values.
- `getMessageCount()` returns the number of messages in a mailbox as retrieved from the data set.
- `addValue(java.lang.String,java.lang.String)` adds a key-value pair to a temporary data map, with an additional check for a specific tag name to set a separate value.
- `getUidToUrl()` returns a hashmap of message UIDs mapped to their corresponding URLs.

## class `com.fsck.k9.mail.store.webdav.WebDavHttpClient`

This class provides functionality for executing HTTP requests and handling gzipped responses in a WebDAV mail store.

This class contains the following public method(s):

- `executeOverride(org.apache.http.client.methods.HttpUriRequest,org.apache.http.protocol.HttpContext)` modifies the request to accept gzip response and then executes the request using the superclass method.
- `modifyRequestToAcceptGzipResponse(org.apache.http.HttpRequest)` adds a header to an HTTP request indicating that the client can accept a gzipped response.
- `getUngzippedContent(org.apache.http.HttpEntity)` gets the content from a given HTTP entity and unzips it if it's compressed using GZip.

## class `com.fsck.k9.mail.store.webdav.WebDavHttpClient$WebDavHttpClientFactory`

This class creates a new instance of the WebDavHttpClient class.

This class contains the following public method(s):

- `create()` creates a new instance of the WebDavHttpClient class.

## class `com.fsck.k9.mail.store.webdav.WebDavStoreSettings`

This class provides settings for a WebDav email store, such as retrieving extra settings and creating a new instance with a new password.

This class contains the following public method(s):

- `getExtra()` returns a map of strings that represent extra settings for a WebDav email store.
- `newPassword(java.lang.String)` creates a new instance of the WebDavStoreSettings class with a new password.

## class `com.fsck.k9.mail.store.webdav.WebDavHandler`

This class is a WebDav handler for a Java mail store that parses XML data and populates a Java object with the data.

This class contains the following public method(s):

- `getDataSet()` returns the dataset of a WebDav handler in a Java mail store.
- `endElement(java.lang.String,java.lang.String,java.lang.String)` removes the first element from a list and resets temporary variables if a certain tag is encountered.
- `startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)` adds the local name of the current element being parsed to a linked list called `mOpenTags`.
- `endDocument()` overrides the `endDocument()` method of the `org.xml.sax.ContentHandler` interface and does nothing when the end of the XML document is reached during parsing.
- `startDocument()` initializes a new instance of the `DataSet` class and assigns it to the `mDataSet` variable in the `WebDavHandler` class.
- `characters(char[],int,int)` adds a value to the mDataSet based on the content of the character array ch, within the specified start and length indexes, and associates it with the last open tag in the mOpenTags stack.

## class `com.fsck.k9.mail.store.webdav.WebDavStoreUriCreator`

This class creates a WebDAV store URI for a given server setting.

This class contains the following public method(s):

- `create(com.fsck.k9.mail.ServerSettings)` creates a WebDAV store URI with the supplied server settings.

## class `com.fsck.k9.mail.store.webdav.WebDavStoreUriDecoder`

This class decodes a WebDavStore URI into its parts and creates a new instance of `WebDavStoreSettings`.

This class contains the following public method(s):

- `decode(java.lang.String)` decodes a given WebDavStore URI into its constituent parts and returns a new instance of `WebDavStoreSettings` using these parts.

## class `com.fsck.k9.mail.store.webdav.HttpGeneric`

This class handles HTTP requests for webdav communication.

This class contains the following public method(s):

- `getMethod()` returns the HTTP method name used in this instance of `HttpGeneric` class.
- `setMethod(java.lang.String)` sets the HTTP method for the webdav communication, as long as the input provided is not null.

## class `com.fsck.k9.mail.store.webdav.WebDavMessage`

This class provides methods for handling email messages stored in a WebDav server.

This class contains the following public method(s):

- `setFlagInternal(com.fsck.k9.mail.Flag,boolean)` sets the given flag for a WebDavMessage instance.
- `setSize(int)` sets the size of a WebDav message through the "mSize" attribute of the WebDavMessage class.
- `setFlag(com.fsck.k9.mail.Flag,boolean)` sets a flag on a WebDavMessage and updates the flag in the remote folder.
- `setUrl(java.lang.String)` sets the URL of a WebDavMessage object while ensuring it is properly formatted and encoded.
- `delete(java.lang.String)` deletes a message by moving it to a specified trash folder using WebDav.
- `setNewHeaders(com.fsck.k9.mail.store.webdav.ParsedMessageEnvelope)` sets new headers for a WebDav email message based on a parsed message envelope.
- `getUrl()` returns the URL of an email message stored in a WebDav server.

## class `com.fsck.k9.mail.store.webdav.ParsedMessageEnvelope`

This class provides methods to manipulate and retrieve information about a parsed email message in a WebDAV email store.

This class contains the following public method(s):

- `getMessageHeaders()` (no description)
- `addHeader(java.lang.String,java.lang.String)` adds the header and its corresponding value to the message's headers map, if the header name is a valid mapping defined in the class.
- `setReadStatus(boolean)` sets the read status of a parsed email message.
- `setUid(java.lang.String)` sets the UID (unique identifier) of the parsed message envelope object to the specified value, if the provided UID is not null.
- `getHeaderList()` returns an array of header strings of a parsed message envelope using the WebDAV protocol.
- `getUid()` returns the UID of a parsed message envelope in the form of a String.
- `getReadStatus()` returns the read status of a parsed message envelope in a WebDAV email store.

## class `com.fsck.k9.mail.store.webdav.WebDavFolder`

This class provides methods to interact with an email folder in a WebDAV email account.

This class contains the following public method(s):

- `getMessages(int,int,java.util.Date,com.fsck.k9.mail.MessageRetrievalListener)` retrieves a list of WebDav messages within a given range and earliest date, with the option to listen for message retrieval events.
- `appendMessages(java.util.List)` appends a list of email messages to a WebDav folder and returns null.
- `create(com.fsck.k9.mail.Folder$FolderType)` simply returns true without any actual implementation or creation of a folder in the WebDav storage.
- `getUrl()` returns the URL of a WebDav folder.
- `isOpen()` (no description)
- `delete(java.util.List,java.lang.String)` deletes a list of email messages by moving them to the trash folder.
- `moveMessages(java.util.List,com.fsck.k9.mail.Folder)` moves a list of email messages to a different folder in a WebDav email account.
- `exists()` returns `true` if the webdav folder exists, otherwise it returns `false`.
- `appendWebDavMessages(java.util.List)` appends a list of messages to a folder using the WebDAV protocol.
- `setUrl(java.lang.String)` sets the URL for the WebDav folder.
- `delete(boolean)` throws an error indicating that the `delete(boolean)` method has not been implemented in the `WebDavFolder` class.
- `areMoreMessagesAvailable(int,java.util.Date)` checks if there are more messages available in a WebDav folder by comparing the index of the oldest message and the earliest date requested.
- `copyMessages(java.util.List,com.fsck.k9.mail.Folder)` copies a list of email messages to a specified folder using the WebDAV protocol.
- `equals(java.lang.Object)` checks if an object is equal to a WebDavFolder object based on their name attribute.
- `getName()` returns the name of a WebDavFolder object in a Java program.
- `getMode()` returns the open mode of a WebDavFolder as read and write.
- `setFlags(java.util.Set,boolean)` sets the flags of messages in a WebDav email folder, but it is currently unimplemented and may cause issues with other methods.
- `getFlaggedMessageCount()` returns -1 because it is not implemented and throws a messaging exception when called.
- `close()` resets the message and unread message count to 0 and sets the folder state to closed for a WebDAV email folder in K9 email client.
- `getUidFromMessageId(com.fsck.k9.mail.Message)` returns null and logs an error message because the method is not yet implemented.
- `getUnreadMessageCount()` opens a WebDavFolder, retrieves the number of unread messages, and returns that count.
- `getMessageCount()` returns the number of messages in a WebDav email folder.
- `setFlags(java.util.List,java.util.Set,boolean)` sets flags for a list of email messages in a WebDav email folder based on the provided flags and a boolean value.
- `fetch(java.util.List,com.fsck.k9.mail.FetchProfile,com.fsck.k9.mail.MessageRetrievalListener)` fetches envelope information, message flag info, and message bodies from a list of WebDav messages based on a given fetch profile and message retrieval listener.
- `getMessage(java.lang.String)` returns a new instance of the `WebDavMessage` class using the provided `uid` and `WebDavFolder`.
- `open(int)` opens a WebDav folder in the specified mode.

## class `com.fsck.k9.mail.store.webdav.WebDavSocketFactory`

This class provides methods for creating and managing SSL sockets for WebDAV connections.

This class contains the following public method(s):

- `createSocket(java.net.Socket,java.lang.String,int,boolean)` creates a SSL socket with a specified host and port, sets the Server Name Indication (SNI) for the SSL socket, and returns the socket.
- `createSocket()` overrides the `createSocket()` method of a superclass to return a socket created by the `mSocketFactory` object.
- `isSecure(java.net.Socket)` checks if the given socket is secure using the underlying scheme socket factory.
- `connectSocket(java.net.Socket,java.lang.String,int,java.net.InetAddress,int,org.apache.http.params.HttpParams)` connects a socket to a specific host and port using a WebDavSocketFactory.

## class `com.fsck.k9.mail.store.webdav.WebDavStore`

This class provides functionality for accessing and managing email messages in a WebDAV email store.

This class contains the following public method(s):

- `createUri(com.fsck.k9.mail.ServerSettings)` creates a URI for a WebDAV store based on the server settings provided.
- `sendMessages(java.util.List)` sends a list of email messages by appending them to a drafts folder, then moving them to a spool folder for subsequent sending.
- `getAuthCookies()` returns the authentication cookies for a WebDav store.
- `getAuthString()` returns the authentication string for the WebDavStore.
- `isCopyCapable()` returns a boolean value indicating whether this WebDavStore is capable of copying email messages.
- `isMoveCapable()` determines whether the WebDavStore is capable of moving emails between folders.
- `getFolder(java.lang.String)` returns a WebDavFolder object with a given name if it exists, otherwise creates a new one and adds it to the list of folders before returning it.
- `isSendCapable()` returns whether or not the WebDavStore is capable of sending email.
- `getUrl()` returns the base URL of a WebDavStore instance.
- `checkSettings()` checks the settings by authenticating the user in a WebDav email store for a Java class.
- `getAlias()` returns the alias of the WebDavStore.
- `getPersonalNamespaces(boolean)` gets a list of personal namespaces and their associated special folders for a WebDav email account.
- `decodeUri(java.lang.String)` decodes a URI string into a WebDavStoreSettings object.
- `getHttpClient()` returns an instance of an HTTP client for the WebDAV protocol with specific configurations and settings.


# package `com.fsck.k9.mail.store`

This package provides classes for managing and configuring remote mail stores.

This package contains the following class(es):

## abstract class `com.fsck.k9.mail.store.RemoteStore`

This abstract class provides methods for managing and creating instances of remote mail stores and decoding and creating store-specific URIs.

This class contains the following public method(s):

- `removeInstance(com.fsck.k9.mail.store.StoreConfig)` removes a reference to a remote mail store instance.
- `decodeStoreUri(java.lang.String)` decodes store-specific URI and returns a ServerSettings object holding the settings contained in the URI for IMAP, POP3, or WebDav stores.
- `getInstance(android.content.Context,com.fsck.k9.mail.store.StoreConfig)` returns an instance of a remote mail store based on the store URI.
- `createStoreUri(com.fsck.k9.mail.ServerSettings)` creates a store URI based on the server settings provided.

## interface `com.fsck.k9.mail.store.StoreConfig`

This interface defines methods for configuring various email folders and settings for a mail store.

This class contains the following public method(s):

- `setSentFolderName(java.lang.String)` sets the name of the sent folder for an email store configuration.
- `getMaximumAutoDownloadMessageSize()` returns the maximum message size that can be automatically downloaded by the email client.
- `isPushPollOnConnect()` checks if push polling should be enabled when connecting to the mail server.
- `setArchiveFolderName(java.lang.String)` sets the name of the folder to which emails are to be archived in a mail store.
- `setInboxFolderName(java.lang.String)` sets the name of the inbox folder for the email store configuration.
- `subscribedFoldersOnly()` returns a boolean value indicating whether only subscribed folders should be shown in the mail store.
- `setTrashFolderName(java.lang.String)` sets the name of the trash folder for the email storage configuration.
- `allowRemoteSearch()` returns a boolean indicating whether remote search is allowed for the email store configuration.
- `getStoreUri()` returns the URI of the mail store.
- `getIdleRefreshMinutes()` returns the number of minutes after which the mailbox should be refreshed while idle.
- `setAutoExpandFolderName(java.lang.String)` sets the name of the folder that should be automatically expanded when a user logs in to the email account.
- `setSpamFolderName(java.lang.String)` sets the name of the spam folder for the email account being configured.
- `isRemoteSearchFullText()` checks whether the remote email server supports full-text search.
- `getInboxFolderName()` returns the name of the inbox folder for the email store configuration.
- `getOutboxFolderName()` returns the name of the folder used for storing outgoing email messages.
- `setDraftsFolderName(java.lang.String)` sets the name of the folder where email drafts are stored in a specific email configuration.
- `getDisplayCount()` returns the number of messages to be displayed in the UI for a store configuration.
- `getDraftsFolderName()` returns the name of the drafts folder for a particular email store configuration.
- `useCompression(com.fsck.k9.mail.NetworkType)` determines whether or not to use compression for a given network type.
- `getTransportUri()` returns the transport URI for connecting to a mail store.


