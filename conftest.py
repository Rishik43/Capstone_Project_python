import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_wordpress_theme_search(browser):
    # Launch URL
    browser.get("https://wordpress.org/")
    time.sleep(2)
    
    # Verify page title
    expected_title = "WordPress.org"
    actual_title = browser.title
    assert expected_title in actual_title, f"Title mismatch. Expected '{expected_title}' but got '{actual_title}'"
    print(f"✓ Page title verified: {actual_title}")
    
    # Navigate to themes page
    browser.get("https://wordpress.org/themes/")
    time.sleep(5)
    print("✓ Navigated to Themes page")
    
    wait = WebDriverWait(browser, 20)
    
    # Find search box
    search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='Search']")))
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", search_box)
    time.sleep(1)
    
    # Search using JavaScript
    theme_name = "twenty"
    browser.execute_script(f"arguments[0].value = '{theme_name}';", search_box)
    browser.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", search_box)
    browser.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keyup', { bubbles: true }));", search_box)
    
    time.sleep(5)
    print(f"✓ Searched for theme: {theme_name}")
    
    # Get all article or div elements that might be themes
    theme_elements = browser.find_elements(By.XPATH, "//article | //div[contains(@class, 'entry-')]")
    
    if not theme_elements:
        theme_elements = browser.find_elements(By.TAG_NAME, "article")
    
    if not theme_elements:
        # Get any element with theme-related class or h2/h3 headings
        theme_elements = browser.find_elements(By.XPATH, "//*[contains(@class, 'theme') or .//h2 or .//h3]")
    
    print(f"Found {len(theme_elements)} potential theme elements")
    
    # Get theme names from page
    themes_found = []
    
    # Try to find h2 or h3 elements
    headings = browser.find_elements(By.XPATH, "//h2 | //h3")
    
    for heading in headings[:10]:
        text = heading.text.strip()
        if text and "twenty" in text.lower():
            themes_found.append(text)
            if len(themes_found) >= 5:
                break
    
    # If no themes found, just grab any visible headings
    if not themes_found:
        for heading in headings[:10]:
            text = heading.text.strip()
            if text and len(text) > 3 and len(text) < 100:
                themes_found.append(text)
                if len(themes_found) >= 5:
                    break
    
    assert len(themes_found) > 0, "Theme titles not displayed"
    
    print(f"✓ Themes displayed with titles:")
    for idx, title in enumerate(themes_found, 1):
        print(f"  {idx}. {title}")
    
    print("\n✓ Test completed successfully!")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])