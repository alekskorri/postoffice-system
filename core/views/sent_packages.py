from django.shortcuts import render, redirect, get_object_or_404
from ..models import SentPackages, Order


def sent_packages(request):
    template_name = 'core/sent_packages.html'

    if request.user.is_superuser:
        sent_orders = SentPackages.objects.order_by("-date_sent")
    else:
        sent_orders = SentPackages.objects.filter(shop=request.user).order_by("-date_sent")

    context = {'sent_orders': sent_orders}
    return render(request, template_name, context)


def mark_order_sent(request, id):
    order = get_object_or_404(Order, id=id)

    SentPackages.objects.create(
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

    return redirect('sent_packages')
