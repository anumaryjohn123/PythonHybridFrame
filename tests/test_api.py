import pytest
import requests
import json
import allure


@pytest.mark.description("Validate API test")
@allure.title('Successful Post request call')
class Test_api_post:
    def test_apiPost(self):
        with open('Utils1/payload.json', 'r') as file:
            payload = json.load(file)

        response = requests.post('https://reqres.in/api/users/1', json=payload)

        if response.status_code == 201:
            # Request was successful
            print(response.json())  # Display the response content in JSON format
        else:
            # Request encountered an error
            print('Error:', response.status_code)
