import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.create_account_page import CreateAccountPage


class TestCreateAccountPage:
    log = logging.getLogger("[TestCreateAccountPage]")

    @pytest.fixture(scope="function")
    def create_account_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        yield CreateAccountPage(driver)
        # Post-conditions
        driver.close()

    def test_registration_error(self, create_account_page, random_user1):
        """
        Error during registration
        Steps:
        - open main page, & click on "Create an Account" (top right)
        - fill fields: first name, last name, email, password (incorrectly)
        Verify:
        - error message for incorrect password appears
        """

        # Fill registration fields for a user
        create_account_page.fill_registration_fields(random_user1)
        self.log.info("Registering as User first name %s", random_user1.firstname)
        self.log.info("Registering as User last name %s", random_user1.lastname)
        self.log.info("Registering email %s", random_user1.email)
        # Verify error message
        create_account_page.verify_register_password_error()
        self.log.info("Password verification. Entered password %s", random_user1.password)

    def test_registration_successful(self, create_account_page, random_user):
        """
        Normal registration
        Steps:
        - open main page, & click on "Create an Account" (top right)
        - fill fields: first name, last name, email, password, & confirm password
        - click on "Create an Account"
        Verify:
        - welcome message with expected Username appears
        """
        # registration process for a user
        welcome_page = create_account_page.register_and_verify(random_user)
        self.log.info("Registering as User first name %s", random_user.firstname)
        self.log.info("Registering as User last name %s", random_user.lastname)
        self.log.info("Registering email %s", random_user.email)
        self.log.info("Entering registration password %s", random_user.password)
        self.log.info("Entering confirmation password %s", random_user.confirm_password)

        # verify welcome message
        welcome_page.verify_successful_registration(random_user.firstname, random_user.lastname)
        self.log.info("Welcome message was verified")
