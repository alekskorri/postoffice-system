from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.home import home
from .views.info import info
from .views.edit import edit
from .views.delete import delete
from .views.create import create
from .views.sent_packages import sent_packages, mark_order_sent
from .views.cancelled_packages import cancelled_packages, mark_order_cancelled

urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('sent_packages/', sent_packages, name="sent_packages"),
    path('order/<id>/sent/', mark_order_sent, name="mark_order_sent"),
    path('cancelled_packages/', cancelled_packages, name="cancelled_packages"),
    path('order/<id>/cancelled/', mark_order_cancelled, name="mark_order_cancelled"),
    path('info/<id>', info, name="info"),
    path('edit/<id>', edit, name="edit"),
    path('delete/<id>', delete, name="delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
