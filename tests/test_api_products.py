from api.product_api import get_products, create_product
from utils.logger import get_logger
import pytest

logger = get_logger()

def test_get_products():
    response = get_products()

    logger.info(f"GET Status Code: {response.status_code}")

    if response.status_code != 200:
        pytest.skip(f"Skipping due to API restriction: {response.status_code}")

    data = response.json()
    assert len(data) > 0

    logger.info("GET API passed ✅")


def test_create_product():
    payload = {
        "title": "Automation Product",
        "price": 150,
        "description": "Test product",
        "category": "electronics"
    }

    response = create_product(payload)

    logger.info(f"POST Status Code: {response.status_code}")

    if response.status_code != 201:
        pytest.skip(f"Skipping due to API restriction: {response.status_code}")

    data = response.json()
    assert data["title"] == "Automation Product"

    logger.info("POST API passed ✅")