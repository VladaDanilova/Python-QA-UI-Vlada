import allure

from Pages.InsightsPage import InsightsPage
from Tests.test_base import BaseTest

class Test_Insights(BaseTest):
    # Case 2
    # Open https://blog.griddynamics.com
    # Click ‘filter’ (check it’s visible and available)
    @allure.title("Check filters on the insights page (case 2)")
    def test_filter(self):
        self.insightsPage = InsightsPage(self.driver)
        assert self.insightsPage.check_filter()

    # Case 2
    # Filter by Cloud and DevOps topic
    # Check there is more than 1 article
    # Reset all filters
    # Check the first article in the list is different than in step 4 and check there is more than 1 article.
    @allure.title("Test filters on the insights page (case 2)")
    def test_filter_by(self):
        self.insightsPage = InsightsPage(self.driver)
        assert self.insightsPage.check_filter_by()
