import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.sign_in_page import SignInPage


class TestMenuPage:
    log = logging.getLogger("[TestMenuPage]")

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

    @pytest.fixture()
    def hello_page(self, sign_in_page, existing_user):
        """Log in as the existing user and return the page"""
        return sign_in_page.sign_in(existing_user)

    def test_gear_available_product_select(self, hello_page):
        """
        - Preconditions:
            - Existing User is logged in
        - Steps:
            - select "Gear" from the menu
            - select a product
            - add it to Cart
            - go to Cart
        - Verify:
            - Cart contains selected product
        """
        # Login as a user and navigate to Gear in Menu
        gear_page = hello_page.menu_page.navigate_to_gear_page()
        # select a product
        gear_page.select_product()
        self.log.info("selecting default product")
        # add selected product to Cart
        gear_page.add_product_to_cart()
        self.log.info("adding selected product to cart")
        # verify confirmation message
        gear_page.verify_added_to_cart_green_banner()
        self.log.info("Successfully added to cart green banner message verification")
        # going to cart clicking the icon:
        gear_page.navigate_to_cart_step1()
        self.log.info("navigating to cart step 1")
        # going to cart clicking the link "view and edit":
        gear_page.navigate_to_cart_step2()
        self.log.info("navigating to cart step 2")
        # verify that Cart contains selected product
        gear_page.verify_cart_with_product()
        self.log.info("Verification that given product is inside the Cart")

    def test_gear_unavailable_product_select(self, hello_page):
        """
        - Preconditions:
            - Existing User is logged in
        - Steps:
            - select "Gear" from the menu
            - select unavailable product
            - add it to Cart
        - Verify:
            - Red banner message that product is unavailable
        """
        # Login as a user and navigate to Gear in Menu
        gear_page = hello_page.menu_page.navigate_to_gear_page()
        self.log.info("selecting Gear from Menu Bar")
        # select a product
        gear_page.select_unavailable_product()
        self.log.info("selecting unavailable product")
        # add selected product to Cart
        gear_page.add_product_to_cart()
        self.log.info("adding selected product to cart")
        # verify confirmation message
        gear_page.verify_red_banner_product_unavailable()
        self.log.info("Product is unavailable red banner message verification")
