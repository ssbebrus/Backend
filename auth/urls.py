from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
app_name = 'auth'
urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('confirm/', views.LoginConfirmAPIView.as_view(), name='confirm'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('info/', views.UserInfoView.as_view(), name='user_info'),
]