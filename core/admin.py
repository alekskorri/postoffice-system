from django.contrib import admin
from .models import Order


class AdminOrders(admin.ModelAdmin):
    list_display = [
        'product', 'price', 'shipment_value', 'total', 'client', 'address', 'phone_number', 'ordered_time',
    ]


admin.site.register(Order, AdminOrders)

