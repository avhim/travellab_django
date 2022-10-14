from django.db import models
from django.urls import reverse

from client.models import Client
from managers.models import Manager
from tours.models import Tours
# Create your models here.


class Dogovor(models.Model):
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Manager, on_delete=models.PROTECT, verbose_name="Менеджер")
    tour = models.ForeignKey(Tours, default=None, on_delete=models.PROTECT, verbose_name="Тур")

    def get_absolute_url(self):
        return reverse('dogovor-detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = "договор"
        verbose_name_plural = 'договоры'
        ordering = ["-timestamp", "-updated"]


class DogClients(models.Model):
    dog = models.ForeignKey(Dogovor, default=None, on_delete=models.PROTECT, related_name='client')
    client = models.ForeignKey(Client, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return self.client.fio_tourist


    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = 'клиенты'
