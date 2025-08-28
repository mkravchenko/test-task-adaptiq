from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)
        return self

    def find(self, locator) -> WebElement:
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def is_element_present(self, locator, timeout: int = 5):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click(self, locator):
        self.find(locator).click()

    def close(self):
        self.driver.quit()
