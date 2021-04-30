from django.urls import path
from . import handlers

urlpatterns = [path("Add-To-Cart", handlers.add_to_cart_handler)]
