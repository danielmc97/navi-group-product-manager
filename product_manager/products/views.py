# products/views.py

from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(stock_status='in_stock')

class SupplierProductListView(ListView):
    model = Product
    template_name = 'products/supplier_product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, 'supplier'):
            return Product.objects.filter(supplier=user.supplier)
        return Product.objects.none()

class BuyerProductListView(ListView):
    model = Product
    template_name = 'products/buyer_product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(stock_status='in_stock')
