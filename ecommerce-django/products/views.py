from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
