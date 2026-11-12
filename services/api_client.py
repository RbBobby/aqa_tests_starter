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
    def get(self, path: str, **kwagrs):
        return self.session.get(f"{self.base_url}{path}", timeout=self.timeout, **kwagrs)

    @allure.step("Выполнить запрос через ApiClient.put к {path}")
    def put (self, path: str, **kwagrs):
        return self.session.get(f"{self.base_url}{path}", timeout=self.timeout, **kwagrs)

    @allure.step("Выполнить запрос через ApiClient.post к {path}")
    def post(self, path: str, **kwagrs):
        return self.session.get(f"{self.base_url}{path}", timeout=self.timeout, **kwagrs)

    @allure.step("Выполнить запрос через ApiClient.delete к {path}")
    def delete(self, path: str, **kwagrs):
        return self.session.get(f"{self.base_url}{path}", timeout=self.timeout, **kwagrs)   

    #Todo Добавить методы get post delete\
    #Добавить close request

