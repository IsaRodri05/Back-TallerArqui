from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from backProducts.mqtt_server import publish_low_stock_alert
from datetime import datetime

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['post'])
    def sell(self, request, pk=None):
        product = self.get_object()
        amount = int(request.data.get("amount", 0))

        if amount <= 0:
            return Response({"error": "Amount must be positive."}, status=status.HTTP_400_BAD_REQUEST)

        if product.stock < amount:
            return Response({"error": "Not enough stock."}, status=status.HTTP_400_BAD_REQUEST)

        # Decrease the stock
        product.stock -= amount
        product.save()

        # Publish a message to MQTT if stock is low
        if product.stock < 10:
            try:
                payload = {
                    "nombre": product.name,
                    "fecha": datetime.now().strftime("%Y-%m-%d"),
                    "hora": datetime.now().strftime("%H:%M"),
                    "cantidad": product.stock
                }
                publish_low_stock_alert(payload)
            except Exception as e:
                return Response({"error": f"MQTT publish failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Product sold successfully",
            "stock_left": product.stock
        })
