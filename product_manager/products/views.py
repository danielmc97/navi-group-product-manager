# products/views.py

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Product
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# login functionality
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name='Buyer').exists():
            return '/products/buyer/products/'
        else:
            return '/products/'  # Redirect to a default view if not a Buyer
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

class SupplierProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/supplier_product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, 'supplier'):
            return Product.objects.filter(supplier=user.supplier)
        return Product.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['products']
        
        if products.exists():
            min_price = products.order_by('price').first().price
            cheaper_analogues = Product.objects.filter(price__lt=min_price)
        else:
            cheaper_analogues = Product.objects.none()
        
        context['cheaper_analogues'] = cheaper_analogues
        return context
    
class BuyerProductListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Product
    template_name = 'products/buyer_product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(stock_status='in_stock')

    def test_func(self):
        return self.request.user.groups.filter(name='Buyer').exists()
    