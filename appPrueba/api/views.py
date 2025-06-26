from rest_framework import viewsets, filters
from appPrueba.models import Articulo, Suscripcion
from .serializers import ArticuloSerializer, SuscripcionSerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['estado']

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer
