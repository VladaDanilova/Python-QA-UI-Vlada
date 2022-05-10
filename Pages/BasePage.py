from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

# method for selecting from the list
    def click_list(self, by_locator1, by_locator2):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator1))
        self.driver.execute_script("arguments[0].click();", element)
        element2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator2))
        self.driver.execute_script("arguments[0].click();", element2)

# method for clicking on the checkbox
    def click_checkbox(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].click();", element)

# method for clicking, for instance, on the link
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

# method for sending keys (make an input)
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

# method for getting text of the element
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

# method for checking if element is visible
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

# method for checking if element is available
    def is_available(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

# method for checking if element is disabled
    def is_disabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return not element.is_enabled()
