from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'stock', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at')