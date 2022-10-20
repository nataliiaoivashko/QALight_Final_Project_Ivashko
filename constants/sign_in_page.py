class SignInConstants:
    # sign in
    SIGN_IN_LINK_XPATH = ".//a[contains(.,'Sign In')]"
    SIGN_IN_EMAIL_FIELD_XPATH = ".//input[@id='email']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@name='login[password]']"
    SIGN_IN_BUTTON_XPATH = ".//span[contains(.,'Sign In')]"
    SIGN_IN_ERROR_XPATH = ".//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.')]"
    SIGN_IN_ERROR_TEXT = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
