from django.urls import path
from .views import product_list, order_create

urlpatterns = [
    path('', product_list, name='product_list'),
    path('order/create/<int:product_id>/', order_create, name='order_create'),

]