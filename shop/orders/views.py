from django.shortcuts import render
from django.views.generic import FormView, DetailView
from .models import *
from .forms import OrderCreateForm
from cart.cart import Cart
from mainapp.models import Category
import smtplib


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
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        massage = OrderItem.objects.all()[0]
        address = str(order.email)
        send_email(order, massage, address)
        cart.clear()
        categories = Category.objects.all()
        return render(request, 'order_created.html', {'order': order, 'categories': categories})


def send_email(order, massage, address):
    sender = "testformassege@gmail.com"
    password = 'rlezrhekthsrclex'
    massage_order = f"Your {order} success"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, address, f"Subject: Your order in shop\n{massage_order}\n{massage}")
    except Exception as _ex:
        print('error')
        return f"{_ex}\nCheck your login or password!"
