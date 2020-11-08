from django.shortcuts import render, redirect
from .models import Order, Product


def index(request):
    context = {"all_products": Product.objects.all()}
    return render(request, "store/index.html", context)


def checkout(request):
    all_charges = 0
    num_of_items = 0
    for order in Order.objects.all():
        all_charges += order.total_price
        num_of_items += order.quantity_ordered
    context = {
        "num_of_orders": num_of_items,
        "total_charge": Order.objects.last().total_price,
        "all_charges": all_charges,
    }
    return render(request, "store/checkout.html", context)


def process(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("/checkout")
