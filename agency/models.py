from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# class User(AbstractUser):
#     is_agency = models.BooleanField(default=False)
#     is_manager = models.BooleanField(default=False)

class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="agency")
    active = models.BooleanField(default=False, verbose_name="Активно")
    title = models.CharField(max_length=255, verbose_name="Название организации")
    unp = models.CharField(max_length=12, default="УНП", verbose_name="УНП")
    bank_name = models.CharField(max_length=32, default="Банк", verbose_name="Название банка")
    bank_bik = models.CharField(max_length=8, default="YYYYBY2X", verbose_name="Бик")
    bank_bill = models.CharField(max_length=34, default="BYXX YYYY XXXX XXXX XXXX XXXX XXXX", verbose_name="Банковский Счет")
    telephones = models.TextField(verbose_name="Телефон", default="Ваш телефон")
    # email = models.EmailField(unique=True, verbose_name="Емейл")
    address = models.TextField(verbose_name="Юр. адрес")
    notes = models.TextField(null=True, blank=True, verbose_name="Заметки")
    contract_number = models.CharField(max_length=32, null=True, blank=True, verbose_name="Номер договора")
    sign_date_contract = models.DateField(null=True, blank=True, verbose_name="Дата подписания")
    director = models.CharField(max_length=255, null=True, verbose_name="ФИО Директора")
    reason = models.CharField(max_length=255, null=True, verbose_name="На основании")

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('agency-profile', kwargs={'slug': self.user.username})

    class Meta:
        verbose_name = 'Агентство'
        verbose_name_plural = 'Агентства'
        ordering = ["-timestamp", "-updated"]


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = Agency(user=instance)
        profile.save()
