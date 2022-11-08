from django.shortcuts import render
from django.views.generic import FormView, DetailView
from .models import *
from .forms import OrderCreateForm
from cart.cart import Cart


class OrderView(FormView):
    template_name = 'order_creation.html'
    form_class = OrderCreateForm
    success_url = 'order_created/'

    def form_valid(self, form):
        order = form.save()
        form.send_email()
        return super().form_valid(form)


class CreatedView(DetailView):

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        order = Order(request)
        return render(request, 'order_created.html', {'order': order})
