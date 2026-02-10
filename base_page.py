from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:
    """
    Base page class with common methods
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def open_url(self, url):
        """Navigate to URL"""
        self.driver.get(url)
    
    def get_title(self):
        """Get page title"""
        return self.driver.title
    
    def find_element(self, locator):
        """Find element with wait"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        """Click element with wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def hover_on_element(self, locator):
        """Hover over element"""
        element = self.find_element(locator)
        self.actions.move_to_element(element).perform()
        time.sleep(1)
    
    def send_keys_to_element(self, locator, text):
        """Send keys to element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def is_element_displayed(self, locator):
        """Check if element is displayed"""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
    
    def get_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        return element.text