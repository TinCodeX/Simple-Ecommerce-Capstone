from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Product, Category, Wishlist
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
# Category Views
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Product Views
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        search = self.request.query_params.get('search')
        if category:
            queryset = queryset.filter(category__name__iexact=category)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated] # Simplified: Assuming only authenticated users can add products

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Wishlist views
class WishlistAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        wishlist = Wishlist.objects.filter(user=request.user)
        # Assuming we just want to list the products in the wishlist
        products = [item.product for item in wishlist]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        product_id = request.data.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            Wishlist.objects.get_or_create(user=request.user, product=product)
            return Response({"message": "Added to wishlist"}, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        product_id = request.data.get('product_id')
        Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
        return Response({"message": "Removed from wishlist"}, status=status.HTTP_204_NO_CONTENT)