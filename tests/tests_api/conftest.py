import pytest

from services.api_client import ApiClient
from services.brands_service import BrandsService
from services.products_service import ProductsService


@pytest.fixture
def brands_service(api_client: ApiClient):
    return BrandsService(api_client)


@pytest.fixture(scope="function")
def products_service(api_client: ApiClient):
    return ProductsService(api_client)


@pytest.fixture(scope="session")
def api_client():
    client = ApiClient()
    yield client
    client.close()