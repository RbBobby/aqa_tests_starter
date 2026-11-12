import allure
from services.api_client import ApiClient

ENDPOINT = "/brandsList"
class BrandsService:

    def __init__(self, api_client: ApiClient):
        self.api_client = api_client
        

    def get_brands(self):

        with allure.step("запрашиваем список брендов"):
            response = self.api_client.get(ENDPOINT)
        with allure.step("проверяем список брендов"):    
            assert response.status_code == 200, f"response.status_code = {response.status_code}. Проверьте API"
        return response