from django.urls import path

from productshop.views import ProductsListView, ProductDetailedView

urlpatterns = [
            path("", ProductsListView.as_view(), name="products_list"),
            path("product/<int:pk>/details", ProductDetailedView.as_view(), name='detailed_view'),
            # path("delete/<int:pk>/", delete_view, name="delete_view"),
            # path("create/", create_view, name="create_view"),
            # path("edit/<int:pk>/", edit_view, name="edit_view")
]