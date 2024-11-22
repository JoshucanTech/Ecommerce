# accounts/admin.py

from django.contrib import admin
from .models import Product


# Custom User Admin class for the CustomUser model
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'description', 'price', 'stock_quantity', 'category',)
    list_filter = ('price',  'category')  # Filters for the product list view

    
# Register your CustomUser model with the custom admin interface
admin.site.register(Product, ProductAdmin)
