
import allure

from services.api_client import ApiClient


class ProductsService:

    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @allure.step("Получить список товаров")
    def get_products(self):
        response = self.api_client.get("/productsList")

        with allure.step("Проверить статус ответа"):
            assert response.status_code == 200, (
                f"Ожидали HTTP 200, получили {response.status_code}"
            )

        return response
