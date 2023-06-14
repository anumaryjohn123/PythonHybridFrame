

import pytest

import allure


from Pages.aws import aws


@pytest.mark.description("Validate AWS test")
@allure.title('Successful extraction of AWS S3 Bucket Data')
class Test_aws:
    def test_search_product(self):
        aws(self)
