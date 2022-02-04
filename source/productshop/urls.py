from django.urls import path

from productshop.views import ProductsListView, ProductDetailedView, ProductDeleteView, ProductCreateView, \
    ProductUpdateView

urlpatterns = [
            path("", ProductsListView.as_view(), name="products_list_view"),
            path("product/<int:pk>/details", ProductDetailedView.as_view(), name='product_detailed_view'),
            path("product/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete_view"),
            path("product/create", ProductCreateView.as_view(), name="product_create_view"),
            path("product/<int:pk>/edit", ProductUpdateView.as_view(), name="product_edit_view")
]