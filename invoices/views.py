from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView

from django.shortcuts import render, redirect
from .forms import ClientFormSet
from .models import Invoices
from .utils import unique_slug_generator

from agency.models import Agency
from client.models import Client
from tours.models import TourDayQuota

from datetime import date
from dateutil.relativedelta import relativedelta
# Create your views here.


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoices
    paginate_by = 10


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    template_name = 'invoices/invoice.html'
    model = Invoices


def zayavka_create_view(request, id):
    if request.user.is_authenticated:
        agency = Agency.objects.get(user=request.user)
    else:
        agency = Agency.objects.none()
    tourdayqouta = TourDayQuota.objects.get(id=id)
    formset = ClientFormSet(queryset=Client.objects.none())
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
            kids = 0
            adult = 0
            for c in client:
                c.invoice = invoice
                if c.date_birth > date.today()-relativedelta(years=16):
                    kids += 1
                else:
                    adult += 1
            invoice.tourists_qouta_child = kids
            invoice.tourists_qouta_adult = adult
            if tourdayqouta.tour.service_price:
                total = tourdayqouta.tour.service_price*adult + tourdayqouta.tour.service_price_child*kids
            else:
                total = tourdayqouta.price_adult * adult + tourdayqouta.price_child * kids
            invoice.ammount_total = total
            invoice.comission = tourdayqouta.tour.comission/100 * total
            invoice.ammount_to_pay = total - invoice.comission
            invoice.save()
            formset.save()
            context['messages'] = 'Заявка №{} создана'.format(invoice.slug)
            return render(request, 'invoices/zayavka.html', context)
    return render(request, 'invoices/zayavka.html', context)
