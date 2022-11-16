from django.shortcuts import render
from django.views.generic import FormView, DetailView
from .models import *
from .forms import OrderCreateForm
from cart.cart import Cart
from mainapp.models import Category


class OrderView(FormView):
    template_name = 'order_creation.html'
    form_class = OrderCreateForm
    success_url = 'order_created/'

    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'order_creation.html', {'categories': categories, 'form': self.form_class})

    def form_valid(self, form):
        form.save()
        form.send_email()
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
        cart.clear()
        categories = Category.objects.all()
        return render(request, 'order_created.html', {'order': order, 'categories': categories})
