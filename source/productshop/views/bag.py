from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView

from productshop.models import ProductInBag, Product


class BagListView(ListView):
    template_name = 'bag/bag_list_view.html'
    model = ProductInBag
    context_object_name = 'products_in_bag'


class BagAddView(View):

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        product_in_bag = ProductInBag.objects.filter(product_id=product.pk)
        if product_in_bag:
            product_in_bag[0].amount += 1
            product_in_bag[0].save()
        else:
            ProductInBag.objects.create(product_id=self.kwargs.get('pk'), amount=1)
        return redirect('products_list_view')


class BagDeleteView(DeleteView):
    model = ProductInBag
    success_url = reverse_lazy('products_in_bag')
    context_object_name = 'product'




