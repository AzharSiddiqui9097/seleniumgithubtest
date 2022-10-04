from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseConfig:
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self, locator):
        WebDriverWait(self.driver, 10).until(EC.title_is(locator))
        return self.driver.title

    def put_value(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(value)

    def click_button(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
