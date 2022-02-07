from django.urls import path

from productshop.views import ProductsListView, ProductDetailedView, ProductDeleteView, ProductCreateView, \
    ProductUpdateView
from productshop.views.bag import BagListView, BagAddView, BagDeleteView
from productshop.views.order import Makeorder

urlpatterns = [
            path("", ProductsListView.as_view(), name="products_list_view"),
            path("product/<int:pk>/details", ProductDetailedView.as_view(), name='product_detailed_view'),
            path("product/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete_view"),
            path("product/create", ProductCreateView.as_view(), name="product_create_view"),
            path("product/<int:pk>/edit", ProductUpdateView.as_view(), name="product_edit_view"),
            path('bag/', BagListView.as_view(), name='products_in_bag'),
            path('bag/<int:pk>/add/', BagAddView.as_view(), name='bag_add_view'),
            path('bag/<int:pk>/delete/', BagDeleteView.as_view(), name="product_in_bag_delete_view"),
            path('make/order/', Makeorder.as_view(), name='makeorder'),
]