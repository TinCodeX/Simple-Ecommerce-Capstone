from django.shortcuts import render

# Create your views here.
# products/views.py
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        search = self.request.query_params.get('search')
        if category:
            queryset = queryset.filter(category__name__iexact=category)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

# products/views.py
class WishlistAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        Wishlist.objects.get_or_create(user=request.user, product_id=product_id)
        return Response({"message": "Added to wishlist"})
    
    def delete(self, request):
        product_id = request.data.get('product_id')
        Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
        return Response({"message": "Removed from wishlist"})