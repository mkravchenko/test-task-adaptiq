from selenium.webdriver.common.by import By

from saucedemo.src.helper import dt
from saucedemo.src.pages.base_page import BasePage


class Header(BasePage):
    CART_COUNT = dt("shopping-cart-badge")

    def get_cart_count(self) -> int:
        if self.is_element_present(self.CART_COUNT):
            return int(self.driver.find_element(*self.CART_COUNT).text.strip())
        else:
            return 0