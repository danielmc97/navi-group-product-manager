# products/views.py

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Product
from django.contrib.auth.forms import AuthenticationForm
# from django.urls import reverse
# from django.urls import reverse_lazy 

#Login

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect(reverse('products:product_list'))
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})


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
