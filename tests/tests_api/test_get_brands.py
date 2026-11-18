
import allure
import pytest
from services.brands_service import BrandsService
from services.products_service import ProductsService


@allure.epic("API магазина")
@allure.feature("Бренды")
@allure.story("Получение списка брендов")
@pytest.mark.brands
@pytest.mark.smoke
@pytest.mark.api
class TestGetBrands:

    @allure.title("Список содержит больше 10 брендов")
    def test_get_count_of_brands(self, brands_service: BrandsService):

        response = brands_service.get_brands()
        with allure.step("Получить количество брендов из JSON-ответа"):
            data_json = response.json()
            count_of_brands = len(data_json["brands"])

        with allure.step("Проверить, что количество брендов больше 10"):
            assert count_of_brands > 10

    @pytest.mark.parametrize("field", ["id", "brand"])
    def test_brand_has_fields(self, brands_service: BrandsService, field):
        response = brands_service.get_brands()
        brands = response.json()["brands"]

        assert brands, "Список брендов пуст"

        for brand in brands:
            assert field in brand, (
                f"Нет поля {field}, в бренде {brand}"
            )

    @pytest.mark.parametrize(
        "brand_name",
        ["Polo", "H&M", "Madame", "Mast & Harbour"]
    )
    @allure.title("Бренд {brand_name} присутствует в каталоге")
    def test_brand_exist(self, brands_service: BrandsService, brand_name):
        response = brands_service.get_brands()
        brands = response.json()["brands"]

        brand_names = []

        for brand in brands:
            brand_names.append(brand["brand"])

        assert brand_name in brand_names, (
            f"Бренд {brand_name} не найден в каталоге"
        )

    @pytest.mark.parametrize("brand_name", ["Polo", "H&M", "Madame"])
    @allure.title("У бренда {brand_name} есть корректные товары")
    def test_brand_has_products(
        self,
        brands_service: BrandsService,
        products_service: ProductsService,
        brand_name
    ):
        with allure.step("Получить списки брендов и товаров"):
            brands_response = brands_service.get_brands()
            products_response = products_service.get_products()

            brands = brands_response.json()["brands"]
            products = products_response.json()["products"]

        with allure.step("Проверить, что списки не пустые"):
            assert brands, "Список брендов пуст"
            assert products, "Список товаров пуст"

        with allure.step(f"Проверить наличие бренда {brand_name} в справочнике"):
            brand_names = [brand["brand"] for brand in brands]

            assert brand_name in brand_names, (
                f"Бренд {brand_name} не найден в справочнике"
            )

        with allure.step(f"Найти товары бренда {brand_name}"):
            brand_products = [
                product for product in products
                if product.get("brand") == brand_name
            ]

            assert brand_products, (
                f"У бренда {brand_name} нет товаров"
            )

        with allure.step("Проверить ID и названия товаров"):
            products_ids = []

            for index, product in enumerate(brand_products):
                assert "id" in product, (
                    f"У товара бренда {brand_name} отсутствует ID"
                )

                product_id = product["id"]

                assert type(product_id) is int and product_id > 0, (
                    f"Некорректный ID товара бренда {brand_name}: "
                    f"{product_id}"
                )

                assert "name" in product, (
                    f"У товара бренда {brand_name} отсутствует название"
                )

                product_name = product["name"]

                assert isinstance(product_name, str) and product_name.strip(), (
                    f"У товара бренда {brand_name} некорректное название: "
                    f"{product_name}"
                )

                products_ids.append(product_id)

        with allure.step("Проверить уникальность ID товаров"):
            assert len(products_ids) == len(set(products_ids)), (
                f"У бренда {brand_name} есть повторяющиеся ID: "
                f"{products_ids}"
            )
