from django.shortcuts import render
from django.db.models import Count
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.

from .models import Hotel


class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels/hotels-list.html'
    paginate_by = 10
    queryset = Hotel.objects.filter(active=True)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['reviews'] = Hotel.objects.filter(slug=kwargs['slug']).annotate(cnt=Count('tours')).filter(cnt__gt=0)
    #     return context


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotels/hotel-detail-view.html'
