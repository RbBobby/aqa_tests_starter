
import allure
import pytest


@allure.epic("API магазина")
@allure.feature("Товары")
@allure.story("Получение списка товаров")
@pytest.mark.products
@pytest.mark.smoke
@pytest.mark.api
class TestGetProducts:

    @allure.title("Список товаров содержит поле products со списком")
    def test_products_is_list(self, products_service):
        with allure.step("Получить список товаров"):
            response = products_service.get_products()
            data = response.json()

        with allure.step("Проверить, что products является списком"):
            assert "products" in data
            assert isinstance(data["products"], list)

    @allure.title("Список содержит больше 33 товаров")
    def test_count_of_products(self, products_service):
        with allure.step("Получить список товаров"):
            response = products_service.get_products()
            data = response.json()

        with allure.step("Проверить количество товаров"):
            assert len(data["products"]) > 33

    @allure.title("У каждого товара есть обязательные поля")
    def test_products_have_required_fields(self, products_service):
        with allure.step("Получить список товаров"):
            response = products_service.get_products()
            products = response.json()["products"]

        required_fields = ["id", "name", "price", "brand", "category"]

        with allure.step("Проверить обязательные поля каждого товара"):
            for index, product in enumerate(products):
                for field in required_fields:
                    assert field in product, (
                        f"У товара с индексом {index}, "
                        f"id={product.get('id')}, отсутствует поле {field}"
                    )

    @allure.title("ID всех товаров уникальны")
    def test_products_ids_are_unique(self, products_service):
        with allure.step("Получить список товаров"):
            response = products_service.get_products()
            products = response.json()["products"]

        with allure.step("Проверить уникальность ID"):
            products_ids = [product["id"] for product in products]

            assert len(products_ids) == len(set(products_ids)), (
                "В списке товаров есть повторяющиеся ID"
            )
