from django.shortcuts import render, redirect, get_object_or_404
from ..models import CancelledPackages, Order


def cancelled_packages(request):
    template_name = 'core/cancelled_packages.html'

    if request.user.is_superuser:
        cancelled_orders = CancelledPackages.objects.order_by("-date_cancelled")
    else:
        cancelled_orders = CancelledPackages.objects.filter(shop=request.user).order_by("-date_cancelled")

    context = {'cancelled_orders': cancelled_orders}
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
        order_time=order.ordered_time,
        image=order.image,
    )

    order.delete()

    return redirect('cancelled_packages')
