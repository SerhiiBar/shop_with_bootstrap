from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', OrderView.as_view(), name='order_creation'),
    path('order_created/', CreatedView.as_view(), name='order_created'),
    ]
