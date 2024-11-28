from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = ('email',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginConfirmSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    otp = serializers.CharField(max_length=20, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        otp = data.get('otp', None)

        if email is None:
            raise serializers.ValidationError(
                'email - обязательное поле'
            )

        if otp is None:
            raise serializers.ValidationError(
                'otp - обязательное поле'
            )
        return data