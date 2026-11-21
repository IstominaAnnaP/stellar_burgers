import pytest
from core.api.user_methods import UserMethods
from core.utils import generators
from selenium import webdriver

@pytest.fixture
def generate_user_with_delete():
    body = generators.generate_create_user_body()
    yield body
    response = UserMethods.login_user(body['email'], body['password'])
    UserMethods.delete_user(response.json()['accessToken'])

@pytest.fixture
def create_user_with_delete():
    body = generators.generate_create_user_body()
    response = UserMethods.create_user(body)

    yield body

    UserMethods.delete_user(response.json()['accessToken'])

@pytest.fixture
def login_user(create_user_with_delete):
    body = create_user_with_delete
    response = UserMethods.login_user(body['email'], body['password'])
    return response.json()['accessToken']

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    if browser_name=="chrome":
        driver = webdriver.Chrome()
    elif browser_name=="firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()