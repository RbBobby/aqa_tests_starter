import pytest
import requests

BASE_URL = "https://automationexercise.com/api"
ENDPOINT = "/productsList"

URL = BASE_URL + ENDPOINT

@pytest.mark.products
@pytest.mark.smoke
@pytest.mark.api
class TestGetProducts:
    def test_get_status_code(self):
        responce = requests.get(URL)
        assert responce.status_code == 200

    def test_gea_count_of_products(self):
        responce = requests.get(URL)
        data_json = responce.json()
        count_of_products = len(data_json["products"])
        assert count_of_products > 33


