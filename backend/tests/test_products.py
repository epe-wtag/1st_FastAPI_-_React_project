import json
from unittest.mock import patch
import pytest
from fastapi import status
from app.oauth2 import create_access_token, get_token_data


@pytest.fixture
def admin_token():
    user_data = {"user_id": 1, "role": "admin"}
    token = create_access_token(user_data)
    return token


def test_get_token_data(mock_jwt_decode):
    mock_jwt_decode.return_value = {"user_id": 1, "role": "admin"}
    payload = get_token_data("mocked_token")

    assert payload.id == "1"
    assert payload.role == "admin"


def test_create_product(test_client, db_session, admin_token):
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100,
        "image_url": "shirt.jpg",
    }

    with patch("app.oauth2.jwt.decode") as mock_jwt_decode:
        mock_jwt_decode.return_value = {"user_id": 1, "role": "admin"}

        response = test_client.post(
            "/api/products/",
            headers={"Authorization": f"Bearer {admin_token}"},
            data=product_data,
        )

    assert response.status_code == status.HTTP_201_CREATED

    assert "id" in response.json()
    assert response.json()["name"] == product_data["name"]
    assert response.json()["description"] == product_data["description"]
    assert response.json()["price"] == product_data["price"]
    assert response.json()["image_url"] == product_data["image_url"]


def test_read_products(test_client, db_session, admin_token):
    with patch("app.oauth2.jwt.decode") as mock_jwt_decode:
        mock_jwt_decode.return_value = {"user_id": 1, "role": "admin"}

        response = test_client.get(
            "/api/products/",
            headers={"Authorization": f"Bearer {admin_token}"},
            params={"skip": 0, "limit": 10},
        )

        assert response.status_code == status.HTTP_200_OK

        products = response.json()
        assert len(products) > 0
        assert "id" in products[0]
        assert "name" in products[0]



def test_read_product(test_client, db_session, admin_token):
    # Create a product in the database
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100,
        "image_url": "shirt.jpg",
    }
    
    with patch("app.oauth2.jwt.decode") as mock_jwt_decode:
        mock_jwt_decode.return_value = {"user_id": 1, "role": "admin"}

        response = test_client.get(
            "/api/products/1",
            headers={"Authorization": f"Bearer {admin_token}"},
        )

    assert response.status_code == status.HTTP_200_OK

    assert response.json()["name"] == product_data["name"]
    assert response.json()["description"] == product_data["description"]
    assert response.json()["price"] == product_data["price"]
    assert response.json()["image_url"] == product_data["image_url"]

