from django.contrib import admin
from .models import Product, ProductVersion
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number')
