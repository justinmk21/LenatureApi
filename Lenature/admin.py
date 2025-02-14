from django.contrib import admin
from .models import Product, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'status', 'category', 'type', 'image']
    list_filter = ['status', 'type']
    search_fields = ['name']