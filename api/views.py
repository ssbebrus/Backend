import boto3
from botocore.config import Config
from rest_framework.permissions import IsAuthenticated
import os

from .serializers import (
    CategorySerializer,
    GoodSerializer,
    RecipientSerializer,
    BasketSerializer,
    BasketItemSerializer,
    DeliveryMethodSerializer,
    PaymentMethodSerializer,
    CheckoutSerializer,
    TransactionSerializer,
)
from .models import (
    Category,
    Good,
    Recipient,
    Basket,
    BasketItem,
    PaymentMethod,
    DeliveryMethod,
    Checkout,
    Transaction
)
# Create your views here.
from rest_framework import viewsets
from .permissions import AdminOrReadOnly, IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser


class BasketInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            basket = Basket.objects.get(user=request.user)
            serializer = BasketSerializer(basket)
            return Response(serializer.data)
        except Basket.DoesNotExist:
            return Response({'error': 'Basket not found'}, status=status.HTTP_404_NOT_FOUND)


class UploadImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (AdminOrReadOnly,)
    # AWS_S3_ENDPOINT_URL = 'http://minio:9000'
    # AWS_STORAGE_BUCKET_NAME = 'goods'
    # AWS_QUERYSTRING_AUTH = False
    s3 = boto3.client(
        's3',
        endpoint_url='http://minio:9000',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        # config=Config(signature_version='s3v4'),
    )
    # Загрузка файла
    bucket_name = 'goods'

    def post(self, request, *args, **kwargs):
        print(request.data)
        file = request.data.get('file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        name = request.data.get('name')
        try:
            self.s3.put_object(Bucket=self.bucket_name, Key=name, Body=file)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        public_url = f"http://localhost:9000/{self.bucket_name}/{name}"
        return Response({"url": public_url}, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly,)
    ordering = ('name',)


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('category',)
    search_fields = ('name', 'category__name')
    ordering_fields = ('price',)
    ordering = (-'id',)


class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

    def perform_create(self, serializer):
        serializer.save(basket=self.request.user.basket)

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return self.queryset.none()
        return self.queryset.filter(basket=self.request.user.basket)


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = (AdminOrReadOnly,)


class DeliveryMethodViewSet(viewsets.ModelViewSet):
    queryset = DeliveryMethod.objects.all()
    serializer_class = DeliveryMethodSerializer
    permission_classes = (AdminOrReadOnly,)


class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = (IsAdminUser,)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAdminUser,)
