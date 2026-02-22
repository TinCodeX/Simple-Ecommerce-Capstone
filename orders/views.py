from django.shortcuts import render

# Create your views here.
# orders/views.py
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cart.models import CartItem
from orders.models import Order, OrderItem
from .serializers import OrderSerializer

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status = self.request.query_params.get('status')
        queryset = Order.objects.filter(user=self.request.user)
        if status:
            queryset = queryset.filter(status__iexact=status)
        return queryset
    
class CheckoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)

        if not cart_items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        total_price = sum([item.product.price * item.quantity for item in cart_items])
        order = Order.objects.create(user=user, total_price=total_price)

        # Convert cart items to order items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Optionally: clear cart
        cart_items.delete()

        return Response({"order_id": order.id, "total_price": order.total_price})