# Generated by Django 4.0.4 on 2022-11-04 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gallery.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('managers', '0001_initial'),
        ('hotel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Тип тура')),
            ],
            options={
                'verbose_name': 'Тип тура',
                'verbose_name_plural': 'Типы туров',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Активно')),
                ('name', models.CharField(default='название тура', max_length=255, verbose_name='Название тура')),
                ('slug', models.SlugField(blank=True, default='page-slug', unique=True, verbose_name='Ссылка на тур')),
                ('head_keywords', models.TextField(blank=True, null=True, verbose_name='сео слова')),
                ('head_description', models.TextField(blank=True, null=True, verbose_name='сео описание')),
                ('main_image', gallery.fields.WEBPField(blank=True, null=True, upload_to='images/tours/%Y/%m/%d', verbose_name='Главное изображение')),
                ('short_title', models.TextField(blank=True, null=True, verbose_name='краткое описание')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Заголовок на изображении')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('currency', models.CharField(default='$', max_length=10, verbose_name='валюта')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Старая цена')),
                ('service_price', models.DecimalField(blank=True, decimal_places=2, default='80', max_digits=7, null=True, verbose_name='Туруслуга взрослый')),
                ('service_price_child', models.DecimalField(blank=True, decimal_places=2, default='40', max_digits=7, null=True, verbose_name='Туруслуга детский')),
                ('route', models.TextField(blank=True, null=True, verbose_name='Маршрут')),
                ('country', models.CharField(blank=True, max_length=30, null=True, verbose_name='Страна')),
                ('num_days', models.IntegerField(default=1, verbose_name='Количество дней')),
                ('description_tour', models.TextField(blank=True, null=True, verbose_name='описание тура')),
                ('included', models.TextField(blank=True, null=True, verbose_name='Включено в стоимость')),
                ('not_included', models.TextField(blank=True, null=True, verbose_name='Не включено в стоимость')),
                ('comission', models.FloatField(blank=True, default=10, null=True, verbose_name='Комиссия %')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ManyToManyField(to='tours.categorytour')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('hotels', models.ManyToManyField(blank=True, null=True, to='hotel.hotel', verbose_name='Отели')),
                ('manager', models.ManyToManyField(default=None, to='managers.manager', verbose_name='Менеджер')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('tour', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tours.tours')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='TourDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptionDay', models.CharField(default='День 1', max_length=12)),
                ('days', models.TextField(blank=True, null=True)),
                ('tour', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tours.tours')),
            ],
            options={
                'verbose_name': 'Описание дня',
                'verbose_name_plural': 'Описание дней',
            },
        ),
        migrations.CreateModel(
            name='TourDayQuota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('tour_date', models.DateField(null=True, verbose_name='Дата тура')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Конец тура')),
                ('total_quotas', models.PositiveIntegerField(blank=True, null=True, verbose_name='Всего мест')),
                ('active_quotas', models.PositiveIntegerField(verbose_name='Оставшиеся места')),
                ('sold_quotas', models.PositiveIntegerField(blank=True, null=True, verbose_name='Проданные места')),
                ('price_adult', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена взрослый')),
                ('price_child', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена детский')),
                ('tour', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tours.tours')),
            ],
            options={
                'verbose_name': 'Дата-Квота',
                'verbose_name_plural': 'Даты-Квоты',
                'ordering': ['tour_date'],
            },
        ),
    ]
