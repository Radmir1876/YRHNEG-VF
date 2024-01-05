from django.contrib import admin
from .models import Manufacturer, Category, Product, Order

admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)

