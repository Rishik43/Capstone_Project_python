import pytest
from pages.home_page import HomePage

class TestWordPress:
    """
    WordPress automation test cases
    """
    
    BASE_URL = "https://wordpress.org/"
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup for each test"""
        self.driver = driver
        self.home_page = HomePage(driver)
    
    def test_verify_title(self):
        """
        Test 1: Launch URL and verify title
        """
        self.home_page.open_url(self.BASE_URL)
        
        title = self.home_page.get_title()
        print(f"\nPage Title: {title}")
        
        assert "WordPress" in title, f"Expected 'WordPress' in title, got {title}"
    
    def test_navigate_to_themes(self):
        """
        Test 2: Navigate to Themes page
        """
        self.home_page.open_url(self.BASE_URL)
        
        # Hover on Download & Extend
        self.home_page.hover_on_download_extend()
        
        # Click on Themes
        themes_page = self.home_page.click_themes()
        
        # Verify we're on themes page
        current_url = self.driver.current_url
        print(f"\nCurrent URL: {current_url}")
        
        assert "themes" in current_url.lower(), "Not on themes page"
    
    def test_search_theme(self):
        """
        Test 3: Search for a theme and verify results
        """
        self.home_page.open_url(self.BASE_URL)
        
        # Navigate to themes
        self.home_page.hover_on_download_extend()
        themes_page = self.home_page.click_themes()
        
        # Search for a theme
        search_term = "twentytwentyfour"
        themes_page.search_theme(search_term)
        
        # Verify themes are displayed
        themes_displayed = themes_page.are_themes_displayed()
        theme_count = themes_page.get_theme_count()
        
        print(f"\nThemes found: {theme_count}")
        
        assert themes_displayed, "No themes displayed after search"
        assert theme_count > 0, "Expected at least one theme"
        
        # Get theme titles
        titles = themes_page.get_theme_titles()
        print(f"Theme titles: {titles}")
    
    def test_complete_flow(self):
        """
        Test 4: Complete end-to-end flow
        """
        # Step 1: Launch and verify title
        self.home_page.open_url(self.BASE_URL)
        title = self.home_page.get_title()
        assert "WordPress" in title
        
        # Step 2: Navigate to themes
        self.home_page.hover_on_download_extend()
        themes_page = self.home_page.click_themes()
        
        # Step 3: Search and verify
        themes_page.search_theme("classic")
        assert themes_page.are_themes_displayed()
        
        print("\nComplete flow test passed!")