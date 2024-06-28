import params
import time
from selenium.webdriver.common.by import By
from common_locator_methods import CommonLocatorMethods
from logger_config import setup_logger

logger = setup_logger()


class CommonPage(CommonLocatorMethods):
    """Common page class that is initialized on every page object class."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    resources = (By.XPATH, "//a[text()='Resources']")

    def move_to_resources(self):
        self.mouse_hover(self.resources)

