from django.shortcuts import render
from Storage import models as storage_model
# Create your views here.

def home_page(request):
    products = storage_model.Product.objects.all()
    newly_arrived_products =storage_model.Product.objects.filter(newly_arrived =True)
    most_wanted_products =storage_model.Product.objects.filter(most_wanted =True)
    best_seller_products =storage_model.Product.objects.filter(best_seller =True)
    return render(request, "HomePage.html" ,{"products": products , "most_wanted": most_wanted_products, "newly_arrived":newly_arrived_products, "best seller":best_seller_products})
    