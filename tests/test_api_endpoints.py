import pytest

@pytest.mark.django_db
def test_anonymous_user_can_access_public_endpoints(client):
    goods_response = client.get('/api/v1/goods/')
    assert goods_response.status_code == 200
    categories_response = client.get('/api/v1/good-categories/')
    assert categories_response.status_code == 200
    delivery_methods_response = client.get('/api/v1/delivery-methods/')
    assert delivery_methods_response.status_code == 200
    payment_methods_response = client.get('/api/v1/payment-methods/')
    assert payment_methods_response.status_code == 200

@pytest.mark.django_db
def test_anonymous_user_cannot_access_protected_endpoints(client):
    basket_items_response = client.get('/api/v1/me/basket-items/')
    assert basket_items_response.status_code == 401
    recipients_response = client.get('/api/v1/recipients/')
    assert recipients_response.status_code == 401
    checkouts_response = client.get('/api/v1/checkouts/')
    assert checkouts_response.status_code == 401
    transactions_response = client.get('/api/v1/transactions/')
    assert transactions_response.status_code == 401

@pytest.mark.django_db
def test_admin_user_can_access_protected_endpoints(admin_client):
    basket_items_response = admin_client.get('/api/v1/me/basket-items/')
    assert basket_items_response.status_code == 200
    recipients_response = admin_client.get('/api/v1/recipients/')
    assert recipients_response.status_code == 200
    checkouts_response = admin_client.get('/api/v1/checkouts/')
    assert checkouts_response.status_code == 200
    transactions_response = admin_client.get('/api/v1/transactions/')
    assert transactions_response.status_code == 200