import pytest as pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.create_account_page import CreateAccountPage
from pages.utils import User


@pytest.fixture(scope="function")
def start_page():
    # Pre-conditions
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(BASE_URL)
    driver.implicitly_wait(6)
    # Steps
    yield CreateAccountPage(driver)
    # Post-conditions
    driver.close()


@pytest.fixture()
def random_user():
    user = User()
    user.fill_data()
    return user


@pytest.fixture()
def existing_user():
    user = User()
    user.fill_data2()
    return user


@pytest.fixture()
def random_user1():
    user = User()
    user.fill_data1()
    return user
