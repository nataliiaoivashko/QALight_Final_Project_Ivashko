from constants.menu import MenuLinksConstants
from pages.base_page import BasePage
from pages.utils import log_decorator


class MenuPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MenuLinksConstants()

    @log_decorator
    def navigate_to_gear_page(self):
        """Click on Gear"""
        self.click(self.constants.GEAR_LINK_XPATH)
        from pages.gear_page import GearPage
        return GearPage(self.driver)
