import requests

from test_get_products import BASE_URL


BASE_URL = "https://automationexercise.com/api"

class BrandsService:

    def __init__(self):
        self.base_url = BASE_URL

    def get_brands(self):
        url = self.base_url + "/brandsList"
        response = requests.get(url)
        return response