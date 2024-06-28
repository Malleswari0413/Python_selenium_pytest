"""We can define the fixture functions in this file to make them accessible across multiple test """
import params
import pytest

from selenium import webdriver
import custom_requests_adapter
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


from pom.login_page import LoginPage
from pom.ebooks_page import EbookPage

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=params.browser)

@pytest.fixture
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser

@pytest.fixture
def get_driver(request, get_browser):
    global driver
    if get_browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # capabilities = DesiredCapabilities.CHROME.copy()
        # capabilities['acceptInsecureCerts'] = True
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_driver_path = "C:\\Users\\ChagalakonduMalleswa\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"
        driver = webdriver.Chrome(options=chrome_options)

        # driver = webdriver.Chrome(ex,options=chrome_options, desired_capabilities=capabilities)
    elif get_browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    elif get_browser == "headless":
        chrome_options = Options()
        #chrome_options.add_argument("--disable-extensions")
        #chrome_options.add_argument("--disable-gpu")
        #chrome_options.add_argument("--no-sandbox") # linux only
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    else:
        print("Driver not supported")
    driver.implicitly_wait(10)
    # ## Add in here each page from the POM in order to initialize the driver for each one.
    request.cls.login_page = LoginPage(driver)
    request.cls.ebooks_page = EbookPage(driver)
    # driver.get('https://googlechromelabs.github.io/chrome-for-testing/latest-patch-versions-per-build.json')
    driver.get(params.url)
    driver.quit()