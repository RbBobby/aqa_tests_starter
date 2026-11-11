import pytest

from services.products_service import ProductsService


@pytest.mark.products
@pytest.mark.smoke
@pytest.mark.api
class TestGetProducts:

    def test_get_count_of_products(self):
        products_service = ProductsService()
        response = products_service.get_products()
        data_json = response.json()

        count_of_products = len(data_json["products"])
        assert count_of_products > 33

    def test_products_structure(self):
        products_service = ProductsService()
        response = products_service.get_products()
        data_json = response.json()

        assert data_json["products"], "Список продуктов пуст"

        for product in data_json["products"]:
            assert "id" in product
            assert "name" in product
            assert "price" in product
            assert "brand" in product
            assert "category" in product

            assert isinstance(product["id"], int)
            assert isinstance(product["name"], str)
            assert isinstance(product["price"], str)
            assert isinstance(product["brand"], str)
            assert isinstance(product["category"], dict)