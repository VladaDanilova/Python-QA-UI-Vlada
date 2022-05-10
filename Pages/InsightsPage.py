from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.ContactPage import ContactPage


class InsightsPage(BasePage):
    GET_IN_TOUCH_BUTTON = (By.XPATH, '//*[contains(@href, "/contact")]/span[1]')
    ABOUT_BUTTON = (By.XPATH, '//a[contains(text(), "About")]')
    TYPE_LIST = (By.ID, 'typelist')
    TOPIC_LIST = (By.ID, 'topiclist')
    CLOUD_AND_DEVOPS = (By.XPATH, "//div[@id='topiclist']/div/span[@data-value='cloud-and-devops']")
    ALL_TOPICS = (By.XPATH, "//div[@id='topiclist']/div/span[@data-value='all']")
    ALL_POST_TITLE = (By.XPATH, "//section[contains(@class, \'all digital\')]//a[@class=\'card latest\']")
    CLOUD_AND_DEVOPS_TITLE = (By.XPATH, "//section[contains(@class, \'cloud-and-devops\')]//h2/*[contains(text(),\'Cloud and DevOps\')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

# open about page
    def open_about_page(self):
        self.do_click(self.ABOUT_BUTTON)

# open contact page
    def open_contact_page(self):
        self.do_click(self.GET_IN_TOUCH_BUTTON)
        return ContactPage(self.driver)

# Check that filter is visible and available
    def check_filter(self):
        check_vis_type = self.is_visible(self.TYPE_LIST)
        check_vis_topic = self.is_visible(self.TOPIC_LIST)
        check_avail_type = self.is_available(self.TYPE_LIST)
        check_avail_topic = self.is_available(self.TOPIC_LIST)
        return bool(check_vis_type and check_vis_topic and check_avail_type and check_avail_topic)

# Filter by Cloud and DevOps and Reset filter
    def check_filter_by(self):
        self.click_list(self.TOPIC_LIST, self.CLOUD_AND_DEVOPS)
        cloud_p = self.get_element_text(self.CLOUD_AND_DEVOPS_TITLE)
        self.click_list(self.TOPIC_LIST, self.ALL_TOPICS)
        all_p = self.get_element_text(self.ALL_POST_TITLE)
        return cloud_p is not all_p
