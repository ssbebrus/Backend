import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
@pytest.mark.django_db
def admin_user():
    return User.objects.create_superuser(
        email = 'admin@gmail.com',
        password = 'admin'
    )

@pytest.fixture
@pytest.mark.django_db
def admin_auth_token(client, admin_user):
    admin_user.otp = 222888
    admin_user.save()
    otp = admin_user.otp
    response = client.post(
        '/api/v1/auth/confirm/',
        {
            'email': admin_user.email,
            'otp': otp
        }
    )
    print(response.data)
    token = response.data['access']
    return token

@pytest.fixture
def admin_client(admin_auth_token):
    from rest_framework.test import APIClient
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + admin_auth_token)
    return client