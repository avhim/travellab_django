from django.urls import path
from .views import AgencyDetailView

urlpatterns = [
    path('profile/', AgencyDetailView.as_view(), name='agency-profile'),
]