from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time

class ThemesPage(BasePage):
    """
    Themes page object
    """
    
    # Locators
    SEARCH_BOX = (By.ID, "wp-filter-search-input")
    THEME_RESULTS = (By.CSS_SELECTOR, ".theme")
    THEME_TITLES = (By.CSS_SELECTOR, ".theme .theme-name")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def search_theme(self, theme_name):
        """Search for a theme"""
        self.send_keys_to_element(self.SEARCH_BOX, theme_name)
        # Small wait for search results
        time.sleep(2)
    
    def are_themes_displayed(self):
        """Check if themes are displayed"""
        try:
            themes = self.driver.find_elements(*self.THEME_RESULTS)
            return len(themes) > 0
        except:
            return False
    
    def get_theme_count(self):
        """Get number of themes displayed"""
        themes = self.driver.find_elements(*self.THEME_RESULTS)
        return len(themes)
    
    def get_theme_titles(self):
        """Get all theme titles"""
        titles = self.driver.find_elements(*self.THEME_TITLES)
        return [title.text for title in titles]