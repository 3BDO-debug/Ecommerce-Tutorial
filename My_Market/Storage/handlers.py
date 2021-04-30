from django.shortcuts import redirect
from . import models

# Create your views here.


def add_to_cart_handler(request):
    product_to_be_added = models.Product.objects.get(
        id=int(request.GET.get("product_id"))
    )
    just_created_cart = models.Cart.objects.create(total_price=0.00)
    just_created_cart.products.add(product_to_be_added.id)

    just_created_cart.total_price = product_to_be_added.product_price
    just_created_cart.save()
    return redirect("/")
