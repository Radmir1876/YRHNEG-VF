from django.shortcuts import render
from .models import Product, Order
from django.http import HttpResponse
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def order_create(request, product_id):
    if request.method == 'POST':
        return HttpResponse('OK')
        product = Product.objects.get(id=request.POST['product'])
        quantity = request.POST['quantity']
        total_cost = product.price * quantity
        customer_name = request.POST['customer_name']
        customer_phone = request.POST['customer_phone']
        order = Order.objects.create(product=product, quantity=quantity, total_cost=total_cost, customer_name=customer_name, customer_phone=customer_phone)
        return render(request, 'order_created.html', {'order': order})
    else:
        products = Product.objects.all()
# Create your views here.
