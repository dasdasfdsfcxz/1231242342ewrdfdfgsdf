from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Invalid price')
        return value

    class Meta:
        model = Product
        fields = ("id", "name", "price")