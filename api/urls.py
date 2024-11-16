from django.urls import path, include
from rest_framework import  routers
from . import views

router = routers.DefaultRouter()
router.register(r'good-categories', views.CategoryViewSet)
router.register(r'goods', views.GoodViewSet)
router.register(r'recipients', views.RecipientViewSet)
router.register(r'me/basket-items', views.BasketItemViewSet)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]