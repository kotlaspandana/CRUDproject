from .models import Product
from .serializer import ProductSerializer
from rest_framework import viewsets
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
