import pytest
from selenium import webdriver
from utilities import ReadConfigurations

@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configurations("basic info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print('Provide a valid browser')

    driver.maximize_window()
    app_url = ReadConfigurations.read_configurations("basic info", "url")

    driver.get(app_url)

    request.cls.driver = driver

    yield

    driver.quit()