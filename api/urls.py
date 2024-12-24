from django.urls import path, include
from rest_framework import  routers
from . import views

router = routers.DefaultRouter()
router.register(r'good-categories', views.CategoryViewSet)
router.register(r'goods', views.GoodViewSet)
router.register(r'recipients', views.RecipientViewSet)
router.register(r'me/basket-items', views.BasketItemViewSet)
router.register(r'payment-methods', views.PaymentMethodViewSet)
router.register(r'delivery-methods', views.DeliveryMethodViewSet)
router.register(r'checkouts', views.CheckoutViewSet)
router.register(r'transactions', views.TransactionViewSet)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/images/', views.UploadImageView.as_view()),
    path('v1/auth/', include('auth.urls')),
    path('v1/me/basket/', views.BasketInfoView.as_view()),
]