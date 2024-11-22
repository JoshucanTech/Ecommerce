from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product




class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'total', 'order_items', 'status']




class OrderItemSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'products', 'price', 'quantity']
        read_only_fields=['price']
        required='products'

    # def create(self, validated_data):
    #     product_id = validated_data.pop('products')
    #     the_product = Product.objects.get(id=product_id)
    #     product_price = the_product.price
    #     order_items = OrderItem.objects.create(
    #         price=product_price,
    #         **validated_data
    #     )
    #     return order_items
        
