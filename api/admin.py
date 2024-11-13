from django.contrib import admin
from .models import (
    Category,
    Good,
    Recipient,
    Basket,
    BasketItem,
)
# Register your models here.
admin.site.register(Category)
admin.site.register(Good)
admin.site.register(Recipient)
admin.site.register(Basket)
admin.site.register(BasketItem)
