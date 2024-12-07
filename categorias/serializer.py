from rest_framework import serializers
from .models import CategoriaModel, ProductosModel

# Crearemos el serializador
class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
      model = CategoriaModel
      fields = "__all__"

class ProductosSerializer(serializers.ModelSerializer):
   class Meta:
      model=ProductosModel
      fields="__all__"