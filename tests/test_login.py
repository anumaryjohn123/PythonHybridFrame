import time

import pytest
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPage


@pytest.mark.usefixtures("setupTeardown")
class Test_Login:
    def test_Login_Page(self):
        login_page = LoginPage(self.driver)
        login_page.loginPage_clickLogin()
        time.sleep(1)
