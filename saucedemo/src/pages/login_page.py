from saucedemo.src.helper import dt
from saucedemo.src.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = dt("username")
    PASSWORD = dt("password")
    SUBMIT = dt("login-button")

    def login(self, username: str, password: str):
        self.find(self.USERNAME).send_keys(username)
        self.find(self.PASSWORD).send_keys(password)
        self.click(self.SUBMIT)
