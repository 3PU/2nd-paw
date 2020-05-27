from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe
import sweetify

stripe.api_key = settings.STRIPE_SECRET


def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get("cart", {})
            total = 0

            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data["stripe_id"],
                )

            except stripe.error.CardError:
                sweetify.sweetalert(request,
                                    "Your card was declined!",
                                    icon="error")

            if customer.paid:
                sweetify.sweetalert(request,
                                    """"Your order has been placed.
                                    You will receive an order
                                    confirmation via email shortly!""",
                                    icon="success")
                request.session["cart"] = {}
                return redirect(reverse("index"))

            else:
                sweetify.sweetalert(request,
                                    "Unable to process payment!",
                                    icon="error")

        else:
            print(payment_form.errors)
            sweetify.sweetalert(request,
                                """We were unable to process the
                                payment with that card!""",
                                icon="error")

    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(
        request, "checkout.html",
        {
            "order_form": order_form,
            "payment_form": payment_form,
            "publishable": settings.STRIPE_PUBLISHABLE
        }
    )
