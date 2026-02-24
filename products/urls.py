from django.urls import path
from .views import (
    ProductListView, ProductCreateView, ProductDetailView,
    CategoryListCreateView, CategoryDetailView, WishlistAPIView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    
    path('wishlist/', WishlistAPIView.as_view(), name='wishlist'),
]