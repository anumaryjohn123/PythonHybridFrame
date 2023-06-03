import self as self

from Pages.BasePage import BasePage
import time
from Utils1.customLogger import LogGen
from Utils1 import ExcelUtils


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    path = "Utils1/Testdata.xlsx"

    logger = LogGen.loggen()

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_css = ".login-button"
    button_logout_css = "a[href='/logout']"
    exp_title = "Dashboard / nopCommerce administration"


    def loginPage_clickLogin(self):
        self.logger.info("*******verify login Page************")

        self.user = ExcelUtils.readData(self.path,'Sheet1',2,1)
        self.password = ExcelUtils.readData(self.path, 'Sheet1', 2, 2)
        self.type_into_element(self.user, "textbox_username_id", self.textbox_username_id)
        self.type_into_element(self.password, "textbox_password_id", self.textbox_password_id)
        time.sleep(1)
        self.element_click("button_login_css", self.button_login_css)
        self.title(self.exp_title)
        time.sleep(2)
        self.element_click("button_logout_css", self.button_logout_css)


