from rest_framework import filters, viewsets
from .models import Categoria, Tecnologia
from .serializers import CategoriaSerializer, TecnologiaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.order_by("nombre")
    serializer_class = CategoriaSerializer

class TecnologiaViewSet(viewsets.ModelViewSet):
    queryset = Tecnologia.objects.order_by("nombre")
    serializer_class = TecnologiaSerializer