import logging

from constants.gear import GearConstants
from pages.base_page import BasePage


class CartPage(BasePage):
    log = logging.getLogger("[CartPage]")

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = GearConstants()
        self.menu_page = CartPage(self.driver)
        # this class is not yet used
