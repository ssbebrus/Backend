from rest_framework import serializers
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


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.CharField(allow_null=True, allow_blank=True)
    class Meta:
        model = Category
        fields = '__all__'


class GoodSerializer(serializers.ModelSerializer):
    image = serializers.CharField(allow_null=True, allow_blank=True)
    class Meta:
        model = Good
        fields = '__all__'


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ('id', 'good', 'quantity')
        read_only_fields = ('basket',)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = '__all__'


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class DeliveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMethod
        fields = '__all__'
