from constants.create_account_page import CreateAccountConstants
from pages.base_page import BasePage
from pages.utils import log_decorator


class CreateAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreateAccountConstants()

    @log_decorator
    def fill_registration_fields(self, user):
        """click on create an account button and fill necessary fields"""
        """clicking on Create an Account button"""
        self.click(xpath=self.constants.CREATE_ACCOUNT_LINK_XPATH)
        """filling firstname, lastname, email and password"""
        self.fill_field(xpath=self.constants.CREATE_ACCOUNT_FIRSTNAME_FIELD_XPATH, value=user.firstname)
        self.fill_field(xpath=self.constants.CREATE_ACCOUNT_LASTNAME_FIELD_XPATH, value=user.lastname)
        self.fill_field(xpath=self.constants.CREATE_ACCOUNT_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.CREATE_ACCOUNT_PASSWORD_FIELD_XPATH, value=user.password)
        self.fill_field(xpath=self.constants.CREATE_ACCOUNT_CONFIRM_PASSWORD_FIELD_XPATH, value=user.confirm_password)

    @log_decorator
    def create_account_button_click_and_verify(self):
        """clicking the main registration button after filling the fields"""
        self.click(xpath=self.constants.CREATE_ACCOUNT_BUTTON_XPATH)
        assert not self.is_exists(xpath=self.constants.CREATE_ACCOUNT_BUTTON_XPATH)

    @log_decorator
    def register_and_verify(self, user):
        """register successfully and navigate to next page"""
        # clicking on Create an Account button
        self.click(xpath=self.constants.CREATE_ACCOUNT_LINK_XPATH)
        # filling firstname, lastname, email and password
        self.fill_field(xpath=self.constants.CREATE_ACCOUNT_FIRSTNAME_FIELD_XPATH, value=user.firstname)
        self.fill_field(xpath=self.constants.CREATE_ACCOUNT_LASTNAME_FIELD_XPATH, value=user.lastname)
        self.fill_field(xpath=self.constants.CREATE_ACCOUNT_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.CREATE_ACCOUNT_PASSWORD_FIELD_XPATH, value=user.password)
        self.fill_field(xpath=self.constants.CREATE_ACCOUNT_CONFIRM_PASSWORD_FIELD_XPATH, value=user.confirm_password)
        # click button
        self.create_account_button_click_and_verify()
        # return new page
        from pages.my_account_page import MyAccountPage
        return MyAccountPage(self.driver)

    @log_decorator
    def verify_register_password_error(self):
        """Verifying that error message for incorrect password appears"""
        assert self.get_element_text(
            self.constants.CREATE_ACCOUNT_ERROR_PASSWORD_XPATH) == self.constants.CREATE_ACCOUNT_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.CREATE_ACCOUNT_ERROR_PASSWORD_XPATH)}"
