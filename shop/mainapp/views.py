from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from cart.forms import *


class MainPage(ListView):
    paginate_by = 8
    model = Product
    template_name = 'productlist.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(available=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cart_product_form'] = CartAddProductForm()
        return context


class CategoryView(ListView):
    paginate_by = 8
    model = Product
    template_name = 'productlist.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context
