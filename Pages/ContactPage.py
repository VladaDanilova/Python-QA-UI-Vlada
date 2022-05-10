from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage

class ContactPage(BasePage):
    FIRST_NAME = (By.XPATH, '//input[contains(@formcontrolname, "firstName")]')
    LAST_NAME = (By.XPATH, '//input[contains(@formcontrolname, "lastName")]')
    EMAIL = (By.XPATH, '//input[contains(@type, "email")]')
    HOW = (By.XPATH, '//gd-select[contains(@formcontrolname, "source")]')
    ONLINE_ADS = (By.XPATH, '//*[@id="ui-select-popup-87"]/gd-select-option[4]')
    TERMS_PRIVACY = (By.XPATH, '//gd-checkbox[contains(@formcontrolname, "policy")]/label/input')
    ALLOW_CONTACT = (By.XPATH, '//gd-checkbox[contains(@formcontrolname, "allowContact")]/label/input')
    SUBMIT_BTN = (By.XPATH, '//*[@id="contact"]/form/button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.CONTACT_URL)

# Fill form with first name, last name, email, how did you hear about us and click on Terms and allow contact
# Check that submit button is disabled
    def fill_not_full_contact_form(self):
        self.do_send_keys(self.FIRST_NAME, TestData.FIRST_NAME)
        self.do_send_keys(self.LAST_NAME, TestData.LAST_NAME)
        self.do_send_keys(self.EMAIL, TestData.EMAIL)
        self.do_click(self.HOW)
        self.do_click(self.ONLINE_ADS)
        self.click_checkbox(self.TERMS_PRIVACY)
        self.click_checkbox(self.ALLOW_CONTACT)
        return self.is_disabled(self.SUBMIT_BTN)
