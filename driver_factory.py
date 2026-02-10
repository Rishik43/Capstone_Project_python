from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class DriverFactory:
    """
    Factory class to create driver instances
    """
    
    @staticmethod
    def get_driver(browser="chrome"):
        """
        Get driver instance based on browser type
        """
        if browser.lower() == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.implicitly_wait(10)
            return driver
        else:
            raise ValueError(f"Browser {browser} not supported")