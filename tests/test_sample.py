import time

import pytest
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage


@pytest.mark.usefixtures("setupTeardown")
class Test_search:
    def test_search_product(self):
        print("sample")
