from rest_framework import serializers
from .models import Categoria, Tecnologia

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        # fields = ['id', 'nombre']

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ["id", "nombre"]