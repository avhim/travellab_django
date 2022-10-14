from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView

from django.shortcuts import render, redirect
from .forms import ClientFormSet
from .models import Invoices
from .utils import unique_slug_generator

from agency.models import Agency
from client.models import Client
from tours.models import TourDayQuota

# Create your views here.


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoices
    paginate_by = 10


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    template_name = 'invoices/invoice.html'
    model = Invoices


def zayavka_create_view(request, id):
    tourdayqouta = TourDayQuota.objects.get(id=id)
    formset = ClientFormSet(queryset=Client.objects.none())
    agency = Agency.objects.get(user=request.user)
    context = {
        "formset": formset,
        "tour": tourdayqouta.tour,
        "tour_date": tourdayqouta.tour_date,
        "agency": agency,
    }

    if request.method == 'POST':
        formset = ClientFormSet(request.POST)
        if formset.is_valid():
            client = formset.save(commit=False)
            invoice = Invoices.objects.create(slug=unique_slug_generator())
            invoice.agency = agency
            invoice.tour = tourdayqouta.tour
            invoice.dates = tourdayqouta
            invoice.tourists_qouta = len(client)
            invoice.save()
            for c in client:
                c.invoice = invoice
            formset.save()
            context['messages'] = 'Заявка №{} создана'.format(invoice.slug)
            return render(request, 'invoices/zayavka.html', context)
    return render(request, 'invoices/zayavka.html', context)


# class ZayvkaAddView(TemplateView):
#     template_name = 'invoices/zayavka.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tdq = TourDayQuota.objects.get(id=kwargs['id'])
#         context['tour_date'] = tdq.tour_date
#         context['tour'] = tdq.tour
#         return context
#
#     def get(self, *args, **kwargs):
#         # Create an instance of the formset
#         context = super().get_context_data(**kwargs)
#         context['formset'] = ClientFormSet(queryset=Client.objects.none())
#         tdq = TourDayQuota.objects.get(id=kwargs['id'])
#         context['tour_date'] = tdq.tour_date
#         context['tour'] = tdq.tour
#         return self.render_to_response(context)
#
#     def post(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         formset = ClientFormSet(data=self.request.POST)
#
#         # Check if submitted forms are valid
#         if formset.is_valid():
#             formset.save(commit=False)
#             invoice = Invoices.objects.create(slug=unique_slug_generator())
#             invoice.agency = Agency.objects.get(user=self.request.user)
#             invoice.dates = TourDayQuota.objects.get(kwargs['id'])
#             invoice.tour = invoice.dates.tour
#             invoice.save()
#             formset.save()
#             message = 'Заявка №{} создана'.format(invoice)
#             return self.render_to_response({'messages': message})
#         print(self.request.POST)
#         return self.render_to_response({'formset': formset})