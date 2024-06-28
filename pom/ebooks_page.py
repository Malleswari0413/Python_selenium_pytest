import params
import time
from selenium.webdriver.common.by import By
from common_locator_methods import CommonLocatorMethods
from pom.common_page import CommonPage
from logger_config import setup_logger


logger = setup_logger()


class EbookPage(CommonLocatorMethods):
    """EbookPage class that is initialized on every page object class."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.common_page = CommonPage(self.driver)
    resource_ebooks = (By.XPATH, "((//a[text()='eBooks'])[1])")
    ebooks = (By.CLASS_NAME, "ebook-page-slider-content")
    ebooks_list = (By.CLASS_NAME, "ebook-details")
    workplace_flexibility = (By.CLASS_NAME, "(//div[@class='ebook-img'])[3]")
    ebook_form_work_flexibility_container = (By.CLASS_NAME, "//div[@class='ebbok-form-slider-content']")

    def goto_ebooks(self):
        self.common_page.move_to_resources()
        self.click_submenu(self.resource_ebooks)
        time.sleep(20)

    def ebook_page(self):
        return self.find_element(self.ebooks)

    def work_flexibility_page(self):
        return self.ebook_form_work_flexibility_container

    def list_all_ebooks(self):
        ebooks_names = []
        elements = self.find_multiple_elements(self.ebooks_list)
        for ele in elements:
            ebooks_names.append(ele.text)
        return ebooks_names

    def select_workplace_flexibility(self):
        middlePos = self.middle_position
        self.driver.execute_script(f"window.scrollTo(0, {middlePos});")
        self.click(self.workplace_flexibility)





