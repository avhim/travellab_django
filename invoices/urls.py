from django.urls import path
from .views import InvoiceDetailView, zayavka_create_view


urlpatterns = [
    path('zayavka/<int:id>', zayavka_create_view, name='invoice-zayavka'), #path('zayavka/<int:id>', zayavka_create_view, name='invoice-zayavka'),
    path('<slug>/', InvoiceDetailView.as_view(), name='invoice-detail'),
]