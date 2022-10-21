import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.sign_in_page import SignInPage


class TestSignInPage:
    log = logging.getLogger("[SignInPage]")

    @pytest.fixture(scope="function")
    def sign_in_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        yield SignInPage(driver)
        # Post-conditions
        driver.close()

    def test_sign_in_error(self, sign_in_page, random_user):
        """
        - Steps:
            - open start page, click "Sign In" link (top right corner)
            - Fill Email & Password fields
            - Click "Sign In" blue button
            - Verify that error message appears
        """
        # Login as a user
        sign_in_page.sign_in(random_user)
        self.log.info("Logged in as a non-existing user")

        # Verify error
        sign_in_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_sign_in_successful(self, sign_in_page, existing_user):
        """
        - Steps:
            - open start page, click "Sign In" link (top right corner)
            - Fill Email & Password fields
            - Click "Sign In" blue button
            - Verify that User has sign in successfully
        """
        # Login as a user
        hello_user_page = sign_in_page.sign_in(existing_user)
        self.log.info("Logging in as an existing user")
        self.log.info("Logged in as User with email %s", existing_user.email)
        self.log.info("Logged in as User with password %s", existing_user.password)

        # Verify login
        hello_user_page.verify_successful_sign_in(existing_user.firstname, existing_user.lastname)
        self.log.info("Verified successful sign in")
