import time

import pytest
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPage

import allure
import pytest


@pytest.mark.description("Validate the Login using chrome Browser")
@allure.feature('Login')
@allure.story('Valid Credentials')
@allure.title('Successful Login Test')
@pytest.mark.usefixtures("setupTeardown")
class Test_Login:
    @allure.title('Successful Login Test')
    def test_Login_Page(self):
        login_page = LoginPage(self.driver)
        login_page.loginPage_clickLogin()
        time.sleep(1)

    @allure.title('Invalid credentials')
    def test_InvalidCredentials(self):
        login_page = LoginPage(self.driver)
        login_page.loginPage_failure()
        time.sleep(1)
