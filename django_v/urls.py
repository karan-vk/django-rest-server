from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import (CustomerViewSet, ProfessionViewSet,
                        DataSheetViewSet, DocumentViewSet)
from core import views



router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet,basename='customer')
router.register(r'profession', ProfessionViewSet)
router.register(r'data-sheet', DataSheetViewSet)
router.register(r'document', DocumentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('custom/get/', views.CustomGet.as_view()),
    path('custom/create/', views.AuthUser.as_view())
]
