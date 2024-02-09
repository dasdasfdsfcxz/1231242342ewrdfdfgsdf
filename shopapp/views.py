from django.shortcuts import render
from .models import Product
from django.http import HttpRequest


def main(request: HttpRequest):
    all_products = Product.objects.all()
    context = {"all_products" : all_products}
    return render (request, "shopapp/index.html", context)