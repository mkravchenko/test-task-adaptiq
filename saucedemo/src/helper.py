from selenium.webdriver.common.by import By

def dt(name: str):
    return (By.CSS_SELECTOR, f'[data-test="{name}"]')