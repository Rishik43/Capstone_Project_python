from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.themes_page import ThemesPage

class HomePage(BasePage):
    """
    Home page object
    """
    
    # Locators
    DOWNLOAD_EXTEND_MENU = (By.XPATH, "//a[contains(text(),'Download & Extend')]")
    THEMES_OPTION = (By.XPATH, "//a[contains(text(),'Themes')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def hover_on_download_extend(self):
        """Hover on Download & Extend menu"""
        self.hover_on_element(self.DOWNLOAD_EXTEND_MENU)
    
    def click_themes(self):
        """Click on Themes option"""
        self.click_element(self.THEMES_OPTION)
        return ThemesPage(self.driver)