from django.contrib import admin
from productshop.models import Product, ProductInBag, Order, ProductOrder


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'remainder', 'price']


class ProductInBagAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'address', 'date_created']


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'amount']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInBag, ProductInBagAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)

