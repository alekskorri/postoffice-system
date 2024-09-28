from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib import messages


def custom_register(request):
    template_name = 'accounts/register.html'

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, template_name, context)


def custom_login(request):
    template_name = 'accounts/login.html'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('home')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = AuthenticationForm()

    context = {'form_login': form}

    return render(request, template_name, context)


def custom_logout(request):
    template_name = 'accounts/logout.html'
    logout(request)
    messages.info(request, "Logged out successfully!")

    return render(request, template_name)
