from rest_framework import serializers
from manageBD.models import Changes

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Changes
        read_only_fields = ('id', 'date', 'time', 'product', 'amount')