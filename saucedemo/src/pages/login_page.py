from saucedemo.src.helper import dt
from saucedemo.src.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = dt("username")
    PASSWORD = dt("password")
    SUBMIT = dt("login-button")

    def login(self, username: str, password: str):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()
