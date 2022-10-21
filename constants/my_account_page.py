class MyAccountConstants:
    MY_ACCOUNT_PAGE_WELCOME_MSG_XPATH = ".//span[@class='logged-in']"
    MY_ACCOUNT_PAGE_WELCOME_MSG_TEXT = "Welcome, {firstname} {lastname}!"
    MY_ACCOUNT_PAGE_SUCCESSFUL_REGISTRATION_MSG_XPATH = ".//div[@data-bind='html: $parent.prepareMessageForHtml(" \
                                                        "message.text)'][contains(.,'Thank you for registering with " \
                                                        "Fake Online Clothing Store.')]"
    MY_ACCOUNT_PAGE_SUCCESSFUL_REGISTRATION_MSG_TEXT = "Thank you for registering with " \
                                                       "Fake Online Clothing Store."
