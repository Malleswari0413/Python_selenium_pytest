import params

from selenium.webdriver.common.by import By
from pom.common_page import CommonPageElement


class LoginPage(CommonPageElement):
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
    recaptcha_checkbox = (By.CSS_SELECTOR, ".recaptcha-checkbox-border")
    submit_login_form = (By.ID, "Form_getForm_action_submitForm")

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
        self.send_keys(self.fill_user_name, params.full_name)
        self.click(self.fill_contact)
        self.send_keys(self.fill_contact, params.contact)
        self.click(self.fill_country_code)
        self.select_dropdown_element(params.country_code)
        self.click(self.recaptcha_checkbox)
        self.click(self.submit_login_form)



