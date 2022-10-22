import logging

from constants.cart import CartConstants
from constants.gear import GearConstants
from pages.base_page import BasePage
from pages.menu_page import MenuPage
from pages.utils import wait_until_ok


class GearPage(BasePage):
    log = logging.getLogger("[GearPage]")

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = GearConstants()
        self.constants = CartConstants()
        self.menu_page = MenuPage(self.driver)

    @wait_until_ok
    def select_product(self):
        """select default available product"""
        self.click(xpath=self.constants.GEAR_Affirm_Water_Bottle_XPATH)
        self.log.info("selecting default product")
        # this test cannot be re-used again. it works only for this specific product.
        # todo: rewrite this test so it can be used with any product using class Product and maybe mapping

    @wait_until_ok
    def add_product_to_cart(self):
        """add selected product to cart"""
        self.click(xpath=self.constants.ADD_TO_CART_BUTTON_XPATH)
        self.log.info("adding selected product to cart")

    @wait_until_ok
    def verify_added_to_cart_green_banner(self):
        """Successfully added to cart green banner message verification"""
        assert self.get_element_text(
            xpath=self.constants.ADDED_TO_CART_GREEN_BANNER_XPATH) == self.constants.ADDED_TO_CART_GREEN_BANNER_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.ADDED_TO_CART_GREEN_BANNER_XPATH)}"
        self.log.info("Successfully added to cart green banner message verification")

    @wait_until_ok
    def navigate_to_cart_step1(self):
        """navigating to cart click 1"""
        self.click(self.constants.CART_ICON_XPATH)
        self.log.info("navigating to cart click 1")

    @wait_until_ok
    def navigate_to_cart_step2(self):
        """navigating to cart click 2"""
        self.click(self.constants.CART_VIEW_AND_EDIT_LINK_XPATH)
        self.log.info("navigating to cart click 2")

    @wait_until_ok
    def verify_cart_with_product(self):
        """Verification that given product is inside the Cart"""
        assert self.get_element_text(
            xpath=self.constants.CART_PRODUCT_VIEW_XPATH) == self.constants.CART_PRODUCT_VIEW_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.CART_PRODUCT_VIEW_XPATH)}"
        self.log.info("Verification that given product is inside the Cart")

    @wait_until_ok
    def select_unavailable_product(self):
        """select unavailable product"""
        self.click(xpath=self.constants.GEAR_fusion_backpack_XPATH)
        self.log.info("selecting unavailable product")
        # this test cannot be re-used again. it works only for this specific product.
        # todo: rewrite this test so it can be used with any product using class Product and maybe mapping

    @wait_until_ok
    def verify_red_banner_product_unavailable(self):
        """Successfully added to cart green banner message verification"""
        assert self.get_element_text(
            xpath=self.constants.PRODUCT_UNAVAILABLE_RED_BANNER_XPATH) == self.constants.PRODUCT_UNAVAILABLE_RED_BANNER_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.PRODUCT_UNAVAILABLE_RED_BANNER_XPATH)}"
        self.log.info("Successfully added to cart green banner message verification")
