
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include

# from django.contrib.admin import AdminSite
#
# class CustomAdminSite(AdminSite):
#     site_header = 'Bebrus'
#     site_title = 'Bebrus'
#     index_title = 'Центр управления интернет-магазином Bebrus'
#
# admin_site = CustomAdminSite()

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="Документация для проекта Backend",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="semaselivan@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('swagger/<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
