from tests.test_base import BaseTest
from logger_config import setup_logger
logger = setup_logger()

class TestHomePage(BaseTest):

    def test_login_to_free_trail(self):
        """This function will fill up the free trail details"""
        login_message = self.login_page.select_logo().text
        assert login_message == "Peace of mind is just a few clicks away!",\
            "The login page not opened"
        logger.info("login to home page and print the logo msg {}".format(login_message))
        self.login_page.form_submit_homepage()
        form_title = self.login_page.login_form_title().text
        logger.info("Fill the form with required details")
        assert form_title == "We Just Need a Few Details.", \
            "It didnt go the form page for fill up some details"
        logger.info("Fill the required information")
        self.login_page.fill_login_form()




