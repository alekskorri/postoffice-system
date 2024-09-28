from django.urls import path
from .views import custom_login, custom_logout, custom_register


urlpatterns = [
    path('', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', custom_register, name='register'),
]