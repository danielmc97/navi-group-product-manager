from django.contrib import admin
from .models import Supplier, Product
# , ProductImage

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'stock_status', 'supplier')
    list_filter = ('stock_status', 'supplier')
    search_fields = ('name', 'code')

# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ('product', 'is_main')
