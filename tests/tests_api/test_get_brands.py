import allure
import pytest
from services.brands_service import BrandsService

@allure.epic("API магазина")
@allure.feature("Бренды")
@allure.story("Получение списка брендов")
@pytest.mark.brands
@pytest.mark.smoke
@pytest.mark.api
class TestGetBrands:
    
    @allure.title("Список содержит больше 10 брендов")
    def test_get_count_of_brands(self, brands_service: BrandsService):

        responce = brands_service.get_brands()
        with allure.step("Получить количество брендов из JSON-ответа"):
            data_json = responce.json()
            count_of_brands = len(data_json["brands"])
        with allure.step("Проверить, что количество брендов больше 10"):
            assert count_of_brands > 10

    @pytest.mark.parametrize("field", ["id", "brand"])
    def test_brand_has_fields(self, brands_service: BrandsService, field):
        response = brands_service.get_brands()
        brands = response.json()["brands"]

        assert brands, "Список брендов пуст"

        for brand in brands:
            assert field in brand, (f"Нет поля {field}, в бренде {brand}")

    @pytest.mark.parametrize("brand_name", ["Polo", "H&M", "Madame", "Mast & Harbour", "Mast"])
    @allure.title("Брунд {brand_name} присутствует в каталоге")
    def test_brand_exist(self, brands_service: BrandsService, brand_name):
        response = brands_service.get_brands()
        brands = response.json()["brands"]

        brand_names = []

        for brand in brands:
            brand_names.append(brand["brand"])

        assert brand_name in brand_names, (f"Бренд {brand_name} не найден в каталоге")



#{"id":1,"brand":"Polo", "age":"35"},