import requests

from services.constans import BASE_URL, TIMEOUT


class ProductsService:

    def __init__(self):
        self.base_url = BASE_URL

    def get_products(self):
        url = self.base_url + "/productsList"
        response = requests.get(url, timeout=TIMEOUT)

        assert response.status_code == 200, (
            f"Ожидали HTTP 200, получили {response.status_code}"
        )

        return response