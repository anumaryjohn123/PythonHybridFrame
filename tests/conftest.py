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

    ########### pytest HTML Report ################

    # It is hook for Adding Environment info to HTML Report
    def pytest_configure(config):
        config._metadata['Project Name'] = 'nop Commerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Pavan'

    # It is hook for delete/Modify Environment info to HTML Report
    @pytest.mark.optionalhook
    def pytest_metadata(metadata):
        metadata.pop("JAVA_HOME", None)
        metadata.pop("Plugins", None)
