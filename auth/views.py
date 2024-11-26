import random

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import LoginSerializer, LoginConfirmSerializer
import pyotp
from .emails import OtpEmail
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login

User = get_user_model()

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            response = Response(serializer.data)
            response.data["message"] = "Одноразовый код отправлен на ваш email"
            response.status = status.HTTP_200_OK
            user = User.objects.get(**serializer.data)
            if user is None:
                response.status = status.HTTP_201_CREATED
                user = serializer.save()
            gen = pyotp.TOTP(user.secret_key)
            otp = gen.now()
            user.otp = otp
            user.save()
            email_message = OtpEmail((user.email,), otp)
            email_message.send(fail_silently=False)
            print(otp)
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginConfirmAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginConfirmSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=serializer.validated_data['email'])
        otp = user.otp
        if otp is None or user is None:
            return Response({'message': 'Некорректные данные'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.validated_data['otp'] != otp:
            return Response({'error': 'Неверный код'}, status=status.HTTP_400_BAD_REQUEST)
        user.otp = None
        user.save()
        refresh = RefreshToken.for_user(user)
        refresh.payload.update({
            'user_id': user.id,
            'email': user.email,
        })
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    def post(self, request):
        refresh_token = request.session.get('refresh')
        if not refresh_token:
            return Response({'error': 'Необходим Refresh token'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({'error': 'Неверный Refresh token'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': 'Выход успешен'}, status=status.HTTP_200_OK)
