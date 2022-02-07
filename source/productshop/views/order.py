from django.shortcuts import redirect
from django.views import View

from productshop.models import Order, ProductInBag, Product, ProductOrder


class Makeorder(View):

    def post(self, request, *args, **kwargs):
        kwargs = request.POST
        bag = ProductInBag.objects.all()
        order = Order.objects.create(username=kwargs['username'], phone_number=kwargs['phone_number'], address=kwargs['address'])
        for item in bag:
            product_ordered = ProductOrder.objects.create(order=order, product=item.product, amount=item.amount)
            item.delete()
        return redirect('products_list_view')