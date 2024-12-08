
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, TypeProduct


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        types = TypeProduct.objects.all()
        products_phone = products.filter(type=1)
        products_electronic = products.filter(type=2)
        products_accessory = products.filter(type=3)
        context = {
            "products": products,
            "products_phone": products_phone,
            "products_electronic": products_electronic,
            "products_accessory": products_accessory
        }
        return render(request, "main/index.html", context=context)
