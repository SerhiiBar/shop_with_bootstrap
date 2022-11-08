from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('<product_id>', views.cart_add, name='cart_add'),
    path('<product_id>/', views.cart_remove, name='cart_remove'),
]
