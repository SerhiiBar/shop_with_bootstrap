import threading

from django.shortcuts import render
from django.views.generic import FormView, DetailView
from .models import *
from .forms import OrderCreateForm
from cart.cart import Cart
from mainapp.models import Category
from .sendmessage import start_send_my_message
# from .sendmessage import send_email
import asyncio


class OrderView(FormView):
    template_name = 'order_creation.html'
    form_class = OrderCreateForm
    success_url = 'order_created/'

    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'order_creation.html', {'categories': categories, 'form': self.form_class})

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreatedView(DetailView):

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        order = Order.objects.all()[0]
        msg = []
        categories = Category.objects.all()
        for item in cart:
            new_order = OrderItem.objects.create(order=order,
                                                 product=item['product'],
                                                 price=item['price'],
                                                 quantity=item['quantity'])
            msg.append((item['product'], item['price'], item['quantity']))
            new_order.update_stock()

        msg = str(msg)
        address = str(order.email)
        try:
            print('Sending email...')
            threading.Thread(target=start_send_my_message, args=(order, msg, address)).start()
            # send_email(order, address, msg)
            print('Email sent!')
            cart.clear()
            return render(request, 'order_created.html', {'order': order, 'categories': categories})

        except Exception as e:
            print('Error:', e)
