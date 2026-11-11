from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import api

router = DefaultRouter()
router.register("categorias", api.CategoriaViewSet, basename="categoria")
router.register("tecnologias", api.TecnologiaViewSet, basename="tecnologia")
urlpatterns = [
    path('', include(router.urls))
]