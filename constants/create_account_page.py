class CreateAccountConstants:
    # create an account
    CREATE_ACCOUNT_LINK_XPATH = ".//a[text()='Create an Account']"
    CREATE_ACCOUNT_FIRSTNAME_FIELD_XPATH = ".//input[@id='firstname']"
    CREATE_ACCOUNT_LASTNAME_FIELD_XPATH = ".//input[@id='lastname']"
    CREATE_ACCOUNT_EMAIL_FIELD_XPATH = ".//input[@id='email_address']"
    CREATE_ACCOUNT_PASSWORD_FIELD_XPATH = ".//input[@id='password']"
    CREATE_ACCOUNT_CONFIRM_PASSWORD_FIELD_XPATH = ".//input[@id='password-confirmation']"
    CREATE_ACCOUNT_BUTTON_XPATH = ".//button[@title='Create an Account']"
    CREATE_ACCOUNT_ERROR_PASSWORD_XPATH = ".//div[@id='password-error']"
    CREATE_ACCOUNT_ERROR_TEXT = "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored."
