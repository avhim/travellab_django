from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, ListView, DetailView
from .models import Dogovor, DogClients


class DogovorDetailView(DetailView):
    template_name = 'documents/tourist_doc.html'
    model = Dogovor

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DogovorDetailView, self).get_context_data(**kwargs)
        print(context)
        # Add in a QuerySet
        context['client'] = DogClients.objects.all()
        context['total_price'] = len(context['client'])*context['dogovor'].tour.price
        context['total_service_price'] = len(context['client'])*context['dogovor'].tour.service_price
        return context




# class DogovorCreateView(LoginRequiredMixin, CreateView):
#     model = Dogovor
#     fields = ['__all__']
#     template_name = "documents/dogovor_form.html"
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class DogovorUpdateView(LoginRequiredMixin, UpdateView):
#     model = Dogovor
#     fields = ['__all__']
#
#
# class DogovorDeleteView(LoginRequiredMixin, DeleteView):
#     model = Dogovor
#     success_url = reverse_lazy('dogovor-list')