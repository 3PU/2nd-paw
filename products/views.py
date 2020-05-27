from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.contrib import messages
from .forms import CreateProductForm
from django.contrib.auth.decorators import login_required
import sweetify


def all_products(request):
    """Displays all products"""
    products = Product.objects.all().exclude(
        title__contains="Monetary Donation")
    return render(request, "products.html", {"products": products})


def products_animal_cat(request):
    """Displays cat products"""
    products = Product.objects.filter(animal="Cat").exclude(
        title__contains="Monetary Donation")
    return render(request, "products.html", {"products": products})


def products_animal_dog(request):
    """Displays dog products"""
    products = Product.objects.filter(animal="Dog").exclude(
        title__contains="Monetary Donation")
    return render(request, "products.html", {"products": products})


def products_category_clothes(request):
    """Displays clothes category"""
    products = Product.objects.filter(category="Clothes").exclude(
        title__contains="Monetary Donation")
    return render(request, "products.html", {"products": products})


def products_category_toys(request):
    """Displays toys category"""
    products = Product.objects.filter(category="Toys").exclude(
        title__contains="Monetary Donation")
    return render(request, "products.html", {"products": products})


def products_category_supplies(request):
    """Displays supply category"""
    products = Product.objects.filter(category="Supplies").exclude(
        title__contains="Monetary Donation")
    return render(request, "products.html", {"products": products})


def make_donation(request):
    """Displays all products"""
    donations = Product.objects.filter(description__contains="zT5M#B")
    return render(request, "donation.html", {"donations": donations})


@login_required
def donate_product(request, pk=None):
    """Allows user to donate/create a product"""
    if request.method == "POST":
        product_form = CreateProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            product_form.save()
            sweetify.sweetalert(
                request,
                """Thank you for your contribution.
                Your product has been added to the shop!""",
                icon="success"
            )
            return redirect("all_products")

        else:
            sweetify.sweetalert(
                request,
                """We could not submit your donation.
                Make sure you enter a correct price
                between 2€-100€.""",
                icon="error"
            )
            product_form = CreateProductForm()

    else:
        product_form = CreateProductForm()

    return render(
        request,
        "create_product.html",
        {'product_form': product_form}
    )


def product_detail(request, id):
    products = get_object_or_404(Product, id=id)
    return render(request, "product_detail.html", {'product': products})
