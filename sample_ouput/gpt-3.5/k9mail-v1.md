# package `com.fsck.k9`

The `com.fsck.k9` package contains classes and interfaces that are used to manage email accounts and settings, restrict event triggers, enhance security of the pseudo-random number generator, validate email addresses, and provide access to context and font size settings in the K-9 email client application for Android.

This package contains the following class(es):

## class `com.fsck.k9.Throttle$MyTimerTask`

The class `com.fsck.k9.Throttle$MyTimerTask` is a timer task that schedules the execution of a `HandlerRunnable` object on a `Handler` instance, but can be cancelled if necessary.

This class contains the following public method(s):

- `run()` -- The method `run()` posts a `HandlerRunnable` object to a `Handler` instance.
- `cancel()` -- The method cancels the execution of a scheduled task.

## class `com.fsck.k9.Throttle`

The purpose of the class `com.fsck.k9.Throttle` is to restrict the frequency at which events can be triggered in a system, by setting a timeout and scheduling callbacks.

This class contains the following public method(s):

- `cancelScheduledCallback()` -- The method cancels a scheduled callback for the Throttle instance.
- `onEvent()` -- The method `onEvent()` updates the timeout and schedules a callback for the Throttle.

## class `com.fsck.k9.PRNGFixes`

The class `com.fsck.k9.PRNGFixes` provides fixes to the pseudo-random number generator to enhance its security.

This class contains the following public method(s):

- `apply()` -- The method applies fixes to the pseudo-random number generator to improve security.

## interface `com.fsck.k9.BaseAccount`

The interface `com.fsck.k9.BaseAccount` defines methods for managing email accounts, including setting and getting the email address, UUID, and description of the account.

This class contains the following public method(s):

- `setEmail(java.lang.String)` -- The method sets the email address for the account.
- `getEmail()` -- The method `getEmail()` returns the email address associated with the account.
- `getUuid()` -- This method returns the universally unique identifier (UUID) of the email account.
- `getDescription()` -- The method is used to get a textual description of the account.
- `setDescription(java.lang.String)` -- This method sets the description of the email account.

## class `com.fsck.k9.Throttle$MyTimerTask$HandlerRunnable`

The purpose of the class is to run a timer task and call a callback if it has not been canceled.

This class contains the following public method(s):

- `run()` -- The `run()` method sets the running timer task to null and kicks the callback if the task has not been canceled.

## class `com.fsck.k9.K9`

The class `com.fsck.k9.K9` is the main class of the K9 email client application for Android, containing various methods for managing settings and preferences of the application.

This class contains the following public method(s):

- `messageListSenderAboveSubject()` -- The method returns a boolean value indicating whether the sender of a message should be displayed above the subject in the message list.
- `setDebug(boolean)` -- (no description)
- `setContactNameColor(int)` -- (no description)
- `setConfirmDeleteStarred(boolean)` -- Sets whether to prompt for confirmation before deleting a starred message in K9 email client.
- `setBackgroundOps(com.fsck.k9.K9$BACKGROUND_OPS)` -- This method sets the background operation mode of the K9 email client and returns true if the new mode is different from the previous mode.
- `setNotificationDuringQuietTimeEnabled(boolean)` -- This method sets the notification during quiet time enabled/disabled flag in the K9 email client.
- `getSplitViewMode()` -- This method returns the split view mode of the K9 email client.
- `setAnimations(boolean)` -- Sets whether animations should be enabled or disabled in the K9 mail app.
- `setDatabasesUpToDate(boolean)` -- The method sets a flag to indicate that all account databases are using the most recent schema and optionally saves the current schema version to SharedPreferences.
- `setGesturesEnabled(boolean)` -- To enable or disable touch gestures in the K9 email client.
- `useBackgroundAsUnreadIndicator()` -- The method determines whether to use a background color as an indicator for unread messages in the K9 email client.
- `isColorizeMissingContactPictures()` -- The method returns whether or not K9 should colorize missing contact pictures.
- `setMessageViewReturnToList(boolean)` -- This method sets a boolean flag indicating whether returning to the message list after viewing a message should be enabled or disabled.
- `getOpenPgpSupportSignOnly()` -- This method returns the value of a boolean flag indicating whether OpenPGP signing is supported in the application.
- `setPgpInlineDialogCounter(int)` -- The purpose of the method is to set the counter for PGP inline dialogs in the email client K9.
- `registerApplicationAware(com.fsck.k9.K9$ApplicationAware)` -- The method registers a component to be notified when the K9 application instance is ready.
- `setNotificationQuickDeleteBehaviour(com.fsck.k9.K9$NotificationQuickDelete)` -- The purpose of the method is to set the notification quick delete behavior of the K9 email client.
- `setHideUserAgent(boolean)` -- The method sets the state of whether to hide the user agent used by K9.
- `setMessageViewArchiveActionVisible(boolean)` -- The method sets the visibility of the archive action in the message view of the K9 email client.
- `setLockScreenNotificationVisibility(com.fsck.k9.K9$LockScreenNotificationVisibility)` -- The method sets the visibility of K-9 Mail's notifications on the lock screen.
- `setMessageListPreviewLines(int)` -- The purpose of this method is to set the number of lines shown for message preview in the K9 email client.
- `setQuietTimeStarts(java.lang.String)` -- The method sets the starting time for quiet mode in the K9 email client.
- `messageViewShowNext()` -- The purpose of this method is to return whether the next message should be shown in the message view or not.
- `setHideTimeZone(boolean)` -- The method sets whether or not the time zone is hidden in K9 email notifications.
- `isMessageViewCopyActionVisible()` -- This method checks whether the copy action is visible in the message view in the K9 email client.
- `showCorrespondentNames()` -- This method returns a boolean value indicating whether K9 application should display correspondent names or not.
- `getPgpSignOnlyDialogCounter()` -- This method returns the counter value of the number of times a user has been warned about signing an encrypted email without encryption.
- `save(com.fsck.k9.preferences.StorageEditor)` -- The method saves various preferences of the K-9 email client to a `StorageEditor` instance.
- `getQuietTimeEnabled()` -- This method returns whether or not the quiet time feature is enabled in the K9 email application.
- `setSplitViewMode(com.fsck.k9.K9$SplitViewMode)` -- The method sets the split view mode for the K9 email client.
- `getSortType()` -- This method returns the current sorting type used in the K9 email client.
- `setMessageViewFixedWidthFont(boolean)` -- The method sets a flag indicating whether the message view font should have a fixed width or not in the K9 email client.
- `setQuietTimeEnabled(boolean)` -- The method is used to enable/disable the quiet time mode in the K-9 email client.
- `getK9ThemeResourceId(com.fsck.k9.K9$Theme)` -- This method returns the resource ID for the appropriate K9 theme based on the specified theme ID.
- `getK9ThemeResourceId()` -- The method returns the resource ID for the K-9 mail app theme.
- `setMessageViewCopyActionVisible(boolean)` -- This method sets the visibility of the copy action button in the email message view of the K9 email client.
- `getK9Language()` -- This method returns the language used by the K9 email client.
- `getK9MessageViewTheme()` -- The method returns the theme to use for displaying a message in K9 mail, either the global theme or the specific message view theme.
- `showContactName()` -- The method returns whether to display the contact name in K9 email app.
- `gesturesEnabled()` -- This method returns a boolean indicating whether gestures are enabled in the K9 email application.
- `setShowContactName(boolean)` -- The method is used to toggle whether or not contact names are displayed.
- `wrapFolderNames()` -- The method returns the value of a static boolean variable that indicates whether folder names should be wrapped in the K9 email client.
- `setMessageListSenderAboveSubject(boolean)` -- The method sets whether the sender should be displayed above the subject in the message list.
- `getLockScreenNotificationVisibility()` -- This method returns the current lock screen notification visibility setting in the K9 email client.
- `getFontSizes()` -- The method returns the font sizes used in the K9 email client.
- `isNotificationDuringQuietTimeEnabled()` -- To check if the notification during quiet time is enabled.
- `measureAccounts()` -- This method returns the value of a boolean flag indicating whether account measurements are enabled in K9.
- `useFixedMessageViewTheme()` -- The method returns whether a fixed message view theme is being used in the K9 email client.
- `setSortAscending(com.fsck.k9.Account$SortType,boolean)` -- The method sets whether the sorting order for a specified account type should be ascending or descending.
- `getBackgroundOps()` -- This method returns the value of the static variable `backgroundOps` in the `K9` class, which specifies the background operations mode.
- `setColorizeMissingContactPictures(boolean)` -- The method is used to set a boolean flag indicating whether missing contact pictures should be colorized.
- `confirmSpam()` -- This method returns a boolean indicating whether the user has confirmed that an email is spam.
- `areDatabasesUpToDate()` -- The purpose of the method `areDatabasesUpToDate()` is to check if all databases are using the current database schema.
- `isThreadedViewEnabled()` -- The method returns a boolean indicating whether the threaded view is enabled in the K9 email client.
- `setWrapFolderNames(boolean)` -- This method sets the state of whether or not K9 wraps long folder names.
- `getK9ComposerTheme()` -- This method returns the theme to use in the composer, either the globally set theme or the theme specifically set for the composer.
- `setMessageListCheckboxes(boolean)` -- This method sets the value of a static boolean variable that determines whether checkboxes are shown in the message list view.
- `onCreate()` -- This method is called when the activity is starting, and it initializes various components of the K9 email client application.
- `getQuietTimeStarts()` -- The method returns the start time of the quiet time feature of the K9 email client.
- `showContactPicture()` -- This method returns a boolean indicating if K9 should show contact pictures.
- `messageListCheckboxes()` -- This method returns a boolean indicating if checkboxes should be displayed in the message list.
- `setAutofitWidth(boolean)` -- This method sets whether or not the width of certain UI elements in the K9 email client should be automatically adjusted based on the screen size of the device.
- `getQuietTimeEnds()` -- The method returns the end time of the quiet time setting in the K9 email app.
- `setMessageViewShowNext(boolean)` -- The method sets whether the next message should be displayed in the message view.
- `setChangeContactNameColor(boolean)` -- This method sets a flag to indicate whether to change the color of contact names in the K9 email app.
- `setConfirmDeleteFromNotification(boolean)` -- Sets whether or not to confirm deletion of a message from a notification in the K9 email client.
- `confirmDeleteStarred()` -- This method returns a boolean indicating if confirmation is needed before deleting a starred item in the K-9 email client.
- `setNotificationHideSubject(com.fsck.k9.K9$NotificationHideSubject)` -- Sets the mode for hiding email subjects in notifications for the K9 email client.
- `setUseFixedMessageViewTheme(boolean)` -- The method sets whether to use a fixed message view theme in K9 email client.
- `autofitWidth()` -- This method returns a boolean value indicating whether autofit width is enabled in the K9 email client.
- `hideUserAgent()` -- The method returns a boolean indicating whether to hide the user agent or not in the K9 email client.
- `setMessageViewDeleteActionVisible(boolean)` -- The method sets the visibility of the delete action button in email message viewing mode.
- `checkCachedDatabaseVersion()` -- The method checks if the stored version of the account databases matches the current version, indicating if database upgrades are required.
- `isHideSpecialAccounts()` -- The method returns whether special accounts are hidden or not.
- `setConfirmMarkAllRead(boolean)` -- This method sets whether to confirm before marking all emails as read.
- `confirmDelete()` -- This method returns whether or not the email deletion confirmation dialog should be shown.
- `isMessageViewArchiveActionVisible()` -- The method returns whether the archive action is visible in the message view.
- `getContactNameColor()` -- The method returns the color used for contact names in K-9 mail.
- `getK9Theme()` -- This method returns the current theme used by the K9 email client.
- `setStartIntegratedInbox(boolean)` -- Sets whether K9 Mail should start with the integrated inbox or not.
- `countSearchMessages()` -- The method returns a boolean indicating whether or not K9 should count search result messages.
- `setMessageViewMoveActionVisible(boolean)` -- The method sets the visibility of a move action in the K9 email client's message view.
- `isDebug()` -- The method checks whether the `K9` class is in debug mode or not.
- `getNotificationHideSubject()` -- This method returns the notification hide subject for the K9 email client.
- `setQuietTimeEnds(java.lang.String)` -- This method sets the end time of a period of quiet time in a email client application.
- `getPgpInlineDialogCounter()` -- The method returns the number of times the PGP inline dialog has been shown in the K9 email client.
- `setBackgroundOps(java.lang.String)` -- This method sets the background operations of the K9 email client to the specified value.
- `setConfirmSpam(boolean)` -- The method sets a boolean flag to confirm user action of marking an email as spam.
- `setServicesEnabled(android.content.Context)` -- Enables/disables certain features in the K9 email client based on whether any accounts are configured.
- `setHideSpecialAccounts(boolean)` -- The method sets whether special accounts should be hidden or not in the K9 email client.
- `isSortAscending(com.fsck.k9.Account$SortType)` -- The method checks if the specified sort type is set to ascending order and returns true if it is, false otherwise.
- `loadPrefs(com.fsck.k9.Preferences)` -- The method loads preferences into static variables used by the K-9 email app.
- `setMessageListStars(boolean)` -- The method sets whether starred messages are shown in the message list or not in the K9 email client.
- `setOpenPgpSupportSignOnly(boolean)` -- The method sets whether or not K9 should only support OpenPGP signing.
- `getNotificationQuickDeleteBehaviour()` -- This method returns the quick delete behavior for notifications used by the K9 email client.
- `showAnimations()` -- This method returns the value of a boolean variable indicating whether animations are enabled in the K9 email client.
- `setUseVolumeKeysForListNavigation(boolean)` -- This method sets the option for using volume keys for list navigation in the K9 email application.
- `getK9MessageViewThemeSetting()` -- The method returns the current theme used for displaying email messages in the K-9 email client.
- `setAttachmentDefaultPath(java.lang.String)` -- To set the default path for saving email attachments in the K9 email client.
- `setPgpSignOnlyDialogCounter(int)` -- The purpose of this method is to set the counter for PGP sign-only dialogs in K9 email client.
- `setThreadedViewEnabled(boolean)` -- The method enables or disables threaded email view in the K9 email client.
- `isMessageViewMoveActionVisible()` -- The purpose of this method is to determine if the message view move action is currently visible.
- `confirmDiscardMessage()` -- The method returns whether or not to confirm discarding a message based on the value of a flag.
- `setOpenPgpProvider(java.lang.String)` -- This method sets the OpenPGP provider used by K9 email client.
- `isMessageViewSpamActionVisible()` -- The method returns a boolean value indicating if the spam action is visible in the message view in the K9 email client.
- `useVolumeKeysForNavigationEnabled()` -- This method returns whether the use of volume keys for navigation is enabled in the K9 email client.
- `isOpenPgpProviderConfigured()` -- To determine if an OpenPGP provider is configured for use in the K9 email client.
- `useVolumeKeysForListNavigationEnabled()` -- The method returns whether the use of volume keys for list navigation is enabled in the K9 email application.
- `setK9MessageViewThemeSetting(com.fsck.k9.K9$Theme)` -- The method sets the message view theme setting in the K9 email client.
- `messageListPreviewLines()` -- The method returns the number of preview lines to be displayed for each message in the message list.
- `setShowContactPicture(boolean)` -- The method sets whether to show contact pictures in K9 email client.
- `setMessageViewSpamActionVisible(boolean)` -- This method sets the visibility of the spam action in the message view of the K-9 email client.
- `getOpenPgpProvider()` -- The method returns the OpenPGP provider string used by the K9 email client.
- `setMeasureAccounts(boolean)` -- The method sets a boolean flag that determines whether or not account measurement should be enabled in K9.
- `confirmDeleteFromNotification()` -- The method returns the value of a static boolean variable `mConfirmDeleteFromNotification` which determines whether the user should be prompted for confirmation before deleting a message from the notification shade.
- `setConfirmDelete(boolean)` -- Sets whether or not to confirm email message deletion in the K9 email client.
- `messageViewFixedWidthFont()` -- The method returns the current state of the `messageViewFixedWidthFont` setting in the K9 email client.
- `isMessageViewDeleteActionVisible()` -- The method checks whether the delete action is visible in the K9 email message view.
- `messageListStars()` -- The method returns a boolean value indicating whether messages in a list can be starred.
- `changeContactNameColor()` -- The purpose of this method is to return a boolean value indicating whether the contact name color has been changed in the K9 email client.
- `startIntegratedInbox()` -- This method returns a boolean value indicating whether the integrated inbox feature of the K9 email client is enabled or not.
- `setSortType(com.fsck.k9.Account$SortType)` -- The method sets the sorting type for emails of a K9 email account.
- `setK9ComposerThemeSetting(com.fsck.k9.K9$Theme)` -- The method sets the theme for the K9 email composer.
- `hideTimeZone()` -- This method returns whether or not the time zone should be hidden in the user interface.
- `getK9ComposerThemeSetting()` -- The method returns the composer theme setting of the K9 email client.
- `setConfirmDiscardMessage(boolean)` -- The method sets a flag to confirm whether to discard a message in the email client application.
- `getAttachmentDefaultPath()` -- The method returns the default file path for email attachments in the K9 email client.
- `saveSettingsAsync()` -- The purpose of the `saveSettingsAsync()` method is to save the settings of the K-9 Mail application asynchronously.
- `setCountSearchMessages(boolean)` -- The method sets a boolean value to determine whether K9 email app should count search messages or not.
- `isQuietTime()` -- This method determines if it is currently within a designated quiet time period.
- `setK9Language(java.lang.String)` -- The method sets the language of the email client K-9 Mail to the specified language.
- `setUseBackgroundAsUnreadIndicator(boolean)` -- The method sets whether the background should be used as an indicator for unread messages in K9 email client.
- `setUseVolumeKeysForNavigation(boolean)` -- The method sets whether or not the volume keys should be used for navigation in the K9 email client.
- `setShowCorrespondentNames(boolean)` -- This method sets whether or not to show correspondent names in the K9 email client.
- `setK9Theme(com.fsck.k9.K9$Theme)` -- The method sets the theme of the K9 email client except for the global theme setting.
- `messageViewReturnToList()` -- The method returns a boolean indicating whether the message view should return to the message list.
- `confirmMarkAllRead()` -- This method returns a boolean value indicating whether the user has confirmed to mark all messages as read in the email application.

## class `com.fsck.k9.EmailAddressValidator`

The purpose of the class is to provide methods to validate email addresses.

This class contains the following public method(s):

- `fixText(java.lang.CharSequence)` -- The method returns an empty string and seems to serve no practical purpose.
- `isValid(java.lang.CharSequence)` -- The method checks if the given text is a valid email address.
- `isValidAddressOnly(java.lang.CharSequence)` -- The method checks if a given text is a valid email address according to a predefined pattern.

## enum `com.fsck.k9.Account$SortType`

The enum `com.fsck.k9.Account$SortType` defines the sorting order options for email accounts in the K-9 Mail app, allowing users to sort their emails by various criteria such as date, subject, or sender.

This class contains the following public method(s):

- `isDefaultAscending()` -- This method returns a boolean value indicating whether the default sorting order is ascending or not.
- `getToast(boolean)` -- The `getToast` method returns a toast message depending on the sort order of the account.

## class `com.fsck.k9.Globals`

The purpose of the class `com.fsck.k9.Globals` is to provide access to the context of the application through its public method `getContext()`.

This class contains the following public method(s):

- `getContext()` -- This method returns the context of the application, throwing an exception if it is not set.

## class `com.fsck.k9.FontSizes`

The purpose of the `com.fsck.k9.FontSizes` class is to provide methods for setting and retrieving font sizes for various elements in an email client, such as message view, message list, and message compose input.

This class contains the following public method(s):

- `getMessageViewContentAsPercent()` -- This method returns the message content percent for the font size used in the message view.
- `getMessageViewDate()` -- The method returns the message view date for the FontSizes class in the form of an integer.
- `getFolderStatus()` -- This method returns the status of a folder as an integer value.
- `setMessageViewContentAsPercent(int)` -- The method sets the font size percentage for the content displayed in the email message view.
- `getMessageViewBCC()` -- This method returns the font size of the Bcc field in the message view.
- `setMessageViewSubject(int)` -- This method sets the font size for the subject line of an email message view.
- `setMessageListPreview(int)` -- The method sets the font size for the message preview in the message list display.
- `getMessageViewAdditionalHeaders()` -- This method returns the number of additional message headers that should be displayed in the message view.
- `getMessageListDate()` -- The method returns the font size of dates in the message list.
- `getMessageViewCC()` -- This method returns the font size of the message view's carbon copy text in pixels.
- `setMessageListDate(int)` -- This method sets the font size of the date in a message list.
- `setMessageViewTo(int)` -- This method sets the message View size to the specified integer value.
- `getMessageComposeInput()` -- The method returns the message compose input font size.
- `getMessageViewSubject()` -- This method returns the font size for the subject of an email message in K-9 Mail's message view.
- `setMessageListSender(int)` -- The purpose of this method is to set the font size for the sender name in the message list.
- `getMessageViewSender()` -- This method retrieves the font size for the sender's name displayed in the message view.
- `load(com.fsck.k9.preferences.Storage)` -- The method loads values for various font sizes from a storage object.
- `setAccountDescription(int)` -- This method sets the font size for the account description.
- `setAccountName(int)` -- The method sets the account name of the font sizes for a particular account.
- `setMessageViewSender(int)` -- Sets the ID for the sender view in the message list.
- `setMessageListSubject(int)` -- The method sets the font size of the subject text in the message list.
- `getMessageListPreview()` -- This method returns the preview message font size for a message list view.
- `getMessageListSender()` -- The method returns the font size for the sender field in the message list view.
- `setMessageViewBCC(int)` -- This method sets the font size for the BCC section of an email message view.
- `setViewTextSize(android.widget.TextView,int)` -- This method sets the text size of a TextView to a specified font size.
- `setMessageViewAdditionalHeaders(int)` -- The method sets the number of additional message headers to be shown in the message view.
- `setFolderName(int)` -- This method sets the font size for folder names in an email client.
- `getMessageViewTo()` -- The method returns the value of the messageViewTo variable which indicates the maximum font size allowed in a message view.
- `getAccountDescription()` -- The method returns the account description's font size.
- `getMessageListSubject()` -- The method returns the font size for the subject line in the message list.
- `setMessageComposeInput(int)` -- This method sets the font size of the message compose input field.
- `setMessageViewDate(int)` -- This method sets the font size of the date in the message view.
- `save(com.fsck.k9.preferences.StorageEditor)` -- The `save` method saves font sizes to shared preferences using a StorageEditor object.
- `getAccountName()` -- This method returns an integer representing the account name.
- `getFolderName()` -- The method returns the name of the font size folder as an integer.
- `setMessageViewCC(int)` -- This method sets the font size for the carbon copy recipients in the message view.
- `setFolderStatus(int)` -- This method sets the status of a folder.

## class `com.fsck.k9.NotificationSetting`

The `com.fsck.k9.NotificationSetting` class provides methods for reading and modifying notification settings for the K-9 email client, including settings for ringtone, vibration, and LED notifications.

This class contains the following public method(s):

- `isRingEnabled()` -- The method returns whether the ringtone is allowed to play or not.
- `isVibrateEnabled()` -- This method returns a boolean indicating whether the vibration notifications are enabled or not.
- `isLedEnabled()` -- This method returns a boolean indicating whether the LED notification is enabled or not.
- `setLed(boolean)` -- This method sets the LED notification setting to either enable or disable.
- `setVibratePattern(int)` -- The method sets the vibration pattern for a notification.
- `getVibrateTimes()` -- The method returns the number of times the device should vibrate for a notification.
- `setRingEnabled(boolean)` -- The method sets whether ringtones are allowed or not, without losing the current ringtone selection.
- `getLedColor()` -- The method returns the current LED color setting.
- `getRingtone()` -- The method returns the URI of the current ringtone setting for notifications in the K-9 email client.
- `setVibrate(boolean)` -- The method sets whether vibration is enabled for this notification setting.
- `getVibration(int,int)` -- This method returns a vibration pattern as an array of long values, based on the pattern and frequency specified as input.
- `getVibration()` -- The `getVibration()` method returns a vibration pattern multiplied by the number of times requested.
- `setVibrateTimes(int)` -- This method sets the number of times the device should vibrate for a notification.
- `getVibratePattern()` -- This method returns the vibration pattern for notifications.
- `setLedColor(int)` -- This method sets the LED color for the notification.
- `setRingtone(java.lang.String)` -- The method sets the ringtone URI for a specified notification setting.

## class `com.fsck.k9.Preferences`

The purpose of the `com.fsck.k9.Preferences` class is to manage the email account preferences in the K-9 mail application, including loading, creating, and deleting accounts, as well as setting and getting the default account.

This class contains the following public method(s):

- `setDefaultAccount(com.fsck.k9.Account)` -- This method sets the default account to be used in the email application.
- `getAvailableAccounts()` -- This method returns a collection of all available accounts registered in the K-9 mail application.
- `loadAccounts()` -- The `loadAccounts()` method loads email accounts from storage and adds them to the `accounts` and `accountsInOrder` structures.
- `getAccounts()` -- The method returns a list of all registered email accounts on the system, or an empty list if there are none.
- `newAccount()` -- The method creates a new email account and adds it to the list of accounts.
- `getAccount(java.lang.String)` -- The method gets and returns the account associated with the given UUID.
- `getPreferences(android.content.Context)` -- The method returns the instance of the Preferences class for the given context, creating it if necessary.
- `deleteAccount(com.fsck.k9.Account)` -- The method deletes a specified email account from the app's preferences, as well as from remote and local storage.
- `getStorage()` -- This method returns the storage object that holds all the preferences data for the K-9 mail client.
- `getDefaultAccount()` -- The method `getDefaultAccount()` returns the default email account, and sets the first account in the list as default if no account is marked as default.

## class `com.fsck.k9.Clock`

The purpose of `com.fsck.k9.Clock` class is to provide a method to retrieve the current time in milliseconds since January 1, 1970 GMT.

This class contains the following public method(s):

- `getTime()` -- This method returns the current time in milliseconds since January 1, 1970 GMT.

## class `com.fsck.k9.Account`

(no description)

This class contains the following public method(s):

- `getLocalStore()` -- The method returns an instance of the local mail store associated with the account.
- `addCertificate(com.fsck.k9.activity.setup.AccountSetupCheckSettings$CheckDirection,java.security.cert.X509Certificate)` -- The method adds a new certificate for the incoming or outgoing server to the local key store.
- `setDisplayCount(int)` -- The method is used to set the number of messages to display in the account and reset the visible message limits.
- `isReplyAfterQuote()` -- The method returns a boolean value indicating whether replies should be placed after quoted text.
- `getIdentities()` -- The method returns a list of identities associated with an email account.
- `setSignatureBeforeQuotedText(boolean)` -- This method sets whether the signature should be placed before or after quoted text in email messages for a specific account.
- `setIdleRefreshMinutes(int)` -- The method sets the number of minutes for the account to wait before automatically refreshing when it is idle.
- `goToUnreadMessageSearch()` -- This method returns a boolean value indicating whether to navigate to the search results of unread messages.
- `setSortType(com.fsck.k9.Account$SortType)` -- The method sets the sorting type for a given email account.
- `setFolderTargetMode(com.fsck.k9.Account$FolderMode)` -- Sets the target mode for syncing folders in the K-9 mail Account.
- `getStoreUri()` -- The purpose of the method is to return the URI of the account's email message store in string format.
- `getMaxPushFolders()` -- This method returns the maximum number of folders that can be pushed to a device.
- `setEnabled(boolean)` -- The method sets the enabled status of the K9 email account.
- `setExpungePolicy(com.fsck.k9.Account$Expunge)` -- The method sets the expunge policy for the email account.
- `limitToDisplayableFolders(com.fsck.k9.search.LocalSearch)` -- This method modifies the supplied `LocalSearch` instance to limit the search to displayable folders according to the current folder display mode.
- `hasDraftsFolder()` -- The purpose of this method is to check if an email account has a drafts folder set.
- `setArchiveFolderName(java.lang.String)` -- The method sets the name of the archive folder for the email account.
- `getSearchableFolders()` -- The method returns the searchable folders associated with a K-9 mail account in a thread-safe manner.
- `isSortAscending(com.fsck.k9.Account$SortType)` -- The method checks if messages should be sorted in ascending order based on the provided sort type and returns a boolean value.
- `setInboxFolderName(java.lang.String)` -- The method sets the name of the inbox folder for the K9 email account.
- `setTransportUri(java.lang.String)` -- This method sets the transport URI for the email account.
- `getFolderSyncMode()` -- The method returns the folder sync mode of a K9 email account.
- `setNotifyContactsMailOnly(boolean)` -- This method sets a flag indicating whether to notify contacts only for new emails received.
- `setSyncRemoteDeletions(boolean)` -- The method sets whether or not to synchronize remote deletions for the email account.
- `setFolderPushMode(com.fsck.k9.Account$FolderMode)` -- The method sets the push mode of the folder and returns whether the push mode has been changed.
- `getAlwaysBcc()` -- This method returns the email address that is always blind copied on outgoing emails for this account.
- `setDraftsFolderName(java.lang.String)` -- This method sets the name of the drafts folder for the email account.
- `setSubscribedFoldersOnly(boolean)` -- The method sets whether or not the account should only display subscribed folders.
- `setMessageFormat(com.fsck.k9.Account$MessageFormat)` -- The method sets the message format for the email account.
- `getLastSelectedFolderName()` -- This method returns the name of the last selected folder for the email account.
- `getQuotePrefix()` -- This method returns the currently set quote prefix for the K9 email client account.
- `getStats(android.content.Context)` -- This method retrieves the statistics for the email account associated with the given context, including the number of unread and flagged messages, and the size of the account.
- `getSpamFolderName()` -- This method returns the name of the spam folder associated with a K-9 email account.
- `syncRemoteDeletions()` -- The method returns a boolean indicating if remote deletions should be synced for the account.
- `save(com.fsck.k9.Preferences)` -- This method saves the Account instance's preferences to the preferences store.
- `useCompression(com.fsck.k9.mail.NetworkType)` -- This method checks if compression should be used for the specified network type and returns a boolean indicating whether compression should be used.
- `setSpamFolderName(java.lang.String)` -- This method sets the name of the spam folder associated with the email account.
- `setAutomaticCheckIntervalMinutes(int)` -- This method sets the automatic email checking interval in minutes for a K9 email account, with an option to turn off automatic checking.
- `setGoToUnreadMessageSearch(boolean)` -- The method sets a boolean flag that determines whether the user should be taken to the first unread message when opening a mailbox.
- `setShowPictures(com.fsck.k9.Account$ShowPictures)` -- This method sets the preference for displaying images in emails for a specific K-9 mail account.
- `setQuotePrefix(java.lang.String)` -- The method sets the prefix to be used for quoting messages in email replies.
- `hashCode()` -- The method returns a unique hash code for the account based on its UUID.
- `getRemoteSearchNumResults()` -- This method returns the number of search results retrieved from the server during a remote search.
- `setFolderDisplayMode(com.fsck.k9.Account$FolderMode)` -- The method sets the display mode of the folders in the email account and returns whether the mode was actually changed.
- `isRemoteSearchFullText()` -- This method is currently disabled and intended to determine whether full-text searching should be enabled for remote email searching in K9 mail client.
- `isSearchByDateCapable()` -- The method checks if the account's store is capable of searching emails by date.
- `getAccountNumber()` -- The method returns the account number associated with a specific account in K-9 mail client.
- `isPushPollOnConnect()` -- This method returns a boolean value indicating whether push polling is enabled on account connection or not.
- `getOutboxFolderName()` -- The purpose of the method is to return the name of the "outbox" folder for the account.
- `getFolderPushMode()` -- The method returns the folder push mode of the account.
- `setSentFolderName(java.lang.String)` -- This method sets the name of the folder where sent emails will be stored for a given account.
- `setChipColor(int)` -- The purpose of the method is to set the chip color of the account and update the cache.
- `getLatestOldMessageSeenTime()` -- This method returns the latest time when an old message was seen in the account.
- `findIdentity(com.fsck.k9.mail.Address)` -- The purpose of the method is to find the identity associated with a given email address within the account's list of identities.
- `setEmail(java.lang.String)` -- This method sets the email address for the first identity of a K9 mail account.
- `setSortAscending(com.fsck.k9.Account$SortType,boolean)` -- This method sets whether the specified sorting type should be in ascending or descending order for the account.
- `getName()` -- This method returns the name of the first identity associated with the email account.
- `generateColorChip(boolean,boolean)` -- The method generates a color chip for an email message based on whether it is read and/or flagged.
- `isAnIdentity(com.fsck.k9.mail.Address)` -- The purpose of this method is to determine whether a given email address corresponds to an identity associated with the account.
- `getFolderUnreadCount(android.content.Context,java.lang.String)` -- The method returns the number of unread messages in a specified folder for a given email account.
- `getEmail()` -- This method returns the email address associated with the first identity of the account.
- `subscribedFoldersOnly()` -- This method returns a boolean indicating whether the account should only display subscribed folders.
- `hasArchiveFolder()` -- The method checks whether the account has an archive folder set and returns true if it does.
- `setFolderNotifyNewMailMode(com.fsck.k9.Account$FolderMode)` -- Sets the new mail notification mode for the specified email folder in the K-9 Mail app account.
- `setReplyAfterQuote(boolean)` -- Sets whether replies should be placed after or before the quoted text in email messages.
- `setLastSelectedFolderName(java.lang.String)` -- This method sets the name of the last selected folder for the email account.
- `getAutomaticCheckIntervalMinutes()` -- This method returns the automatic check interval time in minutes for a K-9 email account, and returns -1 for never.
- `getSignatureUse()` -- The method returns a boolean indicating whether the first identity of the email account should include a signature in outgoing emails or not.
- `setRingNotified(boolean)` -- Sets whether or not the user has been notified of new mail with a ringtone.
- `getMessageFormat()` -- The method gets the current message format setting for the email messages of the account.
- `isNotifyNewMail()` -- This method returns whether the account should notify the user of new emails.
- `setStripSignature(boolean)` -- The method sets whether to remove email signature from outgoing messages.
- `setMarkMessageAsReadOnView(boolean)` -- The method sets a boolean value whether to mark messages as read when viewed.
- `isDefaultQuotedTextShown()` -- This method returns a boolean value indicating whether the default quoted text is shown or not in the email reply.
- `getEarliestPollDate()` -- This method returns the earliest date that messages should be polled for this account based on the maximum age of messages to be downloaded.
- `setRemoteSearchFullText(boolean)` -- Sets whether or not remote search for full text is enabled for the email account.
- `generateAccountNumber(com.fsck.k9.Preferences)` -- This method generates a new account number by checking the existing account numbers in the provided preferences object.
- `setMessageReadReceipt(boolean)` -- The method sets a flag indicating whether read receipts for messages sent from this account should be requested.
- `setCompression(com.fsck.k9.mail.NetworkType,boolean)` -- This method sets whether or not to use compression for a specific network type in an email account.
- `setDefaultQuotedTextShown(boolean)` -- The method sets whether quoted text is displayed by default in emails sent from the K-9 email client.
- `isStripSignature()` -- The method returns a boolean indicating whether email signatures should be stripped from outgoing messages.
- `setQuoteStyle(com.fsck.k9.Account$QuoteStyle)` -- The method sets the quote style for the email client account.
- `isAnIdentity(com.fsck.k9.mail.Address[])` -- The method checks whether any of the given email addresses belongs to an identity associated with the account.
- `isEnabled()` -- This method returns whether or not the account is currently enabled.
- `setSearchableFolders(com.fsck.k9.Account$Searchable)` -- The method sets the folders that are searchable for the email account.
- `isSignatureBeforeQuotedText()` -- The purpose of this method is to return a boolean indicating whether the user has set the preference for showing the email signature before or after the quoted text.
- `isNotifyContactsMailOnly()` -- This method returns a boolean indicating whether only contacts should receive email notifications for this account.
- `getFolderNotifyNewMailMode()` -- This method returns the folder mode for notifying new mail in a K-9 email Account.
- `setName(java.lang.String)` -- This method sets the name of the first identity of an email account.
- `setIdentities(java.util.List)` -- This method sets the list of identities for the email account.
- `allowRemoteSearch()` -- The method returns true if remote search is allowed for this email account in K-9 mail.
- `setSignatureUse(boolean)` -- The method sets the use of a signature for the first identity associated with the account.
- `getRemoteStore()` -- This method returns the remote store associated with this email account.
- `hasTrashFolder()` -- The method checks whether an email account has a trash folder set and returns true if it does.
- `deleteCertificate(java.lang.String,int,com.fsck.k9.activity.setup.AccountSetupCheckSettings$CheckDirection)` -- This method deletes any stored certificate for an old host/port if the existing account settings have been changed to a new host/port.
- `getLocalStorageProviderId()` -- The method returns the ID of the provider used for local storage in K-9 Mail.
- `setAutoExpandFolderName(java.lang.String)` -- Sets the name of the folder to be automatically expanded when selected.
- `hasSpamFolder()` -- This method checks if the email account has a designated spam folder.
- `setMaximumAutoDownloadMessageSize(int)` -- The method sets the maximum size of messages that can be automatically downloaded for a given email account.
- `getQuoteStyle()` -- This method returns the quote style preference of the email account.
- `getSignature()` -- This method returns the signature of the first identity associated with the account.
- `getInboxFolderName()` -- This method returns the name of the inbox folder for a given email account.
- `setRemoteSearchNumResults(int)` -- The method sets the maximum number of search results that can be retrieved remotely for a K9 email account.
- `excludeSpecialFolders(com.fsck.k9.search.LocalSearch)` -- The method modifies a `LocalSearch` instance to exclude certain special folders from the search results.
- `setPushPollOnConnect(boolean)` -- This method sets a boolean flag indicating whether push polling should be initiated on connecting to the account.
- `getTrashFolderName()` -- This method returns the name of the trash folder for the account.
- `toString()` -- The method returns the description of the account as a String.
- `getArchiveFolderName()` -- The method returns the name of the folder designated as the archive folder for the account.
- `getDescription()` -- This method returns the description of the email account associated with the object instance.
- `getAutoExpandFolderName()` -- The method returns the name of the folder set for automatic expansion in the K-9 email client.
- `setMaximumPolledMessageAge(int)` -- The method sets the maximum age of messages that should be considered for polling in the email account.
- `setLocalStorageProviderId(java.lang.String)` -- Sets the local storage provider ID for the email account and switches to the new provider if necessary.
- `hasSentFolder()` -- The `hasSentFolder()` method checks whether an email account has a specific folder set to save sent messages.
- `getMaximumAutoDownloadMessageSize()` -- The method returns the maximum size of a message that can be automatically downloaded in an email account.
- `getSortType()` -- The method returns the current sort type of the email messages stored in the account.
- `setDescription(java.lang.String)` -- This method sets the description of a given email account.
- `getChipColor()` -- The method returns the chip color of the account.
- `getDeletePolicy()` -- This method returns the deletion policy of an email account in the K-9 Mail app.
- `isMarkMessageAsReadOnView()` -- The method returns whether or not messages should be marked as read upon viewing.
- `setDeletePolicy(com.fsck.k9.Account$DeletePolicy)` -- The method sets the delete policy for an email account.
- `isRingNotified()` -- The method returns a boolean value indicating whether a new mail notification has been sent for this account.
- `getDisplayCount()` -- The method returns the number of times the account has been displayed.
- `isAlwaysShowCcBcc()` -- This method returns whether the account always shows Cc/Bcc fields in outgoing messages.
- `getDraftsFolderName()` -- The method returns the name of the drafts folder for the email account.
- `getExpungePolicy()` -- This method returns the current expunge policy of the K-9 email account.
- `getShowPictures()` -- This method returns the value of the "showPictures" variable of the Account class.
- `setCryptoKey(long)` -- This method sets the PGP encryption/decryption key for the email account.
- `isSpecialFolder(java.lang.String)` -- The purpose of the `isSpecialFolder` method is to determine if a given folder name is a special folder (such as inbox, trash, drafts, etc.) for a specific email account.
- `setNotifySelfNewMail(boolean)` -- The method sets the value for whether the account should notify itself when new mail is received.
- `move(com.fsck.k9.Preferences,boolean)` -- The method moves the account up or down in the list of account UUIDs stored in the preferences.
- `getNotificationSetting()` -- The method returns the current notification setting for the email account.
- `getSentFolderName()` -- The method returns the name of the sent folder for the account.
- `setNotifyNewMail(boolean)` -- The purpose of the method is to set whether or not to notify the user of new emails.
- `setFolderSyncMode(com.fsck.k9.Account$FolderMode)` -- This method sets the folder synchronization mode for an email account and returns a boolean indicating if a change was made.
- `setAlwaysBcc(java.lang.String)` -- Sets the email address that always receives a blind carbon copy (BCC) when sending from this email account.
- `setShowOngoing(boolean)` -- To set whether notifications for ongoing synchronization should be shown or not for a specific email account.
- `setAlwaysShowCcBcc(boolean)` -- Sets whether to always show CC and BCC options when composing an email in this account.
- `getIdleRefreshMinutes()` -- This method returns the number of minutes after which the account should be checked for new emails.
- `isNotifySelfNewMail()` -- This method returns a boolean value indicating whether or not the account should notify itself of new mail.
- `setAllowRemoteSearch(boolean)` -- The method sets whether the account allows remote searching or not.
- `isShowOngoing()` -- This method returns a boolean that indicates whether ongoing notifications should be shown for this email account.
- `getCryptoKey()` -- The method returns the PGP crypto key associated with the account.
- `setStoreUri(java.lang.String)` -- The method sets the store URI for the email account.
- `getFolderTargetMode()` -- The purpose of the method is to return the current folder mode target for the account.
- `getTransportUri()` -- The method returns the transport URI for the account.
- `setSignature(java.lang.String)` -- The method sets the signature for the first identity associated with the account.
- `getFolderDisplayMode()` -- This method returns the folder display mode of a particular email account in the K-9 email client.
- `equals(java.lang.Object)` -- The method checks if the given object is an instance of `com.fsck.k9.Account` and if it has the same account UUID, and returns `true` if so, otherwise it calls the `equals` method of the superclass.
- `setLatestOldMessageSeenTime(long)` -- The method sets the time when the latest old message was seen for an email account.
- `excludeUnwantedFolders(com.fsck.k9.search.LocalSearch)` -- The method excludes specific mailbox folders from a LocalSearch, including Trash, Spam, and Outbox, while always including the Inbox.
- `getIdentity(int)` -- The method retrieves the email identity associated with a given index number.
- `getMaximumPolledMessageAge()` -- The method returns the maximum age, in days, of messages that have been polled from the server for a specific email account.
- `isAvailable(android.content.Context)` -- The method checks if the storage provider for the K9 email account is available or ready for use.
- `getUuid()` -- The method `getUuid()` returns the UUID of the account.
- `setTrashFolderName(java.lang.String)` -- This method sets the name of the trash folder for the email account.
- `setMaxPushFolders(int)` -- The method sets the maximum number of folders that can be pushed for synchronization in the account and returns true if the maximum number has been changed.
- `isMessageReadReceiptAlways()` -- This method returns whether the account always sends read receipts for messages.

## interface `com.fsck.k9.K9$ApplicationAware`

The interface `com.fsck.k9.K9$ApplicationAware` is used to allow components associated with it to be initialized when the application instance is ready.

This class contains the following public method(s):

- `initializeComponent(android.app.Application)` -- The method is called when the Application instance is ready and initializes the component associated with the interface.

## class `com.fsck.k9.Identity`

The purpose of the `com.fsck.k9.Identity` class is to represent an email identity in the K-9 Mail app, providing methods to set and retrieve the email address, name, description, signature, and reply-to address.

This class contains the following public method(s):

- `getDescription()` -- The method returns the description of a K-9 mail identity object.
- `setSignature(java.lang.String)` -- The method sets the signature of the email identity.
- `setEmail(java.lang.String)` -- The method sets the email address for the identity.
- `getSignatureUse()` -- This method returns whether or not the Identity object uses a signature in one synchronized thread-safe call.
- `getSignature()` -- The method returns the signature of an email identity.
- `getName()` -- This method returns the name of the Identity object.
- `setDescription(java.lang.String)` -- The method sets the description for the identity.
- `setReplyTo(java.lang.String)` -- The method sets the reply-to address for this email identity.
- `getReplyTo()` -- The `getReplyTo()` method returns the email address set as the reply-to address for this identity.
- `setName(java.lang.String)` -- The method sets the name of an email identity.
- `toString()` -- The `toString()` method is used to return a string representation of the `Identity` instance.
- `getEmail()` -- The method returns the email address of a user's identity in K-9 Mail app.
- `setSignatureUse(boolean)` -- This method sets the usage of the signature for the identity.

## enum `com.fsck.k9.Account$DeletePolicy`

The enum `com.fsck.k9.Account$DeletePolicy` is used to define different deletion policies that can be applied to email messages in an email account.

This class contains the following public method(s):

- `preferenceString()` -- The `preferenceString()` method returns the DeletePolicy setting as a string for use in preferences.
- `fromInt(int)` -- This method retrieves the corresponding `DeletePolicy` enum constant based on a specified integer setting value.


# package `com.fsck.k9.account`

The `com.fsck.k9.account` package is used to handle the creation and configuration of email accounts in the K-9 Mail app.

This package contains the following class(es):

## class `com.fsck.k9.account.AccountCreator`

The `AccountCreator` class is used to create and configure email accounts in the K-9 Mail app.

This class contains the following public method(s):

- `getDefaultDeletePolicy(com.fsck.k9.mail.ServerSettings.Type)` -- This method returns the default delete policy for an email server type.
- `getDefaultPort(com.fsck.k9.mail.ConnectionSecurity,com.fsck.k9.mail.ServerSettings.Type)` -- The method returns the default port number for a given mail server connection security and type.


# package `com.fsck.k9.activity`

The `com.fsck.k9.activity` package contains classes and interfaces that provide the user interface and functionality for various activities and screens in the K-9 Mail app, including composing and managing email messages, displaying account and folder information, and creating and managing settings and preferences.

This package contains the following class(es):

## class `com.fsck.k9.activity.FolderList$FolderListAdapter`

The purpose of the `FolderListAdapter` class is to provide a list adapter for displaying a filtered list of folders in the `FolderList` activity, allowing the user to interact with and select specific folders.

This class contains the following public method(s):

- `getFilter()` -- The purpose of the `getFilter()` method is to return the `mFilter` object that is used for filtering the contents of the folder list.
- `getCount()` -- The method `getCount()` returns the number of elements in a filtered list of folders.
- `getFolder(java.lang.String)` -- This method retrieves a `FolderInfoHolder` object for a given folder name if it exists in the `FolderListAdapter`.
- `isEnabled(int)` -- This method allows all items in the folder list adapter to be enabled.
- `getItemView(int,android.view.View,android.view.ViewGroup)` -- This method returns a view to display a folder item in the UI of the FolderList activity.
- `getView(int,android.view.View,android.view.ViewGroup)` -- This method returns a view to be displayed at a specific position in a list view.
- `areAllItemsEnabled()` -- This method always returns true indicating that all items in the list are enabled.
- `isItemSelectable(int)` -- The method always returns true, indicating that items in the folder list are selectable.
- `getFolderIndex(java.lang.String)` -- The method returns the index of a folder in the filtered list of folders based on its name.
- `setFilter(android.widget.Filter)` -- The method sets the filter to be applied on the list of folders displayed in the FolderListAdapter.
- `getItem(int)` -- The method returns the object at the specified position in the filtered list of folders.
- `getItemId(int)` -- This method returns the unique identifier of the folder at the specified position in the list adapter.
- `getItem(long)` -- The method returns an item at the specified position in the adapter's data set as an Object.
- `hasStableIds()` -- The method indicates whether the list adapter has stable item ids.

## class `com.fsck.k9.activity.Accounts$AccountsHandler`

The purpose of the class `com.fsck.k9.activity.Accounts$AccountsHandler` is to handle various UI-related tasks for the accounts activity in the K9 email client app.

This class contains the following public method(s):

- `progress(boolean)` -- The `progress` method updates the action bar to show a spinning progress indicator when a refresh is in progress.
- `dataChanged()` -- The method updates the UI if the adapter for the accounts list view is not null.
- `accountSizeChanged(com.fsck.k9.Account,long,long)` -- The `accountSizeChanged` method updates the account statistics and displays a toast with information about the change in account size.
- `refreshTitle()` -- The purpose of this method is to refresh the title of the view on the main UI thread.
- `progress(int)` -- The method updates the progress bar in the activity for displaying the progress of an operation.
- `workingAccount(com.fsck.k9.Account,int)` -- The `workingAccount` method displays a toast message indicating the name of the currently selected email account.

## class `com.fsck.k9.activity.MessageCompose`

The purpose of the class `com.fsck.k9.activity.MessageCompose` is to handle the user interface and functionality of composing an email message in the K-9 email application, allowing users to select recipients, add attachments, and send or save drafts of their messages.

This class contains the following public method(s):

- `showContactPicker(int)` -- This method displays the contact picker for selecting recipients of a message and sets a flag to indicate that it is being called from a sub-activity.
- `onOptionsItemSelected(android.view.MenuItem)` -- The `onOptionsItemSelected` method handles when a user selects a menu option in the message composition screen of the K-9 email application.
- `onRecipientsChanged()` -- The method sets a flag to indicate that changes have been made to the recipients in the message compose activity since the last save.
- `onMessageBuildCancel()` -- This method sets the current message builder to null and hides the progress bar when the message build is cancelled.
- `saveDraftEventually()` -- The method sets a flag indicating that changes have been made to the message since the last save as a draft.
- `onClick(android.view.View)` -- The method handles the onClick event for the "identity" button and displays a dialog box to choose an identity.
- `onPrepareOptionsMenu(android.view.Menu)` -- This method is used to prepare and modify the options menu for the message compose activity.
- `onAttachmentRemoved()` -- This method sets the `changesMadeSinceLastSave` variable to true when an attachment is removed in the MessageCompose activity.
- `onCreate(android.os.Bundle)` -- The `onCreate` method initializes the UI and sets up the compose message screen for the user.
- `onProgressCancel(com.fsck.k9.fragment.ProgressDialogFragment)` -- The method is used to handle cancellation of an attachment progress dialog and notify the attachment presenter.
- `onOpenPgpClickDisable()` -- The method disables the OpenPGP encryption for the recipient of the message being composed.
- `performSendAfterChecks()` -- The purpose of this method is to initiate the process of sending the composed email message after performing necessary checks.
- `onAttachmentAdded()` -- This method sets a flag indicating that changes have been made to the email since the last save when an attachment is added to the email being composed.
- `onRetainNonConfigurationInstance()` -- The method retains the current message builder object during configuration changes and detaches its callback if it exists.
- `loadLocalMessageForDisplay(com.fsck.k9.mailstore.MessageViewInfo,com.fsck.k9.activity.MessageCompose$Action)` -- The method loads a local message and updates the UI with the quoted text and formatting options based on the action specified.
- `onFocusChange(android.view.View,boolean)` -- This method is called when a view loses or gains focus, and handles the case where the message content or subject field gains focus by calling `onNonRecipientFieldFocused()` from `recipientPresenter`.
- `updateMessageFormat()` -- The method updates the message format to be used when composing an email based on various conditions, including user preferences and message content.
- `onCreateOptionsMenu(android.view.Menu)` -- This method creates the option menu for the MessageCompose activity and disables the "Save" option if the Drafts folder is not set.
- `onOpenPgpSignOnlyChange(boolean)` -- (no description)
- `onMessageBuildSuccess(com.fsck.k9.mail.internet.MimeMessage,boolean)` -- The method is called when a message is successfully built and it initiates the process of saving or sending the message, depending on whether it is a draft or not.
- `onDestroy()` -- The `onDestroy()` method is responsible for cleaning up resources and notifying the `recipientPresenter` that the activity is being destroyed.
- `launchUserInteractionPendingIntent(android.app.PendingIntent,int)` -- The method launches a user interaction pending intent for the message compose activity.
- `onCreateDialog(int)` -- This method creates and returns a dialog based on the specified integer id.
- `onPause()` -- The purpose of this method is to pause the activity, remove a listener, and check whether to save a draft implicitly.
- `onMessageBuildException(com.fsck.k9.mail.MessagingException)` -- The method handles and displays an exception that occurred while building a message for sending.
- `onBackPressed()` -- The method is used to handle the back button press event in the `MessageCompose` activity.
- `loadQuotedTextForEdit()` -- The purpose of the method is to load the text of a previously sent message for editing purposes.
- `onProgressCancel(com.fsck.k9.fragment.AttachmentDownloadDialogFragment)` -- This method is called when the progress of attaching a file is cancelled, and it calls the `attachmentPresenter.attachmentProgressDialogCancelled()` method.
- `onMessageBuildReturnPendingIntent(android.app.PendingIntent,int)` -- The method starts a pending intent and sets a code to identify it as originating from the message compose screen of the K-9 Mail app.
- `onOpenPgpInlineChange(boolean)` -- The method updates the recipient presenter when the OpenPGP inline setting has changed in the message compose activity.

## class `com.fsck.k9.activity.MessageInfoHolder`

The `MessageInfoHolder` class is used in the K-9 Mail application to store information about a single email message, such as its unique identifier and whether it has been read or not.

This class contains the following public method(s):

- `equals(java.lang.Object)` -- The method checks if the given object is an instance of `MessageInfoHolder` and if it contains the same `message` as the current instance.
- `hashCode()` -- The `hashCode()` method returns the hash code of the unique identifier of a message.

## class `com.fsck.k9.activity.Search`

The purpose of the class `com.fsck.k9.activity.Search` is to create a search activity in the K9 email client app, which can be activated or deactivated and checked for its active state.

This class contains the following public method(s):

- `onStop()` -- The method `onStop()` is called when the `Search` activity is stopped and it deactivates the search.
- `onStart()` -- The `onStart()` method sets the `active` state of the `Search` activity to true.
- `isActive()` -- The `isActive()` method returns a boolean indicating whether the `Search` activity is currently active or not.
- `setActive(boolean)` -- The method sets the value of a static boolean variable "isActive" in the "com.fsck.k9.activity.Search" class.

## interface `com.fsck.k9.activity.ColorPickerDialog$OnColorChangedListener`

The interface is used to define a callback function `colorChanged()` which is called when the user selects a color in a color picker dialog, allowing the caller of the dialog to be notified of the color selection.

This class contains the following public method(s):

- `colorChanged(int)` -- The method is called when the user selects a color in a color picker dialog.

## abstract class `com.fsck.k9.activity.K9PreferenceActivity`

It is a base class for activities that display settings/preferences for the K-9 Mail app, providing a common implementation for setting the language and theme.

This class contains the following public method(s):

- `onCreate(android.os.Bundle)` -- This method sets the language and theme for the K9PreferenceActivity and calls the superclass implementation of onCreate.

## class `com.fsck.k9.activity.MessageList$StorageListenerImplementation`

The purpose of the class is to listen for changes in the storage state and trigger methods accordingly for the email storage provider used for the current account.

This class contains the following public method(s):

- `onUnmount(java.lang.String)` -- This method is called when a storage provider is unmounted, and if the unmounted provider is the one used for storing emails for the current account, it triggers the `onAccountUnavailable()` method on the UI thread.
- `onMount(java.lang.String)` -- The method does nothing when a storage provider is mounted.

## abstract class `com.fsck.k9.activity.K9Activity`

The abstract class `com.fsck.k9.activity.K9Activity` serves as a base activity class for K-9 Mail app and provides methods for dispatching touchscreen events, setting up a gesture detector, and initializing the activity.

This class contains the following public method(s):

- `dispatchTouchEvent(android.view.MotionEvent)` -- This method dispatches a touchscreen event to the activity's view hierarchy.
- `setupGestureDetector(com.fsck.k9.activity.misc.SwipeGestureDetector$OnSwipeGestureListener)` -- The method sets up a gesture detector for the activity with the given swipe gesture listener.
- `onCreate(android.os.Bundle)` -- The `onCreate` method sets up an instance of `K9ActivityCommon` and calls the `onCreate` method of the superclass.

## class `com.fsck.k9.activity.K9ActivityCommon`

The class `com.fsck.k9.activity.K9ActivityCommon` is a utility class that provides common functionality and methods used by various activities in the K-9 Mail app, such as getting the current theme's background color, setting up a gesture detector, and setting the app language.

This class contains the following public method(s):

- `getThemeBackgroundColor()` -- The method returns the background color of the current theme used for the activity.
- `newInstance(android.app.Activity)` -- The method creates a new instance of `K9ActivityCommon` bound to the specified `Activity`.
- `setupGestureDetector(com.fsck.k9.activity.misc.SwipeGestureDetector$OnSwipeGestureListener)` -- The method sets up the swipe gesture detector with a provided listener to notify if a left to right or right to left swipe has been detected.
- `preDispatchTouchEvent(android.view.MotionEvent)` -- This method is called before dispatching touch events in order to handle gestures using a gesture detector.
- `setLanguage(android.content.Context,java.lang.String)` -- This method sets the language of the app to the specified language or the default language if none is provided.

## abstract class `com.fsck.k9.activity.AccountList`

The purpose of the abstract class `com.fsck.k9.activity.AccountList` is to provide the basic functionality and layout for the account list screen in the K-9 email client app.

This class contains the following public method(s):

- `onResume()` -- The purpose of this method is to reload the list of accounts when the `AccountList` activity is resumed.
- `onItemClick(android.widget.AdapterView,android.view.View,int,long)` -- This method handles when an item in the account list is selected, retrieving the selected account and calling the `onAccountSelected` method with the account as an argument.
- `populateListView(java.util.List)` -- The method populates a ListView with a list of accounts, including any special accounts and creates a new AccountsAdapter instance.
- `onCreate(android.os.Bundle)` -- This method sets up the layout and behavior of the account list screen in the K-9 email client app.

## class `com.fsck.k9.activity.LauncherShortcuts`

The purpose of the class `com.fsck.k9.activity.LauncherShortcuts` is to handle the creation of shortcuts for the K-9 Mail app on Android devices.

This class contains the following public method(s):

- `onCreate(android.os.Bundle)` -- This method finishes the activity if it is not triggered by a specific intent for creating shortcuts.

## class `com.fsck.k9.activity.Accounts$PasswordPromptDialog`

The purpose of the class `com.fsck.k9.activity.Accounts$PasswordPromptDialog` is to display a dialog prompt for entering passwords for incoming and outgoing email servers.

This class contains the following public method(s):

- `onTextChanged(java.lang.CharSequence,int,int,int)` -- This method is not used and has no purpose.
- `afterTextChanged(android.text.Editable)` -- This method enables or disables the "OK" button based on whether the user has specified all necessary passwords for incoming and outgoing servers.
- `restore(android.app.Activity)` -- The method restores the password prompt dialog on the given activity.
- `show(com.fsck.k9.activity.Accounts)` -- The `show()` method displays the password prompt dialog on the specified activity screen.
- `retain()` -- The method `retain()` saves passwords and checkbox state entered in the PasswordPromptDialog, dismisses the dialog and clears all references to its UI objects.
- `beforeTextChanged(java.lang.CharSequence,int,int,int)` -- This method is not used in the class implementation.

## class `com.fsck.k9.activity.Accounts$AccountClickListener`

The purpose of the class `com.fsck.k9.activity.Accounts$AccountClickListener` is to handle clicks on email accounts and display search results in the message list of the K9 email client app.

This class contains the following public method(s):

- `onClick(android.view.View)` -- This method is responsible for displaying a search result in the message list of the K9 email client app when a user clicks on an account.

## class `com.fsck.k9.activity.ColorPickerDialog`

The purpose of the `com.fsck.k9.activity.ColorPickerDialog` class is to provide a dialog box that allows users to select a specific color.

This class contains the following public method(s):

- `setColor(int)` -- This method sets the color that the color picker should highlight as the selected color.

## class `com.fsck.k9.activity.ChooseFolder`

The purpose of `com.fsck.k9.activity.ChooseFolder` is to allow the user to choose a folder for email messages in the K-9 Mail application.

This class contains the following public method(s):

- `onOptionsItemSelected(android.view.MenuItem)` -- The method handles the actions to be taken when a menu item is selected for displaying different types of email folders.
- `onCreateOptionsMenu(android.view.Menu)` -- This method inflates a menu with options for choosing a folder and configures a search view for folders.
- `onCreate(android.os.Bundle)` -- This method initializes the activity and sets up the list view and adapter to display folders for the chosen account.

## class `com.fsck.k9.activity.EditIdentity`

The purpose of the `EditIdentity` class is to allow the user to edit an identity, save its state in case of activity lifecycle changes, and return to the previous activity/screen.

This class contains the following public method(s):

- `onCreate(android.os.Bundle)` -- The `onCreate` method initializes the identity editor UI and retrieves the identity data from the intent or creates a new identity if none is passed.
- `onSaveInstanceState(android.os.Bundle)` -- The purpose of this method is to save the state of the identity being edited in case of activity lifecycle changes.
- `onBackPressed()` -- The method saves the changes made to the identity and returns to the previous activity/screen.

## enum `com.fsck.k9.activity.MessageCompose$Action`

The enum `com.fsck.k9.activity.MessageCompose$Action` is used to represent the different actions that can be performed in the MessageCompose activity, and provides a way to retrieve the resource ID for the title of each action.

This class contains the following public method(s):

- `getTitleResource()` -- This method returns the resource ID for the title of the MessageCompose activity action.

## class `com.fsck.k9.activity.UnreadWidgetConfiguration`

The purpose of the class `com.fsck.k9.activity.UnreadWidgetConfiguration` is to provide a configuration screen for an unread widget, allowing the user to customize it and save the configuration in SharedPreferences.

This class contains the following public method(s):

- `onActivityResult(int,int,android.content.Intent)` -- This method handles the result of a startActivityForResult call and performs specific actions based on the request code.
- `getWidgetProperties(android.content.Context,int)` -- This method retrieves the properties of an unread widget based on its ID and returns them as a `com.fsck.k9.helper.UnreadWidgetProperties` object.
- `deleteWidgetConfiguration(android.content.Context,int)` -- This method is used to delete a widget configuration from SharedPreferences.
- `onOptionsItemSelected(android.view.MenuItem)` -- This method handles when the user selects an option from the widget configuration menu, specifically when the "done" button is pressed.
- `onCreate(android.os.Bundle)` -- The purpose of this method is to initialize the widgets in the unread widget configuration screen and retrieve the ID of the selected widget.
- `onCreateOptionsMenu(android.view.Menu)` -- This method creates the options menu for the UnreadWidgetConfiguration activity.

## class `com.fsck.k9.activity.EmailAddressList`

The purpose of `com.fsck.k9.activity.EmailAddressList` is to display a list of email addresses associated with a contact and handle actions when an item in the list is clicked.

This class contains the following public method(s):

- `onItemClick(android.widget.AdapterView,android.view.View,int,long)` -- The method handles the actions to be taken when an item in an email address list is clicked, including displaying a toast message and sending the selected email address back to the calling activity.
- `onCreate(android.os.Bundle)` -- This method sets up and populates the UI for displaying a list of email addresses associated with a contact.

## class `com.fsck.k9.activity.K9PreferenceActivity$PreferenceChangeListener`

The purpose of the class is to listen for changes in preferences and update their summary and value accordingly in the K9 email client's settings activity.

This class contains the following public method(s):

- `onPreferenceChange(android.preference.Preference,java.lang.Object)` -- The method is used to update the summary and value of a preference when it is changed.

## class `com.fsck.k9.activity.Accounts$AccountsAdapter`

The purpose of `com.fsck.k9.activity.Accounts$AccountsAdapter` is to provide an adapter for displaying account details in the account list in the K-9 mail application.

This class contains the following public method(s):

- `getView(int,android.view.View,android.view.ViewGroup)` -- This method is responsible for returning the view used to display the account details in the account list.

## class `com.fsck.k9.activity.AccountList$AccountsAdapter`

The `com.fsck.k9.activity.AccountList$AccountsAdapter` class is used to create a custom view for each account object in the account list in K9 Mail application.

This class contains the following public method(s):

- `getView(int,android.view.View,android.view.ViewGroup)` -- This method is used to create a custom view for each account object in the account list.

## class `com.fsck.k9.activity.FolderList$FolderClickListener`

The purpose of `com.fsck.k9.activity.FolderList$FolderClickListener` is to handle click events on folders in the K-9 Mail app and open the search page for messages in the current folder.

This class contains the following public method(s):

- `onClick(android.view.View)` -- The method opens the search page for messages in the current folder in the K-9 Mail app.

## class `com.fsck.k9.activity.Accounts`

The purpose of the `com.fsck.k9.activity.Accounts` class is to manage and display email accounts within the K-9 email client application.

This class contains the following public method(s):

- `onItemLongClick(android.widget.AdapterView,android.view.View,int,long)` -- The method returns a boolean indicating if an item in the AdapterView was long-clicked.
- `onPrepareDialog(int,android.app.Dialog)` -- The method prepares a dialog for display, setting its message according to the selected option.
- `onExport(boolean,com.fsck.k9.Account)` -- The purpose of the `onExport` method is to allow a user to export their email account settings.
- `onCreateDialog(int)` -- The method creates various confirmation dialogs for deleting, clearing, and recreating email accounts.
- `onCreate(android.os.Bundle)` -- The method `onCreate` initializes the Accounts activity by checking for various conditions and settings, initializing the UI, and restoring any previously saved state.
- `listAccounts(android.content.Context)` -- The method starts the K-9 Mail application's accounts activity.
- `onResume()` -- The method `onResume()` is used to refresh the email accounts list and register listeners for account changes and email storage changes.
- `onCreateContextMenu(android.view.ContextMenu,android.view.View,android.view.ContextMenu.ContextMenuInfo)` -- This method creates a context menu for the accounts activity and sets the menu items depending on the type and status of the account.
- `onItemClick(android.widget.AdapterView,android.view.View,int,long)` -- The method is called when an item in the AdapterView is clicked and opens the clicked account.
- `onCreateOptionsMenu(android.view.Menu)` -- This method inflates the menu for the Accounts activity and sets a reference to the refresh menu item.
- `onPause()` -- (no description)
- `importSettings(android.content.Context)` -- The method imports settings for the K-9 email client from an external source.
- `setProgress(boolean)` -- This method sets the progress state for the account view.
- `onContextItemSelected(android.view.MenuItem)` -- This method handles the selection of an item in the context menu for managing email accounts in the K-9 mail app.
- `onExport(android.content.Intent)` -- The method initiates the export of global settings and accounts data to the specified URI.
- `onRetainNonConfigurationInstance()` -- The `onRetainNonConfigurationInstance()` method saves a reference to a currently displayed dialog or a running AsyncTask.
- `createUnreadSearch(android.content.Context,com.fsck.k9.BaseAccount)` -- The purpose of this method is to create a local search for unread messages in a specific account.
- `onSaveInstanceState(android.os.Bundle)` -- The method saves the state of the Accounts activity to be restored later, including the selected account, unread message count, account statistics, and export settings.
- `onOptionsItemSelected(android.view.MenuItem)` -- This method handles actions when a menu item is selected in the Accounts activity.

## class `com.fsck.k9.activity.MessageLoaderHelper`

The purpose of the `MessageLoaderHelper` class is to asynchronously load, decrypt and handle message content in the K-9 email client app.

This class contains the following public method(s):

- `asyncRestartMessageCryptoProcessing()` -- The method restarts processing of a message with encryption or decryption, depending on whether an OpenPGP provider is configured.
- `onDestroyChangingConfigurations()` -- The method is used to clean up resources and retain loading state to pick up from in a new instance of the class.
- `onDestroy()` -- The method cancels loading processes and removes all loading state before destroying the object.
- `asyncStartOrResumeLoadingMessage(com.fsck.k9.activity.MessageReference,android.os.Parcelable)` -- The method asynchronously starts or resumes the loading of a message, potentially using a cached decryption result.
- `asyncReloadMessage()` -- The method starts or resumes loading a local message in the UI thread asynchronously.
- `downloadCompleteMessage()` -- This method starts downloading the complete message body (including attachments) on the UI thread.
- `onActivityResult(int,int,android.content.Intent)` -- The method handles the result of an activity started for message cryptography.

## class `com.fsck.k9.activity.ConfirmationDialog`

The purpose of the `com.fsck.k9.activity.ConfirmationDialog` class is to create customized confirmation dialogs for Android activities with specified buttons, actions, and messages.

This class contains the following public method(s):

- `create(android.app.Activity,int,int,java.lang.String,int,int,java.lang.Runnable)` -- The method creates a customized confirmation dialog for an Android activity, which includes a title, message, confirm button, and cancel button with actions to be performed when pressed.
- `create(android.app.Activity,int,int,java.lang.String,int,int,java.lang.Runnable,java.lang.Runnable)` -- The method creates a customized confirmation dialog with specified title, message, buttons and actions.
- `create(android.app.Activity,int,int,int,int,int,java.lang.Runnable)` -- This method creates a customized confirmation dialog for an activity with specified title, message, confirm button text, cancel button text, and action to perform if the user confirms.

## interface `com.fsck.k9.activity.AlternateRecipientAdapter$AlternateRecipientListener`

The purpose of `com.fsck.k9.activity.AlternateRecipientAdapter$AlternateRecipientListener` interface is to provide callbacks for when an alternate recipient is selected or removed from a list of possible recipients.

This class contains the following public method(s):

- `onRecipientChange(com.fsck.k9.view.RecipientSelectView$Recipient,com.fsck.k9.view.RecipientSelectView$Recipient)` -- The method is called when the selected recipient is changed to an alternate recipient.
- `onRecipientRemove(com.fsck.k9.view.RecipientSelectView$Recipient)` -- To handle the event when an alternate recipient is removed from the list of possible recipients in the AlternateRecipientAdapter.

## class `com.fsck.k9.activity.FolderList$FolderListHandler`

The purpose of the `com.fsck.k9.activity.FolderList$FolderListHandler` class is to handle and manage the list of folders in the email account, and update the UI based on changes in the account.

This class contains the following public method(s):

- `accountSizeChanged(long,long)` -- This method displays a toast message indicating that the size of an email account has changed.
- `workingAccount(int)` -- The method displays a toast message indicating the current working email account.
- `progress(boolean)` -- The `progress` method sets the visibility of the progress spinner in the action bar menu item.
- `dataChanged()` -- The purpose of this method is to update the data in the `FolderListHandler` and notify the `mAdapter` to refresh its view.
- `newFolders(java.util.List)` -- The method updates the list of folders displayed in the FolderListHandler object with the given list of FolderInfoHolder objects.
- `folderLoading(java.lang.String,boolean)` -- The method updates the loading status of a folder in a UI thread.
- `refreshTitle()` -- The `refreshTitle()` method updates the title and subtitle of the ActionBar with information about the current mailbox folder.

## abstract class `com.fsck.k9.activity.K9ListActivity`

The purpose of the `com.fsck.k9.activity.K9ListActivity` abstract class is to provide a base class for activities that display a list of items in the K-9 Mail application.

This class contains the following public method(s):

- `setupGestureDetector(com.fsck.k9.activity.misc.SwipeGestureDetector$OnSwipeGestureListener)` -- The method sets up a swipe gesture detector with the provided listener for the K9ListActivity.
- `onCreate(android.os.Bundle)` -- This method initializes a new instance of `K9ActivityCommon` with the current `K9ListActivity` and then calls the `onCreate()` method of the parent class.
- `onResume()` -- This method overrides the default implementation of onResume() to resume the activity's UI elements.
- `onKeyUp(int,android.view.KeyEvent)` -- The method avoids audible notification of a volume change by intercepting certain key events if volume keys are used for list navigation.
- `onKeyDown(int,android.view.KeyEvent)` -- The `onKeyDown` method handles list navigation using volume keys if enabled in the settings.
- `dispatchTouchEvent(android.view.MotionEvent)` -- This method dispatches touch events to the activity's base class and returns the result of handling the event.

## class `com.fsck.k9.activity.ChooseFolder$ChooseFolderHandler`

The purpose of the class `com.fsck.k9.activity.ChooseFolder$ChooseFolderHandler` is to handle messages related to setting the progress bar visibility and selected folder in the ChooseFolder activity.

This class contains the following public method(s):

- `handleMessage(android.os.Message)` -- This method handles messages sent to the ChooseFolderHandler class in order to set the progress bar visibility or set the selected folder.
- `progress(boolean)` -- The method is used to send a progress message to the handler thread with a boolean indicating if progress should be shown.
- `setSelectedFolder(int)` -- This method sets the selected folder in the ChooseFolder activity.

## class `com.fsck.k9.activity.ActivityListener`

The purpose of the `com.fsck.k9.activity.ActivityListener` class is to provide a listener for various email-related events and update the user interface accordingly, such as mailbox synchronization status, pending message sending status, and folder status changes.

This class contains the following public method(s):

- `searchStats(com.fsck.k9.AccountStats)` -- The method is invoked to provide search statistics to the user.
- `synchronizeMailboxFailed(com.fsck.k9.Account,java.lang.String,java.lang.String)` -- This method is called when mailbox synchronization fails and resets some variables before informing the user of the failure.
- `synchronizeMailboxStarted(com.fsck.k9.Account,java.lang.String)` -- The method sets variables to track the status of email synchronization and informs the user of the current status.
- `sendPendingMessagesCompleted(com.fsck.k9.Account)` -- The purpose of this method is to notify the activity listener that sending pending messages has been completed for a specific account and update the user interface accordingly.
- `pendingCommandStarted(com.fsck.k9.Account,java.lang.String)` -- This method updates the current processing command and informs the user of the status.
- `sendPendingMessagesFailed(com.fsck.k9.Account)` -- This method is called when sending pending messages fails for an email account and it resets the sending account description and informs the user of the status.
- `getFolderTotal()` -- The method retrieves the total number of folders in a synchronized manner.
- `pendingCommandCompleted(com.fsck.k9.Account,java.lang.String)` -- This method informs the user of the completion status of a pending command for a specific email account.
- `pendingCommandsProcessing(com.fsck.k9.Account)` -- The method updates the status of pending commands for a K-9 mail account and informs the user of the status.
- `getFolderCompleted()` -- The method returns the number of completed folder operations within the activity listener in a thread-safe manner.
- `synchronizeMailboxHeadersProgress(com.fsck.k9.Account,java.lang.String,int,int)` -- This method updates the synchronization progress of mailbox headers for a specified account and folder and informs the user of the current status.
- `synchronizeMailboxHeadersFinished(com.fsck.k9.Account,java.lang.String,int,int)` -- This method is called when synchronizing mailbox headers is finished, and it updates the status of the mailbox being synchronized.
- `folderStatusChanged(com.fsck.k9.Account,java.lang.String,int)` -- The method informs the user of a change in folder status, specifically the unread message count.
- `synchronizeMailboxFinished(com.fsck.k9.Account,java.lang.String,int,int)` -- The method informs the user of the synchronization status of a mailbox by resetting loading variables and nullifying the account.
- `synchronizeMailboxHeadersStarted(com.fsck.k9.Account,java.lang.String)` -- The method updates the description and folder name of the currently loading mailbox headers and informs the user of the loading status.
- `systemStatusChanged()` -- This method informs the user of the status change of the system.
- `onPause(android.content.Context)` -- The method unregisters the tickReceiver when the activity is paused to conserve resources and prevent unnecessary broadcasts.
- `sendPendingMessagesStarted(com.fsck.k9.Account)` -- The method sets the description of the account currently sending pending messages and informs the user of the sending status.
- `informUserOfStatus()` -- The purpose of the method is not clear from the given code snippet as it is empty.
- `synchronizeMailboxProgress(com.fsck.k9.Account,java.lang.String,int,int)` -- This method updates the progress of synchronizing a mailbox for a specified account and folder and informs the user of the status.
- `getOperation(android.content.Context)` -- This method returns a status message describing the current operation being performed by K-9 Mail.
- `onResume(android.content.Context)` -- The method registers a receiver for system time updates when the activity is resumed.
- `pendingCommandsFinished(com.fsck.k9.Account)` -- To inform the user that all pending commands for a specific email account have finished processing.

## class `com.fsck.k9.activity.NotificationDeleteConfirmation`

The purpose of the class is to provide functionality for displaying a delete confirmation dialog for notifications in the K-9 email client.

This class contains the following public method(s):

- `onPrepareDialog(int,android.app.Dialog)` -- This method prepares the confirmation dialog for deleting notifications by setting the message with the number of messages to be deleted.
- `onCreateDialog(int)` -- This method creates a delete confirmation dialog for notifications in the K-9 email client.
- `getIntent(android.content.Context,java.util.List)` -- This method returns an intent to show a notification delete confirmation dialogue for a list of email messages in the K-9 Mail app.
- `getIntent(android.content.Context,com.fsck.k9.activity.MessageReference)` -- This method returns an intent for displaying a delete confirmation notification for a given message in the K-9 Mail app.
- `onCreate(android.os.Bundle)` -- The `onCreate()` method initializes the activity and displays a confirmation dialog for deleting a notification.

## class `com.fsck.k9.activity.ChooseIdentity`

The purpose of the class `com.fsck.k9.activity.ChooseIdentity` is to provide functionality and UI for the "Choose Identity" screen in the K-9 email client and refresh the view when the activity is resumed.

This class contains the following public method(s):

- `onCreate(android.os.Bundle)` -- This method sets up the UI and functionality for the Choose Identity screen in the K-9 email client.
- `onResume()` -- This method refreshes the view when the activity is resumed.

## class `com.fsck.k9.activity.UpgradeDatabases`

The purpose of the class is to upgrade K9 email databases and launch the original activity.

This class contains the following public method(s):

- `onCreate(android.os.Bundle)` -- The `onCreate` method initializes the UI layout and checks if the K9 email databases have already been upgraded before launching the original activity.
- `actionUpgradeDatabases(android.content.Context,android.content.Intent)` -- This method starts the UpgradeDatabases activity if the account databases need upgrading and returns true, otherwise returns false.
- `onResume()` -- The `onResume()` method checks if a database upgrade has been completed and launches the original activity if so, or registers a broadcast receiver and starts a service otherwise.
- `onPause()` -- Unregisters the broadcast receiver for the database upgrade service when the activity is being paused.

## class `com.fsck.k9.activity.Accounts$ImportSelectionDialog`

The class `com.fsck.k9.activity.Accounts$ImportSelectionDialog` is a dialog box that allows the user to select email accounts and specific settings to import, and it provides methods to show, restore, and retain the selection state of the items in the dialog.

This class contains the following public method(s):

- `restore(android.app.Activity)` -- The method restores the dialog and displays it on the specified activity with the previously selected options.
- `show(com.fsck.k9.activity.Accounts)` -- The method shows an import selection dialog for email accounts in the specified activity.
- `show(com.fsck.k9.activity.Accounts,android.util.SparseBooleanArray)` -- The `show` method displays a dialog box that allows the user to select specific settings and accounts to import.
- `retain()` -- The `retain()` method saves the selection state of each list item, dismisses the dialog, and returns true if the dialog is not null; otherwise, it returns false.

## class `com.fsck.k9.activity.AlternateRecipientAdapter`

The class is used to provide an adapter for the recipient select view, which displays a list of alternate email recipients with the option to select them as the primary recipient.

This class contains the following public method(s):

- `getItemId(int)` -- This method returns the item ID at the given position.
- `getCount()` -- This method returns the total number of items in the `recipients` list plus a fixed number of items.
- `bindItemView(android.view.View,com.fsck.k9.view.RecipientSelectView$Recipient)` -- The method binds data to the recipient item views in the AlternateRecipientAdapter.
- `setCurrentRecipient(com.fsck.k9.view.RecipientSelectView$Recipient)` -- Sets the current recipient selected in the recipient select view.
- `getItem(int)` -- This method returns a recipient object at a given position in the `RecipientSelectView`.
- `bindHeaderView(android.view.View,com.fsck.k9.view.RecipientSelectView$Recipient)` -- This method is used to bind and display the header view in the RecipientSelectView for a given recipient.
- `isEnabled(int)` -- The method determines whether the item at a given position is enabled or not, except for the header view which is always disabled.
- `setShowAdvancedInfo(boolean)` -- The method sets a boolean flag to indicate whether advanced information should be shown in an email recipient adapter.
- `getView(int,android.view.View,android.view.ViewGroup)` -- This method is responsible for creating and returning a view for each recipient in the recipient list.
- `setAlternateRecipientInfo(java.util.List)` -- The method sets a list of alternate email recipients, removes the currently selected recipient, and notifies the adapter of the change.
- `newView(android.view.ViewGroup)` -- The method creates a new view for an alternate recipient item in a parent view group.

## interface `com.fsck.k9.activity.MessageLoaderHelper$MessageLoaderCallbacks`

The purpose of the interface `com.fsck.k9.activity.MessageLoaderHelper$MessageLoaderCallbacks` is to provide callbacks for handling message loading and downloading events such as network errors, loading failures, and progress updates.

This class contains the following public method(s):

- `onDownloadErrorNetworkError()` -- The method is called when there is a network error while trying to download a message.
- `onMessageDataLoadFinished(com.fsck.k9.mailstore.LocalMessage)` -- This method is called when the message data has finished loading and provides the loaded `LocalMessage`.
- `onMessageDataLoadFailed()` -- To handle failures in loading message data.
- `onMessageViewInfoLoadFailed(com.fsck.k9.mailstore.MessageViewInfo)` -- The method is called when loading the message view information fails.
- `startIntentSenderForMessageLoaderHelper(android.content.IntentSender,int,android.content.Intent,int,int,int)` -- This method starts an IntentSender for a message loader helper with specified parameters.
- `onDownloadErrorMessageNotFound()` -- The method is called when an error is encountered during message download and the message is not found.
- `onMessageViewInfoLoadFinished(com.fsck.k9.mailstore.MessageViewInfo)` -- This method is called when the loading of a message's view information is finished.
- `setLoadingProgress(int,int)` -- The method sets the loading progress of a message loader in relation to the current and maximum numbers.

## interface `com.fsck.k9.activity.K9ActivityCommon$K9ActivityMagic`

The purpose of the interface `com.fsck.k9.activity.K9ActivityCommon$K9ActivityMagic` is to provide a way of setting up a gesture detector that listens for swipe gestures and notifies a listener in K-9 Mail app's activity classes.

This class contains the following public method(s):

- `setupGestureDetector(com.fsck.k9.activity.misc.SwipeGestureDetector$OnSwipeGestureListener)` -- Sets up a gesture detector that listens for swipe gestures and notifies the provided listener.

## class `com.fsck.k9.activity.UpgradeDatabases$UpgradeDatabaseBroadcastReceiver`

The purpose of the class `com.fsck.k9.activity.UpgradeDatabases$UpgradeDatabaseBroadcastReceiver` is to handle progress updates and completion notifications for the database upgrade service in the K-9 Mail app.

This class contains the following public method(s):

- `onReceive(android.content.Context,android.content.Intent)` -- The method handles receiving progress updates and completion notifications for the database upgrade service.

## class `com.fsck.k9.activity.AlternateRecipientAdapter$RecipientTokenHolder`

The purpose of the class is to hold recipient tokens for the alternate recipient adapter in the K-9 Mail Android app.

This class contains the following public method(s):

- `setShowAsHeader(boolean)` -- The method sets the visibility of a header view in the recipient adapter.

## class `com.fsck.k9.activity.FolderList`

The purpose of the `com.fsck.k9.activity.FolderList` class is to handle the display and functionality of the list of email folders in the K-9 Mail application.

This class contains the following public method(s):

- `onOptionsItemSelected(android.view.MenuItem)` -- This method handles the action to be taken when a menu item is selected in the folder list.
- `onCreateOptionsMenu(android.view.Menu)` -- The purpose of this method is to create the options menu for the folder list activity and inflate the menu with the folder list option and configure the search view.
- `onKeyDown(int,android.view.KeyEvent)` -- This method handles key events and performs various actions based on the key pressed, including changing display modes and showing help messages.
- `onNewIntent(android.content.Intent)` -- This method sets the intent, retrieves account information, and initializes the activity view for the FolderList activity when a new intent is received.
- `onResume()` -- The method `onResume()` refreshes the folder list and messages for any open folders to update unread message count and read status.
- `onCreateContextMenu(android.view.ContextMenu,android.view.View,android.view.ContextMenu.ContextMenuInfo)` -- This method is used to create a context menu for the FolderList activity with a specified layout and header title.
- `onCreate(android.os.Bundle)` -- The `onCreate` method initializes and sets up the UI components and functionalities of the folder list view used in the K9 Mail application.
- `onSearchRequested()` -- This method initiates a search with the account UUID as app data and returns true.
- `actionHandleAccountIntent(android.content.Context,com.fsck.k9.Account,boolean)` -- The `actionHandleAccountIntent` method creates an intent to launch the FolderList activity with a specified account and flag for whether the intent is from a shortcut.
- `onContextItemSelected(android.view.MenuItem)` -- This method handles selected actions from a context menu for a folder in K-9 Mail application.
- `onRetainNonConfigurationInstance()` -- The method returns the list of folders in the adapter for retaining data on configuration changes.
- `actionHandleAccount(android.content.Context,com.fsck.k9.Account)` -- To handle an email account and start the corresponding activity for the folder list in the given context.
- `onPause()` -- This method is called when the activity is being paused and removes a listener from the messaging controller and notifies the listener that the activity is being paused.

## class `com.fsck.k9.activity.Accounts$SimpleDialog`

The purpose of the `com.fsck.k9.activity.Accounts$SimpleDialog` class is to provide methods for displaying and managing a simple alert dialog in the K9 Mail app.

This class contains the following public method(s):

- `restore(android.app.Activity)` -- The method restores a previously shown dialog on the given activity.
- `retain()` -- The method dismisses the current dialog and releases the reference to it.
- `show(com.fsck.k9.activity.Accounts)` -- The `show` method displays an alert dialog with a generated message and an "OK" button that triggers an action in the activity.

## class `com.fsck.k9.activity.MessageReferenceHelper`

The purpose of `com.fsck.k9.activity.MessageReferenceHelper` is to provide methods for converting lists of message reference strings to lists of message references and vice versa.

This class contains the following public method(s):

- `toMessageReferenceList(java.util.List)` -- This method converts a list of message reference strings to a list of message references.
- `toMessageReferenceStringList(java.util.List)` -- This method converts a list of message references to a list of string representations of those references.

## class `com.fsck.k9.activity.MessageReference`

The purpose of the `com.fsck.k9.activity.MessageReference` class is to represent a mail message referencing the account, folder, and UID of the message, and to provide methods for manipulating and comparing these references.

This class contains the following public method(s):

- `toIdentityString()` -- The `toIdentityString()` method generates a unique identifier string for a mail message referencing the account, folder, and UID of the message.
- `withModifiedUid(java.lang.String)` -- This method returns a new MessageReference object with a modified UID.
- `equals(java.lang.String,java.lang.String,java.lang.String)` -- The method checks if the given account UUID, folder name, and UID matches the corresponding values in the message reference object.
- `equals(java.lang.Object)` -- The method compares the account UUID, folder name, and UID of a given `MessageReference` object to another object to determine if they are equal.
- `hashCode()` -- The method calculates a hash code value for a `MessageReference` object based on its account UUID, folder name, and UID.
- `withModifiedFlag(com.fsck.k9.mail.Flag)` -- This method returns a new instance of MessageReference with a modified email flag.
- `getAccountUuid()` -- This method returns the UUID of the account associated with the message reference.
- `getUid()` -- The method returns the unique ID of a message.
- `parse(java.lang.String)` -- This method parses a string representation of a message reference into a MessageReference object in the K-9 Mail app.
- `getFlag()` -- The method returns the flag of a message.
- `toString()` -- The purpose of this method is to return a string representation of a `MessageReference` object.
- `getFolderName()` -- The method returns the name of the folder where a message is stored.

## class `com.fsck.k9.activity.ManageIdentities`

The purpose of the `com.fsck.k9.activity.ManageIdentities` class is to provide functionality for managing email identities in the K-9 email app.

This class contains the following public method(s):

- `onContextItemSelected(android.view.MenuItem)` -- This method handles the context menu item selected by the user for managing email identities.
- `onResume()` -- The `onResume()` method refreshes the view of managing identities in the K-9 email app.
- `onCreateOptionsMenu(android.view.Menu)` -- This method inflates the menu resource for managing email identities.
- `onCreateContextMenu(android.view.ContextMenu,android.view.View,android.view.ContextMenu.ContextMenuInfo)` -- This method creates a context menu for managing email identities and inflates menu items from a specific menu resource.
- `onOptionsItemSelected(android.view.MenuItem)` -- The method handles user selection from options menu for managing email identities.
- `onBackPressed()` -- The method saves the identities and then performs the default action of going back on the Android device.

## class `com.fsck.k9.activity.FolderList$FolderListAdapter$FolderListFilter`

The purpose of the `FolderListFilter` class is to filter the list of folders based on a user-provided search term.

This class contains the following public method(s):

- `getSearchTerm()` -- This method returns the search term used to filter the folder list.

## class `com.fsck.k9.activity.FolderListFilter`

The purpose of the class `com.fsck.k9.activity.FolderListFilter` is to provide filtering functionality for displaying email folders in the K-9 Mail app.

This class contains the following public method(s):

- `invalidate()` -- The method invalidates the original values by setting them to null.

## class `com.fsck.k9.activity.MessageList`

The purpose of the `MessageList` class is to manage the display of the email message list and handle user interactions, such as selecting, composing, and replying to messages in the K-9 Mail app.

This class contains the following public method(s):

- `shortcutIntent(android.content.Context,java.lang.String)` -- This method creates an intent for creating a shortcut to a special folder in the K-9 email client app.
- `startIntentSenderForResult(android.content.IntentSender,int,android.content.Intent,int,int,int)` -- The method starts an intent sender for a result and modifies the request code to include a pending intent mask.
- `onOptionsItemSelected(android.view.MenuItem)` -- This method handles the user's selection of options from the menu in the message list view and the message view, such as sorting messages, marking them as read, and performing actions on individual messages.
- `showNextMessageOrReturn()` -- The method decides whether to show the next message or return to the message list view in K-9 Mail app.
- `onForward(com.fsck.k9.activity.MessageReference)` -- The method forwards an email message to a new recipient and initializes the email composition window with this message.
- `onCreate(android.os.Bundle)` -- The method `onCreate` is responsible for initializing the message list of the email client application and setting up the necessary components and views.
- `onCompose(com.fsck.k9.Account)` -- This method launches the compose activity for the given K-9 email account.
- `setMessageListTitle(java.lang.String)` -- To set the title of the message list in the action bar.
- `updateMenu()` -- The method updates the options menu of the MessageList activity.
- `onCustomKeyDown(int,android.view.KeyEvent)` -- This method handles hotkeys for the message list and message view screens.
- `onResume()` -- The `onResume()` method of the `MessageList` class is responsible for setting up the activity when it has been resumed from a paused state and registering a listener for storage updates.
- `setUnreadCount(int)` -- The method sets the unread count for the message list and updates the action bar accordingly.
- `onSwitchComplete(int)` -- The method removes the message view fragment if the displayed child is the first one.
- `onForward(com.fsck.k9.activity.MessageReference,android.os.Parcelable)` -- The method forwards a selected message to another recipient.
- `onKeyUp(int,android.view.KeyEvent)` -- The `onKeyUp` method swallows certain key up events to avoid audible notification of a volume change, and allows for volume key navigation in the message list if enabled.
- `onReply(com.fsck.k9.activity.MessageReference,android.os.Parcelable)` -- The method is called when the user wants to reply to a message in the message list, and it initiates the reply action.
- `onRestoreInstanceState(android.os.Bundle)` -- The method restores saved state information for the message list activity.
- `openMessage(com.fsck.k9.activity.MessageReference)` -- This method opens a specified message in the message view and displays it to the user.
- `remoteSearchStarted()` -- The method removes the action button for remote search in the message list interface.
- `startSearch(com.fsck.k9.Account,java.lang.String)` -- This method starts a search for messages in a specified folder in an email account.
- `actionDisplaySearch(android.content.Context,com.fsck.k9.search.SearchSpecification,boolean,boolean,boolean)` -- The method launches a search for emails in the K-9 Mail app.
- `onReplyAll(com.fsck.k9.activity.MessageReference,android.os.Parcelable)` -- The method handles the action of replying to all recipients of an email message in the K-9 email client app.
- `setProgress(boolean)` -- The method sets the indeterminate visibility of the progress bar.
- `messageHeaderViewAvailable(com.fsck.k9.view.MessageHeader)` -- Sets the message header for the action bar subject in the message list.
- `onPause()` -- This method removes the listener for storage changes when the activity goes into the paused state.
- `onCreateOptionsMenu(android.view.Menu)` -- This method inflates a menu resource into the activity's action bar, sets the activity's menu to the inflated menu and stores a reference to a particular menu item.
- `onSwipeLeftToRight(android.view.MotionEvent,android.view.MotionEvent)` -- This method handles the gesture of swiping from left to right on the MessageList activity and delegates to the fragment if applicable.
- `setActionBarTitle(java.lang.String)` -- Sets the title of the action bar in the MessageList activity.
- `onSearchRequested()` -- This method overrides the default search behavior to delegate the search request to the message list fragment.
- `showMoreFromSameSender(java.lang.String)` -- The `showMoreFromSameSender` method displays additional messages from the same sender.
- `onBackStackChanged()` -- The method updates the UI depending on the current state of the back stack, including showing/hiding message views and updating the menu.
- `onReply(com.fsck.k9.activity.MessageReference)` -- The method is used to handle user actions related to replying to an email message in the K-9 Mail app.
- `onBackPressed()` -- The `onBackPressed()` method allows the user to navigate back from displaying a message to the message list in an email application.
- `onPrepareOptionsMenu(android.view.Menu)` -- This method configures the options menu for the MessageList activity.
- `onResendMessage(com.fsck.k9.activity.MessageReference)` -- The onResendMessage method resends an email draft for editing.
- `setActionBarSubTitle(java.lang.String)` -- The method sets the subtitle of the ActionBar in the MessageList activity.
- `actionDisplaySearch(android.content.Context,com.fsck.k9.search.SearchSpecification,boolean,boolean)` -- The method opens the message list view with search results based on the given search criteria.
- `intentDisplaySearch(android.content.Context,com.fsck.k9.search.SearchSpecification,boolean,boolean,boolean)` -- The intentDisplaySearch method returns an intent to display a message list search in K-9 Mail.
- `enableActionBarProgress(boolean)` -- Enables or disables a progress indicator in the action bar based on the provided boolean value.
- `actionDisplayMessageIntent(android.content.Context,com.fsck.k9.activity.MessageReference)` -- The method creates an intent to display a specific email message in the K-9 Mail app.
- `setMessageListSubTitle(java.lang.String)` -- This method sets the subtitle of the action bar for the message list activity.
- `showThread(com.fsck.k9.Account,java.lang.String,long)` -- This method shows a thread of messages for a given account, folder, and thread ID.
- `dispatchKeyEvent(android.view.KeyEvent)` -- (no description)
- `displayMessageSubject(java.lang.String)` -- The method displays the given message subject in the action bar or message header depending on the display mode.
- `onSaveInstanceState(android.os.Bundle)` -- The `onSaveInstanceState` method saves the activity's state before it is destroyed, including the display mode, message list display status, and the ID of the first back stack.
- `setActionBarUnread(int)` -- The method sets the visibility and text of an ActionBar view indicating the number of unread messages.
- `onReplyAll(com.fsck.k9.activity.MessageReference)` -- The method handles the action of replying all to a given email message reference.
- `onSwipeRightToLeft(android.view.MotionEvent,android.view.MotionEvent)` -- The method handles the swipe right to left gesture in the message list view by passing it to the MessageListFragment.
- `goBack()` -- The method `goBack()` is used to navigate back to the previous screen or fragment in the `MessageList` activity.
- `setMessageListProgress(int)` -- The purpose of this method is to set the progress of the message list loading.
- `disableDeleteAction()` -- The method disables the delete action menu item in the message list activity.
- `onNewIntent(android.content.Intent)` -- This method handles the creation of a new intent and initializes the display mode and fragments accordingly.

## class `com.fsck.k9.activity.FolderInfoHolder`

The purpose of the class `com.fsck.k9.activity.FolderInfoHolder` is to hold information about local email folders such as their display name, number of unread messages, and system folder status.

This class contains the following public method(s):

- `compareTo(com.fsck.k9.activity.FolderInfoHolder)` -- The method compares two `FolderInfoHolder` objects based on their `name` attribute in a case-insensitive manner.
- `setMoreMessagesFromFolder(com.fsck.k9.mailstore.LocalFolder)` -- (no description)
- `hashCode()` -- The `hashCode()` method returns the computed hash code value of the `name` field.
- `populate(android.content.Context,com.fsck.k9.mailstore.LocalFolder,com.fsck.k9.Account,int)` -- The method populates the FolderInfoHolder object with information about a local email folder, including the number of unread messages, and then closes the folder.
- `getDisplayName(android.content.Context,com.fsck.k9.Account,java.lang.String)` -- This method returns a localized display name for a given mail folder, with special names for system folders like Inbox, Trash and Sent.
- `populate(android.content.Context,com.fsck.k9.mailstore.LocalFolder,com.fsck.k9.Account)` -- The method populates information about a local email folder in order to display it in the user interface.
- `equals(java.lang.Object)` -- The purpose of the method is to check if two `FolderInfoHolder` objects are equal based on their `name` attribute.


# package `com.fsck.k9.activity.compose`

The `com.fsck.k9.activity.compose` package contains classes and interfaces that handle email composition functionality in the K-9 mail app, including recipient management, attachment handling, and PGP encryption and signing.

This package contains the following class(es):

## interface `com.fsck.k9.activity.compose.PgpEnabledErrorDialog$OnOpenPgpDisableListener`

(no description)

This class contains the following public method(s):

- `onOpenPgpClickDisable()` -- The purpose of this method is to handle the action when the user clicks the "disable OpenPGP" button on the error dialog.

## class `com.fsck.k9.activity.compose.RecipientLoader`

The class `com.fsck.k9.activity.compose.RecipientLoader` is designed to load recipient data and deliver it to the caller, caching the data if the loader is started.

This class contains the following public method(s):

- `loadInBackground()` -- The purpose of the method `loadInBackground()` is to load a list of recipient data based on various input parameters, including email addresses, contact URIs, queries, and lookup key URIs.
- `deliverResult(java.util.List)` -- The method delivers the result of a recipient loading operation to the caller, caching the data and only delivering it if the loader is started.

## class `com.fsck.k9.activity.compose.PgpInlineDialog`

The `com.fsck.k9.activity.compose.PgpInlineDialog` class is a dialog used for PGP encryption and decryption in email composition in the K-9 mail app.

This class contains the following public method(s):

- `newInstance(boolean,int)` -- The method creates a new instance of PgpInlineDialog class with arguments for first time usage and a view to highlight.
- `onCreateDialog(android.os.Bundle)` -- (no description)

## class `com.fsck.k9.activity.compose.PgpSignOnlyDialog`

The `com.fsck.k9.activity.compose.PgpSignOnlyDialog` class is used to create a dialog for selecting OpenPGP signing options in the K-9 email client.

This class contains the following public method(s):

- `newInstance(boolean,int)` -- This method creates an instance of the PgpSignOnlyDialog class with specific arguments.
- `onCreateDialog(android.os.Bundle)` -- This method creates a dialog for selecting OpenPGP signing options in the K-9 email client.

## interface `com.fsck.k9.activity.compose.AttachmentPresenter$AttachmentMvpView`

The purpose of the interface `com.fsck.k9.activity.compose.AttachmentPresenter$AttachmentMvpView` is to provide methods to manipulate the view related to attachments in the email composing screen and perform necessary checks before sending or saving the attachment.

This class contains the following public method(s):

- `performSaveAfterChecks()` -- The method performs saving attachment after necessary checks.
- `updateAttachmentView(com.fsck.k9.activity.misc.Attachment)` -- The method updates the view with a given attachment object.
- `performSendAfterChecks()` -- The purpose of this method is to perform checks before sending an attachment in an email.
- `showWaitingForAttachmentDialog(com.fsck.k9.activity.compose.AttachmentPresenter$WaitingAction)` -- The method displays a dialog box indicating that the user is waiting for an attachment to be added during message composition.
- `showPickAttachmentDialog(int)` -- This method displays a selection dialog for picking an attachment with a given requestCode.
- `dismissWaitingForAttachmentDialog()` -- The method dismisses a dialog that is waiting for an attachment to be added in the email composing screen.
- `removeAttachmentView(com.fsck.k9.activity.misc.Attachment)` -- The method removes an attachment view from the composer screen.
- `addAttachmentView(com.fsck.k9.activity.misc.Attachment)` -- The method adds the attachment view for displaying an attachment in the compose screen.
- `showMissingAttachmentsPartialMessageWarning()` -- The method is used to display a warning to the user if there are missing attachments in the partially composed email message.

## class `com.fsck.k9.activity.compose.ComposeCryptoStatus`

The purpose of the `com.fsck.k9.activity.compose.ComposeCryptoStatus` class is to provide information about the encryption status of a compose activity in the K-9 email app, including whether encryption and signing are enabled, recipient email addresses, and any errors related to sending encrypted emails.

This class contains the following public method(s):

- `getSendErrorStateOrNull()` -- The method returns a `SendErrorState` indicating the reason for a failed attempt to send an encrypted email.
- `isPgpInlineModeEnabled()` -- This method returns a boolean indicating whether PGP inline mode is enabled for composing emails in the K-9 email app.
- `getOpenPgpKeyId()` -- This method returns the OpenPGP key ID associated with the ComposeCryptoStatus object.
- `isEncryptionEnabled()` -- The method checks if encryption is enabled for a compose screen in the K-9 email client and returns a boolean value.
- `getRecipientAddresses()` -- The purpose of the `getRecipientAddresses()` method is to return an array of recipient email addresses for a compose activity with encryption status.
- `isProviderStateOk()` -- (no description)
- `isSigningEnabled()` -- The method checks if signing is enabled for the email in ComposeCryptoStatus.
- `shouldUsePgpMessageBuilder()` -- The method checks if PGP message builder should be used based on the current state of the crypto provider.
- `hasRecipients()` -- The purpose of the method is to check if there are any recipients in the recipientAddresses array.

## class `com.fsck.k9.activity.compose.IdentityAdapter`

The purpose of the class `com.fsck.k9.activity.compose.IdentityAdapter` is to provide an adapter for the list of identities associated with the Compose Activity in the K-9 Mail app.

This class contains the following public method(s):

- `hasStableIds()` -- The method returns whether the item IDs are stable across changes to the underlying data.
- `getItemId(int)` -- The method returns the ID of the item at the given position.
- `getView(int,android.view.View,android.view.ViewGroup)` -- This method creates a view for an item at a specific position in the IdentityAdapter for the Compose Activity in the K-9 Mail app.
- `getViewTypeCount()` -- This method returns the number of view types that the adapter currently supports, which is 2.
- `getItem(int)` -- The method returns the item at the specified position in the `mItems` list.
- `getCount()` -- This method returns the number of items in the list of identities associated with the compose activity.
- `isEnabled(int)` -- This method determines whether the item at the specified position in the IdentityAdapter is enabled or disabled based on whether it is an instance of IdentityContainer.
- `getItemViewType(int)` -- This method returns the view type of an item in the adapter, based on whether it is an account or not.

## interface `com.fsck.k9.activity.compose.RecipientPresenter$RecipientsChangedListener`

The interface `com.fsck.k9.activity.compose.RecipientPresenter$RecipientsChangedListener` defines a listener that is notified when there is a change in the recipients of an email being composed in the K9 email client.

This class contains the following public method(s):

- `onRecipientsChanged()` -- The method `onRecipientsChanged()` is called when there is a change in the recipients (To, Cc, Bcc) of an email being composed.

## class `com.fsck.k9.activity.compose.PgpEncryptDescriptionDialog`

The purpose of the class `com.fsck.k9.activity.compose.PgpEncryptDescriptionDialog` is to display a dialog box with a description of PGP encryption and to create a new instance with a highlighted view.

This class contains the following public method(s):

- `newInstance(int)` -- This method creates a new instance of `PgpEncryptDescriptionDialog` with a specified view highlighted.
- `onCreateDialog(android.os.Bundle)` -- This method creates and returns an AlertDialog for displaying a PGP encryption description.

## class `com.fsck.k9.activity.compose.PgpEnabledErrorDialog`

The purpose of the `com.fsck.k9.activity.compose.PgpEnabledErrorDialog` class is to create and display a dialog for PGP encryption enabled error messages in K-9 Mail.

This class contains the following public method(s):

- `newInstance(boolean,int)` -- The method creates and returns a new instance of `PgpEnabledErrorDialog` with specified arguments.
- `onCreateDialog(android.os.Bundle)` -- This method creates and returns a dialog for displaying PGP (Pretty Good Privacy) encryption enabled error messages in K-9 Mail.

## class `com.fsck.k9.activity.compose.RecipientAdapter`

The class `com.fsck.k9.activity.compose.RecipientAdapter` is used to manage the recipients list and display recipient data in the compose email view.

This class contains the following public method(s):

- `setContactPhotoOrPlaceholder(android.content.Context,android.widget.ImageView,com.fsck.k9.view.RecipientSelectView$Recipient)` -- This method sets the contact photo or placeholder image for a recipient in a compose email view.
- `getView(int,android.view.View,android.view.ViewGroup)` -- This method returns the view representing the recipient at the specified position in the recipient adapter.
- `getItem(int)` -- This method gets a recipient at a given position from a list of recipients used in a recipient selection view.
- `getFilter()` -- The `getFilter()` method returns an instance of the `Filter` class used to perform filtering on the recipient list in the Compose Activity.
- `getCount()` -- This method returns the number of recipients in the recipients list or 0 if the list is null.
- `getItemId(int)` -- This method returns the ID of the item at the given position, which is the same as the position itself.
- `setHighlight(java.lang.String)` -- The method sets the highlight value for the recipient adapter.
- `setRecipients(java.util.List)` -- The `setRecipients` method sets the list of recipients for the recipient adapter and notifies the adapter that the data has changed.
- `setShowAdvancedInfo(boolean)` -- The method sets whether to show advanced info for recipients in the recipient adapter.

## interface `com.fsck.k9.activity.compose.PgpSignOnlyDialog$OnOpenPgpSignOnlyChangeListener`

The purpose of this interface is to listen for changes in the OpenPGP sign-only option in the email compose activity, and perform some action based on whether the option is enabled or not.

This class contains the following public method(s):

- `onOpenPgpSignOnlyChange(boolean)` -- This method is called when the user toggles the OpenPGP sign-only option in the email compose activity, passing a boolean indicating if the option is enabled or not.

## class `com.fsck.k9.activity.compose.ComposeCryptoStatus$ComposeCryptoStatusBuilder`

The purpose of `com.fsck.k9.activity.compose.ComposeCryptoStatus$ComposeCryptoStatusBuilder` is to provide a builder class for creating instances of `ComposeCryptoStatus`, allowing for flexible and customizable creation of objects with various settings and configurations.

This class contains the following public method(s):

- `setCryptoMode(com.fsck.k9.activity.compose.RecipientPresenter$CryptoMode)` -- The purpose of the method is to set the crypto mode for the ComposeCryptoStatusBuilder object and return the builder instance itself.
- `build()` -- This method constructs and returns a new instance of `ComposeCryptoStatus` by validating and setting all required fields.
- `setCryptoProviderState(com.fsck.k9.activity.compose.RecipientPresenter$CryptoProviderState)` -- Sets the crypto provider state for the `ComposeCryptoStatus` builder.
- `setRecipients(java.util.List)` -- The `setRecipients` method sets the list of recipients for a ComposeCryptoStatus object.
- `setEnablePgpInline(boolean)` -- Sets whether to enable PGP inline mode for composing encrypted messages.
- `setOpenPgpKeyId(java.lang.Long)` -- This method sets the OpenPGP key ID for the ComposeCryptoStatusBuilder.
- `setPreferEncryptMutual(boolean)` -- This method sets whether to prefer mutual encryption when composing a message.

## class `com.fsck.k9.activity.compose.MessageActions`

The `com.fsck.k9.activity.compose.MessageActions` class provides methods for composing, replying to, and forwarding email messages in the K-9 email client.

This class contains the following public method(s):

- `getActionReplyIntent(android.content.Context,com.fsck.k9.activity.MessageReference)` -- The method returns an Intent for replying to a message in the K-9 email client.
- `actionForward(android.content.Context,com.fsck.k9.activity.MessageReference,android.os.Parcelable)` -- This method opens the message compose screen with a message being forwarded and decrypted.
- `getActionReplyIntent(android.content.Context,com.fsck.k9.activity.MessageReference,boolean,android.os.Parcelable)` -- This method returns an intent for composing a new message as a reply to a given message, optionally with the "reply all" flag set.
- `actionCompose(android.content.Context,com.fsck.k9.Account)` -- This method composes a new email message using the specified or default email account.
- `actionEditDraft(android.content.Context,com.fsck.k9.activity.MessageReference)` -- The `actionEditDraft` method allows continued composition of a message while modifying the way certain actions are handled, such as saving or discarding the message.
- `actionReply(android.content.Context,com.fsck.k9.activity.MessageReference,boolean,android.os.Parcelable)` -- The method composes a new message as a reply to a given message, either reply or reply all, depending on the value of replyAll.

## interface `com.fsck.k9.activity.compose.PgpInlineDialog$OnOpenPgpInlineChangeListener`

The purpose of this interface is to provide a callback for when the user toggles the use of OpenPGP inline encryption in a compose email dialog.

This class contains the following public method(s):

- `onOpenPgpInlineChange(boolean)` -- The method is called when the user toggles the option to use OpenPGP inline encryption in a compose email dialog.

## class `com.fsck.k9.activity.compose.RecipientMvpView`

The `RecipientMvpView` class is responsible for managing and displaying email recipients in the compose screen of the K-9 email client, including autocompletion, error handling, and cryptographic encryption/decryption.

This class contains the following public method(s):

- `showCryptoSpecialMode(com.fsck.k9.activity.compose.RecipientMvpView$CryptoSpecialModeDisplayType)` -- This method is responsible for displaying the appropriate visual indicator for the recipient view's special crypto mode (if any), and hiding it if necessary.
- `showNoRecipientsError()` -- The method sets an error message on a view to indicate that no recipients were specified for an email message.
- `recipientCcTryPerformCompletion()` -- The method tries to perform autocompletion for the recipient's CC field and returns whether it was successful or not.
- `recipientToTryPerformCompletion()` -- The method checks if the recipient view is able to perform completion and returns a boolean value.
- `getCcRecipients()` -- This method returns a list of recipient objects selected in the CC field of the compose email view.
- `getToRecipients()` -- This method returns a list of recipient objects for recipients in the "To" field of a compose email view.
- `getBccRecipients()` -- The method returns a list of recipients added to the Bcc field in the email compose view.
- `recipientBccHasUncompletedText()` -- The method determines if the Bcc recipient field has any uncompleted text.
- `setCryptoProvider(java.lang.String)` -- The method sets the cryptographic provider for the recipient views in the email composer.
- `requestFocusOnCcField()` -- This method sets the focus on the CC field of the compose email screen.
- `showErrorOpenPgpIncompatible()` -- The method displays a Toast message indicating that the OpenPGP provider is incompatible.
- `getToAddresses()` -- The method returns a list of email addresses entered into the "To" field of a compose email view.
- `showOpenPgpEncryptExplanationDialog()` -- The method is used to display an explanation dialog for OpenPGP encryption.
- `launchUserInteractionPendingIntent(android.app.PendingIntent,int)` -- Launches a user interaction pending intent with a specified request code in the associated activity.
- `showToUncompletedError()` -- The purpose of this method is to display an error message when the recipient field is left incomplete.
- `setBccVisibility(boolean)` -- This method sets the visibility of the BCC recipient field in the email composer view.
- `showErrorIsSignOnly()` -- The method displays an error message indicating that the recipient's email address only supports signing, not encryption.
- `showErrorInlineAttach()` -- The purpose of this method is to display a Toast message with an error message for inline attachment of encrypted content.
- `getCcAddresses()` -- The `getCcAddresses()` method returns a list of email addresses that are in the Carbon Copy field of the email being composed.
- `recipientToHasUncompletedText()` -- The method returns a boolean indicating if the "To" recipient field has uncompleted text.
- `onClick(android.view.View)` -- The method handles click events for various views in the recipient field of an email compose screen.
- `onFocusChange(android.view.View,boolean)` -- This method handles the focus change event for recipient fields and calls the appropriate presenter method based on which field was focused.
- `recipientBccTryPerformCompletion()` -- The purpose of this method is to attempt to perform autocomplete for the recipient's blind carbon copy (Bcc) field.
- `isCcVisible()` -- This method returns a boolean indicating whether the CC field is currently visible in the UI.
- `getBccAddresses()` -- This method returns a list of BCC email addresses entered in the recipient view in the email composer of the K-9 email client.
- `setRecipientTokensShowCryptoEnabled(boolean)` -- The method sets whether or not to display crypto-enabled recipient tokens for the "To", "Cc", and "Bcc" fields in a Compose email screen.
- `showErrorContactNoAddress()` -- The purpose of the method is to display an error message as a toast when a selected contact does not have an email address.
- `showErrorNoKeyConfigured()` -- The method displays a Toast message indicating that no key is configured.
- `showErrorOpenPgpUserInteractionRequired()` -- The method shows a toast message indicating that user interaction is required for OpenPGP encryption to proceed.
- `setLoaderManager(android.app.LoaderManager)` -- The method sets the loader manager for the recipient views in the compose email activity.
- `requestFocusOnBccField()` -- The method sets focus on the "Bcc" field in the recipient view.
- `setFontSizes(com.fsck.k9.FontSizes,int)` -- This method sets the font size for the recipient views in an email compose screen.
- `setRecipientExpanderVisibility(boolean)` -- This method sets the visibility of the Bcc expander in the compose recipient view.
- `showContactPicker(int)` -- The purpose of the `showContactPicker(int)` method is to call the `showContactPicker(int)` method of its `activity` field with the specified `requestCode`.
- `showErrorOpenPgpConnection()` -- To display a toast message with an error message related to a failure in establishing an OpenPGP connection.
- `addTextChangedListener(android.text.TextWatcher)` -- The method adds a TextWatcher to the recipient views of a Compose email screen.
- `recipientCcHasUncompletedText()` -- The method returns whether the CC recipient input field has uncompleted text.
- `showOpenPgpInlineDialog(boolean)` -- The method displays a dialog for OpenPGP encryption options in inline parts of a message.
- `showCcUncompletedError()` -- The method displays an error message for an incomplete CC recipient in a recipient view.
- `addRecipients(com.fsck.k9.mail.Message.RecipientType,com.fsck.k9.view.RecipientSelectView$Recipient[])` -- The method adds recipients of different types (TO, CC, BCC) to the respective views.
- `showErrorOpenPgpRetrieveStatus()` -- The method displays a Toast message indicating an error in retrieving OpenPGP key for recipients in the compose view.
- `requestFocusOnToField()` -- The method requests focus on the recipient field of an email message.
- `showBccUncompletedError()` -- The purpose of the `showBccUncompletedError()` method is to display an error message when the Bcc field in a recipient view is incomplete.
- `showCryptoStatus(com.fsck.k9.activity.compose.RecipientMvpView$CryptoStatusDisplayType)` -- The purpose of the `showCryptoStatus` method is to display the status of cryptographic encryption/decryption for a recipient in a graphical user interface.
- `showOpenPgpSignOnlyDialog(boolean)` -- The method shows a dialog for selecting to sign an email with OpenPGP but not encrypt it.
- `isBccVisible()` -- The method checks if the Bcc field is currently visible in the email composer view.
- `setPresenter(com.fsck.k9.activity.compose.RecipientPresenter)` -- The method sets the presenter for the RecipientMvpView and defines listeners for the view's three AddressSelectViews to call presenter methods in response to user actions.
- `showOpenPgpEnabledErrorDialog(boolean)` -- This method shows a dialog indicating that OpenPGP encryption/decryption is only available when it is enabled in the app settings.
- `setCcVisibility(boolean)` -- The method sets the visibility of the Carbon Copy (CC) recipients' field in a Compose email view.

## class `com.fsck.k9.activity.compose.RecipientPresenter`

The purpose of the `com.fsck.k9.activity.compose.RecipientPresenter` class is to handle the recipient-related functionality in the compose activity of the K-9 mail app, including initializing and managing recipient fields, handling encryption and PGP settings, and managing the visibility of CC and BCC fields.

This class contains the following public method(s):

- `onPrepareOptionsMenu(android.view.Menu)` -- This method prepares the options menu for the recipient presenter, specifically showing or hiding certain items based on the current cached crypto status and contact picker availability.
- `initFromSendOrViewIntent(android.content.Intent)` -- This method initializes the recipient fields in the compose activity with email addresses from an Intent object.
- `onSwitchAccount(com.fsck.k9.Account)` -- The method updates the account and adjusts the visibility of the CC and BCC fields based on the account's preferences. It also sets up the cryptography provider.
- `builderSetProperties(com.fsck.k9.message.PgpMessageBuilder,com.fsck.k9.activity.compose.ComposeCryptoStatus)` -- This method sets properties such as recipient addresses and OpenPGP API for a PGP message builder and sets the compose crypto status.
- `onMenuSetPgpInline(boolean)` -- The method sets whether to enable PGP inline encryption and shows a dialog if necessary.
- `getBccAddresses()` -- The method returns a list of email addresses of the Bcc recipients in the email message being composed.
- `getCcAddresses()` -- The method returns a list of CC email addresses associated with the current email being composed.
- `getCurrentCachedCryptoStatus()` -- This method returns the cached crypto status of the recipient presenter.
- `addBccAddresses(com.fsck.k9.mail.Address[])` -- The method adds a list of Blind Carbon Copy (BCC) recipients to the email and updates the visibility of the BCC field in the email compose view.
- `onCryptoModeChanged(com.fsck.k9.activity.compose.RecipientPresenter$CryptoMode)` -- Updates the current encryption mode and triggers an asynchronous update of the encryption status for recipients.
- `initFromTrustIdAction(java.lang.String)` -- The method initializes the recipient presenter with a trustId address and sets the current crypto mode to "choice enabled".
- `onNonRecipientFieldFocused()` -- The method hides empty CC and BCC fields if the account does not always show them.
- `shouldSaveRemotely()` -- The method determines whether recipient information should be saved remotely based on the cached encryption status.
- `builderSetProperties(com.fsck.k9.message.MessageBuilder)` -- The method sets the recipient properties on a given message builder object.
- `initFromReplyToMessage(com.fsck.k9.mail.Message,boolean)` -- The method initializes the recipient fields for a reply message and sets the appropriate PGP encryption mode.
- `checkRecipientsOkForSending()` -- To check whether the recipients of an email message have been correctly entered and are complete before sending.
- `onCryptoPgpClickDisable()` -- This method sets the crypto mode of the recipient to "no choice".
- `onRestoreInstanceState(android.os.Bundle)` -- This method restores the state of recipient views and other variables when the activity is resumed.
- `onMenuAddFromContacts()` -- Opens the contact picker activity to add a recipient from the device's contacts.
- `showPgpSendError(com.fsck.k9.activity.compose.ComposeCryptoStatus$SendErrorState)` -- The purpose of the method `showPgpSendError` is to display different error dialogs based on the type of OpenPGP send error state encountered during the sending of a message.
- `onCryptoPgpInlineChanged(boolean)` -- The method updates the value of the `cryptoEnablePgpInline` variable and triggers an asynchronous update of the crypto status.
- `onSaveInstanceState(android.os.Bundle)` -- The method saves the state of the recipient presenter, including visibility of CC and BCC fields and the current cryptography mode.
- `initFromMailto(com.fsck.k9.helper.MailTo)` -- The method initializes the recipient fields (To/Cc/Bcc) with the values extracted from a MailTo object.
- `initFromDraftMessage(com.fsck.k9.mail.Message)` -- The method initializes the recipients and PGP settings from a draft email message.
- `onPgpPermissionCheckResult(android.content.Intent)` -- This method handles the result of a permission check for OpenPGP encryption and sets the appropriate state for the crypto provider.
- `onActivityDestroy()` -- The method unbinds from the OpenPGP service connection to avoid memory leaks when the associated activity is destroyed.
- `onSwitchIdentity(com.fsck.k9.Identity)` -- The purpose of the method is to handle switching email identities during email composition in the K-9 mail app.
- `onMenuSetEnableEncryption(boolean)` -- The method handles the logic for enabling or disabling email encryption based on the cached crypto status and recipient information.
- `asyncUpdateCryptoStatus()` -- This method updates the cryptographic status of a message recipient asynchronously.
- `onActivityResult(int,int,android.content.Intent)` -- This method handles the result of an activity launched to pick contacts or to interact with OpenPGP or Autocrypt, and performs appropriate actions based on the result.
- `onMenuSetSignOnly(boolean)` -- The method sets the compose screen to sign-only mode and displays a PGPSignOnlyDialog if necessary.
- `getToAddresses()` -- The method returns a list of email addresses in the "To" field of a recipient view in the K-9 mail application.
- `onCryptoPgpSignOnlyDisabled()` -- This method is called when PGP sign-only mode is disabled and it updates the inline PGP state and sets the crypto mode to no-choice.
- `isForceTextMessageFormat()` -- The purpose of the method is to return a boolean flag indicating whether PGP inline is enabled for the email message.

## class `com.fsck.k9.activity.compose.AttachmentPresenter`

The purpose of `com.fsck.k9.activity.compose.AttachmentPresenter` class is to manage attachments in emails being composed in the K-9 Mail app. It provides methods for adding, removing, and loading attachments, as well as checking if it is okay to send or save a draft email with or without attachments.

This class contains the following public method(s):

- `addAttachment(android.net.Uri,java.lang.String)` -- The method adds an attachment with a specified URI and content type to the presenter's list of attachments.
- `checkOkForSendingOrDraftSaving()` -- This method checks if it is okay to send or save a draft email with or without attachments.
- `processMessageToForward(com.fsck.k9.mailstore.MessageViewInfo)` -- This method processes a message to forward and shows a warning if any non-inline attachments are missing.
- `loadNonInlineAttachments(com.fsck.k9.mailstore.MessageViewInfo)` -- To load and add non-inline attachments from a message view information object to the attachment presenter, and return a boolean indicating whether all parts are available or not.
- `onClickRemoveAttachment(android.net.Uri)` -- This method removes an attachment by its URI and all associated views from the AttachmentPresenter.
- `onRestoreInstanceState(android.os.Bundle)` -- This method restores the state of the AttachmentPresenter including waiting actions, loader ID, and attachment list.
- `onClickAddAttachment(com.fsck.k9.activity.compose.RecipientPresenter)` -- The purpose of the `onClickAddAttachment` method is to handle the action of a user pressing a button to add an attachment to an email in the K-9 Mail app, and display any errors or show a dialog to select a file to attach.
- `onActivityResult(int,int,android.content.Intent)` -- This method processes the result of an activity that was started to select email attachments and adds the selected attachments to the email being composed.
- `createAttachmentList()` -- The method creates a list of attachments from a map of attachments.
- `onSaveInstanceState(android.os.Bundle)` -- This method saves the state of the AttachmentPresenter object to a Bundle object.
- `attachmentProgressDialogCancelled()` -- The purpose of the `attachmentProgressDialogCancelled()` method is to reset the action to perform after waiting to none when the attachment progress dialog is cancelled.

## interface `com.fsck.k9.activity.compose.AttachmentPresenter$AttachmentsChangedListener`

The interface `com.fsck.k9.activity.compose.AttachmentPresenter$AttachmentsChangedListener` is used to listen for changes in attachments added or removed from an email being composed.

This class contains the following public method(s):

- `onAttachmentAdded()` -- This method is called when a new attachment is added to the email being composed.
- `onAttachmentRemoved()` -- The method is called when an attachment is removed from the email being composed.


# package `com.fsck.k9.activity.loader`

The purpose of the `com.fsck.k9.activity.loader` package is to provide classes for loading attachment content and metadata asynchronously in the K-9 Mail app.

This package contains the following class(es):

## class `com.fsck.k9.activity.loader.AttachmentContentLoader`

The purpose of the `com.fsck.k9.activity.loader.AttachmentContentLoader` class is to asynchronously load attachment content from a URI and save it to a temporary file.

This class contains the following public method(s):

- `loadInBackground()` -- The purpose of the `loadInBackground()` method is to asynchronously load an attachment from a URI and save it to a temporary file for later use.

## class `com.fsck.k9.activity.loader.AttachmentInfoLoader`

The purpose of `com.fsck.k9.activity.loader.AttachmentInfoLoader` is to load attachment metadata in the background for display in the UI.

This class contains the following public method(s):

- `loadInBackground()` -- The purpose of the `loadInBackground()` method is to load attachment metadata (such as name, size, and content type) in the background for display in the UI.


# package `com.fsck.k9.activity.misc`

The `com.fsck.k9.activity.misc` package contains miscellaneous classes and interfaces used in the K-9 Mail app, ranging from contact picture loading to gesture detection and non-UI data retention.

This package contains the following class(es):

## class `com.fsck.k9.activity.misc.ContactPictureLoader$FallbackGlideModelLoader`

The purpose of the class `com.fsck.k9.activity.misc.ContactPictureLoader$FallbackGlideModelLoader` is to provide a way to load fallback contact pictures using the Glide library.

This class contains the following public method(s):

- `getResourceFetcher(com.fsck.k9.activity.misc.ContactPictureLoader$FallbackGlideParams,int,int)` -- This method returns a `DataFetcher` that retrieves a fallback contact picture using the provided parameters.

## class `com.fsck.k9.activity.misc.ContactPictureLoader$FallbackGlideBitmapDecoder`

The purpose of this class is to provide a fallback option for loading contact pictures using Glide image loading library in case a valid photo URI is not available, by generating a bitmap with a text and background color.

This class contains the following public method(s):

- `decode(com.fsck.k9.activity.misc.ContactPictureLoader$FallbackGlideParams,int,int)` -- This method decodes a contact picture and adds a text and background color to it before returning the decoded bitmap as a resource.
- `getId()` -- This method returns a string identifier for a fallback photo.

## class `com.fsck.k9.activity.misc.ContactPictureLoader`

The purpose of the class `com.fsck.k9.activity.misc.ContactPictureLoader` is to load a contact's picture into an ImageView using their address or photoUri.

This class contains the following public method(s):

- `loadContactPicture(com.fsck.k9.view.RecipientSelectView$Recipient,android.widget.ImageView)` -- The method loads a contact's picture into an ImageView based on the contact's thumbnail URI and address.
- `loadContactPicture(com.fsck.k9.mail.Address,android.widget.ImageView)` -- This method loads a contact's picture into an ImageView using the photoUri retrieved from the ContactsHelper.

## class `com.fsck.k9.activity.misc.ContactPictureLoader$FallbackGlideParams`

The purpose of this class is to provide a unique identifier for a contact's picture using their email address and personal name to load a fallback picture in case the original picture is not available.

This class contains the following public method(s):

- `getId()` -- The method returns a unique identifier for a contact's picture using their email address and personal name.

## interface `com.fsck.k9.activity.misc.SwipeGestureDetector$OnSwipeGestureListener`

The purpose of the interface is to define callbacks for handling swipe gesture events in the K-9 Mail app's gesture detector.

This class contains the following public method(s):

- `onSwipeRightToLeft(android.view.MotionEvent,android.view.MotionEvent)` -- The method is called when a swipe gesture from right to left is detected by a gesture detector and provides information on the motion events that triggered the gesture.
- `onSwipeLeftToRight(android.view.MotionEvent,android.view.MotionEvent)` -- The method is called when a left to right swipe gesture is detected and handles the motion events associated with the gesture.

## class `com.fsck.k9.activity.misc.Attachment`

The class `com.fsck.k9.activity.misc.Attachment` is used to represent an email attachment with methods for creating and manipulating attachments.

This class contains the following public method(s):

- `createAttachment(android.net.Uri,int,java.lang.String)` -- The method creates a new instance of the `Attachment` class with the given `Uri`, `loaderId`, and `contentType`.
- `deriveWithLoadComplete(java.lang.String)` -- This method creates a new `Attachment` object with complete loading state using the absolute file path of the attachment.
- `writeToParcel(android.os.Parcel,int)` -- This method writes the object's data to a Parcel, which is used for transferring objects between processes.
- `describeContents()` -- The method returns a bitmask indicating the type of special object serialization that the object represents.
- `deriveWithLoadCancelled()` -- This method returns a new Attachment object with the loading state set to "CANCELLED" if the current loading state is "METADATA".
- `deriveWithMetadataLoaded(java.lang.String,java.lang.String,long)` -- The method creates a new attachment object with metadata loaded from a URI.

## abstract class `com.fsck.k9.activity.misc.ExtendedAsyncTask`

The purpose of `com.fsck.k9.activity.misc.ExtendedAsyncTask` is to provide additional functionality for working with `AsyncTask` instances in Android activities, such as re-binding the task to a new activity instance or detaching it from an activity.

This class contains the following public method(s):

- `restore(android.app.Activity)` -- The `restore` method rebinds the AsyncTask to a new Activity instance and displays a new progress dialog.
- `retain()` -- The `retain()` method detaches an `AsyncTask` from the `Activity` it was bound to while retaining the instance if necessary.

## class `com.fsck.k9.activity.misc.SwipeGestureDetector`

The `com.fsck.k9.activity.misc.SwipeGestureDetector` class is used for detecting swipe gestures in the K9 email client app and calling listener methods based on the direction of the swipe.

This class contains the following public method(s):

- `onFling(android.view.MotionEvent,android.view.MotionEvent,float,float)` -- This method detects when a swipe gesture is made and calls specific listener methods based on the direction of the swipe.
- `onDown(android.view.MotionEvent)` -- The method updates the last MotionEvent and returns the result of its super implementation.

## interface `com.fsck.k9.activity.misc.NonConfigurationInstance`

The interface `com.fsck.k9.activity.misc.NonConfigurationInstance` is meant to provide a way to retain non-UI related data across activity restarts due to configuration changes, such as screen rotations, in a memory-efficient way.

This class contains the following public method(s):

- `restore(android.app.Activity)` -- The method restores a retained NonConfigurationInstance and creates a new progress dialog bound to the new Activity instance after a configuration change.
- `retain()` -- The `retain()` method determines whether an instance of `NonConfigurationInstance` should be retained during an activity restart due to a configuration change and cleans up resources if necessary to prevent memory leaks.


# package `com.fsck.k9.activity.setup`

The `com.fsck.k9.activity.setup` package provides classes for setting up and customizing email accounts, including handling security settings, authentication types, OpenPGP provider selection, folder settings, and font preferences.

This package contains the following class(es):

## class `com.fsck.k9.activity.setup.OpenPgpAppSelectDialog`

The purpose of the class `com.fsck.k9.activity.setup.OpenPgpAppSelectDialog` is to handle the selection of an OpenPGP provider package.

This class contains the following public method(s):

- `onDismissApgDialog()` -- The purpose of the `onDismissApgDialog()` method is to show the OpenPgp select dialog fragment.
- `onCreate(android.os.Bundle)` -- The method sets the theme of the dialog and shows the OpenPGP app selection dialog fragment if the instance state is null.
- `onSelectProvider(java.lang.String)` -- The method selects an OpenPGP provider package and saves it as a setting, then finishes the process.

## class `com.fsck.k9.activity.setup.OpenPgpAppSelectDialog$ApgDeprecationDialogFragment`

The class is responsible for creating and showing a dialog box warning the user that the third-party app they are using for OpenPGP integration is deprecated and suggesting a replacement.

This class contains the following public method(s):

- `onCreateDialog(android.os.Bundle)` -- This method creates and returns a new instance of `ApgDeprecationWarningDialog` as an Android dialog box.
- `onDismiss(android.content.DialogInterface)` -- This method is called when the dialog is dismissed and it triggers a specific action in the parent activity.

## class `com.fsck.k9.activity.setup.AccountSetupOptions`

The purpose of the `com.fsck.k9.activity.setup.AccountSetupOptions` class is to provide options for setting up and customizing email accounts.

This class contains the following public method(s):

- `onCreate(android.os.Bundle)` -- The purpose of the `onCreate` method is to initialize the UI and retrieve the user's preferences for a specific email account.
- `actionOptions(android.content.Context,com.fsck.k9.Account,boolean)` -- This method starts an activity to display options for an email account setup and allows the user to make it the default account.
- `onClick(android.view.View)` -- This method determines if the "next" button has been clicked and then calls the "onDone" method.

## class `com.fsck.k9.activity.setup.AuthTypeAdapter`

The purpose of the class `com.fsck.k9.activity.setup.AuthTypeAdapter` is to provide an adapter for displaying a list of supported authentication types and managing their positions.

This class contains the following public method(s):

- `getAuthPosition(com.fsck.k9.mail.AuthType)` -- This method returns the position of a given authentication type in the adapter's list of authentication types.
- `useInsecureText(boolean)` -- The method is used to select the appropriate localized text label for the plain authentication type, based on whether the password is transmitted insecurely or not.
- `get(android.content.Context)` -- (no description)

## class `com.fsck.k9.activity.setup.OpenPgpAppSelectDialog$OpenPgpProviderEntry`

The class `OpenPgpProviderEntry` is used in the `OpenPgpAppSelectDialog` to represent an OpenPGP provider and provide a simple name for it.

This class contains the following public method(s):

- `toString()` -- The purpose of this method is to return the simple name of the OpenPGP provider.

## class `com.fsck.k9.activity.setup.AccountSetupAccountType`

The `com.fsck.k9.activity.setup.AccountSetupAccountType` class is responsible for allowing users to select the type of email account and setting up the necessary settings for incoming and outgoing mail for a given account.

This class contains the following public method(s):

- `actionSelectAccountType(android.content.Context,com.fsck.k9.Account,boolean)` -- The `actionSelectAccountType` method starts an activity to select an account type for a given account and has an option to make it the default account.
- `onClick(android.view.View)` -- This method handles the click events for selecting the type of email account and sets up the necessary settings for incoming and outgoing mail.
- `onCreate(android.os.Bundle)` -- The method sets up the account type selection screen and retrieves account information from the intent.

## class `com.fsck.k9.activity.setup.AccountSetupOutgoing`

The `com.fsck.k9.activity.setup.AccountSetupOutgoing` class is responsible for setting up and managing outgoing email server settings for a specific account in the K-9 Mail Android app.

This class contains the following public method(s):

- `onCheckedChanged(android.widget.CompoundButton,boolean)` -- This method sets the visibility of the login settings view depending on whether a checkbox is checked or not, and validates fields accordingly.
- `onSaveInstanceState(android.os.Bundle)` -- The method saves the state of the outgoing email account setup activity.
- `onActivityResult(int,int,android.content.Intent)` -- The `onActivityResult` method handles the result of the outgoing server settings activity for setting up a new email account or editing an existing one.
- `actionOutgoingSettings(android.content.Context,com.fsck.k9.Account,boolean)` -- The method starts an activity for outgoing email settings for a given account in the K-9 Mail Android app.
- `actionEditOutgoingSettings(android.content.Context,com.fsck.k9.Account)` -- The method starts an activity to edit the outgoing settings of a K-9 email account.
- `onCreate(android.os.Bundle)` -- This method sets up the UI and initializes the fields for configuring outgoing email server settings for a specific account in an email client.
- `intentActionEditOutgoingSettings(android.content.Context,com.fsck.k9.Account)` -- The purpose of this method is to create an intent for editing outgoing email settings for a specific account in the K-9 Mail application.
- `onClick(android.view.View)` -- The method handles the onClick event of the "next" button and calls the onNext method.

## class `com.fsck.k9.activity.setup.AccountSettings`

The `AccountSettings` class is used to manage account settings in the K-9 email client, including displaying color pickers, selecting folders, and launching the activity for a specific account.

This class contains the following public method(s):

- `onCreateDialog(int)` -- The `onCreateDialog` method creates and returns a dialog box with various color pickers to allow the user to select colors for account and notification settings.
- `onPrepareDialog(int,android.app.Dialog)` -- This method prepares the dialog for display by setting the appropriate color on the color picker based on the user's selected account or notification setting.
- `actionSettings(android.content.Context,com.fsck.k9.Account)` -- This method starts an Intent to launch the AccountSettings activity with the specified account.
- `onChooseLedColor()` -- The method displays a color picker dialog for choosing an LED color for email notifications in the K-9 email client Account Settings activity.
- `onChooseChipColor()` -- The method displays a color picker dialog for the user to choose a color for their email account chip.
- `onActivityResult(int,int,android.content.Intent)` -- (no description)
- `onChooseAutoExpandFolder()` -- The method allows the user to choose a folder that will automatically expand when viewing messages for a specific email account in K-9 Mail.
- `onCreate(android.os.Bundle)` -- (no description)

## class `com.fsck.k9.activity.setup.SpinnerOption`

The class `com.fsck.k9.activity.setup.SpinnerOption` represents an option in a spinner and provides a method to set the selected value in the spinner.

This class contains the following public method(s):

- `toString()` -- The `toString()` method returns the label of the `SpinnerOption` object.
- `setSpinnerOptionValue(android.widget.Spinner,java.lang.Object)` -- The method sets the selected value in a spinner to the provided value.

## class `com.fsck.k9.activity.setup.FolderSettings`

The class is used to handle folder settings for K9 email accounts, providing methods for saving settings, opening folder settings, and initializing and populating a preferences activity for editing folder settings.

This class contains the following public method(s):

- `onPause()` -- This method saves the folder settings and handles any possible exceptions when the activity is paused.
- `actionSettings(android.content.Context,com.fsck.k9.Account,java.lang.String)` -- The `actionSettings` method is used to open the settings for a specific email folder for a K9 email account.
- `onCreate(android.os.Bundle)` -- The method initializes and populates a preferences activity for editing folder settings in an email application.

## class `com.fsck.k9.activity.setup.AccountSetupCheckSettings`

The purpose of the `com.fsck.k9.activity.setup.AccountSetupCheckSettings` class is to provide methods for setting up and checking email account settings.

This class contains the following public method(s):

- `onDestroy()` -- The method sets two boolean flags to indicate that the activity is destroyed and cancelled.
- `actionCheckSettings(android.app.Activity,com.fsck.k9.Account,com.fsck.k9.activity.setup.AccountSetupCheckSettings$CheckDirection)` -- The purpose of the method is to start the account settings check activity for the specified account and check direction.
- `onClick(android.view.View)` -- The method handles the click event on the cancel button and calls the onCancel method.
- `doPositiveClick(int)` -- The method is called when the user clicks the positive button on a dialog with the ID `R.id.dialog_account_setup_error`, and it finishes the activity.
- `onCreate(android.os.Bundle)` -- This method sets up the UI for checking email account settings and launches a task to perform the check.
- `dialogCancelled(int)` -- The method is called when a dialog is cancelled and it does nothing.
- `onActivityResult(int,int,android.content.Intent)` -- This method sets the result code and finishes the activity.
- `doNegativeClick(int)` -- The method handles negative click action for the account setup error dialog and sets the canceled flag to false.

## class `com.fsck.k9.activity.setup.AccountSetupComposition`

The purpose of `com.fsck.k9.activity.setup.AccountSetupComposition` is to set up the UI for composing an email message and to allow editing of the settings for a K-9 email account.

This class contains the following public method(s):

- `onBackPressed()` -- The purpose of the `onBackPressed()` method is to save the settings and then call the superclass's `onBackPressed()` method.
- `onCreate(android.os.Bundle)` -- This method sets up the UI for composing an email message by populating various text fields and checkboxes.
- `onActivityResult(int,int,android.content.Intent)` -- (no description)
- `onSaveInstanceState(android.os.Bundle)` -- The purpose of this method is to save the UUID of the account being set up in the Bundle to be retrieved later when needed.
- `actionEditCompositionSettings(android.app.Activity,com.fsck.k9.Account)` -- The method starts the composition settings activity to edit the settings of a specified K-9 email account.

## class `com.fsck.k9.activity.setup.ConnectionSecurityAdapter`

The purpose of the class com.fsck.k9.activity.setup.ConnectionSecurityAdapter is to create a spinner adapter for connection security settings and provide methods to get the position of a given connection security type and a ConnectionSecurityAdapter object based on the context.

This class contains the following public method(s):

- `get(android.content.Context,com.fsck.k9.mail.ConnectionSecurity[])` -- This method creates a spinner adapter for connection security settings.
- `getConnectionSecurityPosition(com.fsck.k9.mail.ConnectionSecurity)` -- This method returns the position of a given connection security type in a list of connection security options.
- `get(android.content.Context)` -- This method returns a ConnectionSecurityAdapter object based on the context and available connection security values.

## class `com.fsck.k9.activity.setup.WelcomeMessage`

The class `com.fsck.k9.activity.setup.WelcomeMessage` is responsible for displaying a welcome message during K-9 Mail's setup process and handles user clicks to open new account setup or import existing settings.

This class contains the following public method(s):

- `onCreate(android.os.Bundle)` -- The `onCreate` method initializes the UI components and click listeners for the welcome message screen in K-9 Mail's setup process.
- `onClick(android.view.View)` -- The `onClick` method is triggered when the user clicks on a view, and depending on which view was clicked, either opens a new account setup or imports existing settings.
- `showWelcomeMessage(android.content.Context)` -- The method displays a welcome message by starting a new activity in the passed context.

## class `com.fsck.k9.activity.setup.AccountSetupIncoming`

The purpose of the class is to handle the setup and editing of incoming mail account settings in the K-9 email client for Android.

This class contains the following public method(s):

- `actionIncomingSettings(android.app.Activity,com.fsck.k9.Account,boolean)` -- The method opens the account settings for incoming mail on an Android device and sets the default account if specified.
- `onSaveInstanceState(android.os.Bundle)` -- This method saves the current state of the activity before it is paused or destroyed, by storing the account UUID, security type position, and authentication type position in a Bundle object.
- `intentActionEditIncomingSettings(android.content.Context,com.fsck.k9.Account)` -- The purpose of the method is to create an intent to edit the incoming settings of a K-9 email account.
- `onClick(android.view.View)` -- The method handles the click event for the "next" button and calls the `onNext()` method.
- `actionEditIncomingSettings(android.app.Activity,com.fsck.k9.Account)` -- The method launches the activity for editing incoming email account settings.
- `onActivityResult(int,int,android.content.Intent)` -- This method handles the result of an activity called to set up incoming mail settings or outgoing mail settings for an email account.
- `onCreate(android.os.Bundle)` -- This method sets up the UI and retrieves settings for configuring an incoming mail account.

## class `com.fsck.k9.activity.setup.FontSizeSettings`

The purpose of the class `com.fsck.k9.activity.setup.FontSizeSettings` is to allow users to edit and set font size preferences for the K-9 email client.

This class contains the following public method(s):

- `actionEditSettings(android.content.Context)` -- The method starts the FontSizeSettings activity.
- `onCreate(android.os.Bundle)` -- This method is used to set the font size preferences for various parts of the K-9 email client.
- `onBackPressed()` -- The method saves the font size settings and allows the back button to function normally.

## class `com.fsck.k9.activity.setup.AccountSetupNames`

The class `com.fsck.k9.activity.setup.AccountSetupNames` is responsible for setting up the UI and handling user input to set the names for a given email account in an email app.

This class contains the following public method(s):

- `onClick(android.view.View)` -- The method handles the 'onClick' event for the 'done' button and executes the 'onNext' method.
- `onCreate(android.os.Bundle)` -- This method sets up the UI and listeners for user input and loads existing account data if available in the `onCreate` lifecycle of the `AccountSetupNames` activity.
- `actionSetNames(android.content.Context,com.fsck.k9.Account)` -- This method starts an activity to set the names for a given account in an email app.

## class `com.fsck.k9.activity.setup.SliderPreference`

The purpose of the class `com.fsck.k9.activity.setup.SliderPreference` is to provide functionality for a preference item that is represented by a slider, allowing the user to select a value within a specified range.

This class contains the following public method(s):

- `setValue(float)` -- This method sets the value of a slider preference and ensures that the value is within the range of 0 to 1, and persists the value if necessary.
- `getValue()` -- The purpose of this method is to retrieve the current float value of the SliderPreference.
- `getSummary()` -- The method returns a summary description based on the current value of a SliderPreference object.
- `setSummary(int)` -- The method sets the summary of a slider preference by retrieving a string array resource from the application context.
- `setSummary(java.lang.CharSequence)` -- The method sets a summary for the SliderPreference and resets any previous summaries.
- `setSummary(java.lang.CharSequence[])` -- The method sets an array of summary texts to be displayed in a slider preference.

## class `com.fsck.k9.activity.setup.ConnectionSecurityHolder`

The purpose of the `com.fsck.k9.activity.setup.ConnectionSecurityHolder` class is to hold the security information for an email connection, which is used during email setup.

This class contains the following public method(s):

- `toString()` -- The purpose of the `toString()` method is to convert the `ConnectionSecurityHolder` object into a string representation which is determined by the `resourceId` and `connectionSecurity` variables.

## class `com.fsck.k9.activity.setup.Prefs`

The purpose of the `com.fsck.k9.activity.setup.Prefs` class is to handle launching the K-9 Mail application's preferences screen using an Intent and contains an `onCreate()` method without description.

This class contains the following public method(s):

- `actionPrefs(android.content.Context)` -- This method launches the K-9 Mail application's preferences screen using an Intent.
- `onCreate(android.os.Bundle)` -- (no description)

## class `com.fsck.k9.activity.setup.OpenPgpAppSelectDialog$OpenPgpAppSelectFragment`

The class is a fragment that implements a dialog for selecting an OpenPGP provider and updates the selected provider when the dialog is dismissed.

This class contains the following public method(s):

- `onDismiss(android.content.DialogInterface)` -- This method is called when the OpenPGP app selection dialog is dismissed and updates the selected provider.
- `onCreateDialog(android.os.Bundle)` -- This method creates a dialog that allows the user to select an OpenPGP provider for use with the app.
- `onCreate(android.os.Bundle)` -- The method initializes a variable with the OpenPGP provider selected by the user in the K-9 email app.

## class `com.fsck.k9.activity.setup.AuthTypeHolder`

The `com.fsck.k9.activity.setup.AuthTypeHolder` class is used to hold and represent different authentication types and whether they are secure or insecure in the K-9 Mail Android app.

This class contains the following public method(s):

- `toString()` -- The `toString()` method returns an appropriate string representation of the authentication type holder.
- `setInsecure(boolean)` -- The method sets a boolean value to indicate if a certain authentication type is insecure.

## class `com.fsck.k9.activity.setup.AccountSetupBasics`

The purpose of the class `com.fsck.k9.activity.setup.AccountSetupBasics` is to handle the setup of a new email account in the K9 email client, including validating input fields, checking incoming and outgoing email settings, and creating a dialog to display notes from the email provider.

This class contains the following public method(s):

- `onSaveInstanceState(android.os.Bundle)` -- The `onSaveInstanceState` method saves the state of the account setup basics activity in the given bundle.
- `afterTextChanged(android.text.Editable)` -- The method calls a function to validate input fields after text has been changed.
- `onActivityResult(int,int,android.content.Intent)` -- This method handles the result of an activity started for checking settings for incoming and outgoing email and saves account details if both checks are successful.
- `beforeTextChanged(java.lang.CharSequence,int,int,int)` -- The method is called before the text is changed in a particular EditText, and it accepts the original text as a CharSequence, the starting index of the modified text, the number of characters to be replaced, and the length of the new text as parameters.
- `onClick(android.view.View)` -- The method handles clicks on the "Next" and "Manual setup" buttons in the account setup screen of the K9 email client.
- `onCreate(android.os.Bundle)` -- The method sets up the basic components and listeners for an email account setup screen.
- `onCreateDialog(int)` -- This method creates a dialog to display a note from the email provider during the setup process of a new email account.
- `onTextChanged(java.lang.CharSequence,int,int,int)` -- The method is called when the text in an input field is changed and its purpose is not defined in the provided code.
- `actionNewAccount(android.content.Context)` -- The method launches the `AccountSetupBasics` activity to create a new email account.
- `onClientCertificateChanged(java.lang.String)` -- The method is called when the client certificate is changed and it validates the fields.
- `onCheckedChanged(android.widget.CompoundButton,boolean)` -- The method is called when the user checks or unchecks a checkbox for client certificate selection and updates the view visibility and validates the fields accordingly.


# package `com.fsck.k9.autocrypt`

The `com.fsck.k9.autocrypt` package contains classes related to Autocrypt implementation in the K-9 Mail app, including parsing Autocrypt headers, providing Autocrypt operations, interacting with an OpenPGP API, and representing the Autocrypt header.

This package contains the following class(es):

## class `com.fsck.k9.autocrypt.AutocryptHeaderParser`

The purpose of the class is to parse and process Autocrypt headers in email messages according to the Autocrypt specification.

This class contains the following public method(s):

- `getInstance()` -- The method returns an instance of the `AutocryptHeaderParser` class using the singleton pattern.

## class `com.fsck.k9.autocrypt.AutocryptOperations`

The purpose of the class `com.fsck.k9.autocrypt.AutocryptOperations` is to provide operations related to Autocrypt encryption and peer updates in email messages, such as adding Autocrypt headers to messages and checking for the presence of Autocrypt headers.

This class contains the following public method(s):

- `addAutocryptPeerUpdateToIntentIfPresent(com.fsck.k9.mail.Message,android.content.Intent)` -- This method adds Autocrypt peer update information to an intent if a valid Autocrypt header is present in the email message.
- `getInstance()` -- This method returns an instance of `AutocryptOperations` with a shared instance of `AutocryptHeaderParser`.
- `addAutocryptHeaderToMessage(com.fsck.k9.mail.Message,byte[],java.lang.String,boolean)` -- The method adds an Autocrypt header to a given email message.
- `hasAutocryptHeader(com.fsck.k9.mail.Message)` -- This method checks whether a given email message contains an Autocrypt header.

## class `com.fsck.k9.autocrypt.AutocryptOpenPgpApiInteractor`

The purpose of the `com.fsck.k9.autocrypt.AutocryptOpenPgpApiInteractor` class is to interact with an OpenPGP API and retrieve key material for a given OpenPGP key ID.

This class contains the following public method(s):

- `getInstance()` -- The `getInstance()` method returns a new instance of `AutocryptOpenPgpApiInteractor`.
- `getKeyMaterialFromApi(org.openintents.openpgp.util.OpenPgpApi,long,java.lang.String)` -- The method retrieves key material for a given OpenPGP key ID from an OpenPGP API and returns it as a byte array.

## class `com.fsck.k9.autocrypt.AutocryptHeader`

The purpose of the `AutocryptHeader` class in the K-9 Mail app is to represent the Autocrypt header used in email messages for encrypted communication.

This class contains the following public method(s):

- `hashCode()` -- The `hashCode()` method calculates a hash code value for the AutocryptHeader object based on its keyData, addr, parameters, and isPreferEncryptMutual fields.
- `equals(java.lang.Object)` -- The purpose of the method is to compare two `AutocryptHeader` objects for equality based on their fields.


# package `com.fsck.k9.cache`

The package `com.fsck.k9.cache` provides classes for cache management and efficient retrieval and manipulation of email-related information in the K-9 email client for Android.

This package contains the following class(es):

## class `com.fsck.k9.cache.TemporaryAttachmentStore`

The class `com.fsck.k9.cache.TemporaryAttachmentStore` provides methods for retrieving temporary files used for writing email attachments with sanitized filenames in the K-9 email client for Android.

This class contains the following public method(s):

- `getFileForWriting(android.content.Context,java.lang.String)` -- The method retrieves a file object for writing an attachment to a temporary directory while sanitizing the filename.
- `getFile(android.content.Context,java.lang.String)` -- This method returns a File object representing the temporary attachment directory with a sanitized filename.

## class `com.fsck.k9.cache.EmailProviderCacheCursor`

The class `com.fsck.k9.cache.EmailProviderCacheCursor` provides a cursor for accessing and manipulating cached email data in K-9 Mail.

This class contains the following public method(s):

- `getPosition()` -- This method returns the current position of the cursor, or the position of the next visible row if some rows are hidden.
- `moveToNext()` -- The method moves the cursor to the next row in the result set.
- `moveToPosition(int)` -- The method moves the cursor to the specified position, accounting for any hidden rows in the cursor.
- `moveToLast()` -- The method moves the cursor to the last row of the cache and returns `true` if successful.
- `isLast()` -- This method checks if the current position of the cursor is at the last row of the result set.
- `getInt(int)` -- This method retrieves an integer value from either the message or thread cache, or from the parent class if no value is found.
- `moveToFirst()` -- The method moves the cursor to the first row and returns a boolean value indicating whether the operation was successful or not.
- `move(int)` -- The method moves the cursor by a specified offset and returns true if the new position is valid.
- `moveToPrevious()` -- The method moves the cursor to the previous position and returns whether the move was successful.
- `getCount()` -- This method returns the number of rows in the cursor after excluding those that are hidden.

## class `com.fsck.k9.cache.EmailProviderCache`

The purpose of the `com.fsck.k9.cache.EmailProviderCache` class is to provide a cache for email provider data, allowing for efficient retrieval and manipulation of email-related information such as message and thread IDs, and hidden messages.

This class contains the following public method(s):

- `getCache(java.lang.String,android.content.Context)` -- The method returns an instance of EmailProviderCache for a given email account UUID and application context, creating one if necessary.
- `setValueForThreads(java.util.List,java.lang.String,java.lang.String)` -- The method sets a value for a specific column in the cache for a list of email threads identified by their root IDs.
- `removeValueForThreads(java.util.List,java.lang.String)` -- The method removes a specified column value for a list of email threads from the cache.
- `hideMessages(java.util.List)` -- The method hides a list of email messages by adding their ID and folder ID to a cache.
- `removeValueForMessages(java.util.List,java.lang.String)` -- This method removes the value for the specified column name from the cached data of a list of emails identified by their message IDs.
- `setValueForMessages(java.util.List,java.lang.String,java.lang.String)` -- The method sets a value for a specified column in the cache for a list of email message IDs.
- `getValueForThread(java.lang.Long,java.lang.String)` -- This method retrieves a specific value for a given thread in the email provider cache.
- `getValueForMessage(java.lang.Long,java.lang.String)` -- The method returns the value of a specific column for a given email message ID from the email provider cache.
- `unhideMessages(java.util.List)` -- The method unhides the specified list of messages that were previously hidden in the cache.
- `isMessageHidden(java.lang.Long,long)` -- The method checks if a message is hidden in a specific folder.


# package `com.fsck.k9.controller`

The `com.fsck.k9.controller` package contains classes and interfaces that manage email messages and perform various tasks related to email account synchronization, notification handling, and message sending/receiving in the K9 email client.

This package contains the following class(es):

## interface `com.fsck.k9.controller.ProgressBodyFactory$ProgressListener`

The purpose of the interface `com.fsck.k9.controller.ProgressBodyFactory$ProgressListener` is to provide a way to listen for updates on the progress of a long-running operation.

This class contains the following public method(s):

- `updateProgress(int)` -- This method updates the progress of a long-running operation.

## class `com.fsck.k9.controller.MessagingControllerPushReceiver`

The purpose of the `com.fsck.k9.controller.MessagingControllerPushReceiver` class is to handle push notifications and synchronize email folders with the server.

This class contains the following public method(s):

- `pushError(java.lang.String,java.lang.Exception)` -- The method `pushError` logs error messages and notifies the user if there is a certificate problem during messaging operations.
- `messagesArrived(com.fsck.k9.mail.Folder,java.util.List)` -- The method processes incoming messages and passes them on to the messaging controller.
- `messagesRemoved(com.fsck.k9.mail.Folder,java.util.List)` -- The method updates the messaging controller with the information that messages have been removed from a folder.
- `sleep(com.fsck.k9.mail.power.TracingPowerManager.TracingWakeLock,long)` -- This method causes the device to sleep for a specified amount of time while holding on to a wake lock and using a push wake lock timeout.
- `getPushState(java.lang.String)` -- This method returns the push state of a specified folder in the account.
- `syncFolder(com.fsck.k9.mail.Folder)` -- The `syncFolder` method synchronizes the given email folder with the server.
- `authenticationFailed()` -- This method handles authentication failure for the messaging controller push receiver by calling the `handleAuthenticationFailure` method with the account and a Boolean value as arguments.
- `getContext()` -- The method returns the context of the MessagingControllerPushReceiver class.
- `messagesFlagsChanged(com.fsck.k9.mail.Folder,java.util.List)` -- The method updates the flags of a list of email messages in a specific folder and notifies the message controller of the changes.
- `setPushActive(java.lang.String,boolean)` -- The method enables/disables push notification for a given folderName in the MessagingControllerPushReceiver by notifying all registered MessagingListeners.

## class `com.fsck.k9.controller.MemorizingMessagingListener`

The class is used to keep track of the state and progress of email account syncing and message sending operations in the K9 email client.

This class contains the following public method(s):

- `setPushActive(com.fsck.k9.Account,java.lang.String,boolean)` -- The method sets the pushing state of a specific folder in an email account to either "STARTED" or "FINISHED".
- `pendingCommandsFinished(com.fsck.k9.Account)` -- This method sets the processing state of a specific account's memory to FINISHED when all pending commands have been completed.
- `synchronizeMailboxFinished(com.fsck.k9.Account,java.lang.String,int,int)` -- The method updates the memory of account and folder after synchronizing mailbox and saves syncing state, total messages in mailbox, and new messages synced.
- `synchronizeMailboxStarted(com.fsck.k9.Account,java.lang.String)` -- The method updates the state and progress of a mailbox synchronization operation.
- `pendingCommandStarted(com.fsck.k9.Account,java.lang.String)` -- The method sets the title of the pending command for an account in the messaging listener's memory.
- `synchronizeMailboxFailed(com.fsck.k9.Account,java.lang.String,java.lang.String)` -- The method updates the memory of a mailbox synchronization process as failed and adds an error message.
- `sendPendingMessagesStarted(com.fsck.k9.Account)` -- The method sets the sending state, completed folder count and total folder count for a specified account when pending messages are started to be sent.
- `pendingCommandsProcessing(com.fsck.k9.Account)` -- This method updates the processing state of pending commands for a specific email account.
- `synchronizeMailboxProgress(com.fsck.k9.Account,java.lang.String,int,int)` -- The method updates the progress of email synchronization for a specific mailbox folder in a given account.
- `sendPendingMessagesCompleted(com.fsck.k9.Account)` -- The method sets the sending state of a given account to "FINISHED" after all pending messages have been sent.
- `pendingCommandCompleted(com.fsck.k9.Account,java.lang.String)` -- This method resets the processing command title for a given email account.
- `sendPendingMessagesFailed(com.fsck.k9.Account)` -- The method sets the sending state of pending messages for a specific account to "failed" in the memory of the messaging listener.

## abstract class `com.fsck.k9.controller.SimpleMessagingListener`

The purpose of the abstract class `com.fsck.k9.controller.SimpleMessagingListener` is to provide a set of methods for handling events related to messaging in the K-9 Mail email client, such as mailbox synchronization, message retrieval, and push notifications.

This class contains the following public method(s):

- `setPushActive(com.fsck.k9.Account,java.lang.String,boolean)` -- The method sets whether push notifications are enabled for a specific email account and folder.
- `messageUidChanged(com.fsck.k9.Account,java.lang.String,java.lang.String,java.lang.String)` -- (no description)
- `sendPendingMessagesFailed(com.fsck.k9.Account)` -- The method is called when sending pending messages fails for a given email account.
- `pendingCommandsProcessing(com.fsck.k9.Account)` -- The method is called when pending commands are being processed for a specific email account.
- `sendPendingMessagesCompleted(com.fsck.k9.Account)` -- The method is called when sending pending messages has finished for a specific email account.
- `listFoldersFailed(com.fsck.k9.Account,java.lang.String)` -- The method is called when the attempt to list folders for an email account fails.
- `remoteSearchServerQueryComplete(java.lang.String,int,int)` -- The method is called when a remote search server query is completed, providing the number of results and the maximum number of results.
- `checkMailStarted(android.content.Context,com.fsck.k9.Account)` -- To be executed when a mail check has started for a specific account.
- `pendingCommandStarted(com.fsck.k9.Account,java.lang.String)` -- This method is called when a pending command has started for a specific email account.
- `loadAttachmentFailed(com.fsck.k9.Account,com.fsck.k9.mail.Message,com.fsck.k9.mail.Part,java.lang.String)` -- This method is called when loading an attachment fails.
- `checkMailFinished(android.content.Context,com.fsck.k9.Account)` -- The method is called when the mail checking process is finished in K9 email client and takes the Android context and K9 Account as parameters.
- `remoteSearchFinished(java.lang.String,int,int,java.util.List)` -- The method is called when a remote search on an email folder is finished, and returns the number of results, maximum results, and a list of extra results.
- `remoteSearchFailed(java.lang.String,java.lang.String)` -- The method is called when a remote search fails in an email messaging listener.
- `synchronizeMailboxStarted(com.fsck.k9.Account,java.lang.String)` -- The method is called when mailbox synchronization is started for a specific account and folder in the K-9 Mail email client.
- `synchronizeMailboxNewMessage(com.fsck.k9.Account,java.lang.String,com.fsck.k9.mail.Message)` -- The method is called when a new message is received and is used to update the corresponding mailbox in the account.
- `accountSizeChanged(com.fsck.k9.Account,long,long)` -- The `accountSizeChanged` method updates the size of a given email account.
- `synchronizeMailboxHeadersFinished(com.fsck.k9.Account,java.lang.String,int,int)` -- The method is invoked when header synchronization for a mailbox has finished and provides information on the total number of messages in the mailbox and the number of new messages.
- `sendPendingMessagesStarted(com.fsck.k9.Account)` -- The method is called before sending pending messages for an email account starts.
- `synchronizeMailboxFailed(com.fsck.k9.Account,java.lang.String,java.lang.String)` -- The method is called when synchronization of a mailbox fails, with account, folder, and message information.
- `enableProgressIndicator(boolean)` -- The method enables or disables a progress indicator for message retrieval or sending.
- `synchronizeMailboxProgress(com.fsck.k9.Account,java.lang.String,int,int)` -- The method tracks the progress of mailbox synchronization for a specific folder in an email account.
- `synchronizeMailboxFinished(com.fsck.k9.Account,java.lang.String,int,int)` -- The method is called when mailbox synchronization is finished and provides information about the mailbox status.
- `accountStatusChanged(com.fsck.k9.BaseAccount,com.fsck.k9.AccountStats)` -- The method is called when the status of an email account changes, and it takes the account and its statistics as parameters.
- `messageDeleted(com.fsck.k9.Account,java.lang.String,com.fsck.k9.mail.Message)` -- This method is called when a message is deleted from a folder in an email account.
- `pendingCommandsFinished(com.fsck.k9.Account)` -- The method is called when all pending account commands (such as sending or deleting emails) have been completed.
- `listFoldersStarted(com.fsck.k9.Account)` -- The method is a callback function that is called when retrieving a list of folders for a specified email account has started.
- `folderStatusChanged(com.fsck.k9.Account,java.lang.String,int)` -- This method is called when the status of a folder in a mail account, such as the number of unread messages, has changed.
- `emptyTrashCompleted(com.fsck.k9.Account)` -- This method is called when the emptying of the trash folder for a specific email account is completed.
- `loadMessageRemoteFailed(com.fsck.k9.Account,java.lang.String,java.lang.String,java.lang.Throwable)` -- This method is called when the remote loading of a message failed.
- `synchronizeMailboxHeadersProgress(com.fsck.k9.Account,java.lang.String,int,int)` -- The method updates the progress of synchronizing mailbox headers for a specific folder in an email account.
- `synchronizeMailboxHeadersStarted(com.fsck.k9.Account,java.lang.String)` -- The method is called when the synchronization of mailbox headers has started for a specific folder in a K9 email account.
- `listFolders(com.fsck.k9.Account,java.util.List)` -- The method lists the folders for a given account.
- `listFoldersFinished(com.fsck.k9.Account)` -- The method is called when listing of folders for a particular email account has finished.
- `loadAttachmentFinished(com.fsck.k9.Account,com.fsck.k9.mail.Message,com.fsck.k9.mail.Part)` -- This method is called when loading an email attachment has finished.
- `systemStatusChanged()` -- The `systemStatusChanged()` method is an empty implementation meant to be overridden in order to handle changes in the messaging system's status.
- `synchronizeMailboxRemovedMessage(com.fsck.k9.Account,java.lang.String,com.fsck.k9.mail.Message)` -- The method is called when a message is removed from the server and is responsible for synchronizing the mailbox accordingly.
- `loadMessageRemoteFinished(com.fsck.k9.Account,java.lang.String,java.lang.String)` -- The method is called when a remote message has finished loading for a specific account and folder.
- `remoteSearchStarted(java.lang.String)` -- The method is called when a remote search operation has started for a specific folder.
- `updateProgress(int)` -- The method updates the progress of a messaging process.
- `pendingCommandCompleted(com.fsck.k9.Account,java.lang.String)` -- This method is called when a pending command has been completed for a particular email account.
- `listLocalMessagesAddMessages(com.fsck.k9.Account,java.lang.String,java.util.List)` -- The method retrieves a list of local messages and adds them to a specified folder for a given email account.
- `searchStats(com.fsck.k9.AccountStats)` -- This method is called when the search for messages has finished to receive relevant statistics about the search.

## class `com.fsck.k9.controller.PendingCommandSerializer`

The `com.fsck.k9.controller.PendingCommandSerializer` class is used to serialize and deserialize pending commands into/from JSON strings for storage in a messaging app.

This class contains the following public method(s):

- `unserialize(long,java.lang.String,java.lang.String)` -- This method deserializes a pending command from a JSON string and sets its database ID.
- `serialize(com.fsck.k9.controller.MessagingControllerCommands$PendingCommand)` -- The `serialize` method serializes a given `PendingCommand` object into a JSON string using the appropriate JSON adapter.
- `getInstance()` -- The method returns the singleton instance of the `PendingCommandSerializer` class.

## class `com.fsck.k9.controller.MessagingControllerCommands$PendingMoveOrCopy`

The class is used to create and execute pending move or copy operations for email messages between two folders in an email client.

This class contains the following public method(s):

- `create(java.lang.String,java.lang.String,boolean,java.util.Map)` -- This method creates a pending move or copy operation for a message between two folders with an optional map of message UIDs.
- `create(java.lang.String,java.lang.String,boolean,java.util.List)` -- This method creates a new instance of `PendingMoveOrCopy` object with specified source folder, destination folder, boolean value indicating if it is a copy operation, list of UIDs to be moved or copied.
- `getCommandName()` -- This method returns the name of the command for moving or copying a message in an email client.
- `execute(com.fsck.k9.controller.MessagingController,com.fsck.k9.Account)` -- The method executes a pending move or copy operation for a specified messaging controller and account.

## class `com.fsck.k9.controller.MessagingControllerCommands$PendingEmptyTrash`

The class is used to represent a pending operation to empty the trash folder for a specific email account using the messaging controller in the K-9 Mail app.

This class contains the following public method(s):

- `create()` -- The method creates a new instance of the `PendingEmptyTrash` class.
- `execute(com.fsck.k9.controller.MessagingController,com.fsck.k9.Account)` -- This method executes the pending empty trash operation for the given account using the messaging controller.
- `getCommandName()` -- The method returns a constant indicating that the command is to empty the trash folder.

## class `com.fsck.k9.controller.MessagingControllerCommands$PendingMarkAllAsRead`

The purpose of the class `com.fsck.k9.controller.MessagingControllerCommands$PendingMarkAllAsRead` is to provide functionality to mark all messages as read for a specific email account in the messaging controller.

This class contains the following public method(s):

- `create(java.lang.String)` -- The method creates a new instance of `PendingMarkAllAsRead` with the given folder name.
- `execute(com.fsck.k9.controller.MessagingController,com.fsck.k9.Account)` -- The purpose of this method is to execute a command to mark all messages as read for a specific email account in the messaging controller.
- `getCommandName()` -- The method returns a string representing the command name for marking all as read in a messaging controller.

## abstract class `com.fsck.k9.controller.MessagingControllerCommands$PendingCommand`

The purpose of the abstract class `com.fsck.k9.controller.MessagingControllerCommands$PendingCommand` is to define the structure of a pending command that can be executed on a messaging controller for a specific account.

This class contains the following public method(s):

- `getCommandName()` -- The method returns the name of the pending command as a string.
- `execute(com.fsck.k9.controller.MessagingController,com.fsck.k9.Account)` -- The method executes a pending command for a specific messaging controller and account.

## interface `com.fsck.k9.controller.MessagingListener`

The interface `com.fsck.k9.controller.MessagingListener` defines methods that allow tracking of messaging tasks and events, such as synchronizing emails, listing folders, and sending messages, in the K-9 Mail app.

This class contains the following public method(s):

- `synchronizeMailboxNewMessage(com.fsck.k9.Account,java.lang.String,com.fsck.k9.mail.Message)` -- This method is used to synchronize a new message in a mailbox for a particular account.
- `pendingCommandsProcessing(com.fsck.k9.Account)` -- The method is called when pending commands on the given account are being processed.
- `setPushActive(com.fsck.k9.Account,java.lang.String,boolean)` -- Sets the status of push notifications for a specific email account and folder.
- `pendingCommandsFinished(com.fsck.k9.Account)` -- The method is called to notify that the pending commands for a specific email account have been completed.
- `listFoldersFailed(com.fsck.k9.Account,java.lang.String)` -- This method is called when listing folders on an email account fails.
- `loadMessageRemoteFinished(com.fsck.k9.Account,java.lang.String,java.lang.String)` -- The method signals that loading a message from a remote server has finished.
- `loadAttachmentFailed(com.fsck.k9.Account,com.fsck.k9.mail.Message,com.fsck.k9.mail.Part,java.lang.String)` -- This method is called when an email attachment fails to load for a specific reason.
- `synchronizeMailboxHeadersFinished(com.fsck.k9.Account,java.lang.String,int,int)` -- This method is called to signal that the synchronization of mailbox headers with the server has finished.
- `checkMailStarted(android.content.Context,com.fsck.k9.Account)` -- The method is called when checking for new email has started on a specific account in the K-9 Mail app.
- `loadMessageRemoteFailed(com.fsck.k9.Account,java.lang.String,java.lang.String,java.lang.Throwable)` -- This method is called when the remote loading of a message fails and provides information about the account, folder, UID and the error.
- `messageUidChanged(com.fsck.k9.Account,java.lang.String,java.lang.String,java.lang.String)` -- This method is called when the UID of a message in a folder has changed.
- `remoteSearchServerQueryComplete(java.lang.String,int,int)` -- The method is called when a remote search server query is completed and provides information about the number of results and maximum number of results.
- `folderStatusChanged(com.fsck.k9.Account,java.lang.String,int)` -- This method is called when the status of a folder (such as unread message count) changes for a specific email account.
- `listFoldersStarted(com.fsck.k9.Account)` -- This method is called when the process of listing folders for a given email account has started.
- `enableProgressIndicator(boolean)` -- The purpose of the method is to enable or disable a progress indicator used for messaging operations.
- `synchronizeMailboxRemovedMessage(com.fsck.k9.Account,java.lang.String,com.fsck.k9.mail.Message)` -- The method is used to synchronize the removal of a message from a specific folder in a mail account.
- `synchronizeMailboxHeadersProgress(com.fsck.k9.Account,java.lang.String,int,int)` -- This method reports the progress of synchronizing mailbox headers for a specific folder in an email account.
- `emptyTrashCompleted(com.fsck.k9.Account)` -- The method is called when the trash folder has been successfully emptied for a specific email account.
- `systemStatusChanged()` -- This method is called when the system status of the mail client is changed.
- `loadAttachmentFinished(com.fsck.k9.Account,com.fsck.k9.mail.Message,com.fsck.k9.mail.Part)` -- This method is called when loading an attachment for a specific message has finished.
- `synchronizeMailboxProgress(com.fsck.k9.Account,java.lang.String,int,int)` -- The method tracks the progress of synchronizing a mailbox for a given email account, folder, and number of completed and total items.
- `sendPendingMessagesCompleted(com.fsck.k9.Account)` -- This method is called when the process of sending pending messages for a specific account is completed.
- `synchronizeMailboxHeadersStarted(com.fsck.k9.Account,java.lang.String)` -- This method is invoked when the process of synchronizing mailbox headers has started for a specific account and folder.
- `remoteSearchFinished(java.lang.String,int,int,java.util.List)` -- The method is called when a remote search (e.g. via IMAP) has finished and provides the search results.
- `synchronizeMailboxStarted(com.fsck.k9.Account,java.lang.String)` -- This method is called when a mailbox is about to be synchronized in the email client K-9 Mail.
- `searchStats(com.fsck.k9.AccountStats)` -- The method is used to search and retrieve statistics specific to an email account.
- `pendingCommandCompleted(com.fsck.k9.Account,java.lang.String)` -- The method is called when a pending mail operation is completed for a specific account.
- `messageDeleted(com.fsck.k9.Account,java.lang.String,com.fsck.k9.mail.Message)` -- This method is called when a message is deleted from a folder in a specified account.
- `checkMailFinished(android.content.Context,com.fsck.k9.Account)` -- The method is called when checking mail is finished for a specific account in the K-9 Mail app.
- `remoteSearchStarted(java.lang.String)` -- The method is called when a remote email search operation has started for the specified folder.
- `updateProgress(int)` -- The method updates the progress of a messaging task.
- `listFolders(com.fsck.k9.Account,java.util.List)` -- The method lists the local folders of a given email account in a Java List.
- `remoteSearchFailed(java.lang.String,java.lang.String)` -- The method is called when a remote search fails in the specified folder with the specified error message.
- `listFoldersFinished(com.fsck.k9.Account)` -- The method is called when the process of listing folders for an email account is finished.
- `sendPendingMessagesStarted(com.fsck.k9.Account)` -- The method notifies that sending of pending messages has started for a specific account.
- `accountSizeChanged(com.fsck.k9.Account,long,long)` -- The method informs the listener that the size of an email account has changed.
- `synchronizeMailboxFailed(com.fsck.k9.Account,java.lang.String,java.lang.String)` -- The method is called when synchronizing a mailbox fails and takes as input the account, folder, and error message.
- `sendPendingMessagesFailed(com.fsck.k9.Account)` -- The purpose of this method is to notify when sending pending messages has failed for a specific email account.
- `synchronizeMailboxFinished(com.fsck.k9.Account,java.lang.String,int,int)` -- The method is called when mailbox synchronization is finished and provides information about the current state of the mailbox.
- `accountStatusChanged(com.fsck.k9.BaseAccount,com.fsck.k9.AccountStats)` -- The method is called when the status of an email account has changed, providing the account and its statistics.
- `listLocalMessagesAddMessages(com.fsck.k9.Account,java.lang.String,java.util.List)` -- The method adds a list of local messages to the specified folder for a given email account.
- `pendingCommandStarted(com.fsck.k9.Account,java.lang.String)` -- The method is called when a command has started processing and is pending completion.

## interface `com.fsck.k9.controller.MessagingController$MessageActor`

The purpose of the interface `com.fsck.k9.controller.MessagingController$MessageActor` in Java is to define a method to perform an action on a list of local messages within a specific local folder of a K-9 email account.

This class contains the following public method(s):

- `act(com.fsck.k9.Account,com.fsck.k9.mailstore.LocalFolder,java.util.List)` -- The purpose of the method is to perform an action on a list of local messages within a specific local folder of a K-9 email account.

## class `com.fsck.k9.controller.MessagingControllerCommands$PendingAppend`

The class `com.fsck.k9.controller.MessagingControllerCommands$PendingAppend` is used to create and execute the process of appending a pending message to an email folder for a specified email account.

This class contains the following public method(s):

- `getCommandName()` -- This method returns the command name for pending append to a message.
- `create(java.lang.String,java.lang.String)` -- The method creates a new instance of `PendingAppend` with the given folder name and UID.
- `execute(com.fsck.k9.controller.MessagingController,com.fsck.k9.Account)` -- This method executes the process of appending a pending message to the email folder using the given messaging controller for the specified email account.

## class `com.fsck.k9.controller.MessagingController$Command`

The class `com.fsck.k9.controller.MessagingController$Command` is a command object used by the messaging controller in the K9 email client, used to define and execute various email-related tasks.

This class contains the following public method(s):

- `compareTo(com.fsck.k9.controller.MessagingController$Command)` -- The method compares the priority of two MessagingController Command objects and returns an integer value representing their order.

## class `com.fsck.k9.controller.UidReverseComparator`

The purpose of the class `com.fsck.k9.controller.UidReverseComparator` is to provide a comparator that can be used to sort email messages in reverse order based on their UID.

This class contains the following public method(s):

- `compare(com.fsck.k9.mail.Message,com.fsck.k9.mail.Message)` -- The method compares two email messages by their UID and returns the reverse order.

## class `com.fsck.k9.controller.MessagingController`

The purpose of the `com.fsck.k9.controller.MessagingController` class is to manage email messages and their associated metadata, synchronize email between a device and remote servers, and notify listeners of changes in email accounts.

This class contains the following public method(s):

- `getAccountStats(android.content.Context,com.fsck.k9.Account,com.fsck.k9.controller.MessagingListener)` -- This method gets the statistics for an email account and notifies a listener of any changes.
- `copyMessage(com.fsck.k9.Account,java.lang.String,com.fsck.k9.activity.MessageReference,java.lang.String)` -- Copy a single email message from a source folder to a destination folder for a particular email account.
- `listFoldersSynchronous(com.fsck.k9.Account,boolean,com.fsck.k9.controller.MessagingListener)` -- This method lists folders that are available both locally and remotely for a given email account.
- `getPushers()` -- This method returns a collection of pushers used for message synchronization in the K9 email client.
- `getId(com.fsck.k9.mail.Message)` -- This method returns the ID of a given message object, which is either the database ID of the object if it is a LocalMessage, or a constant value indicating an invalid ID.
- `isCopyCapable(com.fsck.k9.activity.MessageReference)` -- The method checks if a message can be copied.
- `moveMessage(com.fsck.k9.Account,java.lang.String,com.fsck.k9.activity.MessageReference,java.lang.String)` -- The method moves a single message from a source folder to a destination folder within a specified email account.
- `copyMessagesInThread(com.fsck.k9.Account,java.lang.String,java.util.List,java.lang.String)` -- The method copies a list of messages within a thread from one folder to another folder in a given account.
- `isCopyCapable(com.fsck.k9.Account)` -- The method checks if a given email account is capable of copying messages between the local and remote stores.
- `recreate(com.fsck.k9.Account,com.fsck.k9.controller.MessagingListener)` -- The method is used to recreate a particular email account's local store and update its size and status.
- `checkMail(android.content.Context,com.fsck.k9.Account,boolean,boolean,com.fsck.k9.controller.MessagingListener)` -- The purpose of this method is to check email for one or multiple accounts.
- `debugClearMessagesLocally(java.util.List)` -- This method clears the data of locally stored messages for debugging purposes only.
- `expunge(com.fsck.k9.Account,java.lang.String)` -- The method expunges messages marked for deletion in a specific folder for a given email account.
- `markAllMessagesRead(com.fsck.k9.Account,java.lang.String)` -- The method marks all messages in the given folder as read for the specified account.
- `setupPushing(com.fsck.k9.Account)` -- This method sets up the pushing of mail from an account's remote store to the device.
- `getSearchAccountStatsSynchronous(com.fsck.k9.search.SearchAccount,com.fsck.k9.controller.MessagingListener)` -- This method retrieves statistics for a given search account synchronously and notifies a listener with the updated account status.
- `deleteMessage(com.fsck.k9.activity.MessageReference,com.fsck.k9.controller.MessagingListener)` -- The method deletes a specific message and notifies the messaging listener of the deletion.
- `getCheckMailListener()` -- This method returns a listener for checking email in the MessagingController class.
- `setFlagForThreads(com.fsck.k9.Account,java.util.List,com.fsck.k9.mail.Flag,boolean)` -- The method sets a flag for a list of email threads both in cache and on the server asynchronously.
- `loadSearchResults(com.fsck.k9.Account,java.lang.String,java.util.List,com.fsck.k9.controller.MessagingListener)` -- This method loads search results for a given email account and folder, using local and remote stores, and notifies a listener of the progress.
- `saveDraft(com.fsck.k9.Account,com.fsck.k9.mail.Message,long,boolean)` -- The method saves a draft message for a given account and returns the corresponding message object from the local store.
- `isMoveCapable(com.fsck.k9.activity.MessageReference)` -- The method checks if a message can be moved by verifying that its UID does not start with a specific prefix.
- `sendAlternate(android.content.Context,com.fsck.k9.Account,com.fsck.k9.mailstore.LocalMessage)` -- The method sends an alternate version of a message as an email using the default email application on an Android device.
- `getListeners(com.fsck.k9.controller.MessagingListener)` -- This method returns a set of messaging listeners including the provided listener if not null.
- `deleteMessages(java.util.List,com.fsck.k9.controller.MessagingListener)` -- This method deletes a list of messages from a specified folder in the background, notifying a listener when the operation is complete.
- `isMoveCapable(com.fsck.k9.Account)` -- The method checks if both the local and remote stores for a given email account are capable of moving messages.
- `systemStatusChanged()` -- The method notifies all the listeners that the system status has changed.
- `searchLocalMessages(com.fsck.k9.search.LocalSearch,com.fsck.k9.controller.MessagingListener)` -- The method searches for messages in any local account that match a given query and reports the results to a messaging listener.
- `cancelNotificationForMessage(com.fsck.k9.Account,com.fsck.k9.activity.MessageReference)` -- The method cancels the notification for a specific message received by a specific email account.
- `setCheckMailListener(com.fsck.k9.controller.MessagingListener)` -- The method sets the listener for checking new mail and adds or removes it from the list of listeners accordingly.
- `listFolders(com.fsck.k9.Account,boolean,com.fsck.k9.controller.MessagingListener)` -- This method lists the locally and remotely available folders for a given email account.
- `removeListener(com.fsck.k9.controller.MessagingListener)` -- The method removes a messaging listener from the list of listeners.
- `sendPendingMessages(com.fsck.k9.Account,com.fsck.k9.controller.MessagingListener)` -- The method attempts to send any messages sitting in the outbox of a given email account.
- `compact(com.fsck.k9.Account,com.fsck.k9.controller.MessagingListener)` -- This method performs a background task to compact the storage of a specific email account and notify listeners of the change in account size.
- `messagesArrived(com.fsck.k9.Account,com.fsck.k9.mail.Folder,java.util.List,boolean)` -- This method handles the arrival of new email messages for a given account and folder.
- `deleteAccount(com.fsck.k9.Account)` -- The method deletes an email account by removing its associated notifications and removing the account from the messaging listener.
- `loadMessageRemote(com.fsck.k9.Account,java.lang.String,java.lang.String,com.fsck.k9.controller.MessagingListener)` -- The method asynchronously loads a message from a remote server for a given account and folder, and notifies a listener upon completion.
- `clearFolder(com.fsck.k9.Account,java.lang.String,com.fsck.k9.activity.ActivityListener)` -- The purpose of this method is to clear the specified folder of all messages for the provided email account.
- `getFolderUnreadMessageCount(com.fsck.k9.Account,java.lang.String,com.fsck.k9.controller.MessagingListener)` -- This method retrieves the number of unread messages in a specific folder of an email account and notifies a listener of the updated status.
- `addListener(com.fsck.k9.controller.MessagingListener)` -- This method adds a messaging listener to the list of listeners and refreshes the new listener with the current state of the messaging controller.
- `loadMessage(com.fsck.k9.Account,java.lang.String,java.lang.String)` -- This method loads a local email message from a specified folder and marks it as read.
- `setFlag(com.fsck.k9.Account,java.util.List,com.fsck.k9.mail.Flag,boolean)` -- This method sets a specific flag on one or more messages within an email account.
- `refreshListener(com.fsck.k9.controller.MessagingListener)` -- (no description)
- `deleteDraft(com.fsck.k9.Account,long)` -- This method deletes a draft message from the drafts folder of a specified email account.
- `loadMoreMessages(com.fsck.k9.Account,java.lang.String,com.fsck.k9.controller.MessagingListener)` -- This method loads more messages from the specified email account and folder, increasing the visible limit of the folder if applicable.
- `moveMessagesInThread(com.fsck.k9.Account,java.lang.String,java.util.List,java.lang.String)` -- The method moves a group of messages in a thread from a source folder to a destination folder for a given email account.
- `searchRemoteMessages(java.lang.String,java.lang.String,java.lang.String,java.util.Set,java.util.Set,com.fsck.k9.controller.MessagingListener)` -- The purpose of `searchRemoteMessages` is to search for email messages on a remote server based on specified criteria and notify a listener when the search is complete.
- `emptyTrash(com.fsck.k9.Account,com.fsck.k9.controller.MessagingListener)` -- The `emptyTrash` method in `com.fsck.k9.controller.MessagingController` is used to delete all messages from the specified email account's trash folder.
- `sendMessage(com.fsck.k9.Account,com.fsck.k9.mail.Message,com.fsck.k9.controller.MessagingListener)` -- The purpose of this method is to store a message in the Outbox of an email account and attempt to send it.
- `notifyUserIfCertificateProblem(com.fsck.k9.Account,java.lang.Exception,boolean)` -- The purpose of this method is to notify the user if there is a problem with the certificate during email communication.
- `loadMessageRemotePartial(com.fsck.k9.Account,java.lang.String,java.lang.String,com.fsck.k9.controller.MessagingListener)` -- This method loads a partially downloaded message from a remote server for a specified account, folder and message ID and notifies the MessagingListener.
- `loadAttachment(com.fsck.k9.Account,com.fsck.k9.mailstore.LocalMessage,com.fsck.k9.mail.Part,com.fsck.k9.controller.MessagingListener)` -- This method loads an email attachment from a remote server and adds it to a local message, while updating a progress listener and notifying the user in case of error.
- `clearAllPending(com.fsck.k9.Account)` -- The purpose of the method is to clear all pending commands for a given email account.
- `synchronizeMailbox(com.fsck.k9.Account,java.lang.String,com.fsck.k9.controller.MessagingListener,com.fsck.k9.mail.Folder)` -- The method starts a background synchronization of a specified email folder for a given account and notifies the provided listener of the progress.
- `moveMessages(com.fsck.k9.Account,java.lang.String,java.util.List,java.lang.String)` -- The `moveMessages` method moves a list of messages from one folder to another folder for a specific email account.
- `stopAllPushing()` -- The method stops all pushers associated with a message controller.
- `copyMessages(com.fsck.k9.Account,java.lang.String,java.util.List,java.lang.String)` -- This method copies a list of messages from a source folder to a destination folder for a given email account.
- `getInstance(android.content.Context)` -- The method returns a singleton instance of the `MessagingController` class for the provided application context.
- `setFlag(com.fsck.k9.Account,java.lang.String,java.lang.String,com.fsck.k9.mail.Flag,boolean)` -- This method sets or removes a flag for a message referenced by message UID in a given folder for a specified account.
- `setFlag(com.fsck.k9.Account,java.lang.String,java.util.List,com.fsck.k9.mail.Flag,boolean)` -- The `setFlag()` method changes the flag state of a set of messages in a specific folder for a given account.
- `cancelNotificationsForAccount(com.fsck.k9.Account)` -- This method cancels (clears) new mail notification associated with a specific email account.
- `deleteThreads(java.util.List)` -- This method deletes all threads containing the specified messages.
- `sendPendingMessages(com.fsck.k9.controller.MessagingListener)` -- The method sends pending messages for all available accounts using a given messaging listener.
- `clear(com.fsck.k9.Account,com.fsck.k9.controller.MessagingListener)` -- The method clears all messages from a specific account and updates the account's statistics.
- `getListeners()` -- This method returns a set of all registered MessagingListeners for the MessagingController instance.
- `clearCertificateErrorNotifications(com.fsck.k9.Account,com.fsck.k9.activity.setup.AccountSetupCheckSettings$CheckDirection)` -- The method clears certificate error notifications for a given email account in a given direction (incoming or outgoing).
- `getSearchAccountStats(com.fsck.k9.search.SearchAccount,com.fsck.k9.controller.MessagingListener)` -- This method asynchronously retrieves search statistics for a specific account and notifies a listener when it completes.

## class `com.fsck.k9.controller.MessagingControllerCommands$PendingExpunge`

The purpose of the class is to provide methods for creating and executing pending expunge commands on a messaging controller with a specified account.

This class contains the following public method(s):

- `getCommandName()` -- The purpose of the method is to return the expunge command name.
- `create(java.lang.String)` -- This static method creates a new instance of the `PendingExpunge` class with the specified folder name.
- `execute(com.fsck.k9.controller.MessagingController,com.fsck.k9.Account)` -- This method executes a pending expunge operation on a messaging controller with a specified account.

## class `com.fsck.k9.controller.MessagingControllerCommands$PendingSetFlag`

The purpose of the class is to manage pending message flag settings for a given account and messaging controller.

This class contains the following public method(s):

- `create(java.lang.String,boolean,com.fsck.k9.mail.Flag,java.util.List)` -- The method creates a new instance of `PendingSetFlag` class with specified folder, new state, mail flag and UIDs.
- `getCommandName()` -- The method returns a string constant that represents the command to set a flag in a message.
- `execute(com.fsck.k9.controller.MessagingController,com.fsck.k9.Account)` -- This method executes the pending message flag setting for the given account and messaging controller.


# package `com.fsck.k9.crypto`

The overall purpose of the package `com.fsck.k9.crypto` is to provide cryptographic functionalities for the K-9 Mail app, including detection of cryptographic structures in email messages and helper methods for working with OpenPGP encryption.

This package contains the following class(es):

## class `com.fsck.k9.crypto.MessageCryptoStructureDetector`

The purpose of `com.fsck.k9.crypto.MessageCryptoStructureDetector` is to detect the cryptographic structure of email messages, including whether they are encrypted or signed using OpenPGP, multipart encryption formats, or inline PGP encryption.

This class contains the following public method(s):

- `findPrimaryEncryptedOrSignedPart(com.fsck.k9.mail.Part,java.util.List)` -- The method finds the primary encrypted or signed part of a mail and returns it, or returns null if none is found.
- `getSignatureData(com.fsck.k9.mail.Part)` -- This method extracts signature data from an email message.
- `isMultipartSignedOpenPgpProtocol(com.fsck.k9.mail.Part)` -- The method determines if a MIME part is a multipart/signed protocol using OpenPGP and returns a boolean value accordingly.
- `isPartPgpInlineEncrypted(com.fsck.k9.mail.Part)` -- The method checks if a given email part is encrypted with PGP in inline mode.
- `findMultipartEncryptedParts(com.fsck.k9.mail.Part)` -- The method finds all parts of a multipart email that are encrypted and returns them as a list.
- `isMultipartEncryptedOpenPgpProtocol(com.fsck.k9.mail.Part)` -- This method checks whether a given email message part is encrypted using the OpenPGP protocol.
- `isPartMultipartEncrypted(com.fsck.k9.mail.Part)` -- The method checks whether a given email part is encrypted using a multipart encryption format.
- `findMultipartSignedParts(com.fsck.k9.mail.Part,com.fsck.k9.ui.crypto.MessageCryptoAnnotations)` -- The purpose of this method is to find all parts of a signed email message.
- `findPgpInlineParts(com.fsck.k9.mail.Part)` -- The method is used to find all PGP encrypted or signed parts within a given email message.

## class `com.fsck.k9.crypto.OpenPgpApiHelper`

The purpose of the class `com.fsck.k9.crypto.OpenPgpApiHelper` is to provide helper methods for working with OpenPGP encryption in the K-9 Mail app, including building user IDs in the correct format.

This class contains the following public method(s):

- `buildUserId(com.fsck.k9.Identity)` -- This method creates a string representation of an email address that includes the display name and email address in the format required by the OpenPgp API.


# package `com.fsck.k9.fragment`

The `com.fsck.k9.fragment` package contains classes and interfaces related to displaying and managing email messages in the K-9 Mail app, including fragment classes for displaying lists of messages, comparators for sorting and managing messages, and dialogs for displaying progress updates and confirmation prompts.

This package contains the following class(es):

## class `com.fsck.k9.fragment.MessageListFragment`

The purpose of the class `com.fsck.k9.fragment.MessageListFragment` is to display a list of email messages and provide functionality for managing and interacting with those messages, such as sorting, selecting, and performing actions like archiving or deleting.

This class contains the following public method(s):

- `dialogCancelled(int)` -- The method handles the cancellation of a dialog by calling `doNegativeClick()` with the dialog's ID.
- `onCreateView(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle)` -- This method creates and returns the fragment's root view, inflating it from the XML layout and initializing its components.
- `onSwipeRightToLeft(android.view.MotionEvent,android.view.MotionEvent)` -- The method handles a right-to-left swipe gesture as an un-select in a message list fragment.
- `onContextItemSelected(android.view.MenuItem)` -- This method handles the selection of items in the context menu for a message list and performs various actions based on the selected item.
- `isFirst(com.fsck.k9.activity.MessageReference)` -- This method checks if a given message reference is the first item in the message list or if the message list is empty.
- `isOutbox()` -- This method checks if the current folder being displayed is the outbox folder for the email account.
- `onMoveUp()` -- The purpose of this method is to scroll the message list up by one position.
- `onCreate(android.os.Bundle)` -- The purpose of this method is to initialize the MessageListFragment by setting preferences, messaging controller, preview lines, checkboxes, stars, contact picture loader (if enabled), restoring instance state, decoding arguments, creating a cache broadcast receiver, and setting initialized to true.
- `onAttach(android.app.Activity)` -- This method is used to attach the fragment to its parent activity, set the context, and check if the activity implements the required listener interface.
- `onCycleSort()` -- The `onCycleSort()` method cycles through the available sort types for email messages and changes the current sort type to the next one in the array.
- `isLoadFinished()` -- This method checks if all cursors have finished loading data.
- `isCheckMailSupported()` -- The method checks whether checking mail is supported based on whether there are multiple accounts, single account with multiple folders, or remote folder.
- `isMarkAllAsReadSupported()` -- The method returns a boolean value indicating whether marking all messages as read is supported when in single account and single folder mode.
- `openPrevious(com.fsck.k9.activity.MessageReference)` -- This method opens the previous message in the message list fragment based on the provided message reference.
- `selectAll()` -- The method selects all items in the message list.
- `onActivityCreated(android.os.Bundle)` -- This method initializes and sets up the message list and cursor loader for the MessageListFragment.
- `confirmMarkAllAsRead()` -- The purpose of this method is to either show a confirmation dialog or mark all unread messages in the list as read based on the user's preference.
- `onItemClick(android.widget.AdapterView,android.view.View,int,long)` -- This method handles the click event on the items in the message list and performs actions based on the clicked item.
- `onActivityResult(int,int,android.content.Intent)` -- The method handles the result of choosing a folder to move or copy a list of selected email messages to.
- `isManualSearch()` -- The method returns whether the search is a manual search or not, for the MessageListFragment.
- `onDestroyView()` -- The method saves the state of the list view before the fragment is destroyed.
- `onSearchRequested()` -- This method initiates a search for messages in the current folder of the specified email account.
- `newInstance(com.fsck.k9.search.LocalSearch,boolean,boolean)` -- The method creates a new instance of the `MessageListFragment` class with the specified search query, thread display setting, and threaded list setting.
- `onLoaderReset(android.content.Loader)` -- This method is called when a loader is being reset, and it clears the selected items and adapts the cursor to null.
- `isSingleAccountMode()` -- This method returns whether the fragment is currently displaying messages from a single email account.
- `onLoadFinished(android.content.Loader,android.database.Cursor)` -- The `onLoadFinished` method is responsible for handling and displaying the loaded data in the message list.
- `onCompose()` -- The method opens a new email composition window either for a single account or for any account if no account is selected.
- `openNext(com.fsck.k9.activity.MessageReference)` -- The method opens the next message in the list, if it exists, based on the given message reference.
- `checkMail()` -- The purpose of the `checkMail()` method is to check for new emails and synchronize the mailbox for the selected account/folder or all accounts.
- `doPositiveClick(int)` -- This method handles positive clicks on various confirmation dialogs related to spam, deletion, and marking all messages as read in a message list fragment.
- `onOptionsItemSelected(android.view.MenuItem)` -- The method handles clicks on options in the message list fragment menu, such as changing the message sorting or selecting all messages.
- `onRemoteSearch()` -- The purpose of this method is to initiate a remote search for messages, but only if there is an internet connection available.
- `isLast(com.fsck.k9.activity.MessageReference)` -- This method determines whether a given message reference is the last item in the message list adapter for the fragment.
- `onCreateLoader(int,android.os.Bundle)` -- This method creates a loader to load a list of email messages based on search conditions and account preferences.
- `onPause()` -- The `onPause()` method unregisters a broadcast receiver, pauses the activity listener and removes a listener from the messaging controller.
- `isRemoteSearch()` -- The method returns a boolean indicating whether a remote search has been performed or not.
- `onSwipeLeftToRight(android.view.MotionEvent,android.view.MotionEvent)` -- The method handles a left-to-right swipe gesture as a select gesture in the message list.
- `setActiveMessage(com.fsck.k9.activity.MessageReference)` -- This method marks a message as the current "active" message, updating the UI to reflect this change.
- `onReverseSort()` -- The `onReverseSort()` method changes the sorting order of the messages to the opposite direction of the current sorting order.
- `onResume()` -- The `onResume()` method refreshes messages for the currently open folder to update unread message count and read status.
- `isAccountExpungeCapable()` -- This method checks if the email account associated with this fragment is capable of permanently deleting messages (expunging).
- `isRemoteSearchAllowed()` -- The method checks if remote search is allowed for the current account and folder in order to determine if a search should be performed locally or remotely.
- `onToggleFlagged()` -- The method toggles the "flagged" status of a message in the message list.
- `toggleMessageSelect()` -- The method toggles the selection of a message in the message list.
- `isSingleFolderMode()` -- The method returns whether the fragment is in single folder mode or not.
- `onSendPendingMessages()` -- The `onSendPendingMessages()` method triggers the sending of all pending messages for the given account.
- `onCopy()` -- The method copies the selected message.
- `doNegativeClick(int)` -- The method is used to handle negative button clicks on spam or delete confirmation dialogs and sets the active messages reference to null if necessary.
- `isRemoteFolder()` -- The method determines if the current folder is a remote folder based on certain conditions including account type and folder name.
- `onCreateContextMenu(android.view.ContextMenu,android.view.View,android.view.ContextMenu.ContextMenuInfo)` -- This method is used to create and populate a context menu based on the selected message in the message list.
- `changeSort(com.fsck.k9.Account$SortType)` -- The method changes the sorting order of a list of messages based on the chosen sort type.
- `onMoveDown()` -- The purpose of the method `onMoveDown()` is to move the selection down one item in the `listView`.
- `updateTitle()` -- The purpose of this method is to update the title and progress bar of the window based on whether a manual search is being performed or not.
- `updateFooter(java.lang.String)` -- This method updates the footer text in the message list fragment.
- `onMove()` -- This method is called when a message is moved, and it selects the moved message and calls the `onMove()` method with the selected message as a parameter.
- `onStop()` -- The `onStop()` method in `MessageListFragment` cleans up any remote search in progress and fixes a bug related to the `swipeRefreshLayout` before stopping the fragment.
- `onToggleRead()` -- The purpose of the `onToggleRead()` method is to toggle the read status of a message.
- `onSaveInstanceState(android.os.Bundle)` -- The method saves the selected messages, current list state, and various fragment states into a Bundle.
- `isInitialized()` -- The method returns a boolean indicating whether the MessageListFragment has been initialized.
- `onArchive()` -- The method archives the selected email message.
- `onExpunge()` -- The purpose of the method is to call `onExpunge()` on the current folder of the account, if it exists.
- `onDelete()` -- The purpose of the method is to delete the selected message(s) from the message list.

## class `com.fsck.k9.fragment.MessageListFragmentComparators$SenderComparator`

The purpose of the class `com.fsck.k9.fragment.MessageListFragmentComparators$SenderComparator` is to provide a way to compare the sender address of messages displayed in a message list in the K-9 email client.

This class contains the following public method(s):

- `compare(android.database.Cursor,android.database.Cursor)` -- The purpose of this method is to compare the sender address of two given `Cursor` objects and return an integer value indicating their relative ordering.

## class `com.fsck.k9.fragment.ProgressDialogFragment`

The class `com.fsck.k9.fragment.ProgressDialogFragment` is used to create and display a progress dialog with customizable title and message in an Android app.

This class contains the following public method(s):

- `onCancel(android.content.DialogInterface)` -- This method cancels the progress dialog and calls the onCancel callback of the CancelListener interface if the activity implements it.
- `onCreateDialog(android.os.Bundle)` -- This method creates and returns a progress dialog containing a specified title and message.
- `newInstance(java.lang.String,java.lang.String)` -- This method creates a new instance of ProgressDialogFragment with specified title and message arguments.

## class `com.fsck.k9.fragment.AttachmentDownloadDialogFragment`

The `com.fsck.k9.fragment.AttachmentDownloadDialogFragment` class is responsible for displaying a progress dialog for downloading email attachments in the K-9 Mail app.

This class contains the following public method(s):

- `onDestroyView()` -- The `onDestroyView()` method removes a messaging listener from the messaging controller before calling the parent class's `onDestroyView()` method.
- `onCreateDialog(android.os.Bundle)` -- This method creates and displays a progress dialog for downloading email attachments.
- `onCancel(android.content.DialogInterface)` -- The method is called when the dialog is canceled by the user, and it notifies the activity listening for cancellation, if any.
- `newInstance(int,java.lang.String)` -- The method creates a new instance of `AttachmentDownloadDialogFragment` with the size and message arguments set.

## class `com.fsck.k9.fragment.MessageListFragmentComparators$ArrivalComparator`

The class serves as a comparator for messages based on their arrival time, used for sorting messages in the K9 email client's message list.

This class contains the following public method(s):

- `compare(android.database.Cursor,android.database.Cursor)` -- This method compares the arrival time of two messages represented by their respective database cursors.

## interface `com.fsck.k9.fragment.ProgressDialogFragment$CancelListener`

The purpose of the interface `com.fsck.k9.fragment.ProgressDialogFragment$CancelListener` is to provide a callback method that will be invoked when the progress dialog is canceled.

This class contains the following public method(s):

- `onProgressCancel(com.fsck.k9.fragment.ProgressDialogFragment)` -- This method is called when the progress dialog is canceled.

## class `com.fsck.k9.fragment.MessageListFragment$MessageListActivityListener`

The purpose of this class is to listen to events related to the message list activity in K-9 Mail, such as mailbox synchronization, folder updates, and remote searches, and update the UI accordingly.

This class contains the following public method(s):

- `synchronizeMailboxFailed(com.fsck.k9.Account,java.lang.String,java.lang.String)` -- The purpose of this method is to handle the scenario when synchronizing a mailbox fails.
- `synchronizeMailboxFinished(com.fsck.k9.Account,java.lang.String,int,int)` -- This method updates the UI once the mailbox synchronization is finished.
- `folderStatusChanged(com.fsck.k9.Account,java.lang.String,int)` -- This method updates the unread message count for a specific folder in the message list of a specific account.
- `remoteSearchFailed(java.lang.String,java.lang.String)` -- The method displays a toast message to inform the user of a failed remote search for messages in a specified folder.
- `remoteSearchStarted(java.lang.String)` -- The method is called when a remote search for messages in a specific folder has started, and it updates the UI to indicate that a query is being sent.
- `remoteSearchFinished(java.lang.String,int,int,java.util.List)` -- The method updates the UI of the message list activity after a remote search for messages has finished.
- `synchronizeMailboxStarted(com.fsck.k9.Account,java.lang.String)` -- The method is called when mailbox synchronization is started and updates the UI accordingly.
- `enableProgressIndicator(boolean)` -- Enables or disables the progress indicator in the message list activity.
- `remoteSearchServerQueryComplete(java.lang.String,int,int)` -- The method is called when a remote search for messages in a folder has completed and updates the UI with the results.
- `informUserOfStatus()` -- The purpose of the method is to refresh the title displayed to the user.

## class `com.fsck.k9.fragment.MessageListAdapter`

The purpose of the class `com.fsck.k9.fragment.MessageListAdapter` is to handle the creation and binding of views for displaying email message information in a list.

This class contains the following public method(s):

- `newView(android.content.Context,android.database.Cursor,android.view.ViewGroup)` -- This method creates a new view for displaying a message in a list.
- `bindView(android.view.View,android.content.Context,android.database.Cursor)` -- This method binds views to data from a cursor to display email message information.

## class `com.fsck.k9.fragment.MessageListFragmentComparators$FlaggedComparator`

The purpose of this class is to provide a comparator for `Cursor` objects that sorts them based on whether they contain a flagged message or not.

This class contains the following public method(s):

- `compare(android.database.Cursor,android.database.Cursor)` -- This method compares two `Cursor` objects based on whether they contain a flagged message or not.

## class `com.fsck.k9.fragment.MessageListFragmentComparators$SubjectComparator`

The purpose of the class `com.fsck.k9.fragment.MessageListFragmentComparators$SubjectComparator` is to compare the subjects extracted from two database cursors lexicographically.

This class contains the following public method(s):

- `compare(android.database.Cursor,android.database.Cursor)` -- This method compares two subjects extracted from two database cursors and returns -1, 0, or 1 based on their lexicographical order.

## class `com.fsck.k9.fragment.MessageListFragmentComparators$AttachmentComparator`

The purpose of the `com.fsck.k9.fragment.MessageListFragmentComparators$AttachmentComparator` class is to compare two message cursors based on whether or not they have attachments.

This class contains the following public method(s):

- `compare(android.database.Cursor,android.database.Cursor)` -- The `compare` method is used to compare two message cursors based on whether or not they have attachments.

## class `com.fsck.k9.fragment.MessageListFragmentComparators$UnreadComparator`

The class `com.fsck.k9.fragment.MessageListFragmentComparators$UnreadComparator` is used to compare two cursors based on whether the corresponding messages are unread or not in the K-9 Mail app.

This class contains the following public method(s):

- `compare(android.database.Cursor,android.database.Cursor)` -- The method compares two cursors based on whether the corresponding messages are unread or not.

## class `com.fsck.k9.fragment.MessageListHandler`

The purpose of the `com.fsck.k9.fragment.MessageListHandler` class is to handle messages related to the Message list fragment in the K-9 mail application, such as updating the UI, loading folders, and handling user interactions.

This class contains the following public method(s):

- `folderLoading(java.lang.String,boolean)` -- The method sends a message to the MessageListHandler indicating whether a folder is being loaded or not.
- `updateFooter(java.lang.String)` -- The method updates the footer of the message list fragment with the given message.
- `remoteSearchFinished()` -- The `remoteSearchFinished()` method sends a message to the handler to indicate that a remote search has finished.
- `goBack()` -- The purpose of this method is to send a message to the handler to trigger going back to the previous message list.
- `refreshTitle()` -- The `refreshTitle()` method sends a message to refresh the title of the message list.
- `restoreListPosition()` -- This method restores the position of the message list in a fragment.
- `openMessage(com.fsck.k9.activity.MessageReference)` -- This method opens a message specified by a message reference.
- `handleMessage(android.os.Message)` -- This method handles messages received by the MessageListHandler and performs different actions based on the message type.
- `progress(boolean)` -- The method updates the progress indicator in the user interface with the supplied boolean value.

## interface `com.fsck.k9.fragment.AttachmentDownloadDialogFragment$AttachmentDownloadCancelListener`

The interface is used to define a listener for cancel events during attachment downloads in the `AttachmentDownloadDialogFragment` fragment.

This class contains the following public method(s):

- `onProgressCancel(com.fsck.k9.fragment.AttachmentDownloadDialogFragment)` -- The method is called when the user cancels the download progress of an attachment in the fragment.

## class `com.fsck.k9.fragment.ConfirmationDialogFragment`

The class `com.fsck.k9.fragment.ConfirmationDialogFragment` is designed to create and handle confirmation dialogs for the K-9 Mail application.

This class contains the following public method(s):

- `onClick(android.content.DialogInterface,int)` -- The method handles positive, negative, and neutral button clicks in a confirmation dialog and calls the appropriate listener method.
- `newInstance(int,java.lang.String,java.lang.String,java.lang.String,java.lang.String)` -- This method creates a new instance of the ConfirmationDialogFragment with specified parameters.
- `onAttach(android.app.Activity)` -- The `onAttach` method is used to attach the current fragment to an activity and set up a listener for confirmation dialog events.
- `newInstance(int,java.lang.String,java.lang.String,java.lang.String)` -- This method returns a new instance of the `ConfirmationDialogFragment` class with specified parameters.
- `onCreateDialog(android.os.Bundle)` -- The method creates a dialog with the specified title, message, and button text and returns the created dialog.
- `onCancel(android.content.DialogInterface)` -- The method is called when the confirmation dialog is canceled, and it notifies the listener that the dialog has been cancelled.

## class `com.fsck.k9.fragment.MessageViewHolder`

The purpose of the class `com.fsck.k9.fragment.MessageViewHolder` is to hold views and provide a way to handle clicks on specific views within a message view holder.

This class contains the following public method(s):

- `onClick(android.view.View)` -- This method handles clicks on specific views within a message view holder and triggers actions based on which view was clicked.

## class `com.fsck.k9.fragment.MessageListFragmentComparators$ComparatorChain`

The purpose of the class `com.fsck.k9.fragment.MessageListFragmentComparators$ComparatorChain` is to allow multiple comparators to be chained together for use in sorting lists of messages in the K-9 email client app.

This class contains the following public method(s):

- `compare(java.lang.Object,java.lang.Object)` -- The method compares two objects using multiple comparators in a chain until a non-equal comparison is found.

## interface `com.fsck.k9.fragment.ConfirmationDialogFragment$ConfirmationDialogFragmentListener`

The purpose of this interface is to provide a way for a Confirmation Dialog Fragment to communicate button click events to its parent Fragment or Activity.

This class contains the following public method(s):

- `doNegativeClick(int)` -- The method is called when the user clicks on the negative button of a confirmation dialog and passes the ID of the dialog as a parameter.
- `dialogCancelled(int)` -- This method is called when a confirmation dialog is cancelled by the user.
- `doPositiveClick(int)` -- To handle positive button clicks on a Confirmation Dialog Fragment with the given dialog ID.

## class `com.fsck.k9.fragment.MessageListFragmentComparators$DateComparator`

The class `com.fsck.k9.fragment.MessageListFragmentComparators$DateComparator` provides a comparator for sorting database Cursors based on the value of the `DATE_COLUMN` field.

This class contains the following public method(s):

- `compare(android.database.Cursor,android.database.Cursor)` -- The method compares two `Cursor` objects based on the value of the `DATE_COLUMN` field and returns an integer indicating their relative order.

## class `com.fsck.k9.fragment.MessageListFragmentComparators$ReverseIdComparator`

The purpose of the class is to provide a comparator for android.database.Cursor objects based on their "_id" column values in reverse order.

This class contains the following public method(s):

- `compare(android.database.Cursor,android.database.Cursor)` -- The method compares two cursors based on their "_id" column values in reverse order.

## interface `com.fsck.k9.fragment.MessageListFragment$MessageListFragmentListener`

The purpose of the interface `com.fsck.k9.fragment.MessageListFragment$MessageListFragmentListener` is to provide a listener for events in the message list fragment of an email application, such as updating the menu, navigating between messages, and initiating searches.

This class contains the following public method(s):

- `updateMenu()` -- The method updates the menu of the MessageListFragment.
- `setUnreadCount(int)` -- The method sets the number of unread messages in the message list.
- `setMessageListTitle(java.lang.String)` -- The purpose of the method is to set the title of the message list of a fragment in an email application.
- `onForward(com.fsck.k9.activity.MessageReference)` -- The purpose of the method is to trigger a forward action for a given email message.
- `startSearch(com.fsck.k9.Account,java.lang.String)` -- The method is used to initiate a search for messages in a specified folder of a specified email account.
- `onReplyAll(com.fsck.k9.activity.MessageReference)` -- The method handles when the user clicks on the "Reply All" button for a specific email message.
- `showThread(com.fsck.k9.Account,java.lang.String,long)` -- The method is used to display the entire thread of an email conversation.
- `showMoreFromSameSender(java.lang.String)` -- The purpose of the method is to display more messages from the same sender with the given sender address.
- `enableActionBarProgress(boolean)` -- The purpose of the method is to enable or disable the progress indicator in the action bar.
- `setMessageListProgress(int)` -- Sets the progress level for the message list.
- `goBack()` -- The method is used to navigate back to the previous screen or fragment in the message list.
- `remoteSearchStarted()` -- The method notifies the listener that a remote search has been started.
- `setMessageListSubTitle(java.lang.String)` -- The method sets the subtitle for the message list in a K9 email client fragment.
- `onResendMessage(com.fsck.k9.activity.MessageReference)` -- The method is called when a user requests to resend a previously sent message in the MessageListFragment.
- `openMessage(com.fsck.k9.activity.MessageReference)` -- This method is used to open a particular email message referenced by `messageReference`.
- `onCompose(com.fsck.k9.Account)` -- The method is called when the user wants to compose a new message in the specified email account.
- `onReply(com.fsck.k9.activity.MessageReference)` -- The method is called when the user replies to a message in the message list, with the `message` parameter representing the message being replied to.

## class `com.fsck.k9.fragment.MessageListFragment$ActionModeCallback`

The purpose of `com.fsck.k9.fragment.MessageListFragment$ActionModeCallback` is to handle user interactions with the action mode menu in a message list fragment, allowing them to perform various actions on selected messages such as marking them as read or deleting them.

This class contains the following public method(s):

- `showMarkAsRead(boolean)` -- This method shows or hides the "Mark as read" and "Mark as unread" options in the context menu based on the value of the "show" parameter.
- `onCreateActionMode(android.view.ActionMode,android.view.Menu)` -- This method inflates a menu for the contextual action mode and sets its capabilities.
- `showFlag(boolean)` -- This method shows or hides a flag and unflag action in the action mode menu.
- `showSelectAll(boolean)` -- The method is used to show or hide the select all button in the action mode.
- `onDestroyActionMode(android.view.ActionMode)` -- This method is called when an action mode is destroyed and it resets the variables used for a message list's selection state.
- `onPrepareActionMode(android.view.ActionMode,android.view.Menu)` -- This method prepares the contextual action bar by setting the menu items based on the selected messages and their account.
- `onActionItemClicked(android.view.ActionMode,android.view.MenuItem)` -- This method handles user clicks on items in the action mode menu in a message list fragment, performing various actions such as deleting, marking as read or moving messages.

## class `com.fsck.k9.fragment.MessageListFragmentComparators$ReverseComparator`

The purpose of this class is to provide a comparator that allows sorting of objects in reverse order.

This class contains the following public method(s):

- `compare(java.lang.Object,java.lang.Object)` -- This method compares two given objects in reverse order, as the arguments are intentionally switched.


# package `com.fsck.k9.helper`

The `com.fsck.k9.helper` package provides a collection of helper classes and interfaces for common tasks and operations in the K-9 Mail Android application, such as working with emails, contacts, files, and system resources.

This package contains the following class(es):

## class `com.fsck.k9.helper.MergeCursor`

The purpose of `com.fsck.k9.helper.MergeCursor` class is to create a cursor that merges data from multiple cursors based on a comparison criteria.

This class contains the following public method(s):

- `getColumnName(int)` -- This method returns the name of the column at the specified index in the currently active cursor.
- `getDouble(int)` -- The method returns the double value of the specified column from the active cursor.
- `getWantsAllOnMoveCalls()` -- This method returns whether the active cursor wants all `moveToPosition()` calls to be handled or not.
- `getCount()` -- The method returns the total number of rows across all cursors by caching the count for improved performance.
- `isBeforeFirst()` -- The method `isBeforeFirst()` returns true if the cursor is before the first row, or false otherwise.
- `getColumnIndexOrThrow(java.lang.String)` -- This method gets the index of a column or throws an exception if the column does not exist.
- `moveToPosition(int)` -- This method moves the cursor to the specified position within the merged cursor's data set.
- `moveToPrevious()` -- The `moveToPrevious()` method moves the cursor to the previous row in the merged Cursor, taking into account the order defined by the comparator.
- `moveToFirst()` -- The method moves the cursor to the first position and returns whether the move was successful.
- `isFirst()` -- The method returns true if the current cursor position is the first position in the merged cursor and there are at least one row in the cursor, otherwise returns false.
- `isClosed()` -- The method `isClosed()` checks if the active cursor in the MergeCursor object is closed.
- `getPosition()` -- The method returns the current position of the cursor.
- `move(int)` -- The `move(int)` method moves the cursor by a specified offset and returns a boolean indicating if the move was successful.
- `setNotificationUri(android.content.ContentResolver,android.net.Uri)` -- Sets a notification URI to be used to identify changes made to the cursors in the `MergeCursor` object.
- `isNull(int)` -- This method checks if the value at a given column index in the currently active cursor is null or not.
- `registerContentObserver(android.database.ContentObserver)` -- Registers a content observer to receive updates when the underlying data in each cursor changes.
- `getFloat(int)` -- This method retrieves the float value of the specified column from the active cursor.
- `respond(android.os.Bundle)` -- The method responds to extras sent to the MergeCursor, but the implementation is not yet implemented and will result in a runtime exception.
- `registerDataSetObserver(android.database.DataSetObserver)` -- Registers a DataSetObserver for each cursor in the MergeCursor object.
- `unregisterContentObserver(android.database.ContentObserver)` -- The method unregisters a given `ContentObserver` from all the cursors that are part of the `MergeCursor`.
- `getColumnIndex(java.lang.String)` -- This method returns the index of a column with the given name from the active cursor in a merged cursor.
- `setExtras(android.os.Bundle)` -- Sets the extras to be associated with the active cursor.
- `getType(int)` -- This method returns the type of the data in a specified column of the currently active cursor in the MergeCursor.
- `getShort(int)` -- This method returns a short value from the specified column index of the active cursor.
- `copyStringToBuffer(int,android.database.CharArrayBuffer)` -- Copies a string from the active cursor to a character array buffer at a specified column index.
- `getBlob(int)` -- This method returns the blob value of the specified column in the current row of the MergeCursor.
- `unregisterDataSetObserver(android.database.DataSetObserver)` -- The method unregisters the given DataSetObserver from each cursor in the MergeCursor.
- `requery()` -- The method requeries all underlying cursors in order to update the data of the MergeCursor.
- `moveToNext()` -- This method moves the cursor to the next row in the result set, merging multiple cursors based on a comparison criteria.
- `close()` -- The method closes all of the cursors associated with the MergeCursor.
- `getNotificationUri()` -- This method returns the notification URI of the cursor, which is currently not implemented and returns null.
- `getString(int)` -- This method returns the value of the specified column as a string from the active cursor.
- `getColumnNames()` -- The method returns an array of column names of the active cursor.
- `getExtras()` -- This method is not implemented and will throw a runtime exception.
- `getInt(int)` -- This method returns an integer value at a specified column index from the active cursor.
- `isAfterLast()` -- This method checks if the cursor is positioned after the last row or if there are no rows.
- `isLast()` -- This method returns whether the current position in the MergeCursor is at the last position in the cursor.
- `deactivate()` -- The method deactivates all the cursors associated with a MergeCursor object.
- `moveToLast()` -- The method moves the cursor to the last position of the merged cursor.
- `getLong(int)` -- This method returns a long value from the active cursor of a MergeCursor object at the specified column index.
- `getColumnCount()` -- This method returns the number of columns in the currently active cursor of a MergeCursor object.

## class `com.fsck.k9.helper.EmailHelper`

The purpose of `com.fsck.k9.helper.EmailHelper` is to provide a helper method to extract the domain name from an email address.

This class contains the following public method(s):

- `getDomainFromEmailAddress(java.lang.String)` -- The method returns the domain name from a given email address.

## class `com.fsck.k9.helper.IdentityHelper`

The purpose of the `com.fsck.k9.helper.IdentityHelper` class is to provide methods for handling email identities, including finding the identity that a message was sent to.

This class contains the following public method(s):

- `getRecipientIdentityFromMessage(com.fsck.k9.Account,com.fsck.k9.mail.Message)` -- The method finds the identity that a message was sent to, or returns the default identity if the recipient couldn't be determined.

## class `com.fsck.k9.helper.MergeCursorWithUniqueId`

The purpose of the class `com.fsck.k9.helper.MergeCursorWithUniqueId` is to merge two cursors, combine their unique IDs, and return a new cursor with an added unique ID column.

This class contains the following public method(s):

- `getLong(int)` -- The method retrieves a long value from a specified column of the cursor, combining it with a unique ID to create a new long value.
- `getColumnCount()` -- This method returns the number of columns in the merged cursor with an added unique ID column.
- `getColumnIndex(java.lang.String)` -- This method returns the index of a specified column name, or the index of a unique ID column if the specified column name is "_id".
- `getColumnIndexOrThrow(java.lang.String)` -- This method returns the index of the given column name, or throws an exception if the column name is invalid.

## class `com.fsck.k9.helper.UrlEncodingHelper`

The purpose of `com.fsck.k9.helper.UrlEncodingHelper` is to provide methods to encode and decode URL strings using UTF-8 encoding.

This class contains the following public method(s):

- `encodeUtf8(java.lang.String)` -- This method encodes a UTF-8 string into a URL encoded string.
- `decodeUtf8(java.lang.String)` -- The `decodeUtf8` method decodes a string that has been URL encoded using UTF-8 encoding.

## class `com.fsck.k9.helper.MessageHelper`

The class `com.fsck.k9.helper.MessageHelper` provides helper methods for getting message information, converting email addresses to a more user-friendly format, and ensuring only one instance of the class is created per context.

This class contains the following public method(s):

- `getDisplayName(com.fsck.k9.Account,com.fsck.k9.mail.Address[],com.fsck.k9.mail.Address[])` -- The method returns a display name for a message based on the account, senders, and recipients.
- `toFriendly(com.fsck.k9.mail.Address,com.fsck.k9.helper.Contacts)` -- This method returns a user-friendly name for an email address, taking into account whether the email address belongs to a contact in the specified contacts list.
- `populate(com.fsck.k9.activity.MessageInfoHolder,com.fsck.k9.mailstore.LocalMessage,com.fsck.k9.activity.FolderInfoHolder,com.fsck.k9.Account)` -- This method populates a `MessageInfoHolder` object with message information such as sender, recipient, folder, and flags from a `LocalMessage` object.
- `toMe(com.fsck.k9.Account,com.fsck.k9.mail.Address[])` -- The method checks if any of the given email addresses belong to the account owner's identity.
- `toFriendly(com.fsck.k9.mail.Address[],com.fsck.k9.helper.Contacts)` -- The `toFriendly` method converts an array of email addresses to a user-friendly format, with name and contact information, if available.
- `getInstance(android.content.Context)` -- This method returns an instance of the MessageHelper class, ensuring that only one instance is created per Context.

## class `com.fsck.k9.helper.FileHelper`

The class `com.fsck.k9.helper.FileHelper` provides various helper methods for working with files and directories, such as moving, renaming, and sanitizing filenames, creating unique files, updating file modification dates, and recursively moving directories.

This class contains the following public method(s):

- `move(java.io.File,java.io.File)` -- The `move` method moves a file from one location to another, and returns true if the move was successful, false otherwise.
- `createUniqueFile(java.io.File,java.lang.String)` -- The method creates a unique file in a given directory with the given filename by appending a hyphen and a number to it if necessary.
- `sanitizeFilename(java.lang.String)` -- The purpose of the `sanitizeFilename` method is to replace characters in a file name that are not allowed with a replacement character.
- `moveRecursive(java.io.File,java.io.File)` -- The method `moveRecursive` moves a directory from one location to another, including all subdirectories and files within it.
- `touchFile(java.io.File,java.lang.String)` -- The method creates or updates the last modification date of a file located in a specified directory.
- `renameOrMoveByCopying(java.io.File,java.io.File)` -- The method renames or moves a file by copying it to the new location if renaming fails.

## class `com.fsck.k9.helper.K9AlarmManager`

The class provides access to the Android alarm manager and a doze mode checker for managing alarms in the K-9 Mail app. It also allows cancellation of PendingIntent associated with the K9AlarmManager instance.

This class contains the following public method(s):

- `cancel(android.app.PendingIntent)` -- This method cancels a PendingIntent associated with a K9AlarmManager instance.
- `getAlarmManager(android.content.Context)` -- This method returns an instance of the K9AlarmManager class that provides access to the Android alarm manager and a doze mode checker for use in managing alarms in the K-9 Mail app.
- `set(int,long,android.app.PendingIntent)` -- (no description)

## class `com.fsck.k9.helper.UnreadWidgetProperties`

The class `com.fsck.k9.helper.UnreadWidgetProperties` provides methods to retrieve the properties of an unread email widget, such as the widget ID, folder name, and unread message count.

This class contains the following public method(s):

- `getClickIntent(android.content.Context)` -- This method returns an intent that represents the action to be taken when the widget is clicked based on the type of widget.
- `getAppWidgetId()` -- This method returns the ID of the app widget.
- `getFolderName()` -- This method returns the name of the folder configured for the K-9 Mail widget.
- `getTitle(android.content.Context)` -- The method returns the title for an unread widget based on the type of widget and the email account or folder associated with it.
- `getUnreadCount(android.content.Context)` -- This method returns the number of unread email messages for a given context, based on the account, folder, or search account.
- `getAccountUuid()` -- The method returns the unique identifier string of the email account associated with the widget properties.

## class `com.fsck.k9.helper.SizeFormatter`

The purpose of the class `com.fsck.k9.helper.SizeFormatter` is to format file sizes into a human-readable string with appropriate units and precision.

This class contains the following public method(s):

- `formatSize(android.content.Context,long)` -- The method formats a given file size into a human-readable string with appropriate units and precision.

## class `com.fsck.k9.helper.FileBrowserHelper`

The purpose of the `com.fsck.k9.helper.FileBrowserHelper` class is to provide a file browser functionality with a failover mechanism to pick a directory.

This class contains the following public method(s):

- `showFileBrowserActivity(android.app.Fragment,java.io.File,int,com.fsck.k9.helper.FileBrowserHelper$FileBrowserFailOverCallback)` -- This method opens a file browser activity to pick a directory and returns whether or not the action was successful.
- `getInstance()` -- The purpose of this method is to return a singleton instance of the `FileBrowserHelper` class.
- `showFileBrowserActivity(android.app.Activity,java.io.File,int,com.fsck.k9.helper.FileBrowserHelper$FileBrowserFailOverCallback)` -- The method attempts to open a file browser and if none exist, it shows a fallback text dialog.

## class `com.fsck.k9.helper.ParcelableUtil`

The purpose of the `ParcelableUtil` class is to provide methods for converting Parcelable objects to byte arrays and vice versa, for communication or storage purposes.

This class contains the following public method(s):

- `marshall(android.os.Parcelable)` -- This method converts a Parcelable object into a byte array for communication or storage.
- `unmarshall(byte[],android.os.Parcelable$Creator)` -- The method unmarshalls a byte array and returns an object of a specified Parcelable class.

## class `com.fsck.k9.helper.RetainFragment`

The purpose of the class `com.fsck.k9.helper.RetainFragment` is to retain an object across configuration changes in Android apps.

This class contains the following public method(s):

- `setData(java.lang.Object)` -- The method sets the data object of the RetainFragment to the given object.
- `onCreate(android.os.Bundle)` -- The purpose of the method is to set the RetainInstance flag to true in the RetainFragment class.
- `findOrCreate(android.app.FragmentManager,java.lang.String)` -- The method finds or creates a `RetainFragment` object with a given tag.
- `findOrNull(android.app.FragmentManager,java.lang.String)` -- This method finds and returns a `RetainFragment` object from a `FragmentManager` using a specified tag, or returns null if not found.
- `getData()` -- The method returns the stored data object of type T.
- `hasData()` -- The method returns whether or not the `data` variable in the `RetainFragment` class is not null.
- `clearAndRemove(android.app.FragmentManager)` -- The method clears data and removes the fragment from the FragmentManager.

## interface `com.fsck.k9.helper.FileBrowserHelper$FileBrowserFailOverCallback`

The interface serves as a callback mechanism for handling path entered by users or cancellation of input text dialog in a file browser.

This class contains the following public method(s):

- `onPathEntered(java.lang.String)` -- The method is called when the user enters a path and passes that path as a parameter to the method.
- `onCancel()` -- The method is called when the user cancels an input text dialog.

## class `com.fsck.k9.helper.MailTo`

The `com.fsck.k9.helper.MailTo` class is used for parsing and extracting information from mailto URIs, such as email addresses, subject lines, and email bodies, in order to facilitate the creation of email messages.

This class contains the following public method(s):

- `getCc()` -- The purpose of the method is to return an array of carbon copy email addresses.
- `getBody()` -- The method returns the email body of a mailto link.
- `getSubject()` -- The `getSubject()` method returns the subject of an email.
- `getBcc()` -- This method returns an array of email addresses in the Bcc field of a mailto URI.
- `getTo()` -- The method returns an array of email addresses that the email is being sent to.
- `parse(android.net.Uri)` -- This method parses a mailto URI, extracts the recipient's email address and email message details, and returns an object containing the parsed information.
- `isMailTo(android.net.Uri)` -- This method checks if the given URI is a mailto URI.

## class `com.fsck.k9.helper.Contacts`

The purpose of the `com.fsck.k9.helper.Contacts` class is to provide methods to interact with the user's contacts, such as checking if an email address belongs to one of the contacts, retrieving a contact's picture URI, creating and marking contacts as contacted, etc.

This class contains the following public method(s):

- `isInContacts(java.lang.String)` -- The method checks if a given email address belongs to one of the contacts.
- `isAnyInContacts(com.fsck.k9.mail.Address[])` -- The method checks whether any of the provided email addresses are present in the user's contacts.
- `getInstance(android.content.Context)` -- This method returns an instance of the Contacts class, which is appropriate for the device's SDK version, using the given context.
- `getPhotoUri(java.lang.String)` -- This method returns the URI for the picture of a contact with the specified email address, or null if no contact is found or the contact has no picture.
- `contactPickerIntent()` -- The purpose of the method is to create an intent to launch a contacts picker to select an email address.
- `getNameForAddress(java.lang.String)` -- This method retrieves the name of the contact associated with a given email address, or returns null if there is no matching contact.
- `createContact(com.fsck.k9.mail.Address)` -- The method creates a new contact or adds information to an existing contact given an email address.
- `markAsContacted(com.fsck.k9.mail.Address[])` -- The `markAsContacted` method marks the contacts with the provided email addresses as contacted.
- `addPhoneContact(java.lang.String)` -- The purpose of the method is to start the activity that enables users to add a phone number to an existing contact or create a new contact.

## class `com.fsck.k9.helper.SimpleTextWatcher`

The purpose of the class `com.fsck.k9.helper.SimpleTextWatcher` is to provide methods to listen to changes in an EditText field.

This class contains the following public method(s):

- `afterTextChanged(android.text.Editable)` -- (no description)
- `onTextChanged(java.lang.CharSequence,int,int,int)` -- (no description)
- `beforeTextChanged(java.lang.CharSequence,int,int,int)` -- This method is called to notify that text is about to be changed in an EditText field.

## class `com.fsck.k9.helper.ContactPicture`

The purpose of the class `com.fsck.k9.helper.ContactPicture` is to provide a method for loading contact pictures with a customizable fallback default background color.

This class contains the following public method(s):

- `getContactPictureLoader(android.content.Context)` -- This method returns a `ContactPictureLoader` object for loading contact pictures in the current context with a fallback default background color.

## class `com.fsck.k9.helper.ClipboardManager`

The purpose of the class `com.fsck.k9.helper.ClipboardManager` is to provide a convenient way to interact with the system clipboard in an Android application.

This class contains the following public method(s):

- `setText(java.lang.String,java.lang.String)` -- The method copies a text string to the system clipboard with a user-visible label.
- `getInstance(android.content.Context)` -- This method returns a new instance of the ClipboardManager class with the application context as a parameter.

## class `com.fsck.k9.helper.MailTo$CaseInsensitiveParamWrapper`

The purpose of the class is to provide a case-insensitive wrapper for storing and retrieving query parameters in email "mailto" links.

This class contains the following public method(s):

- `getQueryParameters(java.lang.String)` -- This method returns a list of query parameters (values) associated with a given query parameter name (key) in a case-insensitive manner.

## class `com.fsck.k9.helper.ReplyToParser`

The purpose of the class `com.fsck.k9.helper.ReplyToParser` is to parse the email message's reply-to, list-post, from addresses, and account identities to determine the recipients to reply to or reply all to.

This class contains the following public method(s):

- `getRecipientsToReplyTo(com.fsck.k9.mail.Message,com.fsck.k9.Account)` -- The method returns the email addresses to reply to based on the message's reply-to, list-post, from addresses and the account's identities.
- `getRecipientsToReplyAllTo(com.fsck.k9.mail.Message,com.fsck.k9.Account)` -- The method returns a list of email addresses to which a reply to all should be sent, based on the original message and the user's email account.

## class `com.fsck.k9.helper.ExceptionHelper`

The purpose of `com.fsck.k9.helper.ExceptionHelper` is to provide methods for working with Java `Throwable` objects, specifically for retrieving root cause messages.

This class contains the following public method(s):

- `getRootCauseMessage(java.lang.Throwable)` -- The `getRootCauseMessage` method retrieves the root cause message of a Java `Throwable` object.

## class `com.fsck.k9.helper.Utility`

The `com.fsck.k9.helper.Utility` class provides various utility methods that assist in performing common operations in the K-9 Mail Android application, such as checking for network connectivity, validating input fields, and extracting message identifiers from strings.

This class contains the following public method(s):

- `hasConnectivity(android.content.Context)` -- The `hasConnectivity` method checks if there is network connectivity.
- `domainFieldValid(android.widget.EditText)` -- This method checks if the input in the given EditText view is a valid DNS domain or IP address.
- `arrayContainsAny(java.lang.Object[],java.lang.Object[])` -- The method checks if any element in one array is present in another array and returns a boolean value.
- `closeQuietly(android.database.Cursor)` -- The method unconditionally closes a given Cursor, if it is non-null.
- `stripNewLines(java.lang.String)` -- The method removes all newline characters from a given multi-line string.
- `wrap(java.lang.String,int)` -- The method wraps a String to a specified line length and adds a carriage return and newline after each wrapped line.
- `wrap(java.lang.String,int,java.lang.String,boolean)` -- This method wraps a single line of text to a specified column width, inserting a specified string for new lines, and optionally wraps long words.
- `setContactForBadge(com.fsck.k9.ui.ContactBadge,com.fsck.k9.mail.Address)` -- This method assigns a contact to a badge and auto-populates the contact name if it doesn't exist for the given email address.
- `setCompoundDrawablesAlpha(android.widget.TextView,int)` -- The method is intended to set the alpha value of all compound drawables of a given TextView widget, but is currently disabled due to an issue with shared drawables in Android.
- `hasExternalImages(java.lang.String)` -- This method determines if a given content (message) contains external images by searching for "http" or "https" URI schemes in image tags.
- `combine(java.lang.Object[],char)` -- The method combines an array of objects into a single string with a given separator character.
- `requiredFieldValid(android.widget.TextView)` -- This method checks if a required field, represented by the `TextView` object, has a non-empty text value.
- `getMainThreadHandler()` -- This method returns a Handler object that is tied to the main thread.
- `extractMessageId(java.lang.String)` -- The method extracts the unique message identifier from a string.
- `isAnyMimeType(java.lang.String,java.lang.String[])` -- The method checks if a given MIME type matches any of the specified MIME types.
- `combine(java.lang.Iterable,char)` -- The `combine` method returns a string that concatenates the elements of an Iterable with a separator character.
- `extractMessageIds(java.lang.String)` -- This method extracts message ids from a given string and returns them in a list.
- `stripSubject(java.lang.String)` -- This method extracts the original subject value of an email, ignoring response and forward markers and mailing list tags, and trims the result.
- `requiredFieldValid(android.text.Editable)` -- The method checks if the given text field has input by verifying its length and returns a boolean value accordingly.
- `arrayContains(java.lang.Object[],java.lang.Object)` -- The method checks if a given array contains a particular object and returns a boolean value indicating the result.

## class `com.fsck.k9.helper.Preconditions`

The purpose of `com.fsck.k9.helper.Preconditions` is to provide methods for checking preconditions and throwing exceptions if they are not met.

This class contains the following public method(s):

- `checkNotNull(java.lang.Object)` -- The method is used to check whether a given object is null and throws a NullPointerException if it is.


# package `com.fsck.k9.helper.jsoup`

The purpose of the `com.fsck.k9.helper.jsoup` package is to provide helper classes and interfaces for traversing and filtering HTML documents using the JSoup library.

This package contains the following class(es):

## interface `com.fsck.k9.helper.jsoup.NodeFilter`

The purpose of the `com.fsck.k9.helper.jsoup.NodeFilter` interface is to provide a way to filter nodes during a traversal of a HTML document, by giving filter decisions based on callbacks triggered when nodes are visited.

This class contains the following public method(s):

- `head(org.jsoup.nodes.Node,int)` -- The method is a callback that is triggered when a node is first visited during a traversal of a HTML document and returns a filter decision.
- `tail(org.jsoup.nodes.Node,int)` -- The `tail` method is a callback that is triggered when the last descendant of a given node has been visited, providing a final decision on what to do with the node.

## class `com.fsck.k9.helper.jsoup.AdvancedNodeTraversor`

The purpose of the `com.fsck.k9.helper.jsoup.AdvancedNodeTraversor` class is to traverse and filter a `Node` and its descendant nodes in a depth-first manner using the JSoup library.

This class contains the following public method(s):

- `filter(org.jsoup.nodes.Node)` -- This method performs a depth-first filtering of a given root `Node` and its descendant nodes.


# package `com.fsck.k9.mailstore`

The Java package `com.fsck.k9.mailstore` provides classes and interfaces for managing email storage, including local storage implementation, attachments, and database operations, in the K-9 Mail email client.

This package contains the following class(es):

## class `com.fsck.k9.mailstore.StorageManager$SamsungGalaxySStorageProvider`

The class provides a way to retrieve the name and ID of the storage provider specific to Samsung Galaxy S devices in the context of a mailstore in the K-9 email client.

This class contains the following public method(s):

- `getName(android.content.Context)` -- The method returns the name of the storage provider specific to Samsung Galaxy S devices.
- `getId()` -- This method returns the ID of the Samsung Galaxy S storage provider.

## class `com.fsck.k9.mailstore.StorageManager$ExternalStorageProvider`

The purpose of `com.fsck.k9.mailstore.StorageManager$ExternalStorageProvider` is to provide methods for managing external storage, including handling of attachments and databases, and checking if external storage is supported and ready for use.

This class contains the following public method(s):

- `getAttachmentDirectory(android.content.Context,java.lang.String)` -- The method returns a file object pointing to a directory for storing email attachments.
- `init(android.content.Context)` -- The method initializes an external storage provider by setting the root and application directories.
- `getDatabase(android.content.Context,java.lang.String)` -- The method returns a reference to a database file in the application directory with the given ID and ".db" extension.
- `isSupported(android.content.Context)` -- The method always returns true to indicate that external storage is supported.
- `getName(android.content.Context)` -- This method returns the name of the external storage provider using the given Android context.
- `getRoot(android.content.Context)` -- This method returns the root directory of the external storage provider.
- `getId()` -- The method returns the unique identifier for the ExternalStorageProvider.
- `isReady(android.content.Context)` -- The method checks if the external storage is mounted and ready in the device.

## class `com.fsck.k9.mailstore.LocalStore`

The purpose of the `com.fsck.k9.mailstore.LocalStore` class is to provide a local mail storage implementation for the K-9 Mail email client, with methods for managing email folders, messages, and attachments, as well as executing SQL commands and checking email settings.

This class contains the following public method(s):

- `isCopyCapable()` -- The method checks if the email messages stored locally can be duplicated and returns true.
- `getFolder(java.lang.String)` -- This method returns a LocalFolder object with the specified name.
- `isMoveCapable()` -- The method checks if the email client can move messages and always returns `true`.
- `getPendingCommands()` -- This method retrieves a list of pending commands from the "pending_commands" database table.
- `getAttachmentDataSource(java.lang.String)` -- The method returns a data source for the attachment with the specified ID.
- `createFolders(java.util.List,int)` -- The `createFolders` method creates a list of LocalFolders in the database with predefined settings based on the account type.
- `getFoldersAndUids(java.util.List,boolean)` -- This method retrieves the folder name and UID for a list of messages, optionally returning UIDs for all messages in the thread if specified.
- `setFlagForThreads(java.util.List,com.fsck.k9.mail.Flag,boolean)` -- The method sets a flag to a specified value for a list of email threads efficiently using SQL update statements.
- `getAttachmentInfo(java.lang.String)` -- This method retrieves information about a specific email attachment with the given ID.
- `compact()` -- The `compact()` method compacts the local mailstore database by executing a VACUUM command, which can potentially reduce the size of the database.
- `getColumnNameForFlag(com.fsck.k9.mail.Flag)` -- This method returns the column name in the database for a given email flag.
- `setFlag(java.util.List,com.fsck.k9.mail.Flag,boolean)` -- The method changes the state of a flag for a list of messages, using a minimal number of SQL UPDATE statements for performance.
- `delete()` -- The method deletes the local mailstore database.
- `removePendingCommand(com.fsck.k9.controller.MessagingControllerCommands$PendingCommand)` -- The method removes a pending command from the database.
- `getInstance(com.fsck.k9.Account,android.content.Context)` -- This method retrieves an instance of a local mail store based on the specified account and context.
- `checkSettings()` -- The method checks the settings of a local mail store to ensure they are valid and throws a messaging exception if they are not.
- `removeAccount(com.fsck.k9.Account)` -- The method removes the local store instance associated with a given email account.
- `switchLocalStorage(java.lang.String)` -- The method switches the storage provider for the local email store.
- `getPersonalNamespaces(boolean)` -- This method retrieves all personal folder namespaces (folders that belong to the user) in the local email store.
- `addPendingCommand(com.fsck.k9.controller.MessagingControllerCommands$PendingCommand)` -- The method adds a pending command to the SQLite database for later execution.
- `getSize()` -- This method returns the total size of attachments and the database for the current email account.
- `recreate()` -- The method `recreate()` clears and recreates the email database for the LocalStore.
- `resetVisibleLimits(int)` -- The method updates the visible limits of a local mail folder in the database.
- `getDatabase()` -- The method returns a LockableDatabase instance, which is a representation of the local mail storage database used by the LocalStore class.
- `getMessageFulltextCreator()` -- The method returns an instance of the message full text creator used by the local store.
- `searchForMessages(com.fsck.k9.mail.MessageRetrievalListener,com.fsck.k9.search.LocalSearch)` -- The purpose of the method is to search for local messages matching the specified search criteria and return a list of them.
- `clear()` -- The `clear()` method clears all local messages, folders and search data from the mail store database.
- `removePendingCommands()` -- The method removes all pending email commands from the local database.
- `getMessagesInThread(long)` -- The method returns a list of local messages that belong to the specified thread ID.

## class `com.fsck.k9.mailstore.LockableDatabase$StorageListener`

The purpose of the class is to listen for the mounting and unmounting of storage providers and to open or close a dataspace in a lockable database accordingly.

This class contains the following public method(s):

- `onMount(java.lang.String)` -- The method opens or creates a dataspace in a lockable database when a storage provider is mounted, logging the event and handling exceptions.
- `onUnmount(java.lang.String)` -- This method closes the database associated with the given storage provider when the provider is unmounted.

## interface `com.fsck.k9.mailstore.LockableDatabase$DbCallback`

The purpose of the interface is to provide a callback method for performing database operations on a locked SQLiteDatabase and returning relevant data.

This class contains the following public method(s):

- `doDbWork(android.database.sqlite.SQLiteDatabase)` -- This method performs database operations on a locked SQLiteDatabase and returns relevant data, potentially throwing exceptions.

## class `com.fsck.k9.mailstore.CryptoResultAnnotation`

The purpose of the `com.fsck.k9.mailstore.CryptoResultAnnotation` class is to provide information about the result of cryptographic operations on a message, including OpenPGP encryption, decryption, and signature verification.

This class contains the following public method(s):

- `getEncapsulatedResult()` -- This method returns the encapsulated CryptoResultAnnotation object.
- `getOpenPgpSigningKeyIntentIfAny()` -- This method returns a pending intent for the OpenPGP signing key, if one exists.
- `createErrorAnnotation(com.fsck.k9.mailstore.CryptoResultAnnotation$CryptoError,com.fsck.k9.mail.internet.MimeBodyPart)` -- This method creates a `CryptoResultAnnotation` object with an error state and replacement data.
- `createOpenPgpCanceledAnnotation()` -- This method creates a new instance of `CryptoResultAnnotation` with a `CryptoError` of `OPENPGP_UI_CANCELED`.
- `withEncapsulatedResult(com.fsck.k9.mailstore.CryptoResultAnnotation)` -- The method returns a new CryptoResultAnnotation object with the current annotation and the provided annotation encapsulated as its result.
- `getOpenPgpSignatureResult()` -- The method returns the OpenPGP signature result, if present, for a message.
- `createOpenPgpSignatureErrorAnnotation(org.openintents.openpgp.OpenPgpError,com.fsck.k9.mail.internet.MimeBodyPart)` -- This method creates an error annotation for a failed OpenPGP signature verification.
- `getOpenPgpInsecureWarningPendingIntent()` -- The method returns a `PendingIntent` for displaying a warning if the OpenPGP encryption used is insecure.
- `getOpenPgpDecryptionResult()` -- The method returns the result of an OpenPGP decryption operation or null if there was no decryption operation.
- `hasSignatureResult()` -- The method checks whether a signature result exists and returns true if it does.
- `getReplacementData()` -- This method returns a nullable MimeBodyPart object that serves as replacement data for encrypted and signed messages.
- `hasReplacementData()` -- This method checks if the `replacementData` field is not null.
- `isOpenPgpResult()` -- The method checks if both the OpenPGP decryption and signature results are not null and returns a boolean indicating if both are present.
- `hasOpenPgpInsecureWarningPendingIntent()` -- The method checks whether there is an open PGP insecure warning pending intent associated with a crypto result annotation.
- `isOverrideSecurityWarning()` -- This method returns whether the security warning for a specific email was overridden.
- `getErrorType()` -- The method returns the type of crypto error associated with the CryptoResultAnnotation instance.
- `getOpenPgpError()` -- This method returns any OpenPGP error associated with the result annotation.
- `createOpenPgpEncryptionErrorAnnotation(org.openintents.openpgp.OpenPgpError)` -- The method creates a `CryptoResultAnnotation` instance for an OpenPGP encryption error.
- `createOpenPgpResultAnnotation(org.openintents.openpgp.OpenPgpDecryptionResult,org.openintents.openpgp.OpenPgpSignatureResult,android.app.PendingIntent,android.app.PendingIntent,com.fsck.k9.mail.internet.MimeBodyPart,boolean)` -- The method creates a new CryptoResultAnnotation object with OpenPGP decryption and signature results, along with pending intents and an override option for cryptography warnings.
- `hasEncapsulatedResult()` -- This method checks if the `encapsulatedResult` field of the `CryptoResultAnnotation` class is not null and returns a boolean indicating whether it has been set.
- `getOpenPgpPendingIntent()` -- This method returns a `PendingIntent` object for a pending OpenPGP operation.

## class `com.fsck.k9.mailstore.AttachmentViewInfo`

The class `com.fsck.k9.mailstore.AttachmentViewInfo` is used to store information about an email attachment, including whether the attachment's content is available or not.

This class contains the following public method(s):

- `setContentAvailable()` -- Sets the `contentAvailable` property of an `AttachmentViewInfo` object to `true`.
- `isContentAvailable()` -- The method checks whether the content of the attachment is available or not.

## enum `com.fsck.k9.mailstore.DatabasePreviewType`

The enum is used to map different preview types of emails to their corresponding values in the database and to facilitate the conversion between preview types and their database values.

This class contains the following public method(s):

- `fromPreviewType(com.fsck.k9.message.extractors.PreviewResult$PreviewType)` -- This method converts a `PreviewType` from the `PreviewResult` enum into the corresponding `DatabasePreviewType` enum value.
- `getDatabaseValue()` -- The method returns the database value associated with a specific enum value.
- `fromDatabaseValue(java.lang.String)` -- This method returns the `DatabasePreviewType` enum value that corresponds to a given string database value.
- `getPreviewType()` -- The method returns the preview type of a message extracted from a database.

## enum `com.fsck.k9.mailstore.LocalFolder$MoreMessages`

The enum `com.fsck.k9.mailstore.LocalFolder$MoreMessages` is used for identifying if there are more messages to be loaded in a local email folder in the K-9 email client.

This class contains the following public method(s):

- `fromDatabaseName(java.lang.String)` -- This method returns the enum value of `com.fsck.k9.mailstore.LocalFolder.MoreMessages` that matches the given database name.
- `getDatabaseName()` -- This method returns the name of the database associated with this LocalFolder.

## class `com.fsck.k9.mailstore.LocalMimeMessage`

The class `com.fsck.k9.mailstore.LocalMimeMessage` is used to represent a locally stored MIME message and provide methods to access its content such as retrieving the message part ID, associated LocalMessage object, and account UUID.

This class contains the following public method(s):

- `getPartId()` -- The method returns the ID of the message part.
- `getMessage()` -- The method returns the LocalMessage associated with the LocalMimeMessage object.
- `getAccountUuid()` -- The method returns the UUID of the account associated with the current LocalMimeMessage object.

## class `com.fsck.k9.mailstore.StorageManager$HtcIncredibleStorageProvider`

The purpose of the `com.fsck.k9.mailstore.StorageManager$HtcIncredibleStorageProvider` class is to provide a way to obtain the name and unique id of the local storage provider for the HTC Incredible device.

This class contains the following public method(s):

- `getName(android.content.Context)` -- This method returns the name of the local storage provider for the HTC Incredible device.
- `getId()` -- This method returns the unique id of the HTC Incredible storage provider.

## class `com.fsck.k9.mailstore.MessageHelper`

The class `com.fsck.k9.mailstore.MessageHelper` provides methods to assist in managing email messages, including checking if all parts are available and creating empty MIME body parts.

This class contains the following public method(s):

- `isCompletePartAvailable(com.fsck.k9.mail.Part)` -- This method checks if all parts of a particular email message are available for processing.
- `createEmptyPart()` -- This method creates an empty MIME body part.

## class `com.fsck.k9.mailstore.StoreSchemaDefinition$RealMigrationsHelper`

The class `com.fsck.k9.mailstore.StoreSchemaDefinition$RealMigrationsHelper` provides helper methods for making real migrations in the local email store, including getting the context, local store, storage type, account, and serializing mail flags into a string format.

This class contains the following public method(s):

- `getContext()` -- This method returns the context of the local mail store.
- `getLocalStore()` -- The method returns the local store object for the corresponding mail store schema definition's real migrations helper.
- `getStorage()` -- This method returns the type of storage used by the local email store.
- `serializeFlags(java.util.List)` -- The method serializes a list of mail flags into a string format.
- `getAccount()` -- This method returns the account associated with the local mail store.

## class `com.fsck.k9.mailstore.LockableDatabase`

The `LockableDatabase` class provides a mechanism for executing database callbacks in a shared context with locking support, as well as methods for managing the storage provider and deleting the database.

This class contains the following public method(s):

- `execute(boolean,com.fsck.k9.mailstore.LockableDatabase$DbCallback)` -- The method executes a database callback in a shared context, takes care of locking the database storage, and optionally starts a transaction.
- `open()` -- The method opens or creates a data space, while locking write access to prevent data inconsistencies, and adds a listener to the storage manager.
- `recreate()` -- The `recreate()` method deletes the contents of a database and throws an exception if the storage is unavailable.
- `switchProvider(java.lang.String)` -- The `switchProvider` method switches from one storage provider to another while migrating data in the K-9 email app.
- `setStorageProviderId(java.lang.String)` -- The method sets the storage provider identifier for the lockable database.
- `getStorageProviderId()` -- The method returns the storage provider ID of a lockable database.
- `delete()` -- The purpose of the `delete()` method is to delete the backing database of the `LockableDatabase` class.

## class `com.fsck.k9.mailstore.LocalFolder`

The class `com.fsck.k9.mailstore.LocalFolder` represents a local email folder in the K-9 mail client and provides methods for retrieving, managing, and storing email messages in the folder.

This class contains the following public method(s):

- `getMessagesByUids(java.util.List)` -- This method retrieves a list of LocalMessages corresponding to a list of UIDs.
- `getName()` -- This method returns the name of the local email folder.
- `getMessages(int,int,java.util.Date,com.fsck.k9.mail.MessageRetrievalListener)` -- The method retrieves a list of local messages from the specified start to end indices that match the given earliest date and sends these messages to a listener.
- `getMessage(java.lang.String)` -- This method returns a LocalMessage object corresponding to the provided UID from the database for the LocalFolder.
- `getUidFromMessageId(com.fsck.k9.mail.Message)` -- The method throws an exception as it is not intended to be called on LocalFolder.
- `save(com.fsck.k9.preferences.StorageEditor)` -- The method saves the display mode, synchronization mode, notification mode, push mode, and other preferences of a local folder using a storage editor.
- `setDisplayClass(com.fsck.k9.mailstore.FolderClass)` -- The method sets the display class of the folder and updates the folder's display_class column in the database.
- `refresh(java.lang.String,com.fsck.k9.mailstore.LocalFolder$PreferencesHolder)` -- The method refreshes the preferences holder of a local mail folder by loading folder display mode, synchronization mode, notification mode, push mode, inTopGroup, and integrate settings from storage, and updating the holder accordingly.
- `getMessages(com.fsck.k9.mail.MessageRetrievalListener,boolean)` -- This method retrieves a list of local messages from the folder, optionally including deleted messages, and notifies a listener of the progress.
- `addPartToMessage(com.fsck.k9.mailstore.LocalMessage,com.fsck.k9.mail.Part)` -- The purpose of the method is to add a part to a message in the local folder of a K-9 mail client.
- `getSyncClass()` -- This method returns the synchronization class of the current email folder.
- `delete(boolean)` -- The method deletes the local folder and all its messages, optionally including subfolders.
- `isOpen()` -- This method checks if the LocalFolder object is currently open.
- `create(com.fsck.k9.mailstore.FolderType)` -- The method creates a new folder of a given type with a default display count.
- `equals(java.lang.Object)` -- The `equals` method checks if two `LocalFolder` objects have the same name, returning `true` if they do and `false` otherwise.
- `setPushState(java.lang.String)` -- The method sets the push state of a local mail folder.
- `changeUid(com.fsck.k9.mailstore.LocalMessage)` -- Changes the stored UID of a message to the UID in the message itself.
- `getVisibleLimit()` -- This method returns the visible limit of messages in the folder.
- `clearAllMessages()` -- The `clearAllMessages()` method deletes all messages from a local folder.
- `getAccountUuid()` -- This method returns the UUID of the account associated with the local email folder.
- `appendMessages(java.util.List)` -- The `appendMessages` method is used to add new messages to a local folder and replace existing messages if a matching UID is found.
- `setStatus(java.lang.String)` -- The method sets the status of a local folder in the K-9 mail application.
- `exists()` -- The `exists()` method checks whether the folder exists in the local store database.
- `getMode()` -- The method returns the file access mode for the local email storage folder as "read-write".
- `getDatabaseId()` -- This method retrieves the database ID associated with the local folder.
- `hashCode()` -- The `hashCode()` method returns an integer hash code value for the name of the LocalFolder object.
- `getPushState()` -- The method returns the push state of the local email folder.
- `getSignatureUse()` -- The method returns whether or not the signature should be used for an email in the local folder, according to the associated account settings.
- `setInTopGroup(boolean)` -- This method sets whether or not the folder should be displayed in the user's "top group" in the email client.
- `updateLastUid()` -- The method `updateLastUid()` fetches the most recent numeric UID value in a folder, used to determine newness of messages.
- `clearMessagesOlderThan(long)` -- This method clears all messages in a local folder that were received before a specified time.
- `areMoreMessagesAvailable(int,java.util.Date)` -- The purpose of the method is to check if there are more messages available in the local folder after a specified index and before a specified date.
- `getRawSyncClass()` -- The purpose of this method is to return the `FolderClass` object that represents the synchronization status of the folder.
- `copyMessages(java.util.List,com.fsck.k9.mail.Folder)` -- The method copies the given list of email messages to a specified local email folder.
- `setIntegrate(boolean)` -- The method sets a flag indicating whether newly received messages should be automatically integrated into the folder.
- `fetch(java.util.List,com.fsck.k9.mail.FetchProfile,com.fsck.k9.mail.MessageRetrievalListener)` -- This method fetches messages from the local folder and loads message body parts if specified in the fetch profile.
- `setMoreMessages(com.fsck.k9.mailstore.LocalFolder$MoreMessages)` -- This method sets the "more messages" property of a local email folder.
- `storeSmallMessage(com.fsck.k9.mail.Message,java.lang.Runnable)` -- The purpose of this method is to store a message in the local database and set it as fully downloaded while executing a runnable before doing so.
- `setLastSelectedFolderName(java.lang.String)` -- Sets the name of the last selected folder for the account associated with the local folder.
- `isIntegrate()` -- The method returns a boolean value indicating whether or not the folder is integrated with the server.
- `getNotifyClass()` -- The method returns the notification class of the local folder.
- `getAllMessageUids()` -- This method retrieves the UIDs of all non-empty and non-deleted messages in a local mail folder.
- `getOldestMessageDate()` -- This method returns the date of the oldest message in the current folder.
- `setFlags(java.util.List,java.util.Set,boolean)` -- This method sets the specified flags (e.g. seen, answered, flagged) for the given list of messages.
- `getMessageCount()` -- The `getMessageCount()` method returns the number of messages in this folder that are not empty or deleted.
- `save()` -- The `save()` method saves the contents of the local folder to the email storage database.
- `setNotifyClass(com.fsck.k9.mailstore.FolderClass)` -- This method sets the notify class for the local email folder and updates the corresponding folder column.
- `getMoreMessages()` -- This method returns an object that contains more messages for a local folder in an email client.
- `getAllMessagesAndEffectiveDates()` -- The `getAllMessagesAndEffectiveDates()` method retrieves a map of all message UIDs in the folder and their corresponding effective dates.
- `setPushClass(com.fsck.k9.mailstore.FolderClass)` -- The `setPushClass` method sets the push class of the local folder and updates the corresponding database column.
- `close()` -- The purpose of this method is to mark the database ID as -1 to indicate that the folder is closed.
- `delete()` -- The method deletes preferences associated with a local email folder.
- `purgeToVisibleLimit(com.fsck.k9.mailstore.MessageRemovalListener)` -- This method purges messages in a local mail folder up to a specified visible limit and notifies a listener of each purged message.
- `open(int)` -- This method opens an SQLite database connection to the mailbox in read-only or read-write mode, depending on the specified mode, and retrieves information about the folder from the database or creates a new folder if it doesn't exist.
- `getRawPushClass()` -- The method returns the push class of a local folder.
- `setLastChecked(long)` -- The method is used to update the timestamp for the last time this folder was checked for new messages.
- `getMessageUidById(long)` -- This method returns the unique identifier (UID) of a message given its database identifier and folder.
- `setVisibleLimit(int)` -- The method sets the maximum number of messages visible in the folder view and updates the folder's metadata accordingly.
- `isInTopGroup()` -- The method returns whether the folder is in the top-level group.
- `getLastUid()` -- The method returns the last UID (unique identifier) of the local email folder.
- `setSyncClass(com.fsck.k9.mailstore.FolderClass)` -- The method sets the synchronization class for the local mail folder.
- `moveMessages(java.util.List,com.fsck.k9.mail.Folder)` -- This method moves a list of messages to a specified folder while updating their unique IDs and thread info.
- `getDisplayClass()` -- This method returns the display class of the local folder.
- `create(com.fsck.k9.mailstore.FolderType,int)` -- The method creates a local email folder of the specified type with a visible limit.
- `setFlags(java.util.Set,boolean)` -- This method sets the flags for all messages in the local folder to the specified value.
- `syncRemoteDeletions()` -- The method syncs remote deletions with local deletions in the folder.
- `getMessages(com.fsck.k9.mail.MessageRetrievalListener)` -- This method retrieves a list of local email messages and notifies a listener about the retrieval process.
- `hasMoreMessages()` -- The method checks if there are more messages to be fetched from the local folder.
- `getMessagesByReference(java.util.List)` -- This method returns a list of LocalMessage objects that match the given list of MessageReference objects.
- `setLastPush(long)` -- The method sets the timestamp of the last push of new mail messages for a local email folder.
- `getUnreadMessageCount()` -- The method `getUnreadMessageCount()` returns the number of unread messages in the local folder.
- `getRawNotifyClass()` -- This method returns the notify class of the current folder as an object of type `FolderClass`.
- `destroyMessages(java.util.List)` -- The `destroyMessages` method is used to delete multiple email messages from the local storage of the K-9 email client.
- `getPushClass()` -- The method returns the push class of the local folder, which is either inherited or set explicitly.
- `getFlaggedMessageCount()` -- The method returns the number of flagged messages in the local folder.
- `extractNewMessages(java.util.List)` -- The `extractNewMessages` method extracts new messages from a list of messages received by the `LocalFolder`.

## interface `com.fsck.k9.mailstore.MessageRemovalListener`

The interface `com.fsck.k9.mailstore.MessageRemovalListener` allows classes to receive notifications when a message is removed from a mail store.

This class contains the following public method(s):

- `messageRemoved(com.fsck.k9.mail.Message)` -- The method is called when a message is removed from a mail store.

## class `com.fsck.k9.mailstore.TempFileBody`

The `TempFileBody` class is used to store the contents of an email message as a temporary file.

This class contains the following public method(s):

- `getInputStream()` -- The method returns an input stream for reading the contents of a temporary file, or an empty byte array if the file is not found.
- `getSize()` -- This method returns the size in bytes of a temporary file used by the `TempFileBody` class.

## class `com.fsck.k9.mailstore.MimePartStreamParser$PartBuilder`

The `com.fsck.k9.mailstore.MimePartStreamParser$PartBuilder` class is responsible for parsing MIME messages by constructing individual parts and adding them to an email message.

This class contains the following public method(s):

- `epilogue(java.io.InputStream)` -- The `epilogue(java.io.InputStream)` method sets the epilogue of a MIME multipart message.
- `startHeader()` -- The purpose of this method is to start parsing the header of a mime part and do nothing.
- `startBodyPart()` -- The method `startBodyPart()` adds a new body part to a multipart email message.
- `endMessage()` -- The method ends the parsing of a MIME message and removes the current part from the stack.
- `endHeader()` -- The `endHeader()` method does nothing and is used as a placeholder for the end of the header section during the parsing of MIME messages.
- `body(org.apache.james.mime4j.stream.BodyDescriptor,java.io.InputStream)` -- The method is responsible for parsing a MIME email body and setting it as the body of the corresponding email part.
- `endBodyPart()` -- The `endBodyPart()` method closes the current body part being parsed.
- `startMultipart(org.apache.james.mime4j.stream.BodyDescriptor)` -- This method starts processing a multipart section of a MIME message by creating a new MIME multipart object and setting it as the body of the current mail part being constructed.
- `raw(java.io.InputStream)` -- This method is not implemented and will throw an IllegalStateException if invoked.
- `preamble(java.io.InputStream)` -- The method sets the preamble of a MIME multipart using input from an InputStream.
- `endMultipart()` -- The method ends parsing of a MIME multipart and pops the current context off the stack.
- `startMessage()` -- The `startMessage()` method sets up the parsing of a MIME message by creating a new `com.fsck.k9.mail.Message` and adding it to the stack of parsed MIME parts.
- `field(org.apache.james.mime4j.stream.Field)` -- This method adds a raw header to the MIME part being built based on a parsed MIME field.

## interface `com.fsck.k9.mailstore.LockableDatabase$SchemaDefinition`

The purpose of the interface `com.fsck.k9.mailstore.LockableDatabase$SchemaDefinition` is to define the database schema for the LockableDatabase class and provide methods to retrieve the current schema version and upgrade the schema.

This class contains the following public method(s):

- `getVersion()` -- The method returns the current version of the database schema.
- `doDbUpgrade(android.database.sqlite.SQLiteDatabase)` -- The method is used to upgrade the database schema.

## class `com.fsck.k9.mailstore.MessageViewInfoExtractor`

The purpose of the `com.fsck.k9.mailstore.MessageViewInfoExtractor` class is to extract information from an email message and annotations related to its encryption status, and return it for display to the user in a view.

This class contains the following public method(s):

- `extractMessageForView(com.fsck.k9.mail.Message,com.fsck.k9.ui.crypto.MessageCryptoAnnotations)` -- The `extractMessageForView` method extracts information from a given email message and annotations related to its encryption status to be displayed to the user in a view.
- `getInstance()` -- The method returns an instance of `MessageViewInfoExtractor` with dependencies initialized.

## class `com.fsck.k9.mailstore.StorageManager$InternalStorageProvider`

The class `com.fsck.k9.mailstore.StorageManager$InternalStorageProvider` is used to manage the internal storage of K-9 Mail app, including getting the root directory, retrieving database and attachment directory paths, and initializing the storage provider.

This class contains the following public method(s):

- `getRoot(android.content.Context)` -- This method returns the root directory of the internal storage provider.
- `isReady(android.content.Context)` -- This method always returns true, indicating that the internal storage provider is always ready.
- `getDatabase(android.content.Context,java.lang.String)` -- The method returns the absolute path of the database file identified by the provided context and name.
- `getName(android.content.Context)` -- This method returns the label for the internal storage provider in K-9 Mail.
- `isSupported(android.content.Context)` -- The method returns true to indicate that the internal storage provider is always supported.
- `getAttachmentDirectory(android.content.Context,java.lang.String)` -- This method returns the file object for the attachment directory in the app's internal storage by concatenating the given ID with the string ".db_att" and getting the database path from the context.
- `init(android.content.Context)` -- To initialize the internal storage provider by setting the root directory to the file system root.
- `getId()` -- This method returns the ID of the internal storage provider used by the StorageManager class.

## class `com.fsck.k9.mailstore.MessageViewInfo`

The class `com.fsck.k9.mailstore.MessageViewInfo` is used to store information about an email message for display in a user interface, such as whether the message has been viewed or has an error state.

This class contains the following public method(s):

- `createWithErrorState(com.fsck.k9.mail.Message,boolean)` -- This method creates a new MessageViewInfo object with an error state for a given email message and completeness status.

## class `com.fsck.k9.mailstore.AttachmentResolver`

The class `com.fsck.k9.mailstore.AttachmentResolver` is used to retrieve and store information about email attachments, including their content IDs and URIs.

This class contains the following public method(s):

- `getAttachmentUriForContentId(java.lang.String)` -- This method retrieves the URI of an attachment with the given content ID.
- `createFromPart(com.fsck.k9.mail.Part)` -- This method creates an `AttachmentResolver` instance from a given `Part`, which extracts attachment information and builds a map of content IDs to attachment URIs.

## class `com.fsck.k9.mailstore.DeferredFileBody`

The purpose of the class is to provide a deferred writing mechanism for storing email attachments in memory initially and then writing them to disk when necessary, to optimize memory usage.

This class contains the following public method(s):

- `writeTo(java.io.OutputStream)` -- This method writes the content of a DeferredFileBody instance to a specified OutputStream.
- `getEncoding()` -- The method returns the encoding of the content of the file represented by this DeferredFileBody.
- `setEncoding(java.lang.String)` -- The method sets the encoding for the DeferredFileBody, but it throws an exception stating that it cannot be re-encoded.
- `getSize()` -- The method returns the size of the file or data held by the `DeferredFileBody` instance, or throws an exception if the data has not been fully written yet.
- `getInputStream()` -- This method returns an InputStream that provides access to the decrypted contents of an email message.
- `getFile()` -- This method returns the underlying file object, and if the file object is null, it creates and returns a new file by writing the data from memory to the disk.
- `getOutputStream()` -- This method returns an output stream that writes to a deferred file output stream with a specified memory-backed threshold and file factory, which allows for efficient handling of large email attachments.

## class `com.fsck.k9.mailstore.FileBackedBody`

The purpose of `com.fsck.k9.mailstore.FileBackedBody` is to provide a way to read and write the contents of a file-backed email message body.

This class contains the following public method(s):

- `getInputStream()` -- The method returns an input stream for reading the contents of a file-backed email message body.
- `writeTo(java.io.OutputStream)` -- This method writes the content of the body to the provided `OutputStream` by copying it from the input stream obtained from `getInputStream()`.
- `setEncoding(java.lang.String)` -- This method sets the encoding of the body content, but is not supported and will throw a runtime exception.
- `getEncoding()` -- The method returns the encoding type used for the body of the email message.
- `getSize()` -- This method returns the file size of the body stored in the filesystem.

## class `com.fsck.k9.mailstore.LocalBodyPart`

The class `com.fsck.k9.mailstore.LocalBodyPart` represents a locally stored email body part that contains metadata about the associated account, message, size, and part ID.

This class contains the following public method(s):

- `getAccountUuid()` -- The method returns the UUID of the account associated with the email body.
- `getMessage()` -- This method returns the LocalMessage object that corresponds to the LocalBodyPart.
- `getSize()` -- This method returns the size of a local email body part.
- `getPartId()` -- This method returns the ID of the message part.

## abstract class `com.fsck.k9.mailstore.StorageManager$FixedStorageProviderBase`

The purpose of the abstract class `com.fsck.k9.mailstore.StorageManager$FixedStorageProviderBase` is to provide methods that handle initialization and storage of application-specific files for K-9 Mail on Android.

This class contains the following public method(s):

- `init(android.content.Context)` -- The method initializes a directory for storing application-specific files under the root directory specific to the given Android context.
- `getAttachmentDirectory(android.content.Context,java.lang.String)` -- The method returns a file object representing the directory where attachments are stored for a specific email in a K-9 Mail database.
- `getDatabase(android.content.Context,java.lang.String)` -- This method returns a File object corresponding to a database with the given ID name in the application directory.
- `isSupported(android.content.Context)` -- The method checks if the storage directory exists and if it supports the vendor.
- `isReady(android.content.Context)` -- The `isReady` method checks if the specified root directory is ready for use.
- `getRoot(android.content.Context)` -- This method returns the root directory of the storage provider.

## interface `com.fsck.k9.mailstore.StorageManager$StorageProvider`

The interface `com.fsck.k9.mailstore.StorageManager$StorageProvider` provides a set of methods that can be implemented by different storage providers to initialize, retrieve information and access files from different storage systems for an email client application.

This class contains the following public method(s):

- `init(android.content.Context)` -- The method initializes the storage provider with a given Android application context.
- `getRoot(android.content.Context)` -- The method retrieves the root directory of the underlying storage.
- `getAttachmentDirectory(android.content.Context,java.lang.String)` -- The method returns a File object representing the chosen attachment directory.
- `getName(android.content.Context)` -- The method returns a user-friendly, localized name for a storage provider.
- `isSupported(android.content.Context)` -- The method checks if the storage provider can provide valid File handles and returns whether it supports the current device or not.
- `isReady(android.content.Context)` -- This method checks if the underlying storage is ready for read/write operations at the time of invocation.
- `getDatabase(android.content.Context,java.lang.String)` -- This method returns the file object representing the chosen email database file.
- `getId()` -- The `getId()` method is used to retrieve a unique identifier for the current implementation of the `StorageProvider` interface.

## class `com.fsck.k9.mailstore.LocalMessage`

The `LocalMessage` class is used to represent an email message stored locally in the K-9 Mail app and provides methods for manipulating the message's flags, recipients, and content.

This class contains the following public method(s):

- `getDatabaseId()` -- The method returns the ID of the message in the local database.
- `setFlag(com.fsck.k9.mail.Flag,boolean)` -- The method is used to set a flag (such as "deleted" or "read") on a local email message and update the corresponding database with the new flag value.
- `getPreviewType()` -- The method returns the preview type of a local email message.
- `getFolder()` -- This method returns the local folder object where the message is stored.
- `equals(java.lang.Object)` -- The method checks if two `LocalMessage` objects are equal by comparing their account uuid in addition to the default `Message.equals()` implementation.
- `clone()` -- This method creates a copy of a LocalMessage object with the same data as the original.
- `setSubject(java.lang.String)` -- The method sets the subject of a local email message object and marks its header as needing an update.
- `getThreadId()` -- This method returns the thread ID associated with a local email message.
- `getMessagePartId()` -- The method returns the ID of the message part.
- `hasAttachments()` -- The method checks if the email message has any attachments.
- `hashCode()` -- The purpose of this method is to generate a unique hash code for the LocalMessage object based on its super class's hash code and the hash code of its account UUID.
- `getUri()` -- The method returns a unique URI string that represents the location of a LocalMessage object in the file system.
- `setMessageId(java.lang.String)` -- The method sets the message ID of a local email message.
- `getAccount()` -- The method returns the account associated with the LocalMessage object.
- `getSubject()` -- This method returns the subject of a local email message.
- `writeTo(java.io.OutputStream)` -- The method writes the message's updated header and body to the specified output stream.
- `getPreview()` -- The method returns a preview of the email content.
- `debugClearLocalData()` -- The method is used to clear local data associated with a message for debugging purposes only.
- `setRecipients(com.fsck.k9.mailstore.RecipientType,com.fsck.k9.mail.Address[])` -- The method sets the recipients (To, Cc, or Bcc) of the email message.
- `setReplyTo(com.fsck.k9.mail.Address[])` -- The method sets the reply-to addresses for the email message and updates the header accordingly.
- `setFlagInternal(com.fsck.k9.mail.Flag,boolean)` -- The method sets a flag for a local email message.
- `destroy()` -- The purpose of the `destroy()` method is to remove a message from the local database.
- `setUid(java.lang.String)` -- The method sets the unique identifier of the email message and resets the message reference to null.
- `getRootId()` -- The method returns the root ID of the message in the local message store.
- `makeMessageReference()` -- The purpose of this method is to create and return a reference to a local email message in the K-9 Mail app.
- `getMimeType()` -- The method returns the MIME type of the LocalMessage object.
- `setFrom(com.fsck.k9.mail.Address)` -- This method sets the "From" address of the email message and marks the header as needing updating.

## class `com.fsck.k9.mailstore.MimePartStreamParser`

The class `com.fsck.k9.mailstore.MimePartStreamParser` is used to parse an input stream into a MimeBodyPart object using the MimeStreamParser provided by the Apache james.mime4j library.

This class contains the following public method(s):

- `parse(com.fsck.k9.mailstore.util.FileFactory,java.io.InputStream)` -- This method parses a given input stream into a MimeBodyPart object using the MimeStreamParser provided by the Apache james.mime4j library.

## interface `com.fsck.k9.mailstore.StorageManager$StorageListener`

The `com.fsck.k9.mailstore.StorageManager$StorageListener` interface is used to listen for events related to storage providers being mounted and unmounted in order to handle any necessary actions.

This class contains the following public method(s):

- `onMount(java.lang.String)` -- This method is invoked when a storage provider is mounted with read/write access, passing the provider identifier as a parameter.
- `onUnmount(java.lang.String)` -- This method is called when a storage is about to be unmounted in order to handle any necessary actions related to unmounting.

## interface `com.fsck.k9.mailstore.LocalStore$BatchSetSelection`

The purpose of the interface `com.fsck.k9.mailstore.LocalStore$BatchSetSelection` is to provide abstraction for batch set operations on an SQLite database in K-9 Mail.

This class contains the following public method(s):

- `getListItem(int)` -- This method returns a specific item from the argument list at the specified index.
- `getListSize()` -- This method returns the size of the argument list.
- `doDbWork(android.database.sqlite.SQLiteDatabase,java.lang.String,java.lang.String[])` -- Execute a SQL statement with a given database and set of selection arguments.
- `postDbWork()` -- Executes after each invocation of `doDbWork()` method of `LocalStore$BatchSetSelection` interface after the transaction has been committed.

## interface `com.fsck.k9.mailstore.LocalPart`

The `com.fsck.k9.mailstore.LocalPart` interface is used for representing the local part of an email message, and providing methods for retrieving information about the message such as its size, ID, associated account UUID, and the message itself.

This class contains the following public method(s):

- `getPartId()` -- The method returns the ID of the local part of a message.
- `getSize()` -- This method returns the size of the email message.
- `getMessage()` -- The method `getMessage()` retrieves a local message stored in `com.fsck.k9.mailstore.LocalPart` interface.
- `getAccountUuid()` -- The method returns the UUID of the account associated with the email address local part.

## class `com.fsck.k9.mailstore.StorageManager`

The purpose of the class `com.fsck.k9.mailstore.StorageManager` is to provide access to the K-9 Mail database and manage storage providers for email attachments.

This class contains the following public method(s):

- `getDefaultProviderId()` -- This method returns the default provider ID for the StorageManager which is the ID of the first provider defined.
- `onAfterUnmount(java.lang.String)` -- The method is called after a storage path is unmounted and is responsible for releasing the write lock and enabling K-9 email services.
- `addListener(com.fsck.k9.mailstore.StorageManager$StorageListener)` -- The method adds a listener to the list of storage listeners.
- `onBeforeUnmount(java.lang.String)` -- The method is called before a storage path is unmounted and notifies listeners that the provider ID is being unmounted.
- `getDatabase(java.lang.String,java.lang.String)` -- This method returns the resolved database file for a given provider ID.
- `removeListener(com.fsck.k9.mailstore.StorageManager$StorageListener)` -- This method removes a listener for storage changes from the list of registered listeners.
- `getAttachmentDirectory(java.lang.String,java.lang.String)` -- This method retrieves the storage location directory for email attachments from a specific provider.
- `getInstance(android.content.Context)` -- This method returns the instance of the StorageManager class which provides access to the K-9 Mail database.
- `isReady(java.lang.String)` -- The method `isReady` checks if a specified provider is ready for read/write operations.
- `unlockProvider(java.lang.String)` -- The method releases the read lock held on a specific storage provider by the currently executing thread.
- `isMountPoint(java.io.File)` -- This method checks whether the specified file is a mount point (root) of a file system.
- `lockProvider(java.lang.String)` -- The method attempts to lock the underlying storage to prevent concurrent unmount in order to ensure data consistency during file system operations.
- `onMount(java.lang.String,boolean)` -- The `onMount` method is responsible for notifying listeners when a storage path is mounted and resetting the mail service if necessary.
- `getAvailableProviders()` -- This method returns a map of available providers' names indexed by their ID.

## abstract class `com.fsck.k9.mailstore.BinaryAttachmentBody`

The purpose of the `BinaryAttachmentBody` class is to handle binary attachments in email messages by providing methods to set the encoding, write the content to an output stream, and retrieve the contents through an input stream.

This class contains the following public method(s):

- `setEncoding(java.lang.String)` -- Sets the encoding of the binary attachment body.
- `writeTo(java.io.OutputStream)` -- The method writes the binary content of the attachment to the specified `OutputStream`, with possible encoding using either Base64 or Quoted-Printable.
- `getInputStream()` -- This method returns an input stream for reading the binary contents of the attachment body.
- `getEncoding()` -- The `getEncoding()` method returns the encoding type of binary attachment body data.

## class `com.fsck.k9.mailstore.StoreSchemaDefinition`

The purpose of the class `com.fsck.k9.mailstore.StoreSchemaDefinition` is to define the database schema and handle upgrades for the local mail store used by the K-9 Mail client.

This class contains the following public method(s):

- `getVersion()` -- The purpose of the `getVersion()` method is to return the database version used by the local mail store.
- `doDbUpgrade(android.database.sqlite.SQLiteDatabase)` -- This method upgrades the SQLite database used by the K-9 Mail client, handling any exceptions that occur during the upgrade process and resetting the database if necessary.


# package `com.fsck.k9.mailstore.migrations`

The `com.fsck.k9.mailstore.migrations` package contains classes and interfaces for migrating the SQLite database schema used by K-9 Mail email client to newer versions by adding, removing, or updating columns and tables.

This package contains the following class(es):

## class `com.fsck.k9.mailstore.migrations.MigrationTo61`

The class `com.fsck.k9.mailstore.migrations.MigrationTo61` is used for migrating a K9 Mail database to version 6.1 by removing the "K9mail-errors" folder.

This class contains the following public method(s):

- `removeErrorsFolder(android.database.sqlite.SQLiteDatabase)` -- The method removes the "K9mail-errors" folder from the SQLite database passed as a parameter.

## class `com.fsck.k9.mailstore.migrations.MigrationTo44`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo44` is to perform a migration to update the SQLite database schema of an email storage application to version 44 by adding four threading columns to the `messages` table.

This class contains the following public method(s):

- `addMessagesThreadingColumns(android.database.sqlite.SQLiteDatabase)` -- This method adds four threading columns to the `messages` table in an SQLite database for an email storage application.

## class `com.fsck.k9.mailstore.migrations.MigrationTo54`

The purpose of this class is to perform a database migration for the K9 email client app to version 5.4, which involves adding a new column to the "messages" table.

This class contains the following public method(s):

- `addPreviewTypeColumn(android.database.sqlite.SQLiteDatabase)` -- The method adds a column for preview type to the "messages" table in an SQLite database and sets the default value to "none", then updates the preview type to "text" for any messages that have a preview.

## class `com.fsck.k9.mailstore.migrations.MigrationTo42`

The purpose of the `com.fsck.k9.mailstore.migrations.MigrationTo42` class is to handle the migration process from version 4.1 to version 4.2 of the K9 email client, specifically to move folder preferences from a local storage to a preferences storage.

This class contains the following public method(s):

- `from41MoveFolderPreferences(com.fsck.k9.mailstore.migrations.MigrationsHelper)` -- The method moves folder preferences from a local storage to a preferences storage during a migration process from version 4.1 to version 4.2 of the K9 email client.

## class `com.fsck.k9.mailstore.migrations.MigrationTo37`

The main purpose of this class is to provide a migration to version 37 of the SQLite database used in K-9 Mail application by adding a `content_disposition` column to the `attachments` table.

This class contains the following public method(s):

- `addAttachmentsContentDispositionColumn(android.database.sqlite.SQLiteDatabase)` -- This method adds a `content_disposition` column to the `attachments` table in a SQLite database.

## class `com.fsck.k9.mailstore.migrations.MigrationTo60`

The class is responsible for migrating pending commands from a previous version of the app's database to version 6.0.

This class contains the following public method(s):

- `migratePendingCommands(android.database.sqlite.SQLiteDatabase)` -- The method migrates pending commands from a previous version of the app's database to version 6.0.

## class `com.fsck.k9.mailstore.migrations.MigrationTo40`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo40` is to migrate the database schema to version 40 by adding a new "mime_type" column to the "messages" table.

This class contains the following public method(s):

- `addMimeTypeColumn(android.database.sqlite.SQLiteDatabase)` -- The method adds a new "mime_type" column of type TEXT to the "messages" table in a SQLite database.

## class `com.fsck.k9.mailstore.migrations.MigrationTo32`

The class `com.fsck.k9.mailstore.migrations.MigrationTo32` is responsible for the database migration to version 32 of the K-9 Mail app, including updating the 'deleted' column in the 'messages' table.

This class contains the following public method(s):

- `updateDeletedColumnFromFlags(android.database.sqlite.SQLiteDatabase)` -- The method updates the 'deleted' column of the 'messages' table to 1 for rows where the 'flags' column contains the text 'DELETED'.

## class `com.fsck.k9.mailstore.migrations.MigrationTo52`

The class `com.fsck.k9.mailstore.migrations.MigrationTo52` handles the migration process of adding a new column to the "folders" table in a SQLite database used by the K-9 Mail application.

This class contains the following public method(s):

- `addMoreMessagesColumnToFoldersTable(android.database.sqlite.SQLiteDatabase)` -- The method adds a text column named "more_messages" with a default value of "unknown" to the "folders" table in a SQLite database.

## class `com.fsck.k9.mailstore.migrations.MigrationTo36`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo36` is to handle database migrations to version 36 of the K-9 mail client, which includes adding a new column to the attachments table.

This class contains the following public method(s):

- `addAttachmentsContentIdColumn(android.database.sqlite.SQLiteDatabase)` -- The method adds a new column `content_id` of type `TEXT` to the `attachments` table in the specified SQLite `db` if it does not already exist.

## class `com.fsck.k9.mailstore.migrations.MigrationTo51`

The purpose of the `com.fsck.k9.mailstore.migrations.MigrationTo51` class is to handle the migration of messages from an old table structure to a new one, including recreating the MIME structure from message content and attachments.

This class contains the following public method(s):

- `db51MigrateMessageFormat(android.database.sqlite.SQLiteDatabase,com.fsck.k9.mailstore.migrations.MigrationsHelper)` -- This method migrates messages from an old table structure to a new one, recreating MIME structure from message content and attachments.

## class `com.fsck.k9.mailstore.migrations.MigrationTo35`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo35` is to provide a migration path for updating a SQLite database to version 35 by updating the flag of a message.

This class contains the following public method(s):

- `updateRemoveXNoSeenInfoFlag(android.database.sqlite.SQLiteDatabase)` -- This method updates the flag of a message in a SQLite database by replacing 'X_NO_SEEN_INFO' with 'X_BAD_FLAG'.

## class `com.fsck.k9.mailstore.migrations.MigrationTo45`

The class `com.fsck.k9.mailstore.migrations.MigrationTo45` is used to perform migrations of the SQLite database used by K-9 Mail to version 45.

This class contains the following public method(s):

- `changeThreadingIndexes(android.database.sqlite.SQLiteDatabase)` -- The method changes the threading indexes of a SQLite database used in the email client K-9 Mail.

## class `com.fsck.k9.mailstore.migrations.MigrationTo33`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo33` is to provide a database migration that adds a preview column to the messages table in an SQLite database.

This class contains the following public method(s):

- `addPreviewColumn(android.database.sqlite.SQLiteDatabase)` -- The method adds a new column called 'preview' of type TEXT to the 'messages' table in an SQLite database.

## class `com.fsck.k9.mailstore.migrations.MigrationTo43`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo43` is to provide a migration to version 43 of the K-9 Mail application's mailstore, including updating and moving outdated folders.

This class contains the following public method(s):

- `fixOutboxFolders(android.database.sqlite.SQLiteDatabase,com.fsck.k9.mailstore.migrations.MigrationsHelper)` -- This method renames an outdated "OUTBOX" folder and moves any messages in an obsolete localized outbox folder to the drafts folder.

## class `com.fsck.k9.mailstore.migrations.MigrationTo46`

The purpose of `com.fsck.k9.mailstore.migrations.MigrationTo46` is to perform the necessary database migration operations to upgrade the K-9 Mail app's database schema from version 45 to version 46.

This class contains the following public method(s):

- `addMessagesFlagColumns(android.database.sqlite.SQLiteDatabase,com.fsck.k9.mailstore.migrations.MigrationsHelper)` -- The method adds four columns to the "messages" table in an SQLite database and populates them with message flags from the "flags" column.

## class `com.fsck.k9.mailstore.migrations.MigrationTo39`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo39` is to migrate the database schema of the K-9 mail client to version 39.

This class contains the following public method(s):

- `headersPruneOrphans(android.database.sqlite.SQLiteDatabase)` -- The method removes orphaned header data from the database.

## class `com.fsck.k9.mailstore.migrations.MigrationTo51$MimeStructureState`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo51$MimeStructureState` is to represent the state of a MIME structure during a migration process in the email client K-9.

This class contains the following public method(s):

- `applyValues(android.content.ContentValues)` -- The method applies the values of the current MimeStructureState to a ContentValues object.
- `popParent()` -- The method pops the current parent node from the MIME structure state stack and returns the previous parent node.
- `nextMultipartChild(long)` -- The `nextMultipartChild(long)` method returns a new `MimeStructureState` object with the specified `newPartId` and updates the state of the object.
- `getNewRootState()` -- The method returns a new instance of `MimeStructureState` with default values.
- `nextChild(long)` -- This method returns a new instance of `MimeStructureState` representing the next child part in the MIME structure.

## interface `com.fsck.k9.mailstore.migrations.MigrationsHelper`

The purpose of the `com.fsck.k9.mailstore.migrations.MigrationsHelper` interface is to provide helper methods and access to objects necessary for migrating K-9 mail data.

This class contains the following public method(s):

- `getLocalStore()` -- This method returns the local email storage repository.
- `getStorage()` -- This method returns the storage object for K-9 mail.
- `getContext()` -- The method returns the Android context of the current application.
- `serializeFlags(java.util.List)` -- The method serializes a list of mail flags into a string representation.
- `getAccount()` -- This method retrieves the K-9 mail account associated with the current migration.

## class `com.fsck.k9.mailstore.migrations.MigrationTo48`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo48` is to migrate the database schema of K-9 Mail app to version 48 by updating the threads table and creating a trigger.

This class contains the following public method(s):

- `updateThreadsSetRootWhereNull(android.database.sqlite.SQLiteDatabase)` -- This method updates the threads table in a SQLite database by setting the root to the id value where root is null and creates a trigger to set the root to the id value where root is null after a new thread is inserted.

## class `com.fsck.k9.mailstore.migrations.MigrationTo53`

The class `com.fsck.k9.mailstore.migrations.MigrationTo53` is a migration class that is used to update the SQLite database schema for K9-Mail to version 53, including removing null values from the "empty" column in the "messages" table.

This class contains the following public method(s):

- `removeNullValuesFromEmptyColumnInMessagesTable(android.database.sqlite.SQLiteDatabase)` -- The method removes null values from the "empty" column in the "messages" table of the specified SQLite database.

## class `com.fsck.k9.mailstore.migrations.MigrationTo50`

The purpose of `com.fsck.k9.mailstore.migrations.MigrationTo50` is to perform a specific migration task in the version 5.0 of the K-9 email client's mailstore database.

This class contains the following public method(s):

- `foldersAddNotifyClassColumn(android.database.sqlite.SQLiteDatabase,com.fsck.k9.mailstore.migrations.MigrationsHelper)` -- This method adds a new column called "notify_class" to the "folders" table in an SQLite database and sets the default value of this column to "INHERITED", then updates the value of "notify_class" for the inbox folder of a given account to "FIRST_CLASS".

## class `com.fsck.k9.mailstore.migrations.MigrationTo41`

The class `com.fsck.k9.mailstore.migrations.MigrationTo41` is responsible for performing database migrations and updating folder metadata in an SQLite database for use in K-9 Mail version 4.1.

This class contains the following public method(s):

- `db41FoldersAddClassColumns(android.database.sqlite.SQLiteDatabase)` -- This method adds five new columns to the "folders" table in an SQLite database for use in K-9 Mail version 4.1.
- `db41UpdateFolderMetadata(android.database.sqlite.SQLiteDatabase,com.fsck.k9.mailstore.migrations.MigrationsHelper)` -- The method updates folder metadata in an SQLite database for a specific version of an email client.

## class `com.fsck.k9.mailstore.migrations.MigrationTo49`

The class `com.fsck.k9.mailstore.migrations.MigrationTo49` is responsible for performing a database migration to version 49 of the K-9 mail client, which includes creating a composite index on the messages table.

This class contains the following public method(s):

- `createMsgCompositeIndex(android.database.sqlite.SQLiteDatabase)` -- The method creates a composite index on the messages table in a SQLite database to improve performance when querying messages.

## class `com.fsck.k9.mailstore.migrations.Migrations`

The purpose of the class `com.fsck.k9.mailstore.migrations.Migrations` is to provide methods for upgrading the K-9 Mail database.

This class contains the following public method(s):

- `upgradeDatabase(android.database.sqlite.SQLiteDatabase,com.fsck.k9.mailstore.migrations.MigrationsHelper)` -- This method is responsible for upgrading the K-9 Mail database by applying migration steps according to the current database version.

## class `com.fsck.k9.mailstore.migrations.MigrationTo47`

The purpose of `com.fsck.k9.mailstore.migrations.MigrationTo47` is to perform a database migration for K-9 Mail application, specifically migrating the database schema to version 47.

This class contains the following public method(s):

- `createThreadsTable(android.database.sqlite.SQLiteDatabase)` -- This method creates a new 'threads' table, creates indices for the new table, copies thread structure from the 'messages' table to the 'threads' table, removes indices for old thread-related columns in the 'messages' table, and clears out old thread-related columns in the 'messages' table.

## class `com.fsck.k9.mailstore.migrations.MigrationTo31`

The purpose of the `com.fsck.k9.mailstore.migrations.MigrationTo31` class is to perform a migration to version 31 of the SQLite database used by the K-9 Mail email client.

This class contains the following public method(s):

- `changeMsgFolderIdDeletedDateIndex(android.database.sqlite.SQLiteDatabase)` -- The method changes the index of a SQLite database table for email messages by dropping a previous index and creating a new index based on the folder ID, deletion status, and internal date of the messages.

## class `com.fsck.k9.mailstore.migrations.MigrationTo30`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo30` is to handle the migration of the mail store database schema from version 29 to version 30 by adding a "deleted" column to the "messages" table.

This class contains the following public method(s):

- `addDeletedColumn(android.database.sqlite.SQLiteDatabase)` -- The purpose of this method is to add a new column called "deleted" with a default value of 0 to the "messages" table of the given SQLiteDatabase object.

## class `com.fsck.k9.mailstore.migrations.MigrationTo34`

The purpose of the class `com.fsck.k9.mailstore.migrations.MigrationTo34` is to migrate an SQLite database by adding a new column called "flagged_count" to the "folders" table with a default value of 0.

This class contains the following public method(s):

- `addFlaggedCountColumn(android.database.sqlite.SQLiteDatabase)` -- This method adds a new column called "flagged_count" to the "folders" table in an SQLite database, with a default value of 0.


# package `com.fsck.k9.mailstore.util`

The `com.fsck.k9.mailstore.util` package provides utility classes related to managing and manipulating email messages, including creating files, efficiently storing data, and encoding and decoding text messages in accordance with RFC 2646.

This package contains the following class(es):

## class `com.fsck.k9.mailstore.util.DeferredFileOutputStream`

The class `com.fsck.k9.mailstore.util.DeferredFileOutputStream` is used to write data to an OutputStream that is stored either in memory or in a file, and allows access to the data in both cases.

This class contains the following public method(s):

- `getData()` -- This method returns the data stored in the ByteArrayOutputStream if the OutputStream is memory-backed.
- `getFile()` -- Returns the file object associated with the output stream.

## interface `com.fsck.k9.mailstore.util.FileFactory`

The purpose of the `com.fsck.k9.mailstore.util.FileFactory` interface is to provide a way for creating new files in a file system.

This class contains the following public method(s):

- `createFile()` -- The method creates a new file in the file system and returns the `File` object representing it.

## class `com.fsck.k9.mailstore.util.FlowedMessageUtils`

The purpose of `com.fsck.k9.mailstore.util.FlowedMessageUtils` is to encode and decode text messages in accordance with RFC 2646 and check character specifications to ensure the message is formatted correctly.

This class contains the following public method(s):

- `deflow(java.lang.String,boolean)` -- The `deflow` method decodes a text that has been wrapped using "format=flowed".
- `flow(java.lang.String,boolean)` -- The method encodes a text using the standard flowed-format with optional deletion of trailing spaces.
- `flow(java.lang.String,boolean,int)` -- This Java method decodes a text message encoded in accordance with RFC 2646, by reformatting and wrapping each line to fit within specified width limits, while accounting for any quoted text or additional formatting characters.
- `isAlphaChar(java.lang.String,int)` -- The method checks whether a specified character in a string is part of a word, based on RFC guidelines.


# package `com.fsck.k9.message`

The `com.fsck.k9.message` package provides classes and interfaces for constructing and manipulating email messages in the K-9 Mail application for Android, including message builders, Autocrypt status handlers, and identity parsers.

This package contains the following class(es):

## class `com.fsck.k9.message.IdentityHeaderBuilder`

The `com.fsck.k9.message.IdentityHeaderBuilder` class generates metadata about a draft email message, including information about the sender's identity, message format, quoted text mode, and signature.

This class contains the following public method(s):

- `setQuoteTextMode(com.fsck.k9.message.QuotedTextMode)` -- This method sets the `quotedTextMode` property of the `IdentityHeaderBuilder` object.
- `setIdentity(com.fsck.k9.Identity)` -- The method sets the identity for the header builder and returns the builder for further modification.
- `setMessageFormat(com.fsck.k9.message.SimpleMessageFormat)` -- This method sets the format of the message to be used by the IdentityHeaderBuilder.
- `setQuotedHtmlContent(com.fsck.k9.message.quote.InsertableHtmlContent)` -- This method sets the quoted HTML content of an email message.
- `setCursorPosition(int)` -- The method sets the current position (cursor position) of the IdentityHeaderBuilder object.
- `setSignature(java.lang.String)` -- The method sets the signature of the email sender in the IdentityHeaderBuilder object.
- `build()` -- The `build()` method generates a URL-encoded key/value pair string containing metadata about a draft message.
- `setIdentityChanged(boolean)` -- The method sets a boolean value indicating if the identity header of an email message has been changed.
- `setMessageReference(com.fsck.k9.activity.MessageReference)` -- This method sets the message reference for the IdentityHeaderBuilder.
- `setQuoteStyle(com.fsck.k9.Account$QuoteStyle)` -- The method sets the quote style for the identity header of an email message.
- `setBodyPlain(com.fsck.k9.mail.internet.TextBody)` -- The method sets the plain text body of an email message for an identity header builder.
- `setBody(com.fsck.k9.mail.internet.TextBody)` -- The method sets the body of the email message for the identity header builder.
- `setSignatureChanged(boolean)` -- The method sets a boolean value indicating whether the signature of the email content has changed or not.

## interface `com.fsck.k9.message.MessageBuilder$Callback`

The interface `com.fsck.k9.message.MessageBuilder$Callback` is used to handle events during the building of an email message, such as successful completion, cancellation, exceptions, and the return of a pending intent.

This class contains the following public method(s):

- `onMessageBuildCancel()` -- This method is called upon cancellation of the message building process.
- `onMessageBuildReturnPendingIntent(android.app.PendingIntent,int)` -- This method is called by the message builder when it has built a message and returns a pending intent with a request code.
- `onMessageBuildException(com.fsck.k9.mail.MessagingException)` -- The method is called when an exception occurs during the building of an email message.
- `onMessageBuildSuccess(com.fsck.k9.mail.internet.MimeMessage,boolean)` -- The method is called when a message is successfully built and allows for further processing of the built message.

## class `com.fsck.k9.message.SimpleMessageBuilder`

The purpose of `com.fsck.k9.message.SimpleMessageBuilder` class is to create and build simple email messages.

This class contains the following public method(s):

- `newInstance()` -- This method creates a new instance of `SimpleMessageBuilder` with a message ID generator and boundary generator initialized.

## class `com.fsck.k9.message.AutocryptStatusInteractor$RecipientAutocryptStatus`

The class `com.fsck.k9.message.AutocryptStatusInteractor$RecipientAutocryptStatus` is used to represent the Autocrypt status of a recipient in the K-9 Mail application, with this specific method checking if there is a pending intent for the recipient's status notification.

This class contains the following public method(s):

- `hasPendingIntent()` -- This method checks if there is a pending intent set for this recipient's Autocrypt status notification.

## class `com.fsck.k9.message.PgpMessageBuilder`

The purpose of the `com.fsck.k9.message.PgpMessageBuilder` Java class is to provide methods for building PGP messages, setting encryption status and choosing the OpenPGP API used for encryption and decryption operations.

This class contains the following public method(s):

- `buildMessageOnActivityResult(int,android.content.Intent)` -- The method builds a PGP message from user interaction result and handles errors if no mime message is currently being processed.
- `setCryptoStatus(com.fsck.k9.activity.compose.ComposeCryptoStatus)` -- The method sets the status of the message's encryption status during composition.
- `setOpenPgpApi(org.openintents.openpgp.util.OpenPgpApi)` -- Sets the OpenPGP API to be used for encryption and decryption operations.
- `newInstance()` -- The method creates a new instance of `PgpMessageBuilder` with necessary dependencies.

## class `com.fsck.k9.message.ComposePgpEnableByDefaultDecider`

The purpose of the class `com.fsck.k9.message.ComposePgpEnableByDefaultDecider` is to determine whether a message should be encrypted by default.

This class contains the following public method(s):

- `shouldEncryptByDefault(com.fsck.k9.mail.Message)` -- The method returns true if the given message is encrypted, otherwise it returns false by default.

## class `com.fsck.k9.message.ComposePgpInlineDecider`

The purpose of the `ComposePgpInlineDecider` class is to determine if a given email message should be replied to with PGP inline encryption based on the presence of PGP inline parts in the message.

This class contains the following public method(s):

- `shouldReplyInline(com.fsck.k9.mail.Message)` -- The purpose of the `shouldReplyInline` method is to determine if a given email message should be replied to with PGP inline encryption based on whether the message has PGP inline parts.

## enum `com.fsck.k9.message.AutocryptStatusInteractor$RecipientAutocryptStatusType`

The enum defines different types of Autocrypt status for a recipient and provides methods to check if encryption is possible, if the status is mutual, and if it has been confirmed.

This class contains the following public method(s):

- `canEncrypt()` -- The method returns a boolean indicating if encryption is possible for the recipient's Autocrypt status.
- `isMutual()` -- The method checks if the Autocrypt status of a recipient is mutual.
- `isConfirmed()` -- The method returns a boolean indicating if the Autocrypt status for a recipient has been confirmed.

## enum `com.fsck.k9.message.IdentityField`

The enum `com.fsck.k9.message.IdentityField` is used to represent fields in email headers that contain unique identifiers for message tracking or identification.

This class contains the following public method(s):

- `getIntegerFields()` -- The method returns an array of IdentityFields that should be integer values and are sanity checked for integer-ness during decoding.
- `value()` -- This method returns the string value associated with the enum constant.

## class `com.fsck.k9.message.TextBodyBuilder`

The purpose of `com.fsck.k9.message.TextBodyBuilder` is to build a message body for an email, including options for adding quoted text, signatures, and HTML formatting.

This class contains the following public method(s):

- `setAppendSignature(boolean)` -- This method sets whether or not to append a signature to the message body.
- `buildTextPlain()` -- The `buildTextPlain()` method builds a TextBody object that contains the entered text and possibly the quoted original message, with options to add a signature and set the composed message length and offset.
- `setQuotedText(java.lang.String)` -- This method sets the quoted text to be included in the email message body being built.
- `setInsertSeparator(boolean)` -- This method sets the boolean flag indicating whether a separator should be inserted before adding new text to the message body.
- `setReplyAfterQuote(boolean)` -- The method sets a boolean value indicating whether a reply should be placed after a quote in the `TextBodyBuilder`.
- `buildTextHtml()` -- The method builds a TextBody object that contains the entered text of a message (possibly including quoted text from a previous message) in HTML format.
- `setIncludeQuotedText(boolean)` -- The method sets a flag indicating whether or not to include quoted text when building a text body.
- `setQuotedTextHtml(com.fsck.k9.message.quote.InsertableHtmlContent)` -- This method sets the HTML content of quoted text in an email message.
- `setSignature(java.lang.String)` -- This method sets the signature for the email.
- `setSignatureBeforeQuotedText(boolean)` -- Sets whether the signature should be placed before or after the quoted text in the email body.

## class `com.fsck.k9.message.AutocryptStatusInteractor`

The purpose of the class `com.fsck.k9.message.AutocryptStatusInteractor` is to provide an interface for retrieving the Autocrypt status of recipients from an OpenPGP API.

This class contains the following public method(s):

- `getInstance()` -- The method returns an instance of the `AutocryptStatusInteractor` singleton class.
- `retrieveCryptoProviderRecipientStatus(org.openintents.openpgp.util.OpenPgpApi,java.lang.String[])` -- The `retrieveCryptoProviderRecipientStatus` method retrieves the Autocrypt status of recipients from an OpenPGP API.

## class `com.fsck.k9.message.IdentityHeaderParser`

The purpose of `com.fsck.k9.message.IdentityHeaderParser` is to parse an identity string into a map of values for each field.

This class contains the following public method(s):

- `parse(java.lang.String)` -- The method parses an identity string into a map of values for each field.

## abstract class `com.fsck.k9.message.MessageBuilder`

The purpose of the abstract class `com.fsck.k9.message.MessageBuilder` is to provide a way to construct email messages with various options and settings, such as recipients, subject, and quoted text, in the K-9 email client for Android.

This class contains the following public method(s):

- `setSubject(java.lang.String)` -- The method sets the subject of the email message being built by the MessageBuilder object.
- `setCc(java.util.List)` -- The method sets the CC recipients of the email message being built.
- `setRequestReadReceipt(boolean)` -- Sets whether a read receipt should be requested for the email being built.
- `setCursorPosition(int)` -- The method sets the cursor position of the message being built.
- `setReplyAfterQuote(boolean)` -- The method sets whether the reply text should be placed after the quoted original message in an email reply.
- `setQuotedHtmlContent(com.fsck.k9.message.quote.InsertableHtmlContent)` -- Sets the quoted HTML content of a message being built.
- `setInReplyTo(java.lang.String)` -- The method sets the message ID of the parent message that the current message is a reply to.
- `setBcc(java.util.List)` -- The method sets the Bcc recipients for the email message being built.
- `setSignature(java.lang.String)` -- The method sets the signature of the email message being built.
- `setSignatureChanged(boolean)` -- The method sets a boolean value indicating if the signature of the message has been changed.
- `setIsPgpInlineEnabled(boolean)` -- The method sets whether PGP inline encryption is enabled or not for the message being built.
- `setIdentity(com.fsck.k9.Identity)` -- The method sets the identity information for the message being built.
- `setAttachments(java.util.List)` -- The method sets the list of attachments for the email being built.
- `setMessageReference(com.fsck.k9.activity.MessageReference)` -- Sets the message reference for the message being built.
- `reattachCallback(com.fsck.k9.message.MessageBuilder$Callback)` -- The method attaches a new callback for delivering results of a computation, but only after previously detaching one, and delivers the result immediately if the computation finished while the callback was detached.
- `setSentDate(java.util.Date)` -- The method sets the sent date of the email message being built.
- `buildAsync(com.fsck.k9.message.MessageBuilder$Callback)` -- This method asynchronously builds a message and calls a callback method on the UI thread when it finishes.
- `setReferences(java.lang.String)` -- The method sets the "References" header field of the email message being built.
- `setDraft(boolean)` -- The purpose of the method is to set whether the email message being built should be marked as a draft or not.
- `setQuotedText(java.lang.String)` -- The method sets the quoted text of the message being constructed.
- `setSignatureBeforeQuotedText(boolean)` -- This method sets whether the signature should be placed before or after the quoted text in the email message.
- `onActivityResult(int,int,android.content.Intent,com.fsck.k9.message.MessageBuilder$Callback)` -- This method handles the result of an activity and asynchronously builds a message based on the received data.
- `detachCallback()` -- The method detaches the callback temporarily and delivers any result upon reattachment.
- `isDraft()` -- To determine whether the email message being built is a draft or not.
- `setQuoteStyle(com.fsck.k9.Account$QuoteStyle)` -- The purpose of this method is to set the quote style for the message being built.
- `setIdentityChanged(boolean)` -- The method sets a boolean indicating whether the identity of the message has been changed.
- `setMessageFormat(com.fsck.k9.message.SimpleMessageFormat)` -- The method sets the format of the message to be built by the MessageBuilder.
- `setHideTimeZone(boolean)` -- The method sets whether or not to hide the time zone when building a message in the K-9 email client.
- `setText(java.lang.String)` -- This method sets the text of the message being built.
- `setTo(java.util.List)` -- This method sets the list of recipients for the email message.
- `setQuotedTextMode(com.fsck.k9.message.QuotedTextMode)` -- This method sets the mode for quoting text in an email message.


# package `com.fsck.k9.message.extractors`

The purpose of the package `com.fsck.k9.message.extractors` is to extract and manipulate different types of content from email messages, including text, attachments, and encryption, in the K-9 mail client.

This package contains the following class(es):

## class `com.fsck.k9.message.extractors.MessagePreviewCreator`

The purpose of the class `com.fsck.k9.message.extractors.MessagePreviewCreator` is to create a preview of a given email message, extracting its text if it is not encrypted.

This class contains the following public method(s):

- `createPreview(com.fsck.k9.mail.Message)` -- The method creates a preview of a given email message by checking if it's encrypted and extracting its text if not.
- `newInstance()` -- This method creates a new instance of `MessagePreviewCreator` with instances of `TextPartFinder`, `PreviewTextExtractor`, and `EncryptionDetector` initialized as dependencies.

## class `com.fsck.k9.message.extractors.EncryptionDetector`

The purpose of `com.fsck.k9.message.extractors.EncryptionDetector` is to detect whether an email message is encrypted with PGP/MIME or S/MIME or contains inline PGP encrypted text.

This class contains the following public method(s):

- `isEncrypted(com.fsck.k9.mail.Message)` -- The method checks whether the given email message is encrypted with PGP/MIME or S/MIME or contains inline PGP encrypted text.

## class `com.fsck.k9.message.extractors.AttachmentCounter`

The purpose of the class is to count the number of attachments in a given email message, excluding encrypted messages, and provide a way to create new instances of the class with a different `EncryptionDetector` object.

This class contains the following public method(s):

- `getAttachmentCount(com.fsck.k9.mail.Message)` -- The method returns the number of attachments in a given email message, except for encrypted messages which are assumed to have no attachments.
- `newInstance()` -- To create a new instance of the `AttachmentCounter` class with a new `EncryptionDetector` object.

## class `com.fsck.k9.message.extractors.AttachmentInfoExtractor`

The `AttachmentInfoExtractor` class is used to extract information about email attachments, including their URI, size, and content availability, for use in a database or to be displayed in a view.

This class contains the following public method(s):

- `extractAttachmentInfoForDatabase(com.fsck.k9.mail.Part)` -- The method extracts attachment information from an email part for use in a database.
- `getInstance()` -- The method returns a singleton instance of the AttachmentInfoExtractor class with the application context.
- `extractAttachmentInfo(com.fsck.k9.mail.Part)` -- The method extracts information about an email attachment, including its URI, size and content availability.
- `extractAttachmentInfoForView(java.util.List)` -- This method extracts information about attachments in an email message and returns a list of AttachmentViewInfo objects.

## class `com.fsck.k9.message.extractors.PreviewTextExtractor`

The purpose of the `com.fsck.k9.message.extractors.PreviewTextExtractor` class is to extract a plain text preview from a mail `Part` object.

This class contains the following public method(s):

- `extractPreview(com.fsck.k9.mail.Part)` -- The `extractPreview` method extracts a plain text preview from a mail `Part` object.

## class `com.fsck.k9.message.extractors.TextPartFinder`

The purpose of the `com.fsck.k9.message.extractors.TextPartFinder` class is to locate and extract the first text part from an email part.

This class contains the following public method(s):

- `findFirstTextPart(com.fsck.k9.mail.Part)` -- This method finds the first text part in a given email part.

## class `com.fsck.k9.message.extractors.BodyTextExtractor`

The purpose of the `com.fsck.k9.message.extractors.BodyTextExtractor` class is to extract the body text from message parts in a desired message format while handling conversion between HTML and plain text if needed.

This class contains the following public method(s):

- `getBodyTextFromMessage(com.fsck.k9.mail.Part,com.fsck.k9.message.SimpleMessageFormat)` -- The method retrieves the body text from a message part in the desired message format, handling conversions between HTML and plain text if necessary.

## class `com.fsck.k9.message.extractors.PreviewResult`

The purpose of the class `com.fsck.k9.message.extractors.PreviewResult` in the K-9 mail client is to provide a way to extract and handle different types of preview content from email messages, including text, encrypted content, and errors.

This class contains the following public method(s):

- `text(java.lang.String)` -- This method creates a new PreviewResult object with the PreviewType.TEXT type and a given previewText.
- `encrypted()` -- The method returns a PreviewResult object with a PreviewType of ENCRYPTED and null content.
- `getPreviewType()` -- This method returns the preview type of a message from the `PreviewResult` class in the K-9 mail client.
- `none()` -- The method returns a PreviewResult object with type set to NONE and null as the content.
- `isPreviewTextAvailable()` -- This method determines if a preview text is available in the given PreviewResult object.
- `error()` -- The `error()` method returns a new `PreviewResult` object with a preview type of `ERROR` and a null content.
- `getPreviewText()` -- The method returns the preview text of a message and throws an exception if the preview text is not available.

## class `com.fsck.k9.message.extractors.MessageFulltextCreator`

The class is responsible for creating the fulltext of a message by extracting its plain text, but only if the message is not encrypted.

This class contains the following public method(s):

- `newInstance()` -- The method creates a new instance of `com.fsck.k9.message.extractors.MessageFulltextCreator` with a new `TextPartFinder` and `EncryptionDetector` object.
- `createFulltext(com.fsck.k9.mail.Message)` -- The method creates the fulltext of a message by extracting its plain text, unless the message is encrypted.


# package `com.fsck.k9.message.html`

The `com.fsck.k9.message.html` package provides classes for processing, linkifying, sanitizing, and converting HTML content into plain text or displayable HTML format for email messages.

This package contains the following class(es):

## class `com.fsck.k9.message.html.HtmlProcessor`

The class `com.fsck.k9.message.html.HtmlProcessor` is responsible for processing HTML content by removing formatting and sanitizing the content for display.

This class contains the following public method(s):

- `toCompactString(org.jsoup.nodes.Document)` -- The method converts an HTML document into a compact string format by removing all formatting and indentation.
- `newInstance()` -- The method creates a new instance of `HtmlProcessor` with a new instance of `HtmlSanitizer` as its argument.
- `processForDisplay(java.lang.String)` -- The method sanitizes, modifies, and returns a compact version of an HTML string for display.

## class `com.fsck.k9.message.html.UriLinkifier`

The class `com.fsck.k9.message.html.UriLinkifier` is used to convert URIs within a given string of text into clickable links.

This class contains the following public method(s):

- `linkifyText(java.lang.String,java.lang.StringBuffer)` -- The method is used to identify and convert URIs within a given string of text into clickable links.

## interface `com.fsck.k9.message.html.UriParser`

The `com.fsck.k9.message.html.UriParser` interface is used for parsing and linkifying scheme specific URIs found in a given string. It provides a method to linkify a URI starting from a specified position and write the result to a given buffer.

This class contains the following public method(s):

- `linkifyUri(java.lang.String,int,java.lang.StringBuffer)` -- This method parses and linkifies a scheme specific URI found in a given string starting from a specified position, and writes the result to a given buffer.

## class `com.fsck.k9.message.html.HeadCleaner`

The purpose of the `HeadCleaner` class is to provide a method for cleaning the `<head>` section of an HTML document by copying safe nodes from a dirty document to a cleaned document.

This class contains the following public method(s):

- `clean(org.jsoup.nodes.Document,org.jsoup.nodes.Document)` -- The method cleans the `<head>` section of an HTML document by copying safe nodes from a dirty document to a cleaned document.

## class `com.fsck.k9.message.html.HttpUriParser`

The purpose of the class `com.fsck.k9.message.html.HttpUriParser` is to parse HTTP/HTTPS/RTSP URIs and add HTML anchor tags to them for display in an email message.

This class contains the following public method(s):

- `linkifyUri(java.lang.String,int,java.lang.StringBuffer)` -- The method takes a text string, parses any HTTP/HTTPS/RTSP URIs in it, and adds HTML anchor tags to them for display in an email message.

## class `com.fsck.k9.message.html.HtmlConverter`

The purpose of the class `com.fsck.k9.message.html.HtmlConverter` is to convert plain text to HTML, HTML to plain text, and convert emojis in HTML strings to corresponding image tags.

This class contains the following public method(s):

- `wrapMessageContent(java.lang.CharSequence)` -- The purpose of the method is to wrap the given message content in HTML markup that includes a viewport meta tag and CSS styles.
- `textToHtml(java.lang.String)` -- The method converts a plain text string into an HTML string with smart replacement for large documents to prevent OOM errors.
- `textToHtmlFragment(java.lang.String)` -- The method converts a plain text string into an HTML fragment by escaping entities, linkifying the text, and adding newlines and unescaping.
- `htmlToText(java.lang.String)` -- The method converts an HTML string to a plain text string.
- `wrapStatusMessage(java.lang.CharSequence)` -- This method wraps the given status message in an HTML div element with a center aligned and grey colored text style.
- `convertEmoji2Img(java.lang.String)` -- The purpose of the method is to convert emojis in a given HTML string to corresponding image tags.
- `htmlToSpanned(java.lang.String)` -- The `htmlToSpanned` method converts HTML to a formatted `Spanned` object that can be used in a `TextView`.

## class `com.fsck.k9.message.html.EthereumUriParser`

The class `com.fsck.k9.message.html.EthereumUriParser` is responsible for parsing Ethereum URIs in a text and converting them into clickable HTML links.

This class contains the following public method(s):

- `linkifyUri(java.lang.String,int,java.lang.StringBuffer)` -- The method `linkifyUri` searches for Ethereum URIs in a given text and converts them into HTML links with a customizable output buffer.

## class `com.fsck.k9.message.html.BitcoinUriParser`

The purpose of the class `com.fsck.k9.message.html.BitcoinUriParser` is to parse Bitcoin URIs within a text and replace them with HTML hyperlinks.

This class contains the following public method(s):

- `linkifyUri(java.lang.String,int,java.lang.StringBuffer)` -- The method parses a Bitcoin URI within a given text and replaces it with an HTML hyperlink.

## class `com.fsck.k9.message.html.HtmlSanitizer`

(no description)

This class contains the following public method(s):

- `sanitize(java.lang.String)` -- The method sanitizes an HTML string by parsing and cleaning it using JSoup and returns a cleaned document object.

## class `com.fsck.k9.message.html.HeadCleaner$CleaningVisitor`

The purpose of the `com.fsck.k9.message.html.HeadCleaner$CleaningVisitor` class is to visit and clean HTML nodes, ensuring that only safe elements and their attributes are preserved while ignoring unsafe elements and their sub-elements.

This class contains the following public method(s):

- `tail(org.jsoup.nodes.Node,int)` -- The `tail` method updates the `destination` node by moving up one level in the HTML document hierarchy and allowing further parsing of its children.
- `head(org.jsoup.nodes.Node,int)` -- The `head` method is responsible for cleaning and copying safe HTML elements and their attributes from the source to the destination while ignoring unsafe elements and their sub-elements.

## class `com.fsck.k9.message.html.HtmlConverter$ListTagHandler`

The class `com.fsck.k9.message.html.HtmlConverter$ListTagHandler` handles the parsing of list tags in HTML and converts them into a formatted text representation.

This class contains the following public method(s):

- `handleTag(boolean,java.lang.String,android.text.Editable,org.xml.sax.XMLReader)` -- This method handles the parsing of list tags in HTML and converts them into a formatted text representation.

## class `com.fsck.k9.message.html.HtmlConverter$HtmlToTextTagHandler`

The `com.fsck.k9.message.html.HtmlConverter$HtmlToTextTagHandler` class is used to convert HTML tags to their corresponding plain text format in Java.

This class contains the following public method(s):

- `handleTag(boolean,java.lang.String,android.text.Editable,org.xml.sax.XMLReader)` -- This method handles the conversion of HTML tags to their corresponding plain text format, such as replacing an <hr> tag with a line of underscores.


# package `com.fsck.k9.message.quote`

The package `com.fsck.k9.message.quote` provides functionality for quoting and manipulating HTML and text content in email messages.

This package contains the following class(es):

## class `com.fsck.k9.message.quote.InsertableHtmlContent`

The purpose of the class is to provide functionality for inserting and manipulating HTML content in email messages, specifically for quoting and inserting user content.

This class contains the following public method(s):

- `setUserContent(java.lang.String)` -- The method sets the inserted content to the specified content and replaces anything currently in the inserted content buffer.
- `toDebugString()` -- The method `toDebugString()` returns a string containing debugging information about an `InsertableHtmlContent` object.
- `setQuotedContent(java.lang.StringBuilder)` -- This method sets the quoted content for an insertion point in a StringBuilder.
- `setHeaderInsertionPoint(int)` -- This method sets the position to insert HTML content into the header of an email message, and if the position is invalid, it defaults to the beginning of the message.
- `getInsertionPoint()` -- The method returns the insertion point based on the quote style.
- `getFooterInsertionPoint()` -- The method returns the insertion point for a footer in an HTML content.
- `setFooterInsertionPoint(int)` -- The method sets the insertion point of the footer in the HTML content.
- `getQuotedContent()` -- The method returns the quoted content as a string.
- `insertIntoQuotedHeader(java.lang.String)` -- The `insertIntoQuotedHeader` method is used to insert reply/forward headers into the quoted content header of an email message.
- `toString()` -- The method `toString()` builds a string by inserting user content into quoted content and then deleting the original quoted content at the insertion point.
- `insertIntoQuotedFooter(java.lang.String)` -- This method inserts content into the footer of quoted email messages.
- `clearQuotedContent()` -- The `clearQuotedContent()` method removes all quoted content from the HTML message.
- `setInsertionLocation(com.fsck.k9.message.quote.InsertableHtmlContent$InsertionLocation)` -- The method sets the location where user content should be inserted in relation to the quoted content.

## class `com.fsck.k9.message.quote.TextQuoteCreator`

The class `com.fsck.k9.message.quote.TextQuoteCreator` adds quoting markup to a text message based on the provided quote style and prefix.

This class contains the following public method(s):

- `quoteOriginalTextMessage(android.content.res.Resources,com.fsck.k9.mail.Message,java.lang.String,com.fsck.k9.Account$QuoteStyle,java.lang.String)` -- This method adds quoting markup to a text message based on the provided quote style and prefix.

## class `com.fsck.k9.message.quote.HtmlQuoteCreator`

The `com.fsck.k9.message.quote.HtmlQuoteCreator` class provides functionality to add quoting markup to a HTML message based on a specified quote style.

This class contains the following public method(s):

- `quoteOriginalHtmlMessage(android.content.res.Resources,com.fsck.k9.mail.Message,java.lang.String,com.fsck.k9.Account$QuoteStyle)` -- This method adds quoting markup to a HTML message based on a specified quote style.


# package `com.fsck.k9.message.signature`

The `com.fsck.k9.message.signature` package provides classes for removing email signatures from both HTML and text messages.

This package contains the following class(es):

## class `com.fsck.k9.message.signature.HtmlSignatureRemover`

The purpose of the class `com.fsck.k9.message.signature.HtmlSignatureRemover` is to provide a method that can remove the signature from an HTML email.

This class contains the following public method(s):

- `stripSignature(java.lang.String)` -- This method strips the signature from an HTML email.

## class `com.fsck.k9.message.signature.HtmlSignatureRemover$StripSignatureFilter`

The purpose of the class `com.fsck.k9.message.signature.HtmlSignatureRemover$StripSignatureFilter` is to remove HTML email signatures from email messages.

This class contains the following public method(s):

- `head(org.jsoup.nodes.Node,int)` -- This method filters out HTML elements and text nodes that are part of an email signature in order to remove it from an email message.
- `tail(org.jsoup.nodes.Node,int)` -- The `tail` method decides whether to continue filtering the "tail" of a HTML node, based on whether a signature has been found and the type of element encountered.

## class `com.fsck.k9.message.signature.TextSignatureRemover`

The purpose of the `com.fsck.k9.message.signature.TextSignatureRemover` class is to remove signatures from text content that matches a specific pattern.

This class contains the following public method(s):

- `stripSignature(java.lang.String)` -- This method removes the signature from the given content if it matches a specific pattern.


# package `com.fsck.k9.ui`

The package `com.fsck.k9.ui` contains classes that provide user interface functionality for the K-9 email client, including an EditText view for converting line endings and a class for displaying and interacting with contact information.

This package contains the following class(es):

## class `com.fsck.k9.ui.EolConvertingEditText`

The purpose of the class `com.fsck.k9.ui.EolConvertingEditText` is to provide an EditText view that automatically converts line endings between "\r\n" and "\n" based on the platform.

This class contains the following public method(s):

- `setCharacters(java.lang.CharSequence)` -- This method sets the string value of the EolConvertingEditText while converting any line endings to "\n".
- `getCharacters()` -- The `getCharacters()` method returns the text displayed by the EolConvertingEditText with all line endings converted to `"\r\n"`.

## class `com.fsck.k9.ui.ContactBadge`

The purpose of `com.fsck.k9.ui.ContactBadge` is to provide functionality for displaying and interacting with contact information in an Android user interface, including assigning contacts based on email addresses and showing QuickContact windows.

This class contains the following public method(s):

- `assignContactFromEmail(java.lang.String,boolean,android.os.Bundle)` -- This method assigns a contact based on an email address, performing a lookup query if required, and includes extras for the contact edit page if the contact is not found.
- `assignContactUri(android.net.Uri)` -- The method sets the contact URI associated with a ContactBadge, used for displaying the QuickContact window.
- `onInitializeAccessibilityNodeInfo(android.view.accessibility.AccessibilityNodeInfo)` -- This method sets the class name for an accessibility node info instance to the ContactBadge class.
- `assignContactFromEmail(java.lang.String,boolean)` -- The method assigns a contact to the contact badge based on an email address, and optionally defers the lookup until the badge is clicked.
- `onInitializeAccessibilityEvent(android.view.accessibility.AccessibilityEvent)` -- This method sets the class name of the ContactBadge accessibility event.
- `onClick(android.view.View)` -- This method shows a quick contact view for a contact specified by either URI or email address.


# package `com.fsck.k9.ui.compose`

The `com.fsck.k9.ui.compose` package is responsible for handling the display and processing of quoted messages in the message composition screen of the K-9 Mail application.

This package contains the following class(es):

## class `com.fsck.k9.ui.compose.QuotedMessagePresenter`

The purpose of the `com.fsck.k9.ui.compose.QuotedMessagePresenter` class is to handle the display and processing of quoted messages in the message composition screen of K-9 Mail.

This class contains the following public method(s):

- `populateUIWithQuotedMessage(com.fsck.k9.mailstore.MessageViewInfo,boolean,com.fsck.k9.activity.MessageCompose$Action)` -- This method populates the UI with the quoted text of a message for use in a message composition screen.
- `onRestoreInstanceState(android.os.Bundle)` -- This method restores the state of the QuotedMessagePresenter instance after it has been serialized.
- `onSaveInstanceState(android.os.Bundle)` -- This method saves the state of certain variables in the `QuotedMessagePresenter` class to be restored later, such as the quoted text mode, HTML quote, quoted text format, and whether to force plain text.
- `isForcePlainText()` -- This method returns a boolean value indicating whether or not the text should be displayed as plain text.
- `includeQuotedText()` -- This method returns a boolean indicating whether the quoted text should be included in the composed message or not.
- `processDraftMessage(com.fsck.k9.mailstore.MessageViewInfo,java.util.Map)` -- This method processes a draft message by extracting information about how the message was quoted and its format, and then displays the message content in the compose window.
- `isQuotedTextText()` -- The `isQuotedTextText()` method checks if the quoted text format in the composed message is simple text or not.
- `builderSetProperties(com.fsck.k9.message.MessageBuilder)` -- The method is used to set various properties of a MessageBuilder object to values obtained from the view and account.
- `showOrHideQuotedText(com.fsck.k9.message.QuotedTextMode)` -- The method sets the quoted text mode and shows or hides quoted text based on the chosen mode and format.
- `initFromReplyToMessage(com.fsck.k9.mailstore.MessageViewInfo,com.fsck.k9.activity.MessageCompose$Action)` -- The method initializes the UI with a quoted message when replying to an email message.
- `processMessageToForward(com.fsck.k9.mailstore.MessageViewInfo)` -- The method populates the UI with a quoted message when forwarding an email.
- `onSwitchAccount(com.fsck.k9.Account)` -- The method sets the current account to the one passed as a parameter.

## class `com.fsck.k9.ui.compose.QuotedMessageMvpView`

The purpose of `com.fsck.k9.ui.compose.QuotedMessageMvpView` is to display quoted text in a compose email view and allow users to interact with and modify that text.

This class contains the following public method(s):

- `getQuotedText()` -- This method retrieves quoted text from the view.
- `setMessageContentCursorPosition(int)` -- The method sets the cursor position in the message content view of the QuotedMessageMvpView.
- `addTextChangedListener(android.text.TextWatcher)` -- The method adds a TextWatcher to the QuotedMessageMvpView's mQuotedText field.
- `setQuotedText(java.lang.String)` -- The method sets the quoted text to be displayed in the compose screen of an email client.
- `setOnClickPresenter(com.fsck.k9.ui.compose.QuotedMessagePresenter)` -- Sets the presenter for handling onClick events in the QuotedMessageMvpView.
- `showOrHideQuotedText(com.fsck.k9.message.QuotedTextMode,com.fsck.k9.message.SimpleMessageFormat)` -- The method is used to show or hide quoted text in a compose email view based on the provided mode and format.
- `setMessageContentCharacters(java.lang.String)` -- The method sets the content of the message view with the given text.
- `setFontSizes(com.fsck.k9.FontSizes,int)` -- The method sets the font sizes of the quoted text in an email message.
- `setQuotedHtml(java.lang.String,com.fsck.k9.mailstore.AttachmentResolver)` -- The method sets the quoted content and attachment resolver for a quoted message view in the compose UI.


# package `com.fsck.k9.ui.crypto`

The `com.fsck.k9.ui.crypto` package provides classes and an interface for managing cryptographic operations on email messages in the K-9 Mail application, including adding annotations for encryption and signatures, performing encryption and decryption, and reporting the progress and completion of these operations.

This package contains the following class(es):

## class `com.fsck.k9.ui.crypto.MessageCryptoAnnotations`

This class manages cryptographic annotations for an email message in the K-9 Mail application, which can include information on encryption or signature properties for specific parts of the message.

This class contains the following public method(s):

- `findKeyForAnnotationWithReplacementPart(com.fsck.k9.mail.Part)` -- The method finds the key for a cryptographic annotation with a specified replacement part.
- `isEmpty()` -- This method returns a boolean value indicating whether the annotations of a message are empty or not.
- `get(com.fsck.k9.mail.Part)` -- This method retrieves the `CryptoResultAnnotation` for a given email `Part`.
- `has(com.fsck.k9.mail.Part)` -- This method checks if a given mail part has encryption or signature annotation.
- `put(com.fsck.k9.mail.Part,com.fsck.k9.mailstore.CryptoResultAnnotation)` -- This method adds a CryptoResultAnnotation for a specific Part to the MessageCryptoAnnotations object.

## class `com.fsck.k9.ui.crypto.MessageCryptoHelper`

The class `com.fsck.k9.ui.crypto.MessageCryptoHelper` provides methods for handling cryptography operations on email messages, including encryption and decryption.

This class contains the following public method(s):

- `onActivityResult(int,int,android.content.Intent)` -- This method handles the result of a user interaction with a cryptographic operation in the UI.
- `isConfiguredForOutdatedCryptoProvider()` -- The method checks if the app is configured to use an outdated OpenPGP provider package.
- `cancelIfRunning()` -- The method cancels any running background operation related to message cryptography if there is one.
- `detachCallback()` -- The method detaches the current callback lock from the message crypto helper.
- `asyncStartOrResumeProcessingMessage(com.fsck.k9.mail.Message,com.fsck.k9.ui.crypto.MessageCryptoCallback,org.openintents.openpgp.OpenPgpDecryptionResult,boolean)` -- This method asynchronously processes a given message for encryption and decryption, handling callbacks and caching decryption results as necessary.

## interface `com.fsck.k9.ui.crypto.MessageCryptoCallback`

The purpose of `com.fsck.k9.ui.crypto.MessageCryptoCallback` is to provide a callback for reporting the progress and completion of cryptographic operations performed on a message.

This class contains the following public method(s):

- `startPendingIntentForCryptoHelper(android.content.IntentSender,int,android.content.Intent,int,int,int)` -- Starts a new activity that handles Crypto operations with the given parameters.
- `onCryptoOperationsFinished(com.fsck.k9.ui.crypto.MessageCryptoAnnotations)` -- The method is invoked when all cryptographic operations have completed on a message with the provided annotations.
- `onCryptoHelperProgress(int,int)` -- The method is called to report the current progress of a cryptography operation.


# package `com.fsck.k9.ui.dialog`

The package `com.fsck.k9.ui.dialog` contains classes for creating dialog boxes in the user interface of the K-9 email client.

This package contains the following class(es):


# package `com.fsck.k9.ui.message`

The package `com.fsck.k9.ui.message` provides classes for displaying and loading email messages in the K-9 Mail Android app.

This package contains the following class(es):

## class `com.fsck.k9.ui.message.LocalMessageExtractorLoader`

The purpose of the class `com.fsck.k9.ui.message.LocalMessageExtractorLoader` is to extract message view information for the UI by loading a message and its annotations.

This class contains the following public method(s):

- `isCreatedFor(com.fsck.k9.mailstore.LocalMessage,com.fsck.k9.ui.crypto.MessageCryptoAnnotations)` -- This method checks if the given LocalMessage and MessageCryptoAnnotations were used to create this LocalMessageExtractorLoader.
- `loadInBackground()` -- The method loads a message and its annotations to extract message view information for the UI.
- `deliverResult(com.fsck.k9.mailstore.MessageViewInfo)` -- (no description)

## class `com.fsck.k9.ui.message.LocalMessageLoader`

The purpose of the `com.fsck.k9.ui.message.LocalMessageLoader` class is to provide a loader for loading local email messages from the database in the background.

This class contains the following public method(s):

- `isCreatedFor(com.fsck.k9.activity.MessageReference)` -- The method checks if the provided message reference matches the reference of the loaded local message.
- `loadInBackground()` -- This method loads a local email message from the database in the background.
- `deliverResult(com.fsck.k9.mailstore.LocalMessage)` -- The method delivers the result of a local message loading operation to the loader's client.


# package `com.fsck.k9.ui.messageview`

The overall purpose of the `com.fsck.k9.ui.messageview` package is to provide classes and interfaces for displaying and interacting with email messages, including handling attachments, cryptographic processing, and user actions such as replying and forwarding.

This package contains the following class(es):

## interface `com.fsck.k9.ui.messageview.AttachmentViewCallback`

The `AttachmentViewCallback` interface handles user actions related to attachment viewing and saving in a message view.

This class contains the following public method(s):

- `onViewAttachment(com.fsck.k9.mailstore.AttachmentViewInfo)` -- This method is called when a user clicks on an attachment in a message view.
- `onSaveAttachmentToUserProvidedDirectory(com.fsck.k9.mailstore.AttachmentViewInfo)` -- This method saves an attachment to a directory provided by the user.
- `onSaveAttachment(com.fsck.k9.mailstore.AttachmentViewInfo)` -- The method is called when the user saves an attachment from the message view, and passes the information about the attachment being saved.

## class `com.fsck.k9.ui.messageview.MessageViewFragment`

The `com.fsck.k9.ui.messageview.MessageViewFragment` class is responsible for displaying a single email message in the K9 email client and providing user actions such as replying, forwarding, deleting, and moving the message.

This class contains the following public method(s):

- `onForward()` -- The method forwards a message and passes the message reference and decryption result to a listener.
- `onReplyAll()` -- The purpose of the method is to reply to an email, including all recipients, in the MessageViewFragment of the K9 email client.
- `onResume()` -- This method is called when the activity is resumed and it calls the `onResume()` method of the `messageCryptoPresenter`.
- `enableAttachmentButtons(com.fsck.k9.mailstore.AttachmentViewInfo)` -- Enables the attachment buttons for the given attachment in the message view.
- `onClickShowSecurityWarning()` -- The method shows the security warning details for a message in the MessageViewFragment.
- `canMessageBeMovedToSpam()` -- The purpose of the `canMessageBeMovedToSpam()` method is to determine if a message can be moved to the spam folder based on the current message reference and account settings.
- `onCreateView(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle)` -- The `onCreateView` method inflates the message view layout, initializes message view components such as attachments and flags, and sets listeners for user actions.
- `refreshAttachmentThumbnail(com.fsck.k9.mailstore.AttachmentViewInfo)` -- The method refreshes the thumbnail of an email attachment.
- `allHeadersVisible()` -- This method returns whether all headers are currently visible in the message view.
- `onPendingIntentResult(int,int,android.content.Intent)` -- This method processes the result of a pending intent and delegates handling to the appropriate presenter based on the request code.
- `newInstance(com.fsck.k9.activity.MessageReference)` -- This method creates a new instance of the MessageViewFragment and sets arguments for the given MessageReference.
- `doPositiveClick(int)` -- The `doPositiveClick` method handles the positive button click events of different dialogs and performs the corresponding actions such as deleting or refiling a message.
- `onSaveInstanceState(android.os.Bundle)` -- This method is used to save the state information of the message crypto presenter in the message view fragment.
- `onCopy()` -- The `onCopy()` method is responsible for copying an email message to another folder of the same account.
- `showAttachmentLoadingDialog()` -- The purpose of the `showAttachmentLoadingDialog()` method is to display a loading dialog while attachments are being loaded.
- `getMessageReference()` -- The `getMessageReference()` method retrieves the `MessageReference` object of the currently displayed message in the `MessageViewFragment` class of the K9 email app.
- `isMessageRead()` -- The purpose of this method is to check whether the message has been marked as "seen" or "read".
- `getApplicationContext()` -- This method returns the application context of the MessageViewFragment.
- `isCopyCapable()` -- This method returns a boolean value indicating whether the message is copyable or not.
- `onArchive()` -- The purpose of the method `onArchive()` is to move the currently displayed email message to the archive folder of the account associated with the message view.
- `onToggleAllHeadersView()` -- The method toggles the view of all email headers in the message view.
- `onToggleRead()` -- (no description)
- `onMove()` -- The purpose of the `onMove()` method is to handle the moving of a message to a different folder.
- `onSendAlternate()` -- The purpose of the method is to send an alternate version of the current message via the message controller.
- `onDestroy()` -- The `onDestroy()` method is called when the activity is being destroyed, and it handles cleanup tasks such as canceling the message loader helper, depending on whether the activity is changing configurations.
- `onClickShowCryptoKey()` -- The method calls the `onClickShowCryptoKey()` method of an instance of `messageCryptoPresenter` when a specific button is clicked in the message view.
- `onDelete()` -- The purpose of the method is to handle the deletion of a message, either by showing a confirmation dialog or deleting the message directly.
- `doNegativeClick(int)` -- The method does nothing when the negative button is clicked on a dialog with the given ID.
- `onCreate(android.os.Bundle)` -- The method initializes various variables and sets options for the action bar in the fragment.
- `dialogCancelled(int)` -- This method is called when a dialog is cancelled and does nothing.
- `runOnMainThread(java.lang.Runnable)` -- This method runs a given Runnable on the main thread using a handler.
- `moveMessage(com.fsck.k9.activity.MessageReference,java.lang.String)` -- This method moves a message from one folder to another within an email account.
- `onToggleFlagged()` -- The purpose of the `onToggleFlagged()` method is to toggle the `FLAGGED` flag on the current email message and update the message view.
- `canMessageBeArchived()` -- The method checks if a message can be archived based on the current folder and account settings.
- `isMoveCapable()` -- The purpose of the method is to check if the current message can be moved to another folder in the email account.
- `disableAttachmentButtons(com.fsck.k9.mailstore.AttachmentViewInfo)` -- This method disables the attachment buttons for a given attachment in the message view.
- `onSelectText()` -- The purpose of the method is to begin selecting text in the message view.
- `onActivityCreated(android.os.Bundle)` -- This method is called when the activity is created, retrieves message data from arguments, and displays the referenced message in the message view.
- `onSaveAttachment(com.fsck.k9.mailstore.AttachmentViewInfo)` -- The purpose of the `onSaveAttachment()` method is to save an attachment and set it as the current attachment view info.
- `onActivityResult(int,int,android.content.Intent)` -- This method handles the results of activities launched via the MessageViewFragment, including saving attachments and moving or copying messages.
- `onReply()` -- This method handles the user's request to reply to a message by passing the message reference and decryption result to the fragment listener.
- `onSpam()` -- The purpose of the method `onSpam()` is to move the current email message to the spam folder of the associated email account.
- `isInitialized()` -- The method checks if the message view fragment has been initialized.
- `zoom(android.view.KeyEvent)` -- The method zooms the message view in response to a key event.
- `hideAttachmentLoadingDialogOnMainThread()` -- The method hides the attachment loading dialog in the message view fragment on the main thread.
- `onAttach(android.app.Activity)` -- This method attaches the fragment to a parent activity, sets the context, and verifies that the parent activity implements the necessary interface for fragment communication.
- `onSaveAttachmentToUserProvidedDirectory(com.fsck.k9.mailstore.AttachmentViewInfo)` -- This method allows the user to save an email attachment to a directory of their choice.
- `copyMessage(com.fsck.k9.activity.MessageReference,java.lang.String)` -- Copy a message to a specified folder.
- `onRefile(java.lang.String)` -- The method `onRefile` is used to refile a message into a specified destination folder, if move capability is available and the message is not unsynced, and displays a confirmation dialog if the destination folder is the spam folder and spam confirmation is enabled.
- `updateTitle()` -- The method updates the title of the message view with the subject of the message if available.
- `onViewAttachment(com.fsck.k9.mailstore.AttachmentViewInfo)` -- This method sets the current attachment view info and calls the attachment controller to view the attachment.

## class `com.fsck.k9.ui.messageview.AttachmentController`

The `AttachmentController` class is responsible for handling email attachments in K-9 Mail, allowing users to view and save attachments locally.

This class contains the following public method(s):

- `viewAttachment()` -- The `viewAttachment()` method checks if the attachment content is available, and if not, it downloads and views the attachment, otherwise it views the locally stored attachment.
- `saveAttachment()` -- The `saveAttachment()` method saves an email attachment to the default attachment path in K-9 Mail.
- `saveAttachmentTo(java.lang.String)` -- This method saves an email attachment to the designated directory.

## interface `com.fsck.k9.ui.messageview.MessageCryptoPresenter$MessageCryptoMvpView`

The interface provides methods for the message crypto presenter view to restart cryptographic processing, display messages, start pending intents, show a dialog for configuring message encryption, and show a dialog with information about the cryptographic status of a message.

This class contains the following public method(s):

- `restartMessageCryptoProcessing()` -- The method restarts the cryptographic processing of a message in the UI.
- `redisplayMessage()` -- The method redisplayMessage() is used to refresh and display the message again on the screen.
- `startPendingIntentForCryptoPresenter(android.content.IntentSender,java.lang.Integer,android.content.Intent,int,int,int)` -- This method starts a pending intent for the message crypto presenter view.
- `showCryptoConfigDialog()` -- The method shows a dialog box to configure message encryption.
- `showCryptoInfoDialog(com.fsck.k9.view.MessageCryptoDisplayStatus,boolean)` -- The method is used to display a dialog with information about the cryptographic status of a message, including any security warnings.

## class `com.fsck.k9.ui.messageview.MessageTopView`

The `com.fsck.k9.ui.messageview.MessageTopView` Java class is responsible for displaying the header and top portion of an email message view in the K-9 email client, handling loading of pictures and attachments, and displaying cryptographic information and warnings.

This class contains the following public method(s):

- `showMessageCryptoCancelledView(com.fsck.k9.mailstore.MessageViewInfo,android.graphics.drawable.Drawable)` -- The method displays a view indicating that the cryptographic operation for a message has been cancelled, along with an option to retry the operation.
- `enableDownloadButton()` -- The purpose of the `enableDownloadButton()` method is to enable a download button in the UI.
- `setOnDownloadButtonClickListener(com.fsck.k9.ui.messageview.OnClickListener)` -- This method sets a listener to the download button in the message top view.
- `showMessage(com.fsck.k9.Account,com.fsck.k9.mailstore.MessageViewInfo)` -- The `showMessage` method displays the message view container for a given account and message view information, as well as handles the loading of pictures and attachments.
- `onFinishInflate()` -- The method initializes various views and components used for displaying a message at the top of a message view in the K-9 email client.
- `additionalHeadersVisible()` -- This method returns whether additional headers are currently visible in the message view.
- `showAllHeaders()` -- The purpose of the method is to display all additional headers in the message view.
- `setAttachmentCallback(com.fsck.k9.ui.messageview.AttachmentViewCallback)` -- The method sets an attachment view callback for the message top view.
- `displayViewOnLoadFinished(boolean)` -- The method displays the message top view on load finished and optionally animates the progress bar.
- `setOnToggleFlagClickListener(com.fsck.k9.ui.messageview.OnClickListener)` -- The method sets a listener for flag toggling events in the message top view.
- `getMessageHeaderView()` -- This method fetches the message header view displayed at the top of messages in the UI.
- `disableDownloadButton()` -- The purpose of this method is to disable a download button in the user interface of an email message view.
- `setMessageCryptoPresenter(com.fsck.k9.ui.messageview.MessageCryptoPresenter)` -- This method sets the message crypto presenter and updates the header container's on click listener accordingly.
- `showMessageCryptoWarning(com.fsck.k9.mailstore.MessageViewInfo,android.graphics.drawable.Drawable,int,boolean)` -- The method displays a warning message about the cryptographic properties of an email message.
- `showMessageCryptoErrorView(com.fsck.k9.mailstore.MessageViewInfo,android.graphics.drawable.Drawable)` -- The method shows a view indicating that there was an error with message encryption.
- `setLoadingProgress(int,int)` -- The method sets the progress of a loading indicator for a message view.
- `setHeaders(com.fsck.k9.mail.Message,com.fsck.k9.Account)` -- The method sets the headers of a mail message to be displayed in the message top view.
- `setToLoadingState()` -- The method sets the view to a loading state by resetting the displayed child and progress bar.
- `showCryptoProviderNotConfigured(com.fsck.k9.mailstore.MessageViewInfo)` -- The method displays a message view indicating that a cryptography provider has not been configured for the given message view, with a button to configure the provider.
- `showMessageEncryptedButIncomplete(com.fsck.k9.mailstore.MessageViewInfo,android.graphics.drawable.Drawable)` -- This method displays a message that is encrypted but incomplete with a provider icon in a message view.

## class `com.fsck.k9.ui.messageview.MessageContainerView$SavedState`

The purpose of the `com.fsck.k9.ui.messageview.MessageContainerView$SavedState` class is to save the state of visible attachments and displayed pictures in a parcel.

This class contains the following public method(s):

- `writeToParcel(android.os.Parcel,int)` -- The method writes the state of visible attachments and displayed pictures to a parcel.

## interface `com.fsck.k9.ui.messageview.CryptoInfoDialog$OnClickShowCryptoKeyListener`

The interface `com.fsck.k9.ui.messageview.CryptoInfoDialog$OnClickShowCryptoKeyListener` defines the methods for handling click events on crypto keys in the message view, including displaying security warnings and displaying the keys themselves.

This class contains the following public method(s):

- `onClickShowSecurityWarning()` -- The purpose of the method `onClickShowSecurityWarning()` is to display a security warning message when a crypto key is clicked in the message view.
- `onClickShowCryptoKey()` -- The purpose of this method is to handle a click event for displaying the cryptography key.

## interface `com.fsck.k9.ui.messageview.MessageViewFragment$MessageViewFragmentListener`

The purpose of the interface `com.fsck.k9.ui.messageview.MessageViewFragment$MessageViewFragmentListener` is to define public methods for handling actions and updating the UI in the message view fragment of the K-9 email client.

This class contains the following public method(s):

- `disableDeleteAction()` -- The method disables the delete action in the message view fragment.
- `updateMenu()` -- The purpose of the method `updateMenu()` is to update the menu of the message view fragment.
- `onForward(com.fsck.k9.activity.MessageReference,android.os.Parcelable)` -- This method is called when the user clicks on the "Forward" button to forward a message and passes the message reference and decryption result.
- `setProgress(boolean)` -- The purpose of the method is to set the progress state of the message view fragment.
- `showNextMessageOrReturn()` -- The purpose of this method is to display the next message or return to the message list if there are no more messages to display.
- `onReply(com.fsck.k9.activity.MessageReference,android.os.Parcelable)` -- This method is used to handle when the user initiates a reply to a message in the message view fragment, passing in the message reference and decryption result as parameters.
- `messageHeaderViewAvailable(com.fsck.k9.view.MessageHeader)` -- This method provides the implementation for displaying the header of a message in the message view fragment of the K-9 email client.
- `onReplyAll(com.fsck.k9.activity.MessageReference,android.os.Parcelable)` -- This method is called when the user selects the "Reply All" option in the message view, passing the message reference and decryption result for the reply.
- `displayMessageSubject(java.lang.String)` -- The purpose of the method is to display the subject of a message in the UI.

## class `com.fsck.k9.ui.messageview.LockedAttachmentView`

The purpose of the class `com.fsck.k9.ui.messageview.LockedAttachmentView` is to display a locked message attachment view in K-9 mail and allow the user to switch to an unlocked view upon clicking the "locked button".

This class contains the following public method(s):

- `onClick(android.view.View)` -- This method is called when the "locked button" in a message attachment view is clicked, causing the display to switch to an "unlocked view" of the attachment.
- `setAttachment(com.fsck.k9.mailstore.AttachmentViewInfo)` -- The method sets the attachment for the LockedAttachmentView.
- `setCallback(com.fsck.k9.ui.messageview.AttachmentViewCallback)` -- This method sets the callback for an attachment view in K-9 mail.

## interface `com.fsck.k9.ui.messageview.OnCryptoClickListener`

The purpose of the interface `com.fsck.k9.ui.messageview.OnCryptoClickListener` is to handle click events on the crypto-related UI elements in K-9 Mail.

This class contains the following public method(s):

- `onCryptoClick()` -- The purpose of the method `onCryptoClick()` is to handle click events on the crypto-related UI elements in K-9 Mail.

## class `com.fsck.k9.ui.messageview.AttachmentController$IntentAndResolvedActivitiesCount`

The class is used to hold information about an intent associated with an email attachment, including its MIME type, whether there are resolved activities associated with it, and whether its data scheme is "file".

This class contains the following public method(s):

- `getIntent()` -- The method returns the intent associated with the object.
- `getMimeType()` -- This method returns the MIME type of the intent associated with the attachment.
- `hasResolvedActivities()` -- This method checks if there are resolved activities and returns a boolean value indicating their presence or absence.
- `containsFileUri()` -- The method checks if the intent's data scheme is "file".

## interface `com.fsck.k9.ui.messageview.MessageContainerView$OnRenderingFinishedListener`

The purpose of the interface is to provide a callback method `onLoadFinished()` that can be implemented by the listener to receive a notification when the loading of a message's content is complete.

This class contains the following public method(s):

- `onLoadFinished()` -- The method is called when loading of a message's content has finished.

## class `com.fsck.k9.ui.messageview.MessageContainerView`

The purpose of the `com.fsck.k9.ui.messageview.MessageContainerView` class is to display the contents of an email message, including attachments and HTML content, and allow for interaction with the message such as enabling/disabling buttons and zooming in/out.

This class contains the following public method(s):

- `hasHiddenExternalImages()` -- The method returns a boolean that indicates whether the message container view has any hidden external images.
- `onCreateContextMenu(android.view.ContextMenu,android.view.View,android.view.ContextMenu.ContextMenuInfo)` -- This method creates a context menu containing options for interacting with different types of content viewed in a message container.
- `refreshAttachmentThumbnail(com.fsck.k9.mailstore.AttachmentViewInfo)` -- This method refreshes the thumbnail of a given email attachment.
- `enableAttachmentButtons()` -- The `enableAttachmentButtons()` method enables buttons associated with attachments of the message.
- `renderAttachments(com.fsck.k9.mailstore.MessageViewInfo)` -- The method renders the attachments of a given email message.
- `displayMessageViewContainer(com.fsck.k9.mailstore.MessageViewInfo,com.fsck.k9.ui.messageview.MessageContainerView$OnRenderingFinishedListener,boolean,boolean,com.fsck.k9.ui.messageview.AttachmentViewCallback)` -- This method displays the message view container with the specified message information and allows for the rendering of attachments and HTML content.
- `onFinishInflate()` -- This method initializes various views and components used in the MessageContainerView class.
- `showPictures()` -- The purpose of the method is to enable displaying of pictures and refresh the displayed content.
- `enableAttachmentButtons(com.fsck.k9.mailstore.AttachmentViewInfo)` -- The method enables attachment buttons for the given attachment view in the message container view.
- `disableAttachmentButtons()` -- The method disables the buttons for all attachments in the message container view.
- `resetView()` -- The method clears the message container view by setting load pictures to false, removing attachments, and clearing the WebView content.
- `onSaveInstanceState()` -- (no description)
- `disableAttachmentButtons(com.fsck.k9.mailstore.AttachmentViewInfo)` -- The purpose of this method is to disable the attachment buttons of a specified attachment in the message container view.
- `onRestoreInstanceState(android.os.Parcelable)` -- This method restores the instance state of the `MessageContainerView` from a saved `Parcelable` state.
- `onLayoutChanged()` -- The method invalidates the message content view if it exists when the layout changes.
- `beginSelectingText()` -- (no description)
- `zoom(android.view.KeyEvent)` -- The purpose of the method is to zoom in or out of the message content view depending on whether the shift key is pressed on the keyboard.

## class `com.fsck.k9.ui.messageview.CryptoInfoDialog`

The class `CryptoInfoDialog` displays information about the cryptographic status of a message and handles user interaction for the same.

This class contains the following public method(s):

- `onCreateDialog(android.os.Bundle)` -- This method creates a dialog box displaying information about the cryptographic status of a message, and handles the user's interaction with the dialog.
- `newInstance(com.fsck.k9.view.MessageCryptoDisplayStatus,boolean)` -- The method creates a new instance of `CryptoInfoDialog` and sets its arguments based on `displayStatus` and `hasSecurityWarning`.

## class `com.fsck.k9.ui.messageview.AttachmentView`

The `com.fsck.k9.ui.messageview.AttachmentView` class is used to display attachment information and provide functionality for viewing and downloading attachments in the K-9 Mail app's message view.

This class contains the following public method(s):

- `enableButtons()` -- To enable the "view" and "download" buttons for an attachment in the UI.
- `setAttachment(com.fsck.k9.mailstore.AttachmentViewInfo)` -- The method sets the attachment information and updates its display.
- `disableButtons()` -- The `disableButtons()` method disables the view and download buttons for an attachment in the user interface.
- `setCallback(com.fsck.k9.ui.messageview.AttachmentViewCallback)` -- Sets a callback for attachment view events.
- `onLongClick(android.view.View)` -- The method handles long clicks on the download button of an attachment view and invokes the onSaveButtonLongClick() method.
- `onClick(android.view.View)` -- The method handles click events on the attachment view buttons, either opening or downloading the attachment depending on which button is clicked.
- `refreshThumbnail()` -- The purpose of the `refreshThumbnail()` method is to update and display the thumbnail of an attachment in an `ImageView`.
- `getAttachment()` -- This method returns the attachment associated with this view.

## class `com.fsck.k9.ui.messageview.MessageCryptoPresenter`

The purpose of `com.fsck.k9.ui.messageview.MessageCryptoPresenter` is to handle the display and processing of message encryption and decryption related actions for the K-9 email client's message view.

This class contains the following public method(s):

- `onActivityResult(int,int,android.content.Intent)` -- This method handles the results of activities started by the message view, specifically for the unknown key and security warning requests.
- `onCryptoClick()` -- The purpose of `onCryptoClick()` is to handle user input related to email encryption and trigger corresponding actions.
- `onSaveInstanceState(android.os.Bundle)` -- The method saves the state of a boolean variable indicating if a user has chosen to override a warning for encrypting a message.
- `maybeHandleShowMessage(com.fsck.k9.ui.messageview.MessageTopView,com.fsck.k9.Account,com.fsck.k9.mailstore.MessageViewInfo)` -- This method handles the display of various types of message encryption statuses in the UI of the K-9 email client.
- `onResume()` -- This method restarts message crypto processing if the flag for reloading is set.
- `getDecryptionResultForReply()` -- This method returns the decryption result for replying to a message if it is an OpenPGP result.
- `onClickShowMessageOverrideWarning()` -- The method sets a boolean flag and triggers a message to be redisplayed in the messageCryptoMvpView.
- `onClickShowCryptoKey()` -- The purpose of this method is to handle the onClick event for displaying a cryptographic key associated with a message.
- `onClickRetryCryptoOperation()` -- The method retries the failed cryptographic operation for the current message.
- `onClickConfigureProvider()` -- The purpose of the method is to reload the view without recreating it and show a dialog box for configuring the message encryption provider.
- `onClickShowCryptoWarningDetails()` -- This method displays additional details about a security warning related to the message's cryptography.


# package `com.fsck.k9.service`

The `com.fsck.k9.service` package contains classes responsible for providing email synchronization, push notification, background service management, and handling various system broadcast intents for the K-9 Mail Android app.

This package contains the following class(es):

## class `com.fsck.k9.service.RemoteControlReceiver`

The purpose of the `com.fsck.k9.service.RemoteControlReceiver` class is to receive and process incoming intents for remote control of the K-9 Mail application.

This class contains the following public method(s):

- `receive(android.content.Context,android.content.Intent,java.lang.Integer)` -- This method receives and processes incoming intents for remote control of the K-9 Mail application and returns a wake lock ID.

## class `com.fsck.k9.service.RemoteControlService`

The RemoteControlService class is responsible for starting and performing actions based on the Intent received such as changing account settings or rescheduling mail polling.

This class contains the following public method(s):

- `startService(android.content.Intent,int)` -- This method is used to start the RemoteControlService and perform actions based on the Intent received, such as changing account settings or rescheduling mail polling.
- `set(android.content.Context,android.content.Intent,java.lang.Integer)` -- This method sets an Intent to start the RemoteControlService with a specified wakeLockId.

## class `com.fsck.k9.service.ShutdownReceiver`

The purpose of the class `com.fsck.k9.service.ShutdownReceiver` is to release resources and prevent scheduled intents from waking up K-9 when the system is shutting down.

This class contains the following public method(s):

- `onReceive(android.content.Context,android.content.Intent)` -- The method releases resources and prevents scheduled intents from waking up K-9 when the system is shutting down.

## class `com.fsck.k9.service.PollService`

The `PollService` class is used by the K-9 Mail app to periodically check for new email messages.

This class contains the following public method(s):

- `stopService(android.content.Context)` -- This method stops the `PollService` background service used by the K-9 Mail app.
- `startService(android.content.Intent,int)` -- The method starts the PollService and checks for new messages, or renews the wake lock if there is an existing listener.
- `onCreate()` -- Initialize the PollService and prevent it from automatically shutting down.
- `onBind(android.content.Intent)` -- This method binds the `PollService` to a client application and returns an `IBinder` interface for communication between the service and the client.
- `startService(android.content.Context)` -- The method starts the PollService to periodically poll for new email messages.

## class `com.fsck.k9.service.SleepService`

The `com.fsck.k9.service.SleepService` class is responsible for creating and controlling sleep intervals as well as optionally acquiring wakelocks to ensure that the device does not go to sleep during the sleep interval.

This class contains the following public method(s):

- `startService(android.content.Intent,int)` -- This method starts a sleep service and ends it when an alarm is fired.
- `sleep(android.content.Context,long,com.fsck.k9.mail.power.TracingPowerManager.TracingWakeLock,long)` -- The `sleep` method is used to create a sleep interval in the `SleepService` class and optionally acquire a wakelock.

## class `com.fsck.k9.service.MailService`

The purpose of the class `com.fsck.k9.service.MailService` is to provide email synchronization and push notification services for the K-9 Mail app.

This class contains the following public method(s):

- `isSyncBlocked()` -- The method returns a boolean indicating whether synchronization of mail is currently blocked or not.
- `getNextPollTime()` -- The purpose of `getNextPollTime()` is to return the time when the next email polling check should occur.
- `actionCancel(android.content.Context,java.lang.Integer)` -- The method cancels a previously started mail service and releases a wake lock with a given ID.
- `isSyncDisabled()` -- The method returns a boolean indicating whether email synchronization is currently blocked or not.
- `connectivityChange(android.content.Context,java.lang.Integer)` -- The method is used to handle changes in network connectivity and triggers the MailService to start or stop depending on the state of the network.
- `isPollAndPushDisabled()` -- To check if both polling and pushing of emails have been disabled.
- `actionReschedulePoll(android.content.Context,java.lang.Integer)` -- The method reschedules email polling for the K9 email client.
- `startService(android.content.Intent,int)` -- This method starts the MailService and performs various actions based on the intent received.
- `saveLastCheckEnd(android.content.Context)` -- This method saves the current time as the end time of the last email check and stores it in the app preferences.
- `actionReset(android.content.Context,java.lang.Integer)` -- This method resets a MailService and adds a wake lock.
- `onBind(android.content.Intent)` -- The method is used to bind the MailService to a specific intent, but in this implementation it simply returns null and is therefore unused.
- `hasNoConnectivity()` -- The method checks whether there is no connectivity for syncing emails in the K9 email service.
- `onDestroy()` -- (no description)
- `isSyncNoBackground()` -- The method returns a boolean value indicating whether email synchronization should occur without running in the background.
- `onCreate()` -- The method initializes the MailService and logs a message with Timber.
- `actionRestartPushers(android.content.Context,java.lang.Integer)` -- The method restarts the push service for email notifications in the K-9 Mail app.

## class `com.fsck.k9.service.StorageGoneReceiver`

The purpose of the `com.fsck.k9.service.StorageGoneReceiver` class is to handle the actions to be taken when storage is ejected or unmounted in the K-9 Mail app.

This class contains the following public method(s):

- `onReceive(android.content.Context,android.content.Intent)` -- The `onReceive` method handles the actions to be taken when storage is ejected or unmounted in the K-9 Mail app.

## abstract class `com.fsck.k9.service.CoreService`

The abstract class `com.fsck.k9.service.CoreService` provides a framework for managing the lifecycle and execution of tasks in a background service for the K9 email client.

This class contains the following public method(s):

- `onDestroy()` -- The method `onDestroy()` shuts down the thread pool and performs clean-up when the service is stopped.
- `onStartCommand(android.content.Intent,int,int)` -- This method handles the start of the service and releases any associated wake locks.
- `startService(android.content.Intent,int)` -- This method is used by subclasses of `CoreService` to manage the service lifecycle, including wake lock management.
- `onCreate()` -- The purpose of the `onCreate()` method is to initialize the CoreService and create a single-threaded thread pool for the service.
- `onLowMemory()` -- The `onLowMemory()` method is used to log a warning message when the device is running low on memory.
- `execute(android.content.Context,java.lang.Runnable,int,java.lang.Integer)` -- This method executes a specified task in a background thread and manages a wake lock for a specified amount of time while also providing options for setting the auto shutdown for the service.
- `onBind(android.content.Intent)` -- This method is used for binding the service to an activity through an intent, but in this case it does nothing and returns null.

## class `com.fsck.k9.service.CoreReceiver`

The `CoreReceiver` class is used to receive and handle `Intent` objects for the K-9 Mail Android app and manage wake locks.

This class contains the following public method(s):

- `receive(android.content.Context,android.content.Intent,java.lang.Integer)` -- This method receives a context, intent, and wake lock ID and returns the wake lock ID.
- `onReceive(android.content.Context,android.content.Intent)` -- The method `onReceive` receives and handles `Intent` objects, operating the required actions in response.
- `releaseWakeLock(android.content.Context,int)` -- The method releases a previously acquired wake lock.

## class `com.fsck.k9.service.PushService`

The purpose of the `com.fsck.k9.service.PushService` class is to handle the background running of the K-9 Mail email client on Android to receive push notifications for incoming emails.

This class contains the following public method(s):

- `startService(android.content.Context)` -- The method starts the PushService in the background with a wake lock to allow the app to receive push notifications.
- `startService(android.content.Intent,int)` -- The method manages the starting and stopping of `PushService` based on the received intent action.
- `onCreate()` -- The method sets `autoShutdown` to be `false` for the `PushService` class instance.
- `onBind(android.content.Intent)` -- This method binds the PushService to a client activity.
- `stopService(android.content.Context)` -- The `stopService` method is used to stop the `PushService` in the K-9 Mail email client on Android.

## class `com.fsck.k9.service.StorageReceiver`

The purpose of the class `com.fsck.k9.service.StorageReceiver` is to handle storage mount events and notify the `StorageManager` instance to handle the mounted storage.

This class contains the following public method(s):

- `onReceive(android.content.Context,android.content.Intent)` -- The `onReceive` method is responsible for handling storage mount events and notifying the `StorageManager` instance to handle the mounted storage.

## class `com.fsck.k9.service.PollService$Listener`

The class `com.fsck.k9.service.PollService$Listener` is used to interact with the `PollService` in order to check email accounts, release wake locks, and store information about new messages.

This class contains the following public method(s):

- `wakeLockRelease()` -- The `wakeLockRelease()` method releases a wake lock if it has been acquired previously.
- `setStartId(int)` -- This method sets the start ID of the service.
- `checkMailFinished(android.content.Context,com.fsck.k9.Account)` -- The `checkMailFinished` method is used to release the PollService after checking the specified email account.
- `getStartId()` -- The method returns the unique identifier for the invocation of PollService.
- `checkMailStarted(android.content.Context,com.fsck.k9.Account)` -- The method clears the list of already checked accounts when starting to check mail for a K-9 account in the background.
- `wakeLockAcquire()` -- The method acquires a wakelock to ensure the device does not go to sleep during email polling.
- `synchronizeMailboxFinished(com.fsck.k9.Account,java.lang.String,int,int)` -- The method updates the number of new messages for an email account and stores it in a map if the account is set to notify for new messages.

## class `com.fsck.k9.service.DatabaseUpgradeService`

The purpose of `com.fsck.k9.service.DatabaseUpgradeService` is to upgrade the mail database in K-9 Mail through a background process.

This class contains the following public method(s):

- `onBind(android.content.Intent)` -- This method returns an IBinder interface for communicating with the service, but in this case it simply returns null since it is unused.
- `onCreate()` -- The method sets up a LocalBroadcastManager for the DatabaseUpgradeService.
- `onStartCommand(android.content.Intent,int,int)` -- The method starts a background upgrade process for the database if the service is not already running, else it sends the current progress of the upgrade process via broadcast.
- `startService(android.content.Context)` -- The method starts the DatabaseUpgradeService in K-9 Mail to upgrade the mail database.

## class `com.fsck.k9.service.BootReceiver`

The purpose of the `com.fsck.k9.service.BootReceiver` class is to receive various system broadcast intents, schedule alarms, and cancel previously set alarms.

This class contains the following public method(s):

- `scheduleIntent(android.content.Context,long,android.content.Intent)` -- The method schedules an alarm to broadcast an intent at a specific time.
- `cancelIntent(android.content.Context,android.content.Intent)` -- The method cancels a previously set alarm intent by sending a broadcast.
- `receive(android.content.Context,android.content.Intent,java.lang.Integer)` -- The method receives different types of intents and performs actions based on the intent type and returns a wake lock ID.
- `purgeSchedule(android.content.Context)` -- This method cancels any scheduled alarm associated with the application context.


# package `com.fsck.k9.setup`

The purpose of the `com.fsck.k9.setup` package in Java is to provide classes related to setting up and configuring a server, including suggesting server names based on server type and domain name.

This package contains the following class(es):

## class `com.fsck.k9.setup.ServerNameSuggester`

The purpose of the `com.fsck.k9.setup.ServerNameSuggester` class in Java is to suggest a server name based on the server type and domain name.

This class contains the following public method(s):

- `suggestServerName(com.fsck.k9.mail.ServerSettings.Type,java.lang.String)` -- The `suggestServerName` method suggests a server name based on the server type and domain name.


# package `com.fsck.k9.search`

The `com.fsck.k9.search` package provides classes and interfaces for searching emails in the K-9 email client app for Android, allowing users to specify search conditions, accounts to be searched, and build SQL queries for searching emails.

This package contains the following class(es):

## class `com.fsck.k9.search.SearchAccount`

The `com.fsck.k9.search.SearchAccount` class is used to represent a search account in the K-9 email client, which allows users to search for specific emails within their email accounts.

This class contains the following public method(s):

- `getDescription()` -- The method returns the description of the search account.
- `setEmail(java.lang.String)` -- The method sets the email address for the search account.
- `getRelatedSearch()` -- This method returns the related local search object.
- `getUuid()` -- The method returns the ID/UUID of the `SearchAccount` instance.
- `setDescription(java.lang.String)` -- The method sets the description for the SearchAccount.
- `createAllMessagesAccount(android.content.Context)` -- The method creates a search account for all messages in the specified context.
- `getId()` -- The `getId()` method returns the unique identifier of a search account.
- `getEmail()` -- The method returns the email address associated with the search account object.
- `createUnifiedInboxAccount(android.content.Context)` -- The purpose of the method is to create a unified inbox meta account for the K-9 email client that integrates all accounts by default when none are specified.

## interface `com.fsck.k9.search.SearchSpecification`

The `com.fsck.k9.search.SearchSpecification` interface defines the specifications for a search including the conditions, name, and accounts to be searched.

This class contains the following public method(s):

- `getConditions()` -- This method returns the root node of the condition tree used in a search.
- `getName()` -- The method returns the name of the search specification.
- `getAccountUuids()` -- The method returns an array of UUIDs corresponding to the accounts on which this search acts.

## class `com.fsck.k9.search.LocalSearch`

The class `com.fsck.k9.search.LocalSearch` provides methods to perform local email searches in the K-9 email application with various search conditions and settings.

This class contains the following public method(s):

- `or(com.fsck.k9.search.ConditionsTreeNode)` -- The `or` method adds the provided node as the second argument of an OR clause to this node and returns the new top OR node, new root.
- `clone()` -- The `clone()` method creates a copy of a `LocalSearch` object with its own set of conditions, account UUIDs, and predefined settings.
- `describeContents()` -- The `describeContents()` method is used for Parcelable implementation and returns a bitmask indicating the set of special object types contained in the Parcelable instance.
- `isManualSearch()` -- This method returns a boolean value indicating if the search is manually initiated by the user or not.
- `getAccountUuids()` -- The method returns an array of account UUIDs that will be matched against in a local search operation.
- `or(com.fsck.k9.search.SearchSpecification$SearchCondition)` -- The method adds a condition as the second argument of an OR clause to the search node and returns a new OR node.
- `getName()` -- This method returns the name of the saved search.
- `and(com.fsck.k9.search.ConditionsTreeNode)` -- This method adds a provided node as the second argument of an AND clause to the current node and returns a new top AND node.
- `getFolderNames()` -- The `getFolderNames()` method retrieves a list of folder names that match certain conditions specified by the `ConditionsTreeNode` objects in `mLeafSet`.
- `addAccountUuids(java.lang.String[])` -- The purpose of the method is to add account UUIDs to be matched by a search.
- `isPredefined()` -- The method is used to check if a search was hardcoded and shipped with the K-9 email application.
- `getConditions()` -- The method returns the root node of the condition tree used in local email searches in K-9 Mail.
- `searchAllAccounts()` -- The method returns whether or not to search all accounts.
- `writeToParcel(android.os.Parcel,int)` -- This method writes the state of a LocalSearch instance to a Parcel.
- `addAllowedFolder(java.lang.String)` -- The method adds a folder to the list of folders to search in and includes it in the root if no folder subtree was found, otherwise it includes it in the subtree.
- `addAccountUuid(java.lang.String)` -- The method adds a new account UUID to the list of accounts to be included in the search, or clears the list if the UUID is for all accounts.
- `and(com.fsck.k9.search.SearchSpecification$SearchField,java.lang.String,com.fsck.k9.search.SearchSpecification$Attribute)` -- The `and` method adds a search condition to match a specific message table field against a given value with a specified attribute, and combines it with the previously added conditions using the AND operator.
- `and(com.fsck.k9.search.SearchSpecification$SearchCondition)` -- The method adds the provided search condition to a new AND node and returns the new top node as the new root.
- `getRemoteSearchArguments()` -- The method is a temporary workaround for remote search support that retrieves the search arguments for the subject or sender fields.
- `setName(java.lang.String)` -- This method sets the name of the saved search in the `LocalSearch` class.
- `getLeafSet()` -- The method returns all the leaf conditions of the related condition tree as a set.
- `removeAccountUuid(java.lang.String)` -- The method removes an account UUID from the current search.
- `setManualSearch(boolean)` -- Sets whether the search is manual or not.

## class `com.fsck.k9.search.ConditionsTreeNode`

The `ConditionsTreeNode` class is used to represent an expression tree for handling search conditions in the K-9 email client app for Android.

This class contains the following public method(s):

- `describeContents()` -- The method `describeContents()` is used to describe if the object's contents include a file descriptor or not, and is used for implementing the `Parcelable` interface in Android.
- `writeToParcel(android.os.Parcel,int)` -- The method is used to write the values of the `ConditionsTreeNode` object to a `Parcel` which can be used for inter-process communication or persistent storage.
- `or(com.fsck.k9.search.ConditionsTreeNode)` -- The method adds an expression to an OR clause in this node.
- `or(com.fsck.k9.search.SearchSpecification$SearchCondition)` -- This method adds the provided condition to an OR clause of the search specification.
- `preorder()` -- The `preorder()` method returns a list of all nodes in the subtree of a given node, in a pre-order traversal order.
- `and(com.fsck.k9.search.SearchSpecification$SearchCondition)` -- The method adds the provided condition as the second argument of an AND clause to this node and returns a new top AND node as the new root.
- `getLeafSet()` -- The method returns a set of all the leaves in the tree.
- `and(com.fsck.k9.search.ConditionsTreeNode)` -- The method adds an expression as the second argument of an AND clause to this node.
- `getCondition()` -- The `getCondition()` method returns the search condition stored in a node of the `ConditionsTreeNode` class.
- `buildTreeFromDB(android.database.Cursor)` -- This method builds a condition tree from a database cursor pointing to rows representing the nodes of the tree.
- `applyMPTTLabel()` -- The method applies MPTT labeling to the subtree of which the node is the root node.

## class `com.fsck.k9.search.SqlQueryBuilder`

The purpose of `com.fsck.k9.search.SqlQueryBuilder` is to provide methods for building SQL queries for searching emails in the K-9 Mail app.

This class contains the following public method(s):

- `addPrefixToSelection(java.lang.String[],java.lang.String,java.lang.String)` -- This method adds a prefix to each of the specified column names in the given SQL selection string.
- `buildWhereClause(com.fsck.k9.Account,com.fsck.k9.search.ConditionsTreeNode,java.lang.StringBuilder,java.util.List)` -- This method builds a SQL WHERE clause and corresponding selection arguments based on the search conditions for a given account.

## class `com.fsck.k9.search.SearchSpecification$SearchCondition`

The purpose of `com.fsck.k9.search.SearchSpecification$SearchCondition` is to represent a search condition with attributes, fields, and values, and provide methods to clone, write to a parcel, generate a human-readable string, and check for equality.

This class contains the following public method(s):

- `hashCode()` -- The method calculates a hash code for the object based on its attribute, field, and value.
- `clone()` -- This method creates and returns a new instance of the `SearchCondition` class with the same `field`, `attribute`, and `value` parameters.
- `writeToParcel(android.os.Parcel,int)` -- The purpose of the `writeToParcel` method is to write the `value`, `attribute`, and `field` properties of a `SearchCondition` object to the given `Parcel`.
- `toHumanString()` -- The purpose of the `toHumanString()` method is to return a string representation of a field and attribute concatenated together.
- `describeContents()` -- This method returns a bitmask indicating the set of special object types contained in the Parcel.
- `equals(java.lang.Object)` -- The method checks if an object is equal to the current SearchCondition by comparing attribute, field, and value.


# package `com.fsck.k9.view`

The package `com.fsck.k9.view` provides a collection of view classes and interfaces for displaying and interacting with email messages and cryptographic information in the K-9 mail application for Android.

This package contains the following class(es):

## interface `com.fsck.k9.view.MessageHeader$OnLayoutChangedListener`

The purpose of this interface is to provide a way to listen for changes in the layout of a message header in Java.

This class contains the following public method(s):

- `onLayoutChanged()` -- The purpose of this method is to notify when the layout of a message header has changed.

## class `com.fsck.k9.view.HighlightDialogFragment`

The purpose of the class `com.fsck.k9.view.HighlightDialogFragment` is to create a dialog fragment that highlights a view in the background and can be dismissed.

This class contains the following public method(s):

- `onDismiss(android.content.DialogInterface)` -- The method is called when the dialog is dismissed and it hides the showcase view.
- `onStart()` -- The method sets up the dialog fragment by hiding the keyboard, highlighting the view in the background, and setting the background dim.

## interface `com.fsck.k9.view.CryptoModeSelector$CryptoStatusSelectedListener`

The purpose of the `CryptoStatusSelectedListener` interface is to provide a listener for detecting when a user selects a new crypto state in the crypto mode selector.

This class contains the following public method(s):

- `onCryptoStatusSelected(com.fsck.k9.view.CryptoModeSelector$CryptoModeSelectorState)` -- The method is called when the user selects a new crypto state in the crypto mode selector.

## class `com.fsck.k9.view.ViewSwitcher`

The `ViewSwitcher` class is used to switch between two views in an Android app while also providing animation options and callbacks for when the switch is complete.

This class contains the following public method(s):

- `setFirstInAnimation(android.view.animation.Animation)` -- Sets the animation used for the first view when it is shown in the ViewSwitcher.
- `onAnimationStart(android.view.animation.Animation)` -- The method is currently unused and does not have a specific purpose.
- `setSecondOutAnimation(android.view.animation.Animation)` -- This method sets the animation used when the second view in the ViewSwitcher is removed from the screen.
- `getSecondInAnimation()` -- The method returns the animation used for the entrance of the second view in a view switcher.
- `showSecondView()` -- The method switches the displayed child view to the second view while also setting up animations and a callback.
- `setOnSwitchCompleteListener(com.fsck.k9.view.ViewSwitcher$OnSwitchCompleteListener)` -- This method sets the listener for when a ViewSwitcher completes its transition.
- `showFirstView()` -- The method switches the currently displayed view to the first view, while optionally animating the switch.
- `getFirstInAnimation()` -- The method returns the animation used for bringing the first view into the ViewSwitcher.
- `getmFirstOutAnimation()` -- The method returns the animation used for the first view when transitioning out of the ViewSwitcher.
- `setFirstOutAnimation(android.view.animation.Animation)` -- To set the animation used when the first view in the ViewSwitcher is removed from the screen.
- `getSecondOutAnimation()` -- This method returns the animation used for the outgoing view in a view switcher.
- `setSecondInAnimation(android.view.animation.Animation)` -- The method sets the animation used when the second view is being shown during a view transition.
- `onAnimationEnd(android.view.animation.Animation)` -- The method calls the onSwitchComplete method of the listener if it's not null and passes the currently displayed child.
- `onAnimationRepeat(android.view.animation.Animation)` -- This method is unused and has no purpose.

## class `com.fsck.k9.view.NonLockingScrollView`

The purpose of the `NonLockingScrollView` class is to provide a custom implementation of the `ScrollView` that allows for interception of touch events and prevents scrolling of certain child views.

This class contains the following public method(s):

- `onInterceptTouchEvent(android.view.MotionEvent)` -- The method intercepts touch events and potentially prevents child views from falsely handling click events after a drag.
- `requestChildFocus(android.view.View,android.view.View)` -- Prevents scrolling of a child view (MessageWebView) into view if it is already at least partially visible.

## enum `com.fsck.k9.view.MessageCryptoDisplayStatus`

The enum is used to represent the different possible states of a message's encryption and digital signature status, and to provide convenient methods to check these states.

This class contains the following public method(s):

- `isUnencryptedSigned()` -- The method determines if a message is unencrypted and has a valid or invalid digital signature.
- `fromResultAnnotation(com.fsck.k9.mailstore.CryptoResultAnnotation)` -- This method returns a `MessageCryptoDisplayStatus` enum that corresponds to the given `CryptoResultAnnotation` based on the encryption and signing status of the message.
- `hasAssociatedKey()` -- The method checks if the `MessageCryptoDisplayStatus` enum value is associated with an encryption or signing key.

## class `com.fsck.k9.view.MessageWebView`

The purpose of the class `com.fsck.k9.view.MessageWebView` is to provide a WebView to display HTML content with inline attachments and configure it to display messages using user preferences. It also has methods to simulate the shift key being pressed and to block or allow network data.

This class contains the following public method(s):

- `emulateShiftHeld()` -- The purpose of the method `emulateShiftHeld()` is to simulate the shift key being pressed to activate the text selection mode in a WebView.
- `displayHtmlContentWithInlineAttachments(java.lang.String,com.fsck.k9.mailstore.AttachmentResolver,com.fsck.k9.view.MessageWebView$OnPageFinishedListener)` -- This method displays HTML content with inline attachments in a MessageWebView.
- `blockNetworkData(boolean)` -- This method configures a web view to block or allow network data.
- `configure()` -- The method configures a WebView to display a message using user preferences, setting settings such as scroll bar style, zoom, and image loading.

## class `com.fsck.k9.view.MessageHeader`

The purpose of the class `com.fsck.k9.view.MessageHeader` is to display the header information of an email message, handle click and long click events on various views, and update the display status of the message's cryptographic information.

This class contains the following public method(s):

- `setCryptoStatus(com.fsck.k9.view.MessageCryptoDisplayStatus)` -- The method sets the display status of the message's cryptographic information and updates the corresponding icon.
- `onShowAdditionalHeaders()` -- The `onShowAdditionalHeaders()` method toggles the visibility of additional headers in a message header and expands or collapses the `To` and `Cc` fields accordingly.
- `populate(com.fsck.k9.mail.Message,com.fsck.k9.Account)` -- The purpose of the `populate` method is to fill in the message header view with information from the provided `Message` object and `Account` object.
- `setOnCryptoClickListener(com.fsck.k9.ui.messageview.OnCryptoClickListener)` -- The method sets a listener for clickable elements related to email encryption on the message header.
- `onSaveInstanceState()` -- The purpose of this method is to save the current state of the MessageHeader view in order to restore it later.
- `showSubjectLine()` -- The purpose of the method is to show the subject line of an email message.
- `additionalHeadersVisible()` -- The method checks whether the additional headers view for a message is visible or not.
- `onClick(android.view.View)` -- This method handles click events on various views in the MessageHeader and performs different actions based on the clicked view.
- `onLongClick(android.view.View)` -- The method responds to a long click event on a view and copies the corresponding email addresses to the clipboard.
- `hideCryptoStatus()` -- The method hides the crypto status icon displayed in the message header.
- `setOnFlagListener(android.view.View.OnClickListener)` -- The method sets an `OnClickListener` for the "flagged" view in the `MessageHeader` class.
- `createMessage(int)` -- The method creates a string message that includes the number of addresses to be copied to the clipboard.
- `setOnLayoutChangedListener(com.fsck.k9.view.MessageHeader$OnLayoutChangedListener)` -- This method sets a listener to be called when there is a change in layout of the MessageHeader view.
- `shouldShowSender(com.fsck.k9.mail.Message)` -- The method determines whether the sender should be displayed in the message header by comparing the "from" address and the "sender" address of the email message.
- `onRestoreInstanceState(android.os.Parcelable)` -- The method restores the saved state of the MessageHeader view.
- `setCryptoStatusDisabled()` -- The method disables the cryptographic status icon in the message header view.
- `setCryptoStatusLoading()` -- The method sets the crypto status icon to be visible and disabled while indicating that the crypto status is loading.

## class `com.fsck.k9.view.ClientCertificateSpinner`

The purpose of the class `com.fsck.k9.view.ClientCertificateSpinner` is to allow selection and management of client certificates for secure communication in K-9 Mail, a free and open-source email client for Android.

This class contains the following public method(s):

- `setAlias(java.lang.String)` -- The method sets the alias of a client certificate and updates the view accordingly while also notifying any listeners of the change.
- `getAlias()` -- The method returns the selected alias from a spinner, unless the selection is empty in which case it returns null.
- `chooseCertificate()` -- The method allows the user to choose a client certificate and sets it as the alias for the instance of the `ClientCertificateSpinner` class.
- `setOnClientCertificateChangedListener(com.fsck.k9.view.ClientCertificateSpinner$OnClientCertificateChangedListener)` -- The method sets a listener for changes in the selected client certificate in a spinner view.

## abstract class `com.fsck.k9.view.K9WebViewClient`

The purpose of the abstract class `com.fsck.k9.view.K9WebViewClient` is to provide a base class for creating WebViewClients within the K9 email client that can handle web page loading and URL loading in a customized way.

This class contains the following public method(s):

- `newInstance(com.fsck.k9.mailstore.AttachmentResolver)` -- The method creates and returns a new instance of the `K9WebViewClient` class based on the device's Android OS version.
- `onPageFinished(android.webkit.WebView,java.lang.String)` -- The method is called when a web page finishes loading in a K9WebViewClient, and it notifies an onPageFinishedListener if one is present.
- `setOnPageFinishedListener(com.fsck.k9.view.MessageWebView$OnPageFinishedListener)` -- The method sets a listener to receive a notification when a web page has finished loading in a custom message WebView.
- `shouldOverrideUrlLoading(android.webkit.WebView,java.lang.String)` -- This method is used to determine whether to override the URL loading in a WebView within the K9 email client and handle the URL with a browser view intent.

## interface `com.fsck.k9.view.MessageWebView$OnPageFinishedListener`

The interface `com.fsck.k9.view.MessageWebView$OnPageFinishedListener` provides a way to listen for when a web page has finished loading in a `MessageWebView` object.

This class contains the following public method(s):

- `onPageFinished()` -- The method is called when a web page has finished loading in a MessageWebView object.

## interface `com.fsck.k9.view.ClientCertificateSpinner$OnClientCertificateChangedListener`

The interface is used as a listener for changes to the selected client certificate in a spinner, allowing for actions to be taken when a different certificate is selected.

This class contains the following public method(s):

- `onClientCertificateChanged(java.lang.String)` -- The method is called when the selected client certificate in a spinner has changed and passes the new selected alias as a parameter.

## class `com.fsck.k9.view.MessageTitleView`

The purpose of the class `com.fsck.k9.view.MessageTitleView` is to display the title of an email message, including the subject line, in the message header.

This class contains the following public method(s):

- `showSubjectInMessageHeader()` -- The purpose of the method is to show the subject line of a message in the message header.
- `setMessageHeader(com.fsck.k9.view.MessageHeader)` -- The method sets the message header of the MessageTitleView.
- `onDraw(android.graphics.Canvas)` -- Check if the subject line in a message header needs to be hidden and ellipsize the text if it exceeds the maximum number of lines.

## class `com.fsck.k9.view.K9WebViewClient$LollipopWebViewClient`

The purpose of the class `com.fsck.k9.view.K9WebViewClient$LollipopWebViewClient` is to provide support for intercepting network requests made by a WebView on devices running Android Lollipop or higher.

This class contains the following public method(s):

- `shouldInterceptRequest(android.webkit.WebView,android.webkit.WebResourceRequest)` -- This method intercepts network requests made by a WebView and returns a response or `null`.

## class `com.fsck.k9.view.K9WebViewClient$PreLollipopWebViewClient`

The purpose of the `com.fsck.k9.view.K9WebViewClient$PreLollipopWebViewClient` class is to act as a web view client for Android devices running on pre-Lollipop versions, specifically by handling web resource requests.

This class contains the following public method(s):

- `shouldInterceptRequest(android.webkit.WebView,java.lang.String)` -- This method retrieves a web resource response for the given URL through an Android web view.

## class `com.fsck.k9.view.RecipientSelectView$Recipient`

The class `com.fsck.k9.view.RecipientSelectView$Recipient` represents a recipient of an email message and provides methods to retrieve and manipulate recipient information, including display name, email address, and cryptographic status.

This class contains the following public method(s):

- `equals(java.lang.Object)` -- The purpose of this method is to check if the object being compared to the current instance of `Recipient` has the same address.
- `getDisplayNameOrUnknown(android.content.Context)` -- This method returns the display name of the recipient or a placeholder string if the name is null.
- `setCryptoStatus(com.fsck.k9.view.RecipientSelectView$RecipientCryptoStatus)` -- This method sets the recipient's crypto status to the specified value.
- `getContactLookupUri()` -- The method returns a Uri for looking up a contact in the device's Contacts database.
- `isValidEmailAddress()` -- The method checks if the email address is valid by verifying if it has a non-null value.
- `getDisplayNameOrAddress()` -- The method returns the display name of a recipient, or their email address if there is no display name.
- `getCryptoStatus()` -- The method returns the cryptographic status of the email recipient.
- `getNameOrUnknown(android.content.Context)` -- This method returns the name of a recipient or a default "unknown recipient" string if the recipient has no name.

## class `com.fsck.k9.view.FoldableLinearLayout`

The purpose of the class is to provide a container view that allows child views to be added and folded (hidden).

This class contains the following public method(s):

- `addView(android.view.View)` -- This method adds a child view to the foldable container view.

## interface `com.fsck.k9.view.RecipientSelectView$TokenListener`

The interface is used to handle events when a token in a recipient selection view is changed.

This class contains the following public method(s):

- `onTokenChanged(java.lang.Object)` -- The method is called when a token in a recipient selection view is changed.

## class `com.fsck.k9.view.ToolableViewAnimator`

The `com.fsck.k9.view.ToolableViewAnimator` class is a view animator that allows for the display of multiple child views, allowing the user to switch between them.

This class contains the following public method(s):

- `setDisplayedChildId(int)` -- The method sets the currently displayed child view based on the provided ID.
- `setDisplayedChild(int,boolean)` -- The `setDisplayedChild(int,boolean)` method sets the displayed child of the view animator with or without animation based on the given boolean value.
- `setDisplayedChild(int)` -- The method sets the currently displayed child view of the ToolableViewAnimator, but only if it differs from the current one.
- `addView(android.view.View,int,android.view.ViewGroup$LayoutParams)` -- This method adds a view to the ToolableViewAnimator, but only if the view is not in edit mode or if a certain initialization condition is met.
- `getDisplayedChildId()` -- This method returns the ID of the currently displayed child view.

## interface `com.fsck.k9.view.ViewSwitcher$OnSwitchCompleteListener`

The purpose of the interface `com.fsck.k9.view.ViewSwitcher$OnSwitchCompleteListener` is to provide a callback for when a view switch has completed, providing the index of the newly displayed child view.

This class contains the following public method(s):

- `onSwitchComplete(int)` -- The method is called after a view switch has completed and provides the index of the newly displayed child view.

## class `com.fsck.k9.view.NonLockingScrollView$HierarchyTreeChangeListener`

The class `com.fsck.k9.view.NonLockingScrollView$HierarchyTreeChangeListener` provides functionality to listen for changes in the hierarchy tree of a scroll view and performs actions accordingly, such as updating the list of child views needing all touches if they are webviews.

This class contains the following public method(s):

- `onChildViewRemoved(android.view.View,android.view.View)` -- The method removes child views from the parent view and updates a list of children needing all touches if the child is a WebView.
- `onChildViewAdded(android.view.View,android.view.View)` -- The method adds child views to a list that need to receive all touch events if they are webviews, and if they are view groups, it recursively sets the hierarchy change listener for all children.

## class `com.fsck.k9.view.MessageCryptoStatusView`

The purpose of the `com.fsck.k9.view.MessageCryptoStatusView` class is to display the encryption/decryption status of a message by updating the color and icon displayed on the view.

This class contains the following public method(s):

- `setCryptoDisplayStatus(com.fsck.k9.view.MessageCryptoDisplayStatus)` -- Sets the display status of the message's encryption/decryption status by updating the color and icon displayed on the view.

## class `com.fsck.k9.view.FoldableLinearLayout$SavedState`

The purpose of the class `com.fsck.k9.view.FoldableLinearLayout$SavedState` is to save and restore the state of the FoldableLinearLayout in a Parcel. Specifically, it saves whether it is folded or not.

This class contains the following public method(s):

- `writeToParcel(android.os.Parcel,int)` -- The method writes the state of the FoldableLinearLayout, specifically whether it is folded or not, to a Parcel for later persistence or transfer.

## class `com.fsck.k9.view.LinearViewAnimator`

The purpose of `com.fsck.k9.view.LinearViewAnimator` is to provide animations for adding, removing, and transitioning between child views in a linear layout.

This class contains the following public method(s):

- `setUpInAnimation(android.view.animation.Animation)` -- Sets up the animation used to bring a view into the LinearViewAnimator.
- `setUpOutAnimation(android.content.Context,int)` -- The method sets up an animation for when a view is exiting the LinearViewAnimator.
- `setDownInAnimation(android.view.animation.Animation)` -- This method sets the animation used for downward item insertion in a LinearViewAnimator.
- `setUpInAnimation(android.content.Context,int)` -- This method sets up an animation for incoming views in a LinearViewAnimator using an animation resource ID loaded from the provided context.
- `setDownOutAnimation(android.content.Context,int)` -- The method sets a down-out animation on the LinearViewAnimator using a resource ID.
- `setUpOutAnimation(android.view.animation.Animation)` -- This method sets up an animation to be used when a view is removed from the LinearViewAnimator.
- `setDownOutAnimation(android.view.animation.Animation)` -- This method sets the animation used when a child view of the LinearViewAnimator is removed and moves out of the bottom of the screen.
- `setDownInAnimation(android.content.Context,int)` -- The method sets a downward animation for a LinearViewAnimator using an animation resource.
- `setDisplayedChild(int)` -- This method sets the displayed child of a LinearViewAnimator with optional animation.
- `setDisplayedChild(int,boolean)` -- This method sets the currently displayed child of the LinearViewAnimator and animates the transition if specified.

## class `com.fsck.k9.view.MessageHeader$SavedState`

The class `com.fsck.k9.view.MessageHeader$SavedState` is likely used to save the state of a MessageHeader view instance and allow recreation of that state later, for example during orientation changes or other configuration changes.

This class contains the following public method(s):

- `writeToParcel(android.os.Parcel,int)` -- This method writes the values of the object's state to a Parcel object for later retrieval.

## class `com.fsck.k9.view.ThemeUtils`

The purpose of the class `com.fsck.k9.view.ThemeUtils` is to provide methods for retrieving styled colors from a specified theme or the current theme associated with a specified attribute in Android.

This class contains the following public method(s):

- `getStyledColor(android.content.res.Resources.Theme,int)` -- The method retrieves the styled color of a specific attribute from a specified theme.
- `getStyledColor(android.content.Context,int)` -- This method returns a color resource value from the current theme associated with a specified attribute.

## class `com.fsck.k9.view.RecipientSelectView`

The purpose of `com.fsck.k9.view.RecipientSelectView` is to provide a view for selecting email recipients, including autocomplete suggestions and advanced cryptographic capabilities.

This class contains the following public method(s):

- `onLoaderReset(android.content.Loader)` -- This method resets the adapter's highlight and list of recipients when the loader for filtering recipients is reset.
- `hasUncompletedText()` -- The method checks whether there is any unfinished recipient text input in the recipient selection view.
- `onLoadFinished(android.content.Loader,java.util.List)` -- This method is called when the recipients have finished loading, and it sets them in the adapter or shows the alternate pop-up window.
- `setCryptoProvider(java.lang.String,boolean)` -- The method sets the crypto provider and determines whether advanced information should be shown.
- `setLoaderManager(android.app.LoaderManager)` -- This method sets the loader manager used for loading recipient data in the RecipientSelectView.
- `setShowCryptoEnabled(boolean)` -- The method sets whether the recipient select view displays cryptographic capabilities or not and redraws all tokens accordingly.
- `onTouchEvent(android.view.MotionEvent)` -- The method handles touch events on the recipient select view by detecting taps on token spans and displaying alternate options.
- `addRecipients(com.fsck.k9.view.RecipientSelectView$Recipient[])` -- This method adds recipients to the recipient select view.
- `showDropDown()` -- The method displays a dropdown of recipient suggestions if there is a valid adapter, otherwise it returns without doing anything.
- `onCreateLoader(int,android.os.Bundle)` -- This method is responsible for creating and returning a Loader object based on the provided ID and arguments.
- `postShowAlternatesPopup(java.util.List)` -- This method shows a popup containing a list of alternate recipients of an email address in the recipient selection view.
- `setTokenListener(com.fsck.k9.view.RecipientSelectView$TokenListener)` -- Sets a specialized version of TokenCompleteTextView.TokenListener for handling token changes in the recipient select view.
- `getAddresses()` -- The `getAddresses()` method returns an array of email addresses of recipients selected in the `RecipientSelectView`.
- `performCompletion()` -- The method is responsible for completing the input of a recipient in a recipient selection view if a valid option is selected from the dropdown menu, or if there is only one option available.
- `onKeyDown(int,android.view.KeyEvent)` -- The `onKeyDown` method dismisses the alternatesPopup and delegates further handling of the key event to the parent class.
- `isEmpty()` -- The `isEmpty()` method checks if the list of objects in the RecipientSelectView is empty or not.
- `onFocusChanged(boolean,int,android.graphics.Rect)` -- This method displays the keyboard when the view gains focus.
- `onRecipientRemove(com.fsck.k9.view.RecipientSelectView$Recipient)` -- This method dismisses the alternatesPopup and removes the currentRecipient object from the recipient select view.
- `showAlternatesPopup(java.util.List)` -- The purpose of this method is to populate and display a popup window containing alternate email addresses for a selected recipient in the recipient select view.
- `onRecipientChange(com.fsck.k9.view.RecipientSelectView$Recipient,com.fsck.k9.view.RecipientSelectView$Recipient)` -- This method updates a recipient's information with an alternate address and notifies the listener of the change.
- `tryPerformCompletion()` -- The method tries to autocomplete the user input in the recipient field and returns whether or not the number of recipients has changed as a result.

## interface `com.fsck.k9.view.CryptoModeSelector`

The interface `com.fsck.k9.view.CryptoModeSelector` is used to interact with a user interface to select and set the cryptographic status.

This class contains the following public method(s):

- `setCryptoStatusListener(com.fsck.k9.view.CryptoModeSelector$CryptoStatusSelectedListener)` -- The method sets a listener to be notified of changes in the selected cryptographic status in a user interface.
- `setCryptoStatus(com.fsck.k9.view.CryptoModeSelector$CryptoModeSelectorState)` -- The method sets the state of the crypto mode selector.

## class `com.fsck.k9.view.ColorChip`

The class is used to display a clickable colored chip in the K-9 mail application.

This class contains the following public method(s):

- `drawable()` -- The method returns the ShapeDrawable of the ColorChip view.


# package `com.fsck.k9.widget.list`

The purpose of the package `com.fsck.k9.widget.list` is to provide functionality for displaying a list of messages in the form of a widget on the home screen of an Android device.

This package contains the following class(es):

## class `com.fsck.k9.widget.list.MessageListWidgetProvider`

The purpose of the class `com.fsck.k9.widget.list.MessageListWidgetProvider` is to provide functionality for updating and managing a message list widget on the home screen of an Android device.

This class contains the following public method(s):

- `onReceive(android.content.Context,android.content.Intent)` -- This method updates the message list widget when it receives a specific action.
- `onUpdate(android.content.Context,android.appwidget.AppWidgetManager,int[])` -- This method updates the message list widget with the latest information for all app widget instances.
- `triggerMessageListWidgetUpdate(android.content.Context)` -- The method triggers an update of the message list widget for all instances of the widget on the home screen.

## class `com.fsck.k9.widget.list.MessageListWidgetService`

The purpose of the class com.fsck.k9.widget.list.MessageListWidgetService is to provide an implementation of RemoteViewsService to display a list of messages in the form of a widget.

This class contains the following public method(s):

- `onGetViewFactory(android.content.Intent)` -- The method returns a new `RemoteViewsFactory` instance for the `MessageListWidgetService`.

## class `com.fsck.k9.widget.list.MessageListRemoteViewFactory`

The purpose of the class `com.fsck.k9.widget.list.MessageListRemoteViewFactory` is to provide a factory for creating RemoteViews objects for a message list widget.

This class contains the following public method(s):

- `getLoadingView()` -- This method creates and returns a custom loading view for a message list widget.
- `getItemId(int)` -- This method returns the ID of the item at the given position in the list.
- `getCount()` -- The method returns the number of email messages in the mailItems list.
- `onDestroy()` -- This method is called to destroy the remote view factory.
- `hasStableIds()` -- This method returns a boolean indicating if the widget items have stable unique IDs that won't change after being created.
- `onCreate()` -- The method initializes variables used to display messages in the message list widget.
- `getViewTypeCount()` -- The purpose of this method is to return the number of different types of views that the adapter can create.
- `onDataSetChanged()` -- This method loads the message list used by the widget.
- `getViewAt(int)` -- This method returns a RemoteViews object for a specific position in the message list widget.


# package `com.fsck.k9.notification`

The package `com.fsck.k9.notification` provides classes to handle the creation, management, and display of notifications related to email operations in the K-9 Mail Android app, including new mail, sending, syncing, certificate and authentication errors, and wearable devices.

This package contains the following class(es):

## class `com.fsck.k9.notification.CertificateErrorNotifications`

The class `com.fsck.k9.notification.CertificateErrorNotifications` handles displaying and clearing certificate error notifications for email accounts in the K9 Email app.

This class contains the following public method(s):

- `clearCertificateErrorNotifications(com.fsck.k9.Account,boolean)` -- The method is used to clear certificate error notifications for a specified email account and direction type (incoming or outgoing).
- `showCertificateErrorNotification(com.fsck.k9.Account,boolean)` -- This method displays a notification to alert the user of a certificate error for a specific email account.

## class `com.fsck.k9.notification.SendFailedNotifications`

The purpose of the `com.fsck.k9.notification.SendFailedNotifications` class is to handle the display and clearing of notifications for failed email send attempts.

This class contains the following public method(s):

- `showSendFailedNotification(com.fsck.k9.Account,java.lang.Exception)` -- The `showSendFailedNotification` method displays a notification when an email fails to send.
- `clearSendFailedNotification(com.fsck.k9.Account)` -- This method clears the notification for a failed email sent by a specific account.

## class `com.fsck.k9.notification.NotificationContentCreator`

The purpose of `com.fsck.k9.notification.NotificationContentCreator` is to create notification message content objects from email messages and accounts.

This class contains the following public method(s):

- `createFromMessage(com.fsck.k9.Account,com.fsck.k9.mailstore.LocalMessage)` -- This method creates a notification message content object from a given email message and account.

## class `com.fsck.k9.notification.NotificationIds`

The purpose of the class `com.fsck.k9.notification.NotificationIds` is to generate unique notification IDs for different types of email notifications in the K-9 email client.

This class contains the following public method(s):

- `getAuthenticationErrorNotificationId(com.fsck.k9.Account,boolean)` -- This method returns a unique notification ID for authentication errors related to incoming or outgoing emails for a given account.
- `getCertificateErrorNotificationId(com.fsck.k9.Account,boolean)` -- This method returns a notification ID for certificate error notifications, based on the account and incoming/outgoing status.
- `getNewMailStackedNotificationId(com.fsck.k9.Account,int)` -- This method generates and returns a unique notification ID for displaying stacked notifications for new email messages in a specific email account.
- `getNewMailSummaryNotificationId(com.fsck.k9.Account)` -- This method retrieves a unique identifier for a notification related to a new email summary for a given email account.
- `getFetchingMailNotificationId(com.fsck.k9.Account)` -- This method returns the notification ID for fetching incoming mail for a specified K-9 email account.
- `getSendFailedNotificationId(com.fsck.k9.Account)` -- This method is used to get the unique notification id for a send failed notification for a particular email account.

## class `com.fsck.k9.notification.NotificationController`

The purpose of the `NotificationController` class is to handle notifications related to email operations in K-9 Mail, such as displaying notifications for new emails, sending emails, and handling authentication or certificate errors.

This class contains the following public method(s):

- `clearNewMailNotifications(com.fsck.k9.Account)` -- The method clears new mail notifications for a given account.
- `platformSupportsExtendedNotifications()` -- The method checks if the device's platform supports extended notifications by comparing its SDK version to Jelly Bean or later.
- `showSendingNotification(com.fsck.k9.Account)` -- The method is used to display a notification indicating that an email is being sent from a specific email account.
- `removeNewMailNotification(com.fsck.k9.Account,com.fsck.k9.activity.MessageReference)` -- The method removes a new mail notification for a specific account and message reference.
- `showFetchingMailNotification(com.fsck.k9.Account,com.fsck.k9.mail.Folder)` -- The method displays a notification when K-9 Mail is fetching emails.
- `clearSendingNotification(com.fsck.k9.Account)` -- The method clears the notification for a message that is currently being sent from the specified email account.
- `platformSupportsLockScreenNotifications()` -- The method checks whether the current Android version supports lock screen notifications or not.
- `clearCertificateErrorNotifications(com.fsck.k9.Account,boolean)` -- The method clears certificate error notifications for a specific account and incoming server.
- `showSendFailedNotification(com.fsck.k9.Account,java.lang.Exception)` -- The method shows a notification when an email message fails to send.
- `showAuthenticationErrorNotification(com.fsck.k9.Account,boolean)` -- The method displays an authentication error notification for a specified email account.
- `showCertificateErrorNotification(com.fsck.k9.Account,boolean)` -- The method displays a certificate error notification for a given email account.
- `newInstance(android.content.Context)` -- This method creates a new instance of `NotificationController` with the provided context and notification manager.
- `clearSendFailedNotification(com.fsck.k9.Account)` -- The method clears any send failed notifications for a given account.
- `clearAuthenticationErrorNotification(com.fsck.k9.Account,boolean)` -- The method clears authentication error notifications for a given account and incoming server.
- `clearFetchingMailNotification(com.fsck.k9.Account)` -- The method clears the notification for when K-9 Mail is fetching new emails for a specific account.
- `addNewMailNotification(com.fsck.k9.Account,com.fsck.k9.mailstore.LocalMessage,int)` -- The method adds a new email notification to the notification list.

## class `com.fsck.k9.notification.DeviceNotifications`

The purpose of the class `com.fsck.k9.notification.DeviceNotifications` is to handle the creation and management of notifications for new email messages received by a user's account.

This class contains the following public method(s):

- `buildSummaryNotification(com.fsck.k9.Account,com.fsck.k9.notification.NotificationData,boolean)` -- This method is responsible for creating and configuring a summary notification for new email messages received by a user's account.
- `newInstance(com.fsck.k9.notification.NotificationController,com.fsck.k9.notification.NotificationActionCreator,com.fsck.k9.notification.WearNotifications)` -- The method creates a new instance of `DeviceNotifications` with the given parameters.

## class `com.fsck.k9.notification.NotificationData`

The purpose of the `com.fsck.k9.notification.NotificationData` class is to manage and provide information on notifications for email messages in the K9 email client.

This class contains the following public method(s):

- `getNewMessagesCount()` -- This method returns the total count of new messages in the notification area.
- `getAllMessageReferences()` -- This method returns an `ArrayList` of `MessageReference` objects representing all the notifications currently stored in the `NotificationData` object.
- `getHolderForLatestNotification()` -- The method returns the holder for the latest notification.
- `addNotificationContent(com.fsck.k9.notification.NotificationContent)` -- This method adds a new notification content, which may reuse a recycled notification ID or create a new one if the maximum number of active notifications has not been reached.
- `hasSummaryOverflowMessages()` -- The method checks whether there are more messages in the active notifications than the maximum allowed for summary notification.
- `getActiveNotificationIds()` -- The method returns an array of active notification IDs.
- `getUnreadMessageCount()` -- The method returns the total count of unread messages along with the count of new messages.
- `containsStarredMessages()` -- This method checks if any of the active or additional notifications have at least one starred message, and returns true if one or more is found.
- `removeNotificationForMessage(com.fsck.k9.activity.MessageReference)` -- The method removes a notification associated with a specific email message and returns a result indicating whether the removal was successful and whether a replacement notification needs to be created.
- `getAccount()` -- The method returns the account associated with the notification data.
- `getSummaryOverflowMessagesCount()` -- This method returns the number of additional overflow messages that could not fit in the summary notification.
- `getContentForSummaryNotification()` -- This method retrieves a list of notification content for displaying in a summary notification.
- `isSingleMessageNotification()` -- The method checks whether the notification data is for a single message.
- `setUnreadMessageCount(int)` -- The method sets the number of unread messages in a K9 email notification.

## class `com.fsck.k9.notification.NewMailNotifications`

The purpose of the `com.fsck.k9.notification.NewMailNotifications` class is to handle the creation, removal, and clearing of new mail notifications for a given email account, as well as updating the summary notification for the account.

This class contains the following public method(s):

- `addNewMailNotification(com.fsck.k9.Account,com.fsck.k9.mailstore.LocalMessage,int)` -- The method adds a new mail notification for a given account and message, with a specified count of unread messages.
- `clearNewMailNotifications(com.fsck.k9.Account)` -- This method clears all new mail notifications associated with a given email account.
- `newInstance(com.fsck.k9.notification.NotificationController,com.fsck.k9.notification.NotificationActionCreator)` -- The method creates a new instance of the `NewMailNotifications` class with the given dependencies.
- `removeNewMailNotification(com.fsck.k9.Account,com.fsck.k9.activity.MessageReference)` -- The method removes a new mail notification for a specific account and message, and updates the summary notification for the account.

## class `com.fsck.k9.notification.WearNotifications`

The purpose of the `com.fsck.k9.notification.WearNotifications` class is to handle notifications for wearable devices and build stacked notifications for email accounts in the K9 email client app.

This class contains the following public method(s):

- `addSummaryActions(android.support.v4.app.NotificationCompat.Builder,com.fsck.k9.notification.NotificationData)` -- The method adds actions to a summary notification for wearable devices based on the notification data.
- `buildStackedNotification(com.fsck.k9.Account,com.fsck.k9.notification.NotificationHolder)` -- This method builds a stacked notification with multiple messages for a given email account in the K9 email client app.

## class `com.fsck.k9.notification.AuthenticationErrorNotifications`

The class `com.fsck.k9.notification.AuthenticationErrorNotifications` is responsible for showing and clearing notifications for authentication errors on email accounts' incoming or outgoing servers.

This class contains the following public method(s):

- `showAuthenticationErrorNotification(com.fsck.k9.Account,boolean)` -- This method shows a notification for authentication errors on a given account's incoming or outgoing server.
- `clearAuthenticationErrorNotification(com.fsck.k9.Account,boolean)` -- This method clears the authentication error notification for a specific account and incoming server.

## class `com.fsck.k9.notification.SyncNotifications`

The purpose of the class `com.fsck.k9.notification.SyncNotifications` is to manage and display notifications related to email syncing and sending for the K-9 Mail app.

This class contains the following public method(s):

- `clearFetchingMailNotification(com.fsck.k9.Account)` -- The method clears a notification that is related to fetching mail for a specific email account.
- `showFetchingMailNotification(com.fsck.k9.Account,com.fsck.k9.mail.Folder)` -- The method displays a notification for when the app is fetching mail from a specified account and folder.
- `showSendingNotification(com.fsck.k9.Account)` -- This method creates and displays a notification indicating that email from a specified account is being sent.
- `clearSendingNotification(com.fsck.k9.Account)` -- The purpose of this method is to clear the notification of mail being sent for a specific account.

## class `com.fsck.k9.notification.RemoveNotificationResult`

The class is responsible for providing information on the removal of a notification and whether it should be recreated.

This class contains the following public method(s):

- `shouldCreateNotification()` -- This method returns a boolean indicating whether a notification should be created based on the existence of a notification holder.
- `unknownNotification()` -- The method creates a new instance of `RemoveNotificationResult` with `null` values and a flag set to `true`, indicating an unknown notification.
- `getNotificationHolder()` -- This method returns the `NotificationHolder` if `shouldCreateNotification()` returns true, otherwise throws an `IllegalStateException`.
- `createNotification(com.fsck.k9.notification.NotificationHolder)` -- The method creates a new instance of `RemoveNotificationResult` with a given `NotificationHolder` and a flag indicating whether the notification was cancelled.
- `isUnknownNotification()` -- This method checks if the notification is unknown or not.
- `cancelNotification(int)` -- The method creates a new `RemoveNotificationResult` object with the provided notification ID and a `false` value indicating that the notification was not successfully canceled.
- `getNotificationId()` -- This method returns the ID of a notification, unless it is an unknown notification.

## class `com.fsck.k9.notification.NotificationActionCreator`

The class `com.fsck.k9.notification.NotificationActionCreator` contains methods to create pending intents for various actions related to K-9 email notifications, such as marking messages as read, deleting messages, archiving messages, and opening specific folders.

This class contains the following public method(s):

- `createMarkAllAsReadPendingIntent(com.fsck.k9.Account,java.util.List,int)` -- This method creates a pending intent to mark all specified messages as read for a given account and notification ID.
- `createArchiveMessagePendingIntent(com.fsck.k9.activity.MessageReference,int)` -- The method creates a Pending Intent for archiving a K-9 email message from the notification.
- `createDeleteMessagePendingIntent(com.fsck.k9.activity.MessageReference,int)` -- This method creates a pending intent to delete a message either by displaying a confirmation or by directly calling the delete service.
- `createViewFolderPendingIntent(com.fsck.k9.Account,java.lang.String,int)` -- This method creates a pending intent for viewing a specific folder in K-9 email client.
- `createArchiveAllPendingIntent(com.fsck.k9.Account,java.util.List,int)` -- The method creates a PendingIntent to archive all messages for a given account and list of message references.
- `createMarkMessageAsReadPendingIntent(com.fsck.k9.activity.MessageReference,int)` -- The method creates a PendingIntent to mark a message as read when the corresponding notification is clicked.
- `createDeleteAllPendingIntent(com.fsck.k9.Account,java.util.List,int)` -- The method creates a PendingIntent to delete all messages associated with a notification, with an option to confirm before deleting.
- `getDeleteAllPendingIntent(com.fsck.k9.Account,java.util.List,int)` -- This method returns a PendingIntent for deleting all the pending notifications.
- `createViewFolderListPendingIntent(com.fsck.k9.Account,int)` -- The method creates a pending intent that launches the folder list activity for a specific K-9 email account.
- `createViewMessagePendingIntent(com.fsck.k9.activity.MessageReference,int)` -- This method creates a Pending Intent that opens the message referenced by a notification when clicked.
- `getMarkAllAsReadPendingIntent(com.fsck.k9.Account,java.util.List,int)` -- The method returns a PendingIntent for marking all notifications of a specific account as read.
- `createReplyPendingIntent(com.fsck.k9.activity.MessageReference,int)` -- This method creates a PendingIntent for replying to a specific email message.
- `createViewMessagesPendingIntent(com.fsck.k9.Account,java.util.List,int)` -- Creates a pending intent for viewing a list of messages based on the account and message references provided.
- `createDismissAllMessagesPendingIntent(com.fsck.k9.Account,int)` -- The method creates a pending intent to dismiss all messages in a notification for a specific account.
- `createDismissMessagePendingIntent(android.content.Context,com.fsck.k9.activity.MessageReference,int)` -- This method creates a PendingIntent to dismiss a notification for a specific message.
- `createMarkMessageAsSpamPendingIntent(com.fsck.k9.activity.MessageReference,int)` -- The purpose of this method is to create a Pending Intent that will mark a message as spam when triggered from a notification.

## class `com.fsck.k9.notification.LockScreenNotification`

The purpose of `com.fsck.k9.notification.LockScreenNotification` is to provide methods for configuring and creating lock screen notifications for the K-9 Mail app.

This class contains the following public method(s):

- `configureLockScreenNotification(android.support.v4.app.NotificationCompat.Builder,com.fsck.k9.notification.NotificationData)` -- This method configures the visibility of lock screen notifications based on user preferences and notification data.
- `newInstance(com.fsck.k9.notification.NotificationController)` -- This static method creates a new instance of `LockScreenNotification` with the given `NotificationController`.

## class `com.fsck.k9.notification.NotificationGroupKeys`

The purpose of the class `com.fsck.k9.notification.NotificationGroupKeys` is to generate group keys for notifications related to a specific account.

This class contains the following public method(s):

- `getGroupKey(com.fsck.k9.Account)` -- This method returns the group key for notifications related to a specific account by concatenating a prefix with the account number.

## class `com.fsck.k9.notification.NotificationActionService`

The purpose of `com.fsck.k9.notification.NotificationActionService` is to handle various notification actions for the K-9 Mail app, such as marking messages as read or archiving them.

This class contains the following public method(s):

- `createDeleteAllMessagesIntent(android.content.Context,java.lang.String,java.util.List)` -- Creates an intent to delete all messages for a specified account and list of message references.
- `startService(android.content.Intent,int)` -- This method handles various notification actions (such as marking messages as read or archiving them) based on the intent received.

## class `com.fsck.k9.notification.AddNotificationResult`

The `com.fsck.k9.notification.AddNotificationResult` class is responsible for handling the creation and management of notifications in the K-9 Mail Android app, including replacing, cancelling, and retrieving information about existing notifications.

This class contains the following public method(s):

- `newNotification(com.fsck.k9.notification.NotificationHolder)` -- The method creates a new `AddNotificationResult` object with the given `NotificationHolder` and a `false` value for a boolean parameter.
- `shouldCancelNotification()` -- This method returns a boolean indicating whether a notification should be cancelled before it is reused.
- `replaceNotification(com.fsck.k9.notification.NotificationHolder)` -- The purpose of the method is to create a new instance of `AddNotificationResult` with the given `NotificationHolder` and a flag indicating that a notification was replaced.
- `getNotificationHolder()` -- The method returns a NotificationHolder object for use in the K-9 Mail Android app's notification system.
- `getNotificationId()` -- The method gets the notification ID stored in `notificationHolder` if `shouldCancelNotification()` returns true, else it throws an exception.


# package `com.fsck.k9.power`

The package `com.fsck.k9.power` is for managing the device idle state and battery optimizations in the K-9 Mail app.

This package contains the following class(es):

## abstract class `com.fsck.k9.power.DeviceIdleManager`

The purpose of the abstract class `com.fsck.k9.power.DeviceIdleManager` is to manage the device idle state and register a broadcast receiver to listen for any changes in the idle state.

This class contains the following public method(s):

- `registerReceiver()` -- The method is used to register a broadcast receiver to listen for device idle state changes.
- `getInstance(android.content.Context)` -- This method returns a static instance of `DeviceIdleManager` based on whether the device supports idle mode and if the app is whitelisted.
- `unregisterReceiver()` -- The method unregisters a broadcast receiver from receiving future broadcasts.

## class `com.fsck.k9.power.DozeChecker`

The purpose of the class `com.fsck.k9.power.DozeChecker` is to check whether the device is in idle mode and whether the app is whitelisted to ignore battery optimizations.

This class contains the following public method(s):

- `isDeviceIdleModeSupported()` -- This method checks if the device supports the idle mode introduced in Android Marshmallow.
- `isAppWhitelisted()` -- The method checks if the app is whitelisted to ignore battery optimizations imposed by the system.

## class `com.fsck.k9.power.DeviceIdleReceiver`

The purpose of the class `com.fsck.k9.power.DeviceIdleReceiver` is to receive notifications when the device enters or exits idle mode and reset the K-9 Mail service accordingly.

This class contains the following public method(s):

- `onReceive(android.content.Context,android.content.Intent)` -- The method is a callback that is triggered when the device enters or exits idle mode and resets the K-9 Mail service if the device is not in idle mode.

## class `com.fsck.k9.power.DeviceIdleManager$RealDeviceIdleManager`

The purpose of the `com.fsck.k9.power.DeviceIdleManager$RealDeviceIdleManager` class is to manage the device idle state and register/unregister the `DeviceIdleReceiver` for the K-9 Mail app.

This class contains the following public method(s):

- `unregisterReceiver()` -- This method unregisters the `DeviceIdleReceiver` if it was previously registered.
- `registerReceiver()` -- The method registers a device idle receiver.

## class `com.fsck.k9.power.DeviceIdleManager$NoOpDeviceIdleManager`

The `NoOpDeviceIdleManager` class is a no-operation implementation of the `DeviceIdleManager` class, used for cases when the device does not support idle mode.

This class contains the following public method(s):

- `unregisterReceiver()` -- This method unregisters the receiver by doing nothing, as it is a no-op implementation.
- `registerReceiver()` -- The method `registerReceiver()` does nothing as it is a no-op implementation for the `DeviceIdleManager` class.


# package `com.fsck.k9.preferences`

The package `com.fsck.k9.preferences` contains classes for managing and manipulating preferences and settings related to the K-9 Mail email client application.

This package contains the following class(es):

## class `com.fsck.k9.preferences.FolderSettings`

The purpose of the `com.fsck.k9.preferences.FolderSettings` class is to provide methods for converting and upgrading folder settings in the K-9 Mail application.

This class contains the following public method(s):

- `convert(java.util.Map)` -- This method converts a `java.util.Map` object of folder settings from `java.lang.Object` to `java.lang.String` format.
- `upgrade(int,java.util.Map)` -- The method upgrades the folder settings by running the generic `upgrade()` method with specific parameters.

## class `com.fsck.k9.preferences.GlobalSettings$DirectorySetting`

The purpose of `com.fsck.k9.preferences.GlobalSettings$DirectorySetting` is to provide a way to store and validate directory paths in K-9 Mail's global settings.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- This method converts a string to a directory path and validates that it exists on the file system.

## class `com.fsck.k9.preferences.GlobalSettings$SettingsUpgraderV12`

The class is responsible for upgrading the global settings of the K-9 Mail app to version 12 by changing the notificationHideSubject based on the keyguardPrivacy setting.

This class contains the following public method(s):

- `upgrade(java.util.Map)` -- The method upgrades the global settings by changing the notificationHideSubject based on the value of the keyguardPrivacy setting.

## class `com.fsck.k9.preferences.Settings$BooleanSetting`

The class is likely a part of a preferences/settings system in the K9 email client for Android, and specifically handles boolean preferences by providing a method to convert a string representation of a boolean value into a Boolean object.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- The method converts a string representation of a boolean value into a Boolean object.

## abstract class `com.fsck.k9.preferences.Settings$PseudoEnumSetting`

The abstract class `com.fsck.k9.preferences.Settings$PseudoEnumSetting` is a template for creating settings that act like enums but are not actual enums, allowing for more flexibility in customization of preferences.

This class contains the following public method(s):

- `toPrettyString(java.lang.Object)` -- The method returns the mapping of a specific value in a human-readable format.
- `fromPrettyString(java.lang.String)` -- The method converts a user-friendly string representation of a preference setting to its corresponding internal value.

## class `com.fsck.k9.preferences.SettingsExporter`

The purpose of the class `com.fsck.k9.preferences.SettingsExporter` is to export the settings of an Android app, including global settings and settings for specified accounts, to a file on external storage or a specified URI.

This class contains the following public method(s):

- `exportToFile(android.content.Context,boolean,java.util.Set)` -- The purpose of this method is to export the settings of an Android app to a file on external storage, including global settings and settings for specified accounts.
- `exportToUri(android.content.Context,boolean,java.util.Set,android.net.Uri)` -- This method exports K-9 Mail app settings to a specified URI (file or content provider).
- `generateDatedExportFileName()` -- This method generates a filename for exporting K-9 Mail settings with the current date.

## class `com.fsck.k9.preferences.GlobalSettings$LanguageSetting`

The purpose of the class `com.fsck.k9.preferences.GlobalSettings$LanguageSetting` is to provide a way to manage language settings in the K-9 Mail email client.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- This method converts a string value to a language setting, and if the value is not valid, it throws an exception.

## class `com.fsck.k9.preferences.Settings$EnumSetting`

The class `com.fsck.k9.preferences.Settings$EnumSetting` is likely used to store and manage preferences for a specific setting that is represented as an Enum type object in the K-9 email client for Android.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- This method converts a String to an Enum type object.

## class `com.fsck.k9.preferences.CheckBoxListPreference`

The class `com.fsck.k9.preferences.CheckBoxListPreference` is a custom preference class that allows the user to select multiple options from a list using checkboxes.

This class contains the following public method(s):

- `getCheckedItems()` -- The method returns an array of booleans representing the checked state of each item in a list.
- `setItems(java.lang.CharSequence[])` -- The method sets the items to be displayed in a checkbox list preference.
- `setCheckedItems(boolean[])` -- This method sets the boolean array of checked items for a checkbox list preference.

## class `com.fsck.k9.preferences.Settings`

The `com.fsck.k9.preferences.Settings` class manages the conversion and upgrading of settings for the email client K-9 Mail.

This class contains the following public method(s):

- `convert(java.util.Map,java.util.Map)` -- This method converts settings from the internal representation to the string representation used in the preference storage.
- `upgrade(int,java.util.Map,java.util.Map,java.util.Map)` -- The method upgrades settings for a given version using custom upgraders and a settings structure.

## class `com.fsck.k9.preferences.GlobalSettings$TimeSetting`

The purpose of the class `com.fsck.k9.preferences.GlobalSettings$TimeSetting` is to handle time-setting preferences in the K9 email application.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- This method converts a string into a time-setting value and validates it against a regular expression.

## class `com.fsck.k9.preferences.SettingsImporter$ImportedServerSettings`

The `com.fsck.k9.preferences.SettingsImporter$ImportedServerSettings` class is used to store and retrieve settings for an imported mail server, including any extra settings that may be present.

This class contains the following public method(s):

- `getExtra()` -- The method returns an unmodifiable map of extra settings for an imported mail server.

## class `com.fsck.k9.preferences.Settings$ColorSetting`

The class `com.fsck.k9.preferences.Settings$ColorSetting` is used to handle color settings and conversions between different representations of colors in K-9 Mail's preferences.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- This method converts a String representation of a color setting into an Integer.
- `fromPrettyString(java.lang.String)` -- This method converts a hexadecimal color string of the format "#RRGGBB" to an `Integer` value.
- `toPrettyString(java.lang.Integer)` -- This method converts an integer representing a color to a hexadecimal string value with a hashtag (#) prefix.

## class `com.fsck.k9.preferences.AccountSettings$RingtoneSetting`

The class `com.fsck.k9.preferences.AccountSettings$RingtoneSetting` represents a setting for the ringtone of an email account in the K-9 Mail app. Its `fromString` method is used to convert a string representation of the setting into an actual instance of the `RingtoneSetting` class.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- The `fromString` method returns a given string value.

## class `com.fsck.k9.preferences.AccountSettings$DeletePolicySetting`

The class `com.fsck.k9.preferences.AccountSettings$DeletePolicySetting` is designed to manage and validate the delete policy settings for email accounts in the K-9 Mail app.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- The `fromString` method converts a string to an Integer and validates it against a predefined mapping, and if valid, returns the Integer value.

## class `com.fsck.k9.preferences.Settings$IntegerRangeSetting`

The class `com.fsck.k9.preferences.Settings$IntegerRangeSetting` is used to store integer values within a specified range and provides a method for converting a string to an integer within that range.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- This method converts a string value to an integer and checks if it falls within a specified range before returning the integer value.

## class `com.fsck.k9.preferences.Settings$WebFontSizeSetting`

The class represents a setting for the web font size in the K9 email client and provides a method for parsing and validating a String representation of the setting.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- The method converts a String value into an Integer while validating it against a mapping and throwing an exception if it fails.

## class `com.fsck.k9.preferences.GlobalSettings$SubThemeSetting`

The class `com.fsck.k9.preferences.GlobalSettings$SubThemeSetting` is used to manage sub-theme settings for the K9 email application, including converting string representations of sub-theme settings to K9 Theme objects and vice versa.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- (no description)
- `toPrettyString(com.fsck.k9.K9$Theme)` -- (no description)
- `fromPrettyString(java.lang.String)` -- This method converts a String representation of a sub-theme setting to a K9 Theme object.

## class `com.fsck.k9.preferences.GlobalSettings`

The class `com.fsck.k9.preferences.GlobalSettings` is used to manage and convert settings from various formats in the K-9 Mail email client.

This class contains the following public method(s):

- `convert(java.util.Map)` -- The method converts a `java.util.Map` of `java.lang.Object` values to a `java.util.Map` of `java.lang.String` values using the `SETTINGS` constant defined in `com.fsck.k9.preferences.GlobalSettings`.
- `upgrade(int,java.util.Map)` -- The method upgrades the settings stored in validatedSettings to the latest version based on the version passed as an argument and returns a set of all the settings upgraded.

## class `com.fsck.k9.preferences.AccountSettings$StringResourceSetting`

`com.fsck.k9.preferences.AccountSettings$StringResourceSetting` is a class that maps string values to their corresponding resource values and provides a method to get the string value if it exists.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- This method returns a string value if it exists in the mapping, and throws an exception otherwise.

## class `com.fsck.k9.preferences.AccountSettings$IntegerResourceSetting`

The purpose of the `com.fsck.k9.preferences.AccountSettings$IntegerResourceSetting` class is to provide functionality for converting a string to an integer value for a specific account setting.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- The method converts a string to an integer value for a specific account setting while handling any parsing errors that may occur.

## class `com.fsck.k9.preferences.GlobalSettings$SettingsUpgraderV31`

The purpose of this class is to upgrade font size preferences in the passed settings map to a new format and convert old size preferences into new size preferences using its public methods.

This class contains the following public method(s):

- `convertFromOldSize(int)` -- To convert old size preferences into new size preferences, returning an integer value representing the new size.
- `upgrade(java.util.Map)` -- The method upgrades the font size setting in the passed `settings` map to a new format and returns the name of the updated setting.

## class `com.fsck.k9.preferences.AccountSettings$StorageProviderSetting`

The purpose of the class `com.fsck.k9.preferences.AccountSettings$StorageProviderSetting` is to manage and provide access to storage providers for email accounts in the K-9 email app.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- This method validates whether a given string matches an available storage provider and returns it if it does. Otherwise, it throws a runtime exception.
- `getDefaultValue()` -- The method returns the default storage provider ID for the K-9 email app.

## interface `com.fsck.k9.preferences.Settings$SettingsUpgrader`

The `com.fsck.k9.preferences.Settings$SettingsUpgrader` interface is used to upgrade a settings map and returns a set of removed setting names.

This class contains the following public method(s):

- `upgrade(java.util.Map)` -- The method upgrades the provided settings map and returns a Set of removed setting names or null if none were removed.

## class `com.fsck.k9.preferences.StorageEditor`

The purpose of the `com.fsck.k9.preferences.StorageEditor` class is to provide a way to edit and modify preferences in a key-value storage system, allowing for the addition, removal, and modification of values associated with specific keys.

This class contains the following public method(s):

- `putLong(java.lang.String,long)` -- The `putLong` method is used to add a long value to a key-value store and return the editor to allow for chaining method calls.
- `putBoolean(java.lang.String,boolean)` -- The method is used to store a boolean value for a given key in a storage editor.
- `putInt(java.lang.String,int)` -- This method adds an integer value to the changes map of the StorageEditor instance.
- `putString(java.lang.String,java.lang.String)` -- This method puts a string value into the changes map with the provided key, and removes the key if the value is null.
- `copy(android.content.SharedPreferences)` -- The method copies the contents of an input SharedPreferences object to the current StorageEditor instance.
- `commit()` -- The method commits the changes made in the preferences storage.
- `remove(java.lang.String)` -- The method adds a key to a list of removals in order to remove it from the storage.

## class `com.fsck.k9.preferences.GlobalSettings$SettingsUpgraderV24`

The purpose of the class `com.fsck.k9.preferences.GlobalSettings$SettingsUpgraderV24` is to upgrade the preferences settings for the K-9 email client, specifically setting the "messageViewTheme" to "USE_GLOBAL".

This class contains the following public method(s):

- `upgrade(java.util.Map)` -- This method upgrades the preferences settings for the K-9 email client, specifically making sure that the "messageViewTheme" setting is set to "USE_GLOBAL" if it was previously set to match the overall theme.

## class `com.fsck.k9.preferences.SettingsImporter`

The purpose of `com.fsck.k9.preferences.SettingsImporter` is to provide methods for importing settings and account configurations for the K-9 Mail app in Android.

This class contains the following public method(s):

- `getImportStreamContents(java.io.InputStream)` -- This method parses an input stream containing settings, determines if it contains global and/or account settings, and returns the account names and UUIDs found.
- `importSettings(android.content.Context,java.io.InputStream,boolean,java.util.List,boolean)` -- This method imports global settings and/or account configurations from an input stream for a specified list of accounts and overwrites existing accounts if requested.

## class `com.fsck.k9.preferences.IdentitySettings$SignatureSetting`

The purpose of the `SignatureSetting` class is to provide methods for managing the signature setting of an email identity, including retrieving the default value and converting a string value.

This class contains the following public method(s):

- `getDefaultValue()` -- This method returns the default value for the signature setting of an email identity.
- `fromString(java.lang.String)` -- This method returns a given string value.

## abstract class `com.fsck.k9.preferences.Settings$SettingsDescription`

The purpose of the abstract class `com.fsck.k9.preferences.Settings$SettingsDescription` is to provide a description of a setting's default value, its internal and human-readable string representations, and methods to convert between them.

This class contains the following public method(s):

- `getDefaultValue()` -- This method returns the internal representation of the default value of the setting.
- `fromString(java.lang.String)` -- The method converts a string representation of a setting's value to its internal representation and throws an exception if the value is invalid.
- `toString(java.lang.Object)` -- The method returns the string representation of a setting's value in its internal format.
- `fromPrettyString(java.lang.String)` -- The method converts the pretty-printed version of a setting's value to its internal representation.
- `toPrettyString(java.lang.Object)` -- The method converts a setting value to a human-readable string representation.

## class `com.fsck.k9.preferences.IdentitySettings`

The purpose of the class `com.fsck.k9.preferences.IdentitySettings` is to provide methods for upgrading and converting settings for an email identity in the K-9 Mail email client.

This class contains the following public method(s):

- `upgrade(int,java.util.Map)` -- The method upgrades the settings for an email identity in K-9 Mail based on the version and a map of validated settings.
- `convert(java.util.Map)` -- This method converts a map of object-type values to a map of string-type values specifically for identity settings in the K9 email client.

## class `com.fsck.k9.preferences.IdentitySettings$OptionalEmailAddressSetting`

The purpose of the class is to provide methods for handling email addresses in identity settings, including validation and conversion of input values.

This class contains the following public method(s):

- `fromPrettyString(java.lang.String)` -- This method converts a pretty string representation of an email address into a non-null string value.
- `fromString(java.lang.String)` -- This method validates and returns a string email address for a specific identity setting.
- `toPrettyString(java.lang.String)` -- The method returns an empty string if the input value is null, otherwise returns the input value.
- `toString(java.lang.String)` -- This method returns a string input value if it is not null, and null if it is.

## class `com.fsck.k9.preferences.Storage`

The purpose of the class `com.fsck.k9.preferences.Storage` is to provide methods for storing and retrieving key-value pairs in SharedPreferences in an Android application.

This class contains the following public method(s):

- `isEmpty()` -- The `isEmpty()` method returns whether or not the `storage` object is empty.
- `contains(java.lang.String)` -- The method checks if the given key is contained in the storage.
- `getString(java.lang.String,java.lang.String)` -- This method gets the string value associated with a given key from the storage or returns the default value if it doesn't exist.
- `getBoolean(java.lang.String,boolean)` -- The method retrieves a boolean value from the stored preferences, or returns a default value if the key is not found, and parses the string representation of the value to a boolean.
- `edit()` -- The purpose of the `edit()` method is to return a new `com.fsck.k9.preferences.StorageEditor` instance based on the current `com.fsck.k9.preferences.Storage` instance.
- `getLong(java.lang.String,long)` -- This method gets the value associated with the given key as a long, and returns a default value if the key is not found or the value cannot be parsed as a long.
- `getInt(java.lang.String,int)` -- The method returns an integer value associated with a given key in the storage or a provided default value if the key is not found or the value cannot be parsed as an integer.
- `getAll()` -- The method returns a map containing all the key-value pairs stored in the preferences storage.
- `getStorage(android.content.Context)` -- The `getStorage` method retrieves an instance of the `Storage` class for a given Android context, creating a new instance if necessary or returning an existing one.

## class `com.fsck.k9.preferences.TimePickerPreference`

The class `com.fsck.k9.preferences.TimePickerPreference` provides a way to display and set time preferences in an Android app and allows for persistence and validation of time values.

This class contains the following public method(s):

- `onTimeChanged(android.widget.TimePicker,int,int)` -- This method is called when the time is changed in a TimePickerPreference and persists the new time and notifies the change listener.
- `getTime()` -- This method returns the time value as a string in the format "hh:mm" from the TimePickerPreference.
- `setDefaultValue(java.lang.Object)` -- The purpose of this method is to set the default value of a TimePickerPreference object and validate that the default value is a valid time string.

## class `com.fsck.k9.preferences.Settings$StringSetting`

The class represents a string setting in the K-9 Mail email client preferences and provides a method to convert a string value to a `String` object.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- The method returns a `String` value that is passed in as an argument.

## class `com.fsck.k9.preferences.Settings$FontSizeSetting`

The purpose of the `com.fsck.k9.preferences.Settings$FontSizeSetting` class is to handle font size settings and provide a method to parse font size strings and return their integer values.

This class contains the following public method(s):

- `fromString(java.lang.String)` -- The purpose of the `fromString` method is to parse a string and return its integer value if it is a valid font size according to a predefined mapping, otherwise it throws an exception.

## class `com.fsck.k9.preferences.GlobalSettings$ThemeSetting`

The class `com.fsck.k9.preferences.GlobalSettings$ThemeSetting` is responsible for converting between a string representation of a K9 theme and the corresponding enum value, as well as providing a readable string format for the theme setting.

This class contains the following public method(s):

- `toString(com.fsck.k9.K9$Theme)` -- The method returns a string representation of the ordinal value of a given K9 theme.
- `fromString(java.lang.String)` -- The `fromString` method parses a String representing a theme and returns the corresponding enum value.
- `toPrettyString(com.fsck.k9.K9$Theme)` -- The method returns a String representing the theme setting in a readable format for display purposes.
- `fromPrettyString(java.lang.String)` -- The method converts a string representation of a theme setting into a K9 theme object.

## class `com.fsck.k9.preferences.AccountSettings`

The class `com.fsck.k9.preferences.AccountSettings` is used to manage and manipulate email account settings in the K-9 Mail app, including upgrading and converting these settings.

This class contains the following public method(s):

- `upgrade(int,java.util.Map)` -- The method upgrades the account settings of an email account based on a specified version and validated settings.
- `convert(java.util.Map)` -- This method converts a map of account settings from object type to string type.


# package `com.fsck.k9.provider`

The purpose of the package `com.fsck.k9.provider` is to provide classes and interfaces to interact with the K-9 Mail content provider and manage email messages, attachments, and temporary files in the K9 email client on Android devices.

This package contains the following class(es):

## class `com.fsck.k9.provider.AttachmentProvider`

The purpose of the `com.fsck.k9.provider.AttachmentProvider` is to provide an interface for accessing and manipulating email attachments stored locally by the K-9 Mail application in an Android device.

This class contains the following public method(s):

- `onCreate()` -- The `onCreate()` method returns `true` to indicate that the `AttachmentProvider` has been successfully created.
- `update(android.net.Uri,android.content.ContentValues,java.lang.String,java.lang.String[])` -- The method throws an UnsupportedOperationException and does not provide any functionality.
- `insert(android.net.Uri,android.content.ContentValues)` -- The method throws an UnsupportedOperationException when called.
- `getAttachmentUri(java.lang.String,long)` -- The method returns a URI to retrieve a specific attachment from a given email account and attachment ID.
- `openFile(android.net.Uri,java.lang.String)` -- This method opens a file for a given attachment URI and returns a `ParcelFileDescriptor`.
- `delete(android.net.Uri,java.lang.String,java.lang.String[])` -- This method throws an UnsupportedOperationException and does not perform any deletion on the given Uri.
- `getType(android.net.Uri)` -- This method retrieves the MIME type of an attachment given its URI.
- `query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)` -- This method queries the local store for information about an email attachment and returns a cursor containing the requested data.

## class `com.fsck.k9.provider.MessageProvider$MessagesQueryHandler`

The purpose of the class `com.fsck.k9.provider.MessageProvider$MessagesQueryHandler` is to handle queries for retrieving message data from the message provider in a mail application.

This class contains the following public method(s):

- `query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)` -- This method queries the message provider to retrieve a Cursor containing the requested message data.
- `getPath()` -- The method returns the path "inbox_messages/" for the messages query handler of a mail application.

## class `com.fsck.k9.provider.MessageProvider$AccountNumberExtractor`

The purpose of the class `com.fsck.k9.provider.MessageProvider$AccountNumberExtractor` is to extract the account number integer value from a `MessageInfoHolder` object.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- This method retrieves the account number integer value from a `MessageInfoHolder` object.

## class `com.fsck.k9.provider.MessageProvider$CountExtractor`

The class `com.fsck.k9.provider.MessageProvider$CountExtractor` is designed to extract the count of messages from a message provider as a Java Integer object.

This class contains the following public method(s):

- `getField(java.lang.Object)` -- This method returns the count as a Java Integer object.

## class `com.fsck.k9.provider.MessageProvider$DeleteUriExtractor`

The purpose of the class `com.fsck.k9.provider.MessageProvider$DeleteUriExtractor` is to extract the URI for deleting a specified message in K-9 Mail.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- This method generates a URI for deleting a specified message in K-9 Mail.

## class `com.fsck.k9.provider.EmailProvider`

The purpose of the `com.fsck.k9.provider.EmailProvider` class is to provide access to the email provider database and handle queries, updates, and deletions of email messages.

This class contains the following public method(s):

- `query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)` -- This method queries the email provider database to retrieve messages or account statistics based on the given Uri, projection, selection, selectionArgs, and sortOrder parameters.
- `delete(android.net.Uri,java.lang.String,java.lang.String[])` -- The method is designed to delete data from the EmailProvider but is not currently implemented.
- `getType(android.net.Uri)` -- This method is not implemented and throws a runtime exception when called.
- `update(android.net.Uri,android.content.ContentValues,java.lang.String,java.lang.String[])` -- This method updates the specified row(s) with the given ContentValues in the EmailProvider content provider.
- `insert(android.net.Uri,android.content.ContentValues)` -- The method is not implemented yet and throws a runtime exception.
- `onCreate()` -- This method is used to initialize the EmailProvider and returns true after successful execution.

## class `com.fsck.k9.provider.MessageProvider$AccountColorExtractor`

The class `com.fsck.k9.provider.MessageProvider$AccountColorExtractor` is responsible for extracting the account color of a message for use in displaying it in the user interface.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- This method extracts the account color of a message for use in displaying it in the user interface.

## class `com.fsck.k9.provider.MessageProvider$HasAttachmentsExtractor`

The class is used to extract whether a message has attachments or not from a `MessageInfoHolder` object in the K-9 Mail application.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- This method returns a boolean value indicating whether the message has attachments or not.

## class `com.fsck.k9.provider.MessageProvider$MessageInfoHolderRetrieverListener`

The class is responsible for retrieving and providing information about message holders and local messages in the K-9 email client application.

This class contains the following public method(s):

- `searchStats(com.fsck.k9.AccountStats)` -- The method puts the message information holders into a queue for use by the caller.
- `listLocalMessagesAddMessages(com.fsck.k9.Account,java.lang.String,java.util.List)` -- This method adds local messages to a list of `MessageInfoHolder`s, along with additional information about their folder and account.

## class `com.fsck.k9.provider.DecryptedFileProvider`

The class provides a content provider for temporary decrypted files that can be accessed by other apps, with methods to create, delete, and trim these files, and to decode encoded files.

This class contains the following public method(s):

- `onTrimMemory(int)` -- The method is executed when the system is running low on memory and deletes old temporary files.
- `getFileFactory(android.content.Context)` -- The method returns a `FileFactory` that creates temporary decrypted files and registers a receiver to clean up those files.
- `getUriForProvidedFile(android.content.Context,java.io.File,java.lang.String,java.lang.String)` -- This method generates a `Uri` for a given file to be used by other apps for accessing the file's content along with optional encoding and MIME type.
- `deleteOldTemporaryFiles(android.content.Context)` -- This method deletes temporary files that are older than a certain threshold time.
- `getType(android.net.Uri)` -- The method returns the MIME type of the content specified by the given URI.
- `delete(android.net.Uri,java.lang.String,java.lang.String[])` -- The method throws an exception when attempting to delete a decrypted file in order to protect sensitive information.
- `openFile(android.net.Uri,java.lang.String)` -- This method opens a file for reading from a given URI, decodes it if it is encoded in base64 or quoted-printable, and returns a `ParcelFileDescriptor`.

## class `com.fsck.k9.provider.MessageProvider$ThrottlingQueryHandler`

The purpose of `com.fsck.k9.provider.MessageProvider$ThrottlingQueryHandler` is to provide a query handler that returns a cursor for a given URI and ensures that the cursor is closed after a certain time period to prevent memory leaks.

This class contains the following public method(s):

- `getPath()` -- The method returns the path of the query handler.
- `query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)` -- This method returns a cursor for a given URI, and ensures that the cursor is closed after a certain time period to prevent memory leaks.

## class `com.fsck.k9.provider.MessageProvider$SubjectExtractor`

The purpose of the class `com.fsck.k9.provider.MessageProvider$SubjectExtractor` is to extract the subject of an email message.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- The `getField` method returns the subject of a given email message.

## class `com.fsck.k9.provider.MessageProvider$PreviewExtractor`

The purpose of the class `com.fsck.k9.provider.MessageProvider$PreviewExtractor` is to extract the preview of a message for display purposes.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- This method returns the preview of a message for display purposes.

## class `com.fsck.k9.provider.MessageProvider$IncrementExtractor`

The purpose of the class `com.fsck.k9.provider.MessageProvider$IncrementExtractor` is to extract an incremented count of the number of messages from a `MessageInfoHolder` object.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- The method returns an incremented count of the number of messages.

## class `com.fsck.k9.provider.MessageProvider$HasStarExtractor`

The purpose of the class `com.fsck.k9.provider.MessageProvider$HasStarExtractor` is to extract the "has starred" field from a `MessageInfoHolder` object in the K-9 Mail app.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- The method returns a Boolean indicating if a MessageInfoHolder's message has the FLAGGED flag set.

## class `com.fsck.k9.provider.MessageProvider$ReverseDateComparator`

The purpose of the class is to compare `MessageInfoHolder` objects based on their `compareDate` attribute in reverse order.

This class contains the following public method(s):

- `compare(com.fsck.k9.activity.MessageInfoHolder,com.fsck.k9.activity.MessageInfoHolder)` -- The method compares two `MessageInfoHolder` objects based on their `compareDate` attribute in reverse order.

## class `com.fsck.k9.provider.AttachmentTempFileProvider`

`com.fsck.k9.provider.AttachmentTempFileProvider` is used to manage temporary files created for email attachments in the K9 email client on Android devices.

This class contains the following public method(s):

- `deleteOldTemporaryFiles(android.content.Context)` -- This method deletes old temporary files from a specified directory and returns whether all files were successfully deleted.
- `getMimeTypeUri(android.net.Uri,java.lang.String)` -- This method returns a new Uri with the provided mimeType added as a query parameter, only if the contentUri has not yet been typed and is within the authority of the AttachmentTempFileProvider.
- `getType(android.net.Uri)` -- This method returns the MIME type of a given `android.net.Uri`.
- `onTrimMemory(int)` -- The `onTrimMemory(int)` method deletes old temporary files and unregisters a file cleanup receiver when the system is low on memory.
- `createTempUriForContentUri(android.content.Context,android.net.Uri)` -- This method creates a temporary file URI for a content URI, which can be used to access the content of the original URI.
- `delete(android.net.Uri,java.lang.String,java.lang.String[])` -- The method throws an UnsupportedOperationException when attempting to delete a file through the AttachmentTempFileProvider.

## class `com.fsck.k9.provider.MessageProvider`

The class provides an interface to interact with the K-9 Mail content provider, allowing messages to be queried, inserted, updated, and deleted.

This class contains the following public method(s):

- `update(android.net.Uri,android.content.ContentValues,java.lang.String,java.lang.String[])` -- The method updates the values of rows in the message provider with the given selection criteria.
- `getType(android.net.Uri)` -- This method returns the MIME type of the content at the given URI.
- `onCreate()` -- This method initializes the `MessageProvider` by setting up query handlers and registering a content resolver notifier.
- `delete(android.net.Uri,java.lang.String,java.lang.String[])` -- This method deletes a message specified by its URI.
- `insert(android.net.Uri,android.content.ContentValues)` -- The method is used to insert a new message into the K-9 Mail content provider.
- `query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)` -- This method queries the message provider's content provider for message data using the specified parameters.

## interface `com.fsck.k9.provider.MessageProvider$QueryHandler`

The purpose of the interface `com.fsck.k9.provider.MessageProvider$QueryHandler` is to define a contract for classes responsible for handling queries on a specific Uri path, and to provide a method `query` that performs the query and returns the resulting data.

This class contains the following public method(s):

- `getPath()` -- This method returns the path that the implementing class is responsible for.
- `query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)` -- The method performs a query on the specified Uri with the provided projection, selection criteria, and sort order, and returns a cursor containing the resulting data.

## interface `com.fsck.k9.provider.MessageProvider$FieldExtractor`

The purpose of the interface is to provide a way to extract a specific field from an object of a given type.

This class contains the following public method(s):

- `getField(java.lang.Object)` -- This method retrieves a field of type K from an object of type T.

## class `com.fsck.k9.provider.EmailProvider$SpecialColumnsCursor`

The purpose of the class `com.fsck.k9.provider.EmailProvider$SpecialColumnsCursor` is to provide a custom cursor for retrieving columns from the K9 email client's content provider, including special columns that require additional handling.

This class contains the following public method(s):

- `getColumnCount()` -- This method returns the number of columns in the cursor.
- `getDouble(int)` -- The method returns the double value of the column identified by the given index, after mapping it to the appropriate column index.
- `isNull(int)` -- This method checks whether the specified column value is null or not in the given EmailProvider's cursor, including special column values.
- `getColumnName(int)` -- This method returns the name of the column at the specified index.
- `getColumnNames()` -- This method returns a copy of the array of column names associated with the cursor.
- `getLong(int)` -- The method retrieves a long value from the cursor for a specified column index and throws an exception if the column is a special column that can only be retrieved as a string.
- `getShort(int)` -- The method returns a short value for the specified column index, throwing a runtime exception if the column is a special column.
- `getColumnIndex(java.lang.String)` -- This method returns the index of the specified column name in the cursor or in the parent cursor if it cannot be found.
- `getType(int)` -- This method returns the type of data stored in a specific column of the cursor.
- `getInt(int)` -- This method retrieves an integer value from the cursor for the given column index, with an exception thrown if the column is a special column requiring only string retrieval.
- `getFloat(int)` -- This method retrieves the float value of a column at the given index, while throwing an exception if the column is a special column that can only be retrieved as a string.
- `getBlob(int)` -- The method returns the value of the specified column as a byte array, but raises an error if the column is a special column that can only be retrieved as a string.
- `getColumnIndexOrThrow(java.lang.String)` -- This method returns the index of the specified column if it exists, or throws an IllegalArgumentException if the column name is unknown.
- `getString(int)` -- This method returns a string value for the specified column index, either from the super class or from a predefined special column value.

## class `com.fsck.k9.provider.MessageProvider$AccountsQueryHandler`

The class `com.fsck.k9.provider.MessageProvider$AccountsQueryHandler` provides methods to retrieve data for all email accounts configured in the app and returns a cursor containing specified fields in the projection.

This class contains the following public method(s):

- `query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)` -- This method retrieves data for all accounts.
- `getAllAccounts(java.lang.String[])` -- The method retrieves data from all email accounts configured in the app and returns a cursor containing the specified fields in the projection.
- `getPath()` -- The method returns the path "accounts" for the AccountsQueryHandler in the MessageProvider class in Java.

## class `com.fsck.k9.provider.MessageProvider$AccountExtractor`

The purpose of the `com.fsck.k9.provider.MessageProvider$AccountExtractor` class is to extract the account description of a message.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- This method retrieves the account description of a given message.

## class `com.fsck.k9.provider.MessageProvider$SenderAddressExtractor`

The `com.fsck.k9.provider.MessageProvider$SenderAddressExtractor` class extracts the sender email address from a `MessageInfoHolder` object.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- This method returns the sender email address from a `MessageInfoHolder` object.

## class `com.fsck.k9.provider.MessageProvider$UnreadQueryHandler`

The purpose of the `com.fsck.k9.provider.MessageProvider$UnreadQueryHandler` class is to handle unread message queries for a specific email account.

This class contains the following public method(s):

- `getPath()` -- This method returns the path for a specific content URI for querying unread messages in a given account.
- `query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)` -- This method retrieves the unread messages for a specific email account.

## class `com.fsck.k9.provider.MessageProvider$IdExtractor`

The class `com.fsck.k9.provider.MessageProvider$IdExtractor` is used to extract the database ID of a message from the message info holder.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- This method retrieves the database ID of a message using the message info holder.

## class `com.fsck.k9.provider.AttachmentTempFileProvider$AttachmentTempFileProviderCleanupReceiver`

The class is responsible for cleaning up temporary attachment files in the K-9 Mail application and unregistering the related receiver.

This class contains the following public method(s):

- `onReceive(android.content.Context,android.content.Intent)` -- The method cleans up temporary attachment files and unregisters the cleanup receiver if all files were deleted.

## class `com.fsck.k9.provider.MessageProvider$SenderExtractor`

The purpose of the class `com.fsck.k9.provider.MessageProvider$SenderExtractor` is to extract the sender information from a `MessageInfoHolder` object.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- This method returns the sender of a message held in a `MessageInfoHolder`.

## class `com.fsck.k9.provider.MessageProvider$MonitoredCursor`

The purpose of the `com.fsck.k9.provider.MessageProvider$MonitoredCursor` class is to provide a monitored cursor that allows efficient access to email messages stored in a content provider in the K9 email application.

This class contains the following public method(s):

- `unregisterDataSetObserver(android.database.DataSetObserver)` -- The method unregisters a given DataSetObserver from the MonitoredCursor's underlying Cursor.
- `isBeforeFirst()` -- The method checks if the cursor is before the first row of the result set.
- `getInt(int)` -- This method returns the integer value of the specified column by checking whether the cursor is closed or not.
- `moveToPrevious()` -- This method moves the cursor to the previous row and returns a boolean indicating whether the operation succeeded or not.
- `getPosition()` -- This method returns the current position of the cursor.
- `getColumnNames()` -- This method returns an array of column names from a monitored cursor after checking that it is not closed.
- `getNotificationUri()` -- This method returns the notification URI associated with the data set of the cursor.
- `getColumnCount()` -- This method returns the number of columns in the monitored cursor's table.
- `setNotificationUri(android.content.ContentResolver,android.net.Uri)` -- Sets the notification URI for the monitored cursor to be notified of changes to the specified URI.
- `getColumnName(int)` -- This method returns the name of the column specified by the given index in the monitored cursor.
- `isNull(int)` -- The method checks if the given column index contains a null value and returns a boolean value accordingly.
- `getString(int)` -- This method returns the value of the requested column as a String from the underlying cursor after verifying that the cursor is not closed.
- `getColumnIndexOrThrow(java.lang.String)` -- This method returns the index of a given column name or throws an exception if the column does not exist.
- `copyStringToBuffer(int,android.database.CharArrayBuffer)` -- This method copies a string from a specified column in the cursor to a character array buffer.
- `deactivate()` -- The `deactivate()` method closes the cursor and releases all associated resources.
- `requery()` -- The method `requery()` checks if the cursor is closed and executes a requery on the cursor if it is not closed.
- `isLast()` -- The method checks if the cursor is on the last row of the result set.
- `isClosed()` -- The method checks if a monitored cursor is closed or not.
- `getBlob(int)` -- This method retrieves a blob (binary large object) value at the specified column index of a monitored cursor for use in the K9 email application.
- `close()` -- The `close()` method closes the cursor, sets it to null, releases the semaphore and logs it.
- `unregisterContentObserver(android.database.ContentObserver)` -- The method unregisters a content observer from the monitored cursor.
- `registerDataSetObserver(android.database.DataSetObserver)` -- Registers a DataSetObserver to be notified when the data set changes.
- `getLong(int)` -- This method retrieves the value of the requested column as a long data type.
- `getWantsAllOnMoveCalls()` -- This method returns whether the cursor wants to receive all onMove() calls.
- `isAfterLast()` -- This method returns a boolean indicating if the cursor is positioned after the last result.
- `isFirst()` -- This method returns true if the current cursor position is the first row and false otherwise.
- `getShort(int)` -- This method retrieves the value of the specified column as a short data type from a cursor and checks if the cursor is closed.
- `moveToNext()` -- The method moves to the next row in the cursor's result set and returns a boolean indicating if the move was successful or not.
- `respond(android.os.Bundle)` -- The method responds to the given bundle of extras and returns the response provided by the cursor.
- `registerContentObserver(android.database.ContentObserver)` -- The method registers a content observer with the cursor to receive notifications of changes to the underlying data.
- `getFloat(int)` -- The method returns the float value of the specified column index from the cursor of a monitored message provider.
- `getCount()` -- The method returns the number of rows in the cursor after ensuring it is not closed.
- `moveToFirst()` -- The method moves the cursor to the first row and returns a boolean indicating whether the move was successful.
- `fillWindow(int,android.database.CursorWindow)` -- This method fills a provided database cursor window with data from the underlying cursor.
- `getType(int)` -- This method returns the data type of a specified column in a cursor.
- `moveToLast()` -- The method moves the cursor to the last row in the dataset.
- `move(int)` -- The method moves the cursor by a given offset and returns a boolean indicating whether the operation was successful.
- `moveToPosition(int)` -- Moves the cursor to the specified position and returns a boolean indicating whether the move was successful.
- `getExtras()` -- This method returns the extras associated with the cursor.
- `setExtras(android.os.Bundle)` -- This method sets the extras bundle for the monitored cursor.
- `getWindow()` -- This method returns the CursorWindow associated with the underlying Cursor if it is not closed.
- `getColumnIndex(java.lang.String)` -- This method returns the index for a given column name in the cursor for a monitored message provider.
- `getDouble(int)` -- The `getDouble(int)` method retrieves the double value from the specified column of the monitored cursor, after checking if the cursor is closed.
- `onMove(int,int)` -- The method is used to handle a cursor move event.

## class `com.fsck.k9.provider.UnreadWidgetProvider`

The `com.fsck.k9.provider.UnreadWidgetProvider` class is responsible for updating and managing unread email widgets in the K-9 mail client app.

This class contains the following public method(s):

- `updateWidget(android.content.Context,android.appwidget.AppWidgetManager,com.fsck.k9.helper.UnreadWidgetProperties)` -- The `updateWidget` method updates the content of an unread widget with the latest unread message count and sets up a click intent to open the configuration activity.
- `onUpdate(android.content.Context,android.appwidget.AppWidgetManager,int[])` -- This method updates one or more widgets with unread email counts.
- `onDeleted(android.content.Context,int[])` -- The method removes configurations of deleted widgets from the database.
- `updateUnreadCount(android.content.Context)` -- The method updates all of the unread widgets for the specified Context.

## class `com.fsck.k9.provider.MessageProvider$SendDateExtractor`

The purpose of the class `com.fsck.k9.provider.MessageProvider$SendDateExtractor` is to extract and return the date and time when a message was sent.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- The method returns the date and time (in milliseconds) when a message was sent.

## class `com.fsck.k9.provider.MessageProvider$UriExtractor`

The purpose of the `com.fsck.k9.provider.MessageProvider$UriExtractor` class is to provide a method for extracting the URI field from a `MessageInfoHolder` object.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- The method returns the URI field from a MessageInfoHolder object.

## class `com.fsck.k9.provider.EmailProvider$IdTrickeryCursor`

The purpose of this class is to provide a cursor that can map "_id" column names to "id" column names, allowing it to work with database tables that have different column naming conventions.

This class contains the following public method(s):

- `getColumnIndex(java.lang.String)` -- This method returns the index of the given column name, substituting "_id" with "id" if necessary.
- `getColumnIndexOrThrow(java.lang.String)` -- This method is used to retrieve the column index of a specified column name, or throw an exception if the column does not exist.

## class `com.fsck.k9.provider.DecryptedFileProvider$DecryptedFileProviderCleanupReceiver`

The purpose of the class is to delete temporary files created by `DecryptedFileProvider` and unregister the `FileCleanupReceiver` when the device screen is turned off.

This class contains the following public method(s):

- `onReceive(android.content.Context,android.content.Intent)` -- This method is called when the device screen is turned off, and it deletes temporary files created by `DecryptedFileProvider` and unregisters the `FileCleanupReceiver` if all files are successfully deleted.

## class `com.fsck.k9.provider.MessageProvider$UnreadExtractor`

The class is used to extract the unread status of a message in the `MessageInfoHolder` object.

This class contains the following public method(s):

- `getField(com.fsck.k9.activity.MessageInfoHolder)` -- This method returns a `Boolean` value indicating whether the message in the `MessageInfoHolder` object is marked as read or not.


# package `com.fsck.k9.remotecontrol`

The overall purpose of the package `com.fsck.k9.remotecontrol` is to enable remote access and control of K9 Mail app accounts and functionality.

This package contains the following class(es):

## class `com.fsck.k9.remotecontrol.AccountReceiver`

The purpose of the `com.fsck.k9.remotecontrol.AccountReceiver` class is to handle broadcast intents and retrieve a list of accounts in K-9 Mail and pass them to a designated receptor.

This class contains the following public method(s):

- `onReceive(android.content.Context,android.content.Intent)` -- This method handles a broadcast intent to retrieve a list of accounts in K-9 Mail and passes them to a designated receptor.

## interface `com.fsck.k9.remotecontrol.K9AccountReceptor`

The interface provides a method to retrieve the UUIDs and descriptions of all accounts associated with an instance of K9 email client. It is likely used for remote access and control of K9 email client.

This class contains the following public method(s):

- `accounts(java.lang.String[],java.lang.String[])` -- The method returns the account UUIDs and their descriptions.

## class `com.fsck.k9.remotecontrol.K9RemoteControl`

The class `com.fsck.k9.remotecontrol.K9RemoteControl` allows remote control of the K9 Mail app by setting actions and broadcasting intents with specific permissions and fetching accounts from the app.

This class contains the following public method(s):

- `set(android.content.Context,android.content.Intent)` -- The method sets an action for a given Intent and broadcasts it with a specific permission.
- `fetchAccounts(android.content.Context,com.fsck.k9.remotecontrol.K9AccountReceptor)` -- This method fetches accounts from K9 Mail app and returns them to the provided receptor.


