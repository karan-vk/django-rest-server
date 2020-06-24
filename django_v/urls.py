from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core.views import CustomerViewSet




router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
