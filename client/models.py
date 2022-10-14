from django.db import models
# from dogovor.models import Dogovor
from invoices.models import Invoices
# Create your models here.

CATEGORY_CHOICE = (
    ("делает самостоятельно", "Делает самостоятельно"),
    ("делаем мы", "Оформить с нашими туристами"),
)


class Client(models.Model):
    fio_tourist = models.CharField(max_length=255, verbose_name='ФИО туриста')
    fio_tourist_lat = models.CharField(max_length=255, blank=True, null=True, verbose_name='ФИО туриста латиницей')

    passport = models.CharField(max_length=15, verbose_name='Паспорт')
    passport_id = models.CharField(max_length=19, blank=True, null=True, verbose_name='Идентификационный номер')
    place_issue = models.CharField(max_length=255, blank=True, null=True, verbose_name='Орган выдавший паспорт')
    date_passport_issue = models.DateField(blank=True, null=True, verbose_name='Дата выдачи паспорт')
    date_passport_exp = models.DateField(blank=True, null=True, verbose_name='Срок действия')

    date_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    insurance = models.CharField(max_length=100, choices=CATEGORY_CHOICE, default='делает самостоятельно', verbose_name='страховка')
    registration = models.CharField(max_length=255, blank=True, null=True, verbose_name='Прописка')
    email = models.EmailField(blank=True)

    # dog = models.ManyToManyField(Dogovor, default=None, verbose_name='договора')
    invoice = models.ForeignKey(Invoices, on_delete=models.SET_NULL, default=None, null=True, verbose_name='счета')

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fio_tourist

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = 'клиенты'
        ordering = ["-date_created"]