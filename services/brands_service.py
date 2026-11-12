import requests

BASE_URL = "https://automationexercise.com/api"

class BrandsService:

    def __init__(self):
        self.base_url = BASE_URL

    def get_brands(self):
        url = self.base_url + "/brandsList"
        response = requests.get(url)
        assert response.status_code == 200, f"response.status_code = {response.status_code}. Проверьте API"