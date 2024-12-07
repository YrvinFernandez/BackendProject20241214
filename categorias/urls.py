from django.urls import path
from .views import CategoriasListCreateView, ProductosListCreateView, CategoriasGetUpdateDeleteView, ProductosGetUpdateDeleteView

urlpatterns = [
    path('categorias/',CategoriasListCreateView.as_view(), name='list_create_cat'),
    path('productos/',ProductosListCreateView.as_view(), name='list_create_pro'),
    path('categorias/<int:id>', CategoriasGetUpdateDeleteView.as_view(), name='read_update_delete'),
    path('productos/<int:id>', ProductosGetUpdateDeleteView.as_view(), name='read_update_delete')
]
