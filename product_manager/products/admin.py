from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Supplier, Product, User
# , ProductImage

# 
# class UserAdmin(DjangoUserAdmin):
#     model = User
# admin.site.register(User, UserAdmin)

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
