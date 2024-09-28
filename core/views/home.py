from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import Order


def home(request):
    template_name = 'core/home.html'
    shops = User.objects.all()

    if request.user.is_superuser:
        selected_shop = request.GET.get('shop')
        if selected_shop:
            order_data = Order.objects.defer('id').filter(shop_id=selected_shop).order_by("-ordered_time")
        else:
            order_data = Order.objects.defer('id').order_by("-ordered_time")
    else:
        order_data = Order.objects.defer('id').filter(shop=request.user).order_by("-ordered_time")

    paginator = Paginator(order_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'shops': shops, 'page_obj': page_obj}
    return render(request, template_name, context)