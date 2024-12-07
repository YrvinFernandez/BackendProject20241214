from django.db import models

class CategoriaModel(models.Model):
    id=models.AutoField(primary_key=True, unique=True, null=False)
    nombre=models.CharField(max_length=100, unique=True, null=False)
    createdAt= models.DateTimeField(auto_now_add=True, db_column='created_at')
    updatedAt=models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table='categorias'

class ProductosModel(models.Model):
    id=models.AutoField(primary_key=True, unique=True, null=False)
    nombre=models.CharField(max_length=70, null=False)
    descripcion=models.CharField(max_length=150,)
    imagen=models.ImageField(upload_to='imagen', null=False)
    precio=models.FloatField()
    disponible=models.BooleanField(default=True)
    createdAt=models.DateTimeField(auto_now_add=True, db_column='created_at')
    categoria=models.ForeignKey(to=CategoriaModel, on_delete=models.CASCADE, db_column='categoria_id')

    class Meta:
        db_table='productos'
