from django.shortcuts import render, get_object_or_404
from ..models import Order, SentPackages, CancelledPackages


def info(request, id):
    template_name = 'core/info.html'

    order = Order.objects.filter(id=id).first()

    if order is None:
        order = SentPackages.objects.filter(id=id).first()

    if order is None:
        order = CancelledPackages.objects.filter(id=id).first()

    context = {'order': order}
    return render(request, template_name, context)
