import pytest
from tests.test_base import BaseTest
from logger_config import setup_logger
logger = setup_logger()

class TestEbookPage(BaseTest):
    @pytest.mark.ebook
    def test_ebooks(self):
        """This function will check the list of ebooks"""
        self.ebooks_page.goto_ebooks()
        assert self.ebooks_page.ebook_page().text == "eBooks", "Ebook page not loaded"
        ebooks_list = self.ebooks_page.list_all_ebooks()
        logger.info("list of books {}".format(ebooks_list))

    @pytest.mark.ebook
    def test_workplace_flexibility(self):
        """It will give the content of workplace flexibility"""
        self.ebooks_page.goto_ebooks()
        self.ebooks_page.select_workplace_flexibility()
        assert self.ebooks_page.work_flexibility_page()=="Workplace Flexibility: The Future of Work is Flexible", \
            "workplace flexibily not opened"


