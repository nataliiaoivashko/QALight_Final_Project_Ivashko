from constants.my_account_page import MyAccountConstants
from pages.base_page import BasePage
from pages.menu_page import MenuPage
from pages.utils import wait_until_ok


class MyAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MyAccountConstants()
        self.menu_page = MenuPage(self.driver)

    @wait_until_ok(timeout=5, period=0.5)
    def verify_successful_registration(self, firstname, lastname):
        """Verify successful registration using 1. welcome and 2. confirmation banner message"""
        firstname = firstname
        lastname = lastname
        assert self.get_element_text(self.constants.MY_ACCOUNT_PAGE_WELCOME_MSG_XPATH) == \
               self.constants.MY_ACCOUNT_PAGE_WELCOME_MSG_TEXT.format(firstname=firstname, lastname=lastname), \
            f"Actual message: {self.get_element_text(self.constants.MY_ACCOUNT_PAGE_WELCOME_MSG_XPATH)}"
        assert self.get_element_text(self.constants.MY_ACCOUNT_PAGE_SUCCESSFUL_REGISTRATION_MSG_XPATH) == \
               self.constants.MY_ACCOUNT_PAGE_SUCCESSFUL_REGISTRATION_MSG_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.MY_ACCOUNT_PAGE_SUCCESSFUL_REGISTRATION_MSG_XPATH)}"

    @wait_until_ok(timeout=5, period=0.5)
    def verify_successful_sign_in(self, firstname, lastname):
        """Verify successful registration using welcome message"""
        firstname = firstname
        lastname = lastname
        assert self.get_element_text(self.constants.MY_ACCOUNT_PAGE_WELCOME_MSG_XPATH) == \
               self.constants.MY_ACCOUNT_PAGE_WELCOME_MSG_TEXT.format(firstname=firstname, lastname=lastname), \
            f"Actual message: {self.get_element_text(self.constants.MY_ACCOUNT_PAGE_WELCOME_MSG_XPATH)}"
