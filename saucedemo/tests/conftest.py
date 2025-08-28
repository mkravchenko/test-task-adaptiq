from pytest import fixture
from selenium import webdriver

from saucedemo.src.config import Config
from saucedemo.src.pages.base_page import BasePage
from saucedemo.src.pages.header import Header
from saucedemo.src.pages.inventory_page import InventoryPage
from saucedemo.src.pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment key: dev / stage / prod"
    )


@fixture(scope='session')
def config(request) -> Config:
    env = request.config.getoption('--env')
    return Config().load_config(env)


@fixture(scope='session')
def driver(config):
    driver = webdriver.Chrome()
    return driver


@fixture(scope='session')
def base_page(driver) -> BasePage:
    return BasePage(driver)


@fixture(scope='session')
def login_page(driver) -> LoginPage:
    return LoginPage(driver)


@fixture(scope='session')
def header(driver) -> Header:
    return Header(driver)


@fixture(scope='session')
def inventory_page(driver) -> InventoryPage:
    return InventoryPage(driver)


@fixture(scope='session', autouse=True)
def login(login_page, config):
    login_page.open(config.url)
    login_page.login(config.user_name, config.password)
