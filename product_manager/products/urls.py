from django.urls import path
from . import views
from .views import ProductListView, SupplierProductListView, BuyerProductListView

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('supplier/products/', views.SupplierProductListView.as_view(), name='supplier_product_list'),
    path('buyer/products/', views.BuyerProductListView.as_view(), name='buyer_product_list'),
]
