import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

web_driver = None
@pytest.fixture(scope='class')
def browser_automation(request, browser):
    global web_driver
    if browser == 'Chrome':
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = web_driver

    yield
    web_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


# This will give us the functionality to provide the browser name in the command line
# eg: pytest -s -v --browser chrome
@pytest.fixture(scope='class')
def browser(request):
    return request.config.getoption('--browser')
