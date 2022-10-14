from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

from agency.models import Agency
from tours.models import Tours, TourDayQuota
# from client.models import Client


# Create your models here.

class Invoices(models.Model):
    slug = models.SlugField(default='', blank=True, verbose_name="Номер счета")
    agency = models.ForeignKey(Agency, null=True, on_delete=models.PROTECT, verbose_name="Агент", related_name='invoices')
    tour = models.ForeignKey(Tours, null=True, on_delete=models.PROTECT, verbose_name="Название тура")
    # client = models.ForeignKey(Client, verbose_name="Туристы")
    dates = models.ForeignKey(TourDayQuota, null=True, on_delete=models.PROTECT, verbose_name="Даты тура")
    paid = models.BooleanField(default=False, verbose_name="Оплачен?")
    tourists_qouta = models.IntegerField(blank=True, null=True, verbose_name="Количество туристов")
    ammount_to_pay = models.FloatField(blank=True, null=True, verbose_name="Итого к оплате")

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'
        ordering = ["-timestamp", "-updated"]


# def pre_save_receiver_page_model(sender, instance, *args, **kwargs):
#     if instance.slug == 'page-slug' or instance.slug == '':
#         instance.slug = unique_slug_generator(instance)
#
#
# pre_save.connect(pre_save_receiver_page_model, sender=Invoices)
