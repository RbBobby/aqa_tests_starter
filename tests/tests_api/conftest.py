import pytest

from services.brands_service import BrandsService

from services.api_client import ApiClient

@pytest.fixture
def brands_service(api_client: ApiClient):
    return BrandsService(api_client)

@pytest.fixture(scope="session")
def api_client():
    client = ApiClient()
    yield client
    client.close()

#function
#class
#module
#packadge
#session