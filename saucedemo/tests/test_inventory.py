"""Tests for inventory page"""

from pytest import fixture
from selenium.webdriver.remote.webelement import WebElement


@fixture(scope="module")
def inventory_items(inventory_page) -> list[WebElement]:
    return inventory_page.get_inventory_items()


def test_verify_inventory_items_availability(inventory_items):
    assert len(inventory_items) == 6, f"Inventory items should have 6 items"
    assert all(item.is_displayed() for item in inventory_items), "Inventory items should be displayed"


def test_verify_possibility_to_add_the_item(inventory_page, header):
    exp_number_of_cart_items = header.get_cart_count() + 1
    inventory_page.add_item_to_cart_by_index(0)
    assert header.get_cart_count() == exp_number_of_cart_items, "Inventory items should have 1 item added"
