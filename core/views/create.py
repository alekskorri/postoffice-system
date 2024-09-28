from django.shortcuts import render, redirect
from ..forms import OrderForm
from django.contrib import messages
from django.db import transaction
from django.utils import timezone


def create(request):
    template_name = 'core/create.html'

    if request.method == 'POST':
        form_order = OrderForm(request.POST, request.FILES)
        if form_order.is_valid():
            try:
                with transaction.atomic():
                    create_package = form_order.save(commit=False)
                    create_package.shop = request.user
                    create_package.save()

                    messages.success(request, 'The Package is created successfully')
                    return redirect('home')
            except Exception as e:
                messages.error(request, f'Failed to create: {str(e)}')
        else:
            messages.error(request, 'Error during creating the object')

    else:
        form_order = OrderForm()

    context = {'form': form_order}

    return render(request, template_name, context)
