from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from productshop.models import Product
from productshop.forms import ProductForm
from productshop.views.base import SearchView


class ProductsListView(SearchView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products_list.html'
    paginate_by = 10
    paginate_orphans = 0
    ordering = ['category', 'name']
    search_fields = ['name']
    #
    # products = Product.objects.filter(remainder__gte=1).order_by('category', 'name')
    # return render(request, 'products/products_list.html', {"products": products})


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
        return reverse('product_detailed_view', kwargs={'pk': self.object.pk})


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


