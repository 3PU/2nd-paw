from django.shortcuts import render
from .models import Product

"""Displays all products"""
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

"""Displays cat products"""
def products_animal_cat(request):
    products = Product.objects.filter(animal="Cat")
    return render(request, "products.html", {"products": products})

"""Displays dog products"""
def products_animal_dog(request):
    products = Product.objects.filter(animal="Dog")
    return render(request, "products.html", {"products": products})

"""Displays clothes category"""
def products_category_clothes(request):
    products = Product.objects.filter(category="Clothes")
    return render(request, "products.html", {"products": products})

"""Displays toys category"""
def products_category_toys(request):
    products = Product.objects.filter(category="Toys")
    return render(request, "products.html", {"products": products})

"""Displays supply category"""
def products_category_supplies(request):
    products = Product.objects.filter(category="Supplies")
    return render(request, "products.html", {"products": products})