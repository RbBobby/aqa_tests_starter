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
    """
    def test_get_status_code(self):
        brands_service = BrandsService()
        responce = brands_service.get_brands()
        assert responce.status_code == 200
    """
    
    @allure.title("Список содержит больше 10 брендов")
    def test_get_count_of_brands(self, brands_service: BrandsService):

        responce = brands_service.get_brands()
        with allure.step("Получить количество брендов из JSON-ответа"):
            data_json = responce.json()
            count_of_brands = len(data_json["brands"])
        with allure.step("Проверить, что количество брендов больше 10"):
            assert count_of_brands > 10
