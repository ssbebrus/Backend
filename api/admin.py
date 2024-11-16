from django.contrib import admin
from .models import (
    Category,
    Good,
    Recipient,
    Basket,
    BasketItem,
    PaymentMethod,
    DeliveryMethod,
    Checkout,
    Transaction,
)
# Register your models here.
admin.site.register(Category)
admin.site.register(Good)
admin.site.register(Recipient)
admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(PaymentMethod)
admin.site.register(DeliveryMethod)
admin.site.register(Checkout)
admin.site.register(Transaction)
