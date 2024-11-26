from rest_framework_simplejwt.tokens import AccessToken


def get_payload(token):
    return AccessToken(token).payload