from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
        error_messages = {
            "name": {
                "required": "The field is required to be filled"
            }
        }


