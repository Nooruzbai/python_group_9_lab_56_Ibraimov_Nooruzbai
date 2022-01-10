from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import CHOICES
from .models import Product
from productshop.forms import ProductForm


# Create your views here.

def index_view(request):
    products = Product.objects.filter(remainder__gte=1).order_by('category', 'name')
    return render(request, 'index.html', {"products": products})


def detailed_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product Not Found")
    return render(request, 'detailed_view.html', {'product': product})


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, "delete_product.html", {'product': product})
    else:
        product.delete()
        return redirect("index")


def create_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "create_product.html", {'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            new_product = form.save()
            return redirect('index')
        return render(request, 'create_product.html', {'form': form})


def edit_view(request, pk):
    products = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': products.name,
            'description': products.description,
            'category': products.category,
            'remainder': products.remainder,
            "price": products.price
        })
        return render(request, 'edit_view.html', {'products': products, 'form': form, 'choices': CHOICES})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            products.name = form.cleaned_data.get('name')
            products.description = form.cleaned_data.get('description')
            products.category = form.cleaned_data.get('category')
            products.remainder = form.cleaned_data.get('remainder')
            products.price = form.cleaned_data.get('price')
            products.save()
            return redirect('index')
        return render(request, 'edit_view.html', {'products': products, 'form': form, 'choices': CHOICES})


