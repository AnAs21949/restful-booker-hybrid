
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).click()
    
    def type(self, locator, text: str):
        return self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
    
    def text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def wait_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_url(self, partial_url):
        self.wait.until(EC.url_contains(partial_url))
    
    def scroll_and_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        
