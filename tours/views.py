from django.views.generic import TemplateView, ListView, DetailView
from client.forms import ClientForm
from .models import Tours, TourDayQuota, CategoryTour
from datetime import date
from django.db.models import Count


class HomeView(ListView):
    model = Tours
    template_name = 'home.html'
    paginate_by = 10
    queryset = Tours.objects.filter(active=True)

# context for extra models
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = CategoryTour.objects.all()

        context['categories'] = CategoryTour.objects.filter(tours__active=True).annotate(cnt=Count('tours')).filter(cnt__gt=0)
        return context


class CategoryTourListView(ListView):
    model = Tours
    template_name = 'tours/tours-list.html'

    def get_queryset(self, **kwargs):
        queryset = Tours.objects.filter(category__id=self.kwargs['category_id'], active=True)
        return queryset


# Create your views here.
class TourDetailView(DetailView):
    model = Tours
    template_name = 'tours/tour-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tdq'] = TourDayQuota.objects.filter(tour__slug=self.kwargs['slug'], active=True, tour_date__gte=date.today())
        return context


# class TourListView(ListView):
#     model = Tours
#     template_name = 'tour/tours-list.html'
#     queryset = Tours.objects.filter(active=True)
#     paginate_by = 10
