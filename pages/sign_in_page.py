from constants.sign_in_page import SignInConstants
from pages.base_page import BasePage
from pages.utils import log_decorator


class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = SignInConstants()

    @log_decorator
    def sign_in(self, user):
        """Sign in as the random user and navigate to welcome page"""
        # clicking on Sign In Link on top right
        self.click(xpath=self.constants.SIGN_IN_LINK_XPATH)
        # Fill login info: email and password
        self.fill_field(xpath=self.constants.SIGN_IN_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=user.password)
        # Click button
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)
        # return new page
        from pages.my_account_page import MyAccountPage
        return MyAccountPage(self.driver)

    @log_decorator
    def verify_sign_in_error(self):
        """Verify invalid Sign In error"""
        assert self.get_element_text(
            self.constants.SIGN_IN_ERROR_XPATH) == self.constants.SIGN_IN_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_IN_ERROR_XPATH)}"
