from django import forms
from django.core.exceptions import ValidationError

from .models import Product, Order


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
        error_messages = {
            "name": {
                "required": "The field is required to be filled"
            }
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label='Search')


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = "__all__"
        error_messages = {
            "name": {
                "required": "The field is required to be filled"
            }
        }


