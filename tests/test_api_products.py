from api.product_api import get_products, create_product
from utils.logger import get_logger

logger = get_logger()

def test_get_products():
    response = get_products()

    logger.info("GET request sent")

    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0   # ✅ validate data

    logger.info("GET API passed ✅")


def test_create_product():
    payload = {
        "title": "Automation Product",
        "price": 150,
        "description": "Test product",
        "category": "electronics"
    }

    response = create_product(payload)

    logger.info("POST request sent")

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Automation Product"   # ✅ validate response

    logger.info("POST API passed ✅")