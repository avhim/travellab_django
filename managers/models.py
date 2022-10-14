from django.db import models

# Create your models here.


class Manager(models.Model):
    fio = models.CharField(max_length=255)
    osnovanie = models.CharField(max_length=255)
    foto = models.ImageField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.fio