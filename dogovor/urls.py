from django.urls import path
from .views import DogovorDetailView


urlpatterns = [
    path('<int:pk>/', DogovorDetailView.as_view(), name='dogovor-detail'),
]