import pytest
from selenium import webdriver

from Utils1.ReadConfig import read_configuration


@pytest.fixture()
def setupTeardown(request):
    browser = read_configuration("basic info","browser")
    print(browser)
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.edge()
    else:
        print("Provide valid browser name from list")
    driver.maximize_window()
    driver.get(read_configuration("basic info", "url"))
    request.cls.driver = driver
    yield
    driver.quit()



