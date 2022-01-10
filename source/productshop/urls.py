from django.urls import path

from productshop.views import index_view, detailed_view, delete_view, create_view, edit_view

urlpatterns = [
            path("", index_view, name="index"),
            path("details/<int:pk>/", detailed_view, name='detailed_view'),
            path("delete/<int:pk>/", delete_view, name="delete_view"),
            path("create/", create_view, name="create_view"),
            path("edit/<int:pk>/", edit_view, name="edit_view")
]