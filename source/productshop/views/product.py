from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from productshop.models import CHOICES
from productshop.models import Product
from productshop.forms import ProductForm


class ProductsListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products_list.html'
    paginate_by = 5
    paginate_orphans = 0
    ordering = ['name']


class ProductDetailedView(DetailView):
    template_name = 'products/details_product.html'
    model = Product
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/delete_product.html"
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('products_list')


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/create_product.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detailed_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    form_class = ProductForm
    template_name = "products/edit_product.html"
    model = Product

    def get_success_url(self):
        return reverse('products_list_view')


# def edit_view(request, pk):
#     products = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         form = ProductForm(initial={
#             'name': products.name,
#             'description': products.description,
#             'category': products.category,
#             'remainder': products.remainder,
#             "price": products.price
#         })
#         return render(request, 'products/edit_product.html', {'products': products, 'form': form, 'choices': CHOICES})
#     else:
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             products.name = form.cleaned_data.get('name')
#             products.description = form.cleaned_data.get('description')
#             products.category = form.cleaned_data.get('category')
#             products.remainder = form.cleaned_data.get('remainder')
#             products.price = form.cleaned_data.get('price')
#             products.save()
#             return redirect('index')
#         return render(request, 'products/edit_product.html', {'products': products, 'form': form, 'choices': CHOICES})


