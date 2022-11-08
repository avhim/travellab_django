from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation

from reviews.models import Comment
from gallery.models import Gallery
from managers.models import Manager
from hotel.models import Hotel
from gallery.fields import WEBPField
from .utils import end_date_generator


class Tours(models.Model):
    active = models.BooleanField(default=False, verbose_name='Активно')
    name = models.CharField(max_length=255, default='название тура', verbose_name='Название тура')  # tour name
    slug = models.SlugField(unique=True, default='page-slug', blank=True, verbose_name="Ссылка на тур")

    head_keywords = models.TextField(null=True, blank=True, verbose_name="сео слова")
    head_description = models.TextField(null=True, blank=True, verbose_name="сео описание")

    main_image = WEBPField(upload_to='images/tours/%Y/%m/%d', null=True, blank=True,
                                   verbose_name="Главное изображение")  # main image
    short_title = models.TextField(null=True, blank=True, verbose_name="краткое описание")
    title = models.TextField(null=True, blank=True, verbose_name="Заголовок на изображении")  # main image title

    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    currency = models.CharField(max_length=10, default='$', verbose_name="валюта")
    old_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Старая цена")

    service_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default='80', verbose_name="Туруслуга взрослый")
    service_price_child = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default='40', verbose_name="Туруслуга детский")

    route = models.TextField(null=True, blank=True, verbose_name="Маршрут")
    country = models.CharField(max_length=30, null=True, blank=True, verbose_name="Страна")
    num_days = models.IntegerField(default=1, verbose_name="Количество дней")

    description_tour = models.TextField(null=True, blank=True, verbose_name="описание тура")

    included = models.TextField(null=True, blank=True, verbose_name="Включено в стоимость")
    not_included = models.TextField(null=True, blank=True, verbose_name="Не включено в стоимость")

    hotels = models.ManyToManyField(Hotel, verbose_name="Отели")
    comission = models.FloatField(null=True, blank=True, default=10, verbose_name="Комиссия %")
    category = models.ManyToManyField('CategoryTour', verbose_name="Тип тура")
    comments = GenericRelation(Comment, related_query_name='tour', verbose_name="Комментарии")
    gallery = GenericRelation(Gallery, related_query_name='tour', verbose_name="Галерея")

    manager = models.ManyToManyField(Manager, default=None, verbose_name="Менеджер")

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tour-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ["-timestamp", "-updated"]


class TourImage(models.Model):
    tour = models.ForeignKey(Tours, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class TourDays(models.Model):
    tour = models.ForeignKey(Tours, default=None, on_delete=models.CASCADE)
    descriptionDay = models.CharField(default="День 1", max_length=12)
    days = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.descriptionDay

    class Meta:
        verbose_name = 'Описание дня'
        verbose_name_plural = 'Описание дней'


class TourDayQuota(models.Model):
    tour = models.ForeignKey(Tours, default=None, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    tour_date = models.DateField(null=True, verbose_name="Дата тура")
    end_date = models.DateField(null=True, blank=True, verbose_name="Конец тура")
    total_quotas = models.PositiveIntegerField(null=True, blank=True, verbose_name="Всего мест")
    active_quotas = models.PositiveIntegerField(verbose_name="Оставшиеся места")
    sold_quotas = models.PositiveIntegerField(null=True, blank=True, verbose_name="Проданные места")
    price_adult = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена взрослый")
    price_child = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена детский")

    def __str__(self):
        return self.tour_date.strftime("%d-%m-%Y")

    class Meta:
        verbose_name = 'Дата-Квота'
        verbose_name_plural = 'Даты-Квоты'
        ordering = ["tour_date"]


class CategoryTour(models.Model):
    title = models.CharField(max_length=150, verbose_name="Тип тура")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип тура'
        verbose_name_plural = 'Типы туров'
        ordering = ["title"]



def pre_save_receiver_page_model(sender, instance, *args, **kwargs):
    instance.end_date = end_date_generator(instance)


pre_save.connect(pre_save_receiver_page_model, sender=TourDayQuota)
