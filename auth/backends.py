import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
User = get_user_model()

from rest_framework_simplejwt.tokens import AccessToken


class JWTAuthentication(ModelBackend):
    def authenticate(self, token):
        try:
            payload = AccessToken(token).payload
            user_id = payload.get('user_id')
            user = User.objects.get(id=user_id)
        except:
            return None
        return user
