from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Product

class ProductListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Product.objects.all()

        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        if min_price:
            queryset = queryset.filter(price__gte = min_price)

        if max_price:
            queryset = queryset.filter(price__lte = max_price)

        return queryset


class ProductRetrieveDeleteUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    