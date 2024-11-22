from .models import Order, OrderItem
from .serializers import OrderItemSerializer, OrderSerializer
from rest_framework import generics, permissions
from products.models import Product
from rest_framework.exceptions import NotFound


class OrderItemListView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        # Extract the product ID from the validated data
        product_id = self.request.data.get('products')  # Assuming 'products' is the key in request data

        if not product_id:
            raise NotFound(detail="Product ID is required.")  # If no product_id, raise an error

        # Retrieve the product by ID
        try:
            the_product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found.")  # Handle case if product is not found

        # Get the product price
        product_price = the_product.price

        # Save the OrderItem with the correct price from the product
        # We pass the product price as the value for the 'price' field.
        user = self.request.user
        serializer.save(user=user, price=product_price)



class OrderItemUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



class OrderUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer