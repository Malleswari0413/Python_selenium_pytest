import pytest
from pom.login_page import LoginPage
from tests.test_base import BaseTest
from logger_config import setup_logger
logger = setup_logger()

class TestHomePage(BaseTest):
    # Class automatically manage a tearUp and tearDown

    def test_login(self):
        "Test login handles to login to the homepage"
        login_message = self.login_page.select_logo().text
        assert login_message == "Peace of mind is just a few clicks away!",\
            "The login page not opened"
        self.login_page.form_submit_homepage()
        form_title = self.login_page.login_form_title().text
        assert form_title == "We Just Need a Few Details.", \
            "It didnt go the form page for fill up some details"

    def test_login_to_free_trail(self):
        """This function will fill up the free trail details"""
        self.login_page.login_form_title()




