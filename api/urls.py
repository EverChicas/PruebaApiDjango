from django.urls import path, include
from .views import index, CredencialAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register("credenciales", CredencialAPI)

urlpatterns = [
    path('', index,name='index'),
    path('', include(router.urls)),
]
