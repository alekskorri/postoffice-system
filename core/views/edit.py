from django.shortcuts import render, get_object_or_404, redirect
from ..models import Order
from ..forms import OrderForm
from django.contrib import messages
from django.db import transaction


def edit(request, id):
    template_name = 'core/edit.html'

    obj = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=obj)

        if form.is_valid():
            try:
                with transaction.atomic():
                    package = form.save(commit=False)
                    package.save()
                messages.success(request, 'The record is updated successfully')
                return redirect('home')
            except Exception as e:
                messages.error(request, f'Failed to update: {str(e)}')
        else:
            messages.error(request, 'Failed to update...')

    else:
        form = OrderForm(instance=obj)

    context = {'form': form}
    return render(request, template_name, context)