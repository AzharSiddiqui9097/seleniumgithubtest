from selenium.webdriver.common.by import By
from SeleniumTestbyRCVacademy.SeleniumTestCases.BaseConfig import BaseConfig
from SeleniumTestbyRCVacademy.SeleniumTestCases.config import ConfigData
import time


class ConfigPage(BaseConfig):
    company_name_locator = (By.XPATH, "//input[@id='CompanyNameTextBox']")
    next_button = (By.XPATH, "//input[@id='NextButton']")
    username_box = (By.XPATH, "//input[@id='LoginNameTextBox']")
    password_box = (By.XPATH, "//input[@id='PasswordTextBox']")
    login_button = (By.CSS_SELECTOR, "#LoginButton")
    remember_me = (By.XPATH, "//input[@id='RememberMeCheckBox']")
    admin = (By.XPATH, "//li[11]//a[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ConfigData.url)

    def perform_login(self, company_key, username, password, title):
        self.put_value(self.company_name_locator, company_key)
        self.click_button(self.next_button)
        self.put_value(self.username_box, username)
        self.put_value(self.password_box, password)
        self.click_button(self.remember_me)
        time.sleep(2)
        self.click_button(self.login_button)
        self.click_button(self.admin)
        return self.get_page_title(title)

