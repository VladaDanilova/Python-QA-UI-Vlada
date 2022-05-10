from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LeadershipPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.LEADERSHIP_URL)

# click on the needed name
    def click_name(self, name):
        NAME_LABEL = (By.XPATH, '//div[contains(text(), "'+name+'")]')
        self.do_click(NAME_LABEL)

# click on the about to get more information
    def check_about(self, text):
        TEXT = (By.XPATH, '//span[contains(text(), "'+text+'")]')
        return self.is_visible(TEXT)
