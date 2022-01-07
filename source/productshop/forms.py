from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
        error_messages={
            "name": {
                "required": "Поле обязательно для заполнения"
            }
        }

