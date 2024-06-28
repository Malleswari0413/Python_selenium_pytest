from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class CommonLocatorMethods:
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.viewport_height = driver.execute_script("return window.innerHeight;")
        self.middle_position = self.viewport_height / 2

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_multiple_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def get_count_elements(self, locator):
        return len(self.find_multiple_elements(locator))

    def click(self, by_locator: object) -> object:
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_title(self):
        return self.driver.title

    def switch_to_iframe(self, locator):
        iframe = self.find_element(locator)
        self.driver.switch_to.frame(iframe)

    def click_submenu(self, locator):
        element_to_hover_over = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).click().perform()

    def mouse_hover(self, locator):
        element_to_hover_over = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()

    def select_dropdown_element(self, locator, value=None, index=None, visible_text=None):
        select = Select(self.find_element(locator))
        if value:
            select.select_by_value(value)
        if index:
            select.select_by_index(index)
        if visible_text:
            select.select_by_visible_text(visible_text)

