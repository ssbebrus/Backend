from rest_framework_simplejwt.tokens import AccessToken


def get_payload(token):
    token_parts = token.split()
    token = token_parts[1]
    return AccessToken(token).payload