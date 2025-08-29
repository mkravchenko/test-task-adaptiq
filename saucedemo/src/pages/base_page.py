from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from saucedemo.src.constants import Timeout


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(Timeout.implicit)

    def open(self, url: str):
        self.driver.get(url)
        return self

    def is_element_present(self, locator, timeout: int = 5):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def close(self):
        self.driver.quit()
