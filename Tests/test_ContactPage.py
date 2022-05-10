import allure

from Pages.InsightsPage import InsightsPage
from Tests.test_base import BaseTest

class Test_Contact(BaseTest):

    # Case 3
    #
    # Open https://blog.griddynamics.com
    # Click on Get In Touch button
    # Ensure page Contact Us opened
    # Fill in the form not fully
    # Click on checkbox “I have read and accepted the Terms & Conditions and Privacy Policy”
    # Click on checkbox “I allow Grid Dynamics to contact me”
    # Ensure Contact button is inactive

    @allure.title("Test contact form (case 3)")
    def test_submit_btn(self):
        self.contactPage = InsightsPage(self.driver).open_contact_page()
        assert self.contactPage.fill_not_full_contact_form()
