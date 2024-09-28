from django.shortcuts import render
from ..models import Order



def home(request):
    template_name = 'core/home.html'

    if request.user.is_superuser:
        order_data = Order.objects.defer('id').order_by("-ordered_time")
    else:
        order_data = Order.objects.defer('id').filter(shop=request.user).order_by("-ordered_time")

    context = {'order': order_data}
    return render(request, template_name, context)