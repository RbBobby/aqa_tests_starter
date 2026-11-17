
import allure
import requests

from services.constans import TIMEOUT, BASE_URL


class ApiClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT
        self.session = requests.Session()

    def close(self):
        self.session.close()

    @allure.step("Выполнить GET-запрос к {path}")
    def get(self, path: str, **kwargs):
        return self.session.get(
            f"{self.base_url}{path}",
            timeout=self.timeout,
            **kwargs
        )

    @allure.step("Выполнить POST-запрос к {path}")
    def post(self, path: str, **kwargs):
        return self.session.post(
            f"{self.base_url}{path}",
            timeout=self.timeout,
            **kwargs
        )

    @allure.step("Выполнить PUT-запрос к {path}")
    def put(self, path: str, **kwargs):
        return self.session.put(
            f"{self.base_url}{path}",
            timeout=self.timeout,
            **kwargs
        )

    @allure.step("Выполнить DELETE-запрос к {path}")
    def delete(self, path: str, **kwargs):
        return self.session.delete(
            f"{self.base_url}{path}",
            timeout=self.timeout,
            **kwargs
        )
