import allure
import pytest
import requests

BASE_URL = "https://automationexercise.com/api"
ENDPOINT = "/productsList"

URL = BASE_URL + ENDPOINT

@allure.epic("API магазина")
@allure.feature("Товары")
@allure.story("Получение списка товаров")
@pytest.mark.products
@pytest.mark.smoke
@pytest.mark.api
class TestGetProducts:
    @allure.title("API списка товаров возвращает HTTP 200")
    @allure.description("Отправить запрос списка товаров и проверить HTTP-статус ответа.")
    def test_get_status_code(self):
        with allure.step("Запросить список товаров"):
            responce = requests.get(URL)
        with allure.step("Проверить, что API вернул HTTP 200"):
            assert responce.status_code == 200

    @allure.title("Список содержит больше 33 товаров")
    @allure.description("Получить список товаров и проверить, что в нём больше 33 элементов.")
    def test_gea_count_of_products(self):
        with allure.step("Запросить список товаров"):
            responce = requests.get(URL)
        with allure.step("Получить количество товаров из JSON-ответа"):
            data_json = responce.json()
            count_of_products = len(data_json["products"])
        with allure.step("Проверить, что количество товаров больше 33"):
            assert count_of_products > 33



