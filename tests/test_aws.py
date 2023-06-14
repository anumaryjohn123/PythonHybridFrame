import time

import pytest
from selenium.webdriver.common.by import By
import allure

from Pages.HomePage import HomePage
from Pages.aws import aws


@pytest.mark.description("Validate AWS test")
@allure.title('Successful extraction of AWS S3 Bucket Data')
class Test_aws:
    def test_search_product(self):
        aws(self)
