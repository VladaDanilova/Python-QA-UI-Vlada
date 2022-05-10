from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.LeadershipPage import LeadershipPage


class AboutPage(BasePage):
    LEADERSHIP_BUTTON = (By.XPATH, '//a[contains(text(), "Leadership")]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.ABOUT_URL)

# open leadershop page
    def open_leadership_page(self):
        self.do_click(self.LEADERSHIP_BUTTON)
        return LeadershipPage(self.driver)
