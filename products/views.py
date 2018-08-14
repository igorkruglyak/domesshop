from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models import *
from products.models import *


def catalog(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, "products/catalog.html", locals())



def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product.html', {'product': product})
