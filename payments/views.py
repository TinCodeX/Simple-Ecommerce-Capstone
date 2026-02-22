from django.shortcuts import render

# Create your views here.
# payments/views.py
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.models import Order
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripePaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get("order_id")
        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        intent = stripe.PaymentIntent.create(
            amount=int(order.total_price * 100),  # Stripe expects cents
            currency='usd',
            metadata={'order_id': order.id},
        )

        return Response({
            "client_secret": intent.client_secret,
            "order_id": order.id
        })