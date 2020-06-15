from selenium import webdriver
import pytest
from helper import CHROME_DRIVER_PATH


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    yield driver
    driver.quit()
