from rest_framework.permissions import IsAuthenticated

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
from .permissions import AdminOrReadOnly, OwnerOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly,)


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (AdminOrReadOnly,)


class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    permission_classes = (OwnerOrReadOnly,)


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
    permission_classes = (AdminOrReadOnly,)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (AdminOrReadOnly,)
