from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status,permissions
from .models import CategoriaModel, ProductosModel
from .serializer import CategoriaSerializer, ProductosSerializer
from .pagination import CustomPagination
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404

#class ListCreateCategorias(generics.ListCreateAPIView):
    #queryset=CategoriaModel.objects.all().order_by('id')
    #serializer_class=CategoriaSerializer
   
class CategoriasListCreateView(generics.GenericAPIView):
    queryset = CategoriaModel.objects.all().order_by('id')
    serializer_class = CategoriaSerializer
    http_method_names = ['get', 'post']
    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        #serializer = self.serializer_class(self.get_queryset(), many=True)
        #return Response(data=serializer.data, status=status.HTTP_200_OK)
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(
            self.get_queryset(), request
        )
        serializer = self.serializer_class(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
class CategoriasGetUpdateDeleteView(generics.GenericAPIView):
    queryset = CategoriaModel.objects
    serializer_class = CategoriaSerializer
    http_method_names = ['get', 'patch', 'delete']

    def get(self, request, id):
        record = get_object_or_404(
            self.queryset, pk=id
        )
        serializer = self.serializer_class(record, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        record = get_object_or_404(
            self.queryset, pk=id
        )
        serializer = self.serializer_class(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        
        record = get_object_or_404(self.queryset, pk=id)
        record.delete()
        
        return Response(
            {"message": "Categoria eliminada exitosamente."},
            status=status.HTTP_204_NO_CONTENT
        )

#class ListCreateProductos(generics.ListCreateAPIView):
#    queryset=ProductosModel.objects.all().order_by('id')
#    serializer_class=ProductosSerializer
class ProductosListCreateView(generics.GenericAPIView):
    queryset = ProductosModel.objects.all().order_by('id')
    serializer_class = ProductosSerializer
    http_method_names = ['get', 'post']
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        #serializer = self.serializer_class(self.get_queryset(), many=True)
        #return Response(data=serializer.data, status=status.HTTP_200_OK)
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(
            self.get_queryset(), request
        )
        serializer = self.serializer_class(paginated_queryset, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
class ProductosGetUpdateDeleteView(generics.GenericAPIView):
    queryset = ProductosModel.objects
    serializer_class = ProductosSerializer
    http_method_names = ['get', 'patch', 'delete']

    def get(self, request, id):
        record = get_object_or_404(
            self.queryset, pk=id
        )
        serializer = self.serializer_class(record, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        record = get_object_or_404(
            self.queryset, pk=id
        )
        serializer = self.serializer_class(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        
        record = get_object_or_404(self.queryset, pk=id)
        record.delete()
        
        return Response(
            {"message": "Categoria eliminada exitosamente."},
            status=status.HTTP_204_NO_CONTENT
        )