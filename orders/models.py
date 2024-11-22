from django.db import models
from django.conf import settings
from products.models import Product



class Order(models.Model):
    ORDER_STATUS = [
        ('pending','Pending'),
        ('completed','Completed'),
        ('cancelled','Cancelled')
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="order_products")
    status = models.CharField(max_length=30, choices=ORDER_STATUS, default="pending")


    def __str__(self):
        return f"{self.pk} - {self.user}"

    
    @property
    def total(self):
        order = sum(item.price * item.quantity for item in self.order_items.all())
        return order
    
    





class OrderItem(models.Model):    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    products = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="order_products")
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()


    def __str__(self):
        return f"{self.pk} - {self.order}"


    @property
    def sub_total(self):
        return self.price * self.quantity
        # return 0
    


