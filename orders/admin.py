# accounts/admin.py

from django.contrib import admin
from .models import Order, OrderItem

# Order Admin
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('id', 'user', 'status', 'total')
    
admin.site.register( Order, OrderAdmin)


# Order Item Admin
class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('order', 'price', 'quantity', 'sub_total', )
    
admin.site.register(OrderItem, OrderItemAdmin)
 