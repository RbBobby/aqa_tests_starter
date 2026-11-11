import requests

BASE_URL = "https://automationexercise.com/api"

class productsService:

    def __init__(self):
        self.base_url = BASE_URL

    def get_products(self):
        url = self.base_url + "/productsList"
        response = requests.get(url)
        assert response.status_code == 200
        return response