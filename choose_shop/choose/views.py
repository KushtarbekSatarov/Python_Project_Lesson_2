from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import ProductFilter


class IntroduceViewset(viewsets.ModelViewSet):
    queryset =Intorduce.objects.all()
    serializer_class = IntroduceSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['title']

class Great_ProductViewset(viewsets.ModelViewSet):
    queryset = Great_Product.objects.all()
    serializer_class = Great_ProductSerializer
    permission_classes = [permissions.IsAuthenticated]