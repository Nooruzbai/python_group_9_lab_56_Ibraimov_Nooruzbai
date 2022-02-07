from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView

from productshop.models import ProductInBag, Product


class BagListView(ListView):
    template_name = 'bag/bag_list_view.html'
    model = ProductInBag
    context_object_name = 'products_in_bag'


class BagAddView(View):

    def post(self, request, *args, **kwargs):
        print(self.kwargs.get('pk'))
        # product_pk = request.POST.get('pk')
        product = get_object_or_404(Product, pk=kwargs['pk'])
        print(product)
        product_in_bag = ProductInBag.objects.filter(product_id=product.pk)
        print(product_in_bag)
        if product_in_bag:
            product_in_bag[0].amount += 1
            product_in_bag[0].save()
        else:
            ProductInBag.objects.create(product_id=self.kwargs.get('pk'), amount=1)
        return redirect('products_list_view')


        # print(bag)
        # return redirect('products_list_view')

    # def get_context_data(self, **kwargs):
    #
#
    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context['form'] = SearchForm()
    #         if self.search_value:
    #             context['form'] = SearchForm(initial={"search": self.search_value})
    #             context['search'] = self.search_value
    #         return context

#
# class BagDeleteView(DeleteView):
