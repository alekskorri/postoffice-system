from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from ..models import SentPackages
from django.contrib import messages


def order_calculations(request):
    template_name = 'core/order_calculations.html'
    shops = User.objects.all()

    if request.user.is_superuser:
        selected_shop = request.GET.get('shop')
        if selected_shop:
            orders = SentPackages.objects.filter(shop_id=selected_shop).order_by("-date_sent")
        else:
            orders = SentPackages.objects.order_by("-date_sent")
    else:
        orders = SentPackages.objects.filter(shop=request.user).order_by("-date_sent")

    selected_orders = request.session.get('selected_orders', [])

    if request.method == 'POST':
        selected_order_id = request.POST.get('select_order')
        remove_order_id = request.POST.get('remove_order')
        remove_all = request.POST.get('remove_all')

        if selected_order_id:
            if selected_order_id not in selected_orders:
                selected_orders.append(selected_order_id)
            else:
                messages.info(request, 'The Order is already selected!')

        elif remove_order_id and remove_order_id in selected_orders:
            selected_orders.remove(remove_order_id)

        elif remove_all == 'true':
            selected_orders.clear()

        request.session['selected_orders'] = selected_orders
        request.session.modified = True
        return redirect('order_calculations')

    selected_orders_objs = SentPackages.objects.filter(id__in=selected_orders).order_by("-date_sent")
    total_sum = sum(order.total for order in selected_orders_objs)
    total_shipment_value = sum(order.shipment_value for order in selected_orders_objs)
    total_price = sum(order.price for order in selected_orders_objs)

    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'selected_orders_objs': selected_orders_objs,
        'total_sum': total_sum,
        'total_shipment_value': total_shipment_value,
        'total_price': total_price,
        'shops': shops,
    }
    return render(request, template_name, context)
