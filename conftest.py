import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from api_client import register_new_user_and_return_login_password, delete_user
from pages.recovery_page import RecoveryPage
from urls import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    elif request.param == "firefox":
        browser = webdriver.Firefox()

    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def create_user():
    user_data = register_new_user_and_return_login_password()
    yield user_data
    delete_user(user_data["email"], user_data["password"])


@pytest.fixture
def authorized_driver(driver, create_user):
    auth_page = RecoveryPage(driver)
    auth_page.open(Urls.LOGIN_PAGE)
    auth_page.enter_email(create_user["email"])
    auth_page.enter_password(create_user["password"])
    auth_page.click_login()

    auth_page.wait.until(EC.url_to_be(Urls.BASE_URL))

    yield driver

