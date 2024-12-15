from rest_framework import serializers
from .models import CategoriaModel, ProductosModel

# Crearemos el serializador
class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
      model = CategoriaModel
      fields = "__all__"

class ProductosSerializer(serializers.ModelSerializer):
   imagen_url = serializers.SerializerMethodField()
   
   class Meta:
      model=ProductosModel
      fields="__all__"
   def get_imagen_url(self, obj):
        request = self.context.get('request')  # Obtiene el request actual
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None