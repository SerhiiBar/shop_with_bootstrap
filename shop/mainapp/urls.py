from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='mainpage'),
    path('product/<slug:product_slug>/', ProductView.as_view(), name='product_detail'),
    path('category/<slug:category_slug>/', CategoryView.as_view(), name='category'),
]
