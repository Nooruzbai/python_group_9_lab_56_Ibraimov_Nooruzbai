from django.contrib import admin
from productshop.models import Product, ProductInBag


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'remainder', 'price']


class ProductInBagAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInBag, ProductInBagAdmin)

