from django.shortcuts import render

# Create your views here.
# cart/views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CartItem
from products.models import Product

class UpdateCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        user = request.user

        try:
            cart_item = CartItem.objects.get(user=user, product_id=product_id)
            cart_item.quantity = quantity
            cart_item.save()
        except CartItem.DoesNotExist:
            return Response({"error": "Item not in cart"}, status=404)

        return Response({"message": "Quantity updated", "product_id": product_id, "quantity": quantity})