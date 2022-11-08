from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

from reviews.models import Comment
from gallery.models import Gallery
from gallery.fields import WEBPField


# Create your models here.
class Hotel(models.Model):
    active = models.BooleanField(default=False, verbose_name="Опубликовано")
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название отеля")
    slug = models.SlugField(unique=True, default='hotel-slug', blank=True, verbose_name="Ссылка на отель")
    image_thumb = WEBPField(upload_to='images/hotels/%Y/%m/%d', null=True, blank=True, verbose_name="Главное изображение")
    price_from = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Стоимость от")
    currency = models.CharField(max_length=15, null=True, blank=True, verbose_name="Валюта")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Адрес")
    description = models.TextField(null=True, blank=True, verbose_name="Описание отеля")

    badges = models.ManyToManyField('Badges', verbose_name="Значки")
    comments = GenericRelation(Comment, related_query_name='hotel', verbose_name="Комментарии")
    gallery = GenericRelation(Gallery, related_query_name='hotel', verbose_name="Галерея")

    timestamp = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Опубликовано")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Время изменения")

    def get_absolute_url(self):
        return reverse('hotel-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title} в {self.address}'

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
        ordering = ["-timestamp", "-updated"]


class Badges(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, default=None, on_delete=models.CASCADE, verbose_name="Отель")
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Тип номера")
    amount = models.IntegerField(default=0, verbose_name="Количество номеров")
    free = models.IntegerField(default=0, verbose_name="Свободно номеров")
    booked = models.IntegerField(default=0, verbose_name="Забронировано номеров")
    gallery = GenericRelation(Gallery, related_query_name='hotel-room', verbose_name="Фото номера")
    description = models.TextField(null=True, blank=True, verbose_name="Описание номера")
    extra_bed = models.BooleanField(default=False, verbose_name="Доп кровать")
    square = models.FloatField(default=0, verbose_name="Площадь, м2")
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Цена за ночь")

    def __str__(self):
        return self.title
