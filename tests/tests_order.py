from orders.models import Order, OrderItem
from products.models import Product
from category.models import Category
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class setUp(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test category")
        self.products = Product.objects.create(
            name="test_name", 
            description="test description", 
            price="100",
            stock_quantity=10,
            category=self.category
        )
        self.user = User.objects.create(
            email="test_name", 
            username="test username", 
            first_name="test first_name",
            last_name="test last_name",
            address="test address",
            password="password"
        )
        self.order = Order.objects.create(
            user=self.user, 
            status="completed", 
        )

        
    def test_create_order_item_price(self):    
        order_item = OrderItem.objects.create(
            order=self.order, 
            products=self.products, 
            price=self.products.price,
            quantity=10,
        )
        
        self.assertEqual(order_item.price, self.products.price)