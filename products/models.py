from django.db import models
from category.models import Category

# Create your models here.
# name, description, price, stock quantity, and category
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    price = models.PositiveBigIntegerField()
    stock_quantity = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_products")

    def __str__(self):
        return f"{self.pk} - {self.name}"