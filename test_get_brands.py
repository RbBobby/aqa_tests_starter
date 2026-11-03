import pytest
from services.brands_service import BrandsService

@pytest.mark.brands
@pytest.mark.smoke
@pytest.mark.api
class TestGetBrands:
    def test_get_status_code(self):
        brands_service = BrandsService()
        responce = brands_service.get_brands()
        assert responce.status_code == 200

    def test_get_count_of_brands(self):
        brands_service = BrandsService()
        responce = brands_service.get_brands()
        data_json = responce.json()
        count_of_brands = len(data_json["brands"])
        assert count_of_brands > 10