from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm'),
    path('good/create/', views.CreateGoodView.as_view(), name='good_create'),
]