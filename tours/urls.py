from django.urls import path
from .views import TourDetailView, CategoryTourListView


urlpatterns = [
    path('category/<int:category_id>', CategoryTourListView.as_view(), name='category-view'),
    path('<slug>/', TourDetailView.as_view(), name='tour-detail'),
]