

from Pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    register_css = ".ico-register"

    def homePage_registerLink(self):
        return self.element_click("register_css", self.register_css)


