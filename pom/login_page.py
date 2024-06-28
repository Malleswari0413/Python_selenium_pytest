import params
import time
from selenium.webdriver.common.by import By
from common_locator_methods import CommonLocatorMethods
from logger_config import setup_logger

logger = setup_logger()


class LoginPage(CommonLocatorMethods):
    """Login page class that is initialized on every page object class."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    logo = (By.XPATH, "//h1[contains(.,'Peace of mind is just a few clicks away!')]")
    submit_email_homepage = (By.ID, "Form_submitForm_EmailHomePage")
    submit_action = (By.ID, "Form_submitForm_action_request")
    form_title = (By.CSS_SELECTOR, ".form-title")
    fill_user_name = (By.ID, "Form_getForm_subdomain")
    fill_full_name = (By.ID, "Form_getForm_Name")
    fill_contact = (By.ID, "Form_getForm_Contact")
    fill_country_code = (By.ID, "Form_getForm_Country")
    recaptcha_checkbox = (By.XPATH, "//span[@id='recaptcha-anchor']/div")
    submit_login_form = (By.ID, "Form_getForm_action_submitForm")
    repatcha_iframe = (By.XPATH, "//iframe[@title='reCAPTCHA']")

    def select_logo(self):
        return self.find_element(self.logo)

    def form_submit_homepage(self):
        self.click(self.submit_email_homepage)
        self.send_keys(self.submit_email_homepage, params.email)
        self.click(self.submit_action)

    def login_form_title(self):
        return self.find_element(self.form_title)

    def fill_login_form(self):
        self.click(self.fill_user_name)
        self.send_keys(self.fill_user_name, params.username)

        self.click(self.fill_full_name)
        self.send_keys(self.fill_full_name, params.full_name)
        self.click(self.fill_contact)
        self.send_keys(self.fill_contact, params.contact)
        self.select_dropdown_element(self.fill_country_code, value=params.country_code)
        # Switch to the iframe
        self.switch_to_iframe(self.repatcha_iframe)
        middlePos = self.middle_position
        self.driver.execute_script(f"window.scrollTo(0, {middlePos+1050});")
        self.click(self.recaptcha_checkbox)
        self.driver.switch_to.default_content()
        # wait to handle captcha verification
        time.sleep(60)
        self.click(self.submit_login_form)




