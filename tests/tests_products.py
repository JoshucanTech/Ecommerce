from products.models import Product
from category.models import Category
from django.test import TestCase

class setUp(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test category")
        
    def test_create_product(self):    
        product = Product.objects.create(
            name="test_name", 
            description="test description", 
            price="100",
            stock_quantity=10,
            category=self.category
        )
        
        self.assertEqual(product.name, "test_name")