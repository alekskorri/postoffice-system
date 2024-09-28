from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from ..models import CancelledPackages, Order


def cancelled_packages(request):
    template_name = 'core/cancelled_packages.html'

    shops = User.objects.all()

    if request.user.is_superuser:
        selected_shop = request.GET.get('shop')
        if selected_shop:
            cancelled_orders = CancelledPackages.objects.filter(shop_id=selected_shop).order_by("-date_cancelled")
        else:
            cancelled_orders = CancelledPackages.objects.order_by("-date_cancelled")
    else:
        cancelled_orders = CancelledPackages.objects.filter(shop=request.user).order_by("-date_cancelled")

    paginator = Paginator(cancelled_orders, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'shops': shops}
    return render(request, template_name, context)


def mark_order_cancelled(request, id):
    order = get_object_or_404(Order, id=id)

    CancelledPackages.objects.create(
        shop=order.shop,
        product=order.product,
        price=order.price,
        shipment_value=order.shipment_value,
        total=order.total,
        client=order.client,
        address=order.address,
        phone_number=order.phone_number,
        ordered_time=order.ordered_time,
        image=order.image,
    )

    order.delete()

    return redirect('/core')
