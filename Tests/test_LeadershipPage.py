import allure

from Config.config import TestData
from Pages.AboutPage import AboutPage
from Pages.InsightsPage import InsightsPage
from Tests.test_base import BaseTest

class Test_Leadership(BaseTest):

    # Case #1:
    #
    # Open https://blog.griddynamics.com
    # Go to About page
    # Find Leonard Livschitz and click on the name
    # Verify that information about Leonard has appeared. The text “director of Grid Dynamics’ board of directors since 2006
    # and the Chief Executive Officer of Grid Dynamics since 2014” is visible.
    @allure.title("Test leadership page (case 1)")
    def test_check_info(self):
        InsightsPage(self.driver).open_about_page()
        self.leadershipPage = AboutPage(self.driver).open_leadership_page()
        self.leadershipPage.click_name(TestData.NAME_LABEL)
        assert self.leadershipPage.check_about(TestData.ABOUT_INFO)
