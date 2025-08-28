from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from saucedemo.src.helper import dt
from saucedemo.src.pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_ITEMS_LIST = dt("inventory-item")
    ADD_TO_CART_BUTTON = dt("add-to-cart-sauce-labs-backpack")
    REMOVE_FROM_CART_BUTTON = dt("remove-sauce-labs-backpack")

    def get_inventory_items(self) -> list[WebElement]:
        return self.driver.find_elements(*self.INVENTORY_ITEMS_LIST)

    def add_item_to_cart_by_index(self, index: int) -> None:
        items = self.get_inventory_items()
        if index >= len(items):
            raise IndexError(f'Found {len(items)} inventory items. Index {index} is out of range.`')

        try:
            items[index].find_element(*self.ADD_TO_CART_BUTTON).click()
        except NoSuchElementException:
            raise IndexError(f'Inventory item by {index=} already added to cart or button does not exist.')