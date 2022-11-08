# Generated by Django 4.0.4 on 2022-11-04 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Активно')),
                ('title', models.CharField(max_length=255, verbose_name='Название организации')),
                ('unp', models.CharField(default='УНП', max_length=12, verbose_name='УНП')),
                ('bank_name', models.CharField(default='Банк', max_length=32, verbose_name='Название банка')),
                ('bank_bik', models.CharField(default='YYYYBY2X', max_length=8, verbose_name='Бик')),
                ('bank_bill', models.CharField(default='BYXX YYYY XXXX XXXX XXXX XXXX XXXX', max_length=34, verbose_name='Банковский Счет')),
                ('telephones', models.TextField(default='Ваш телефон', verbose_name='Телефон')),
                ('address', models.TextField(verbose_name='Юр. адрес')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('contract_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Номер договора')),
                ('sign_date_contract', models.DateField(blank=True, null=True, verbose_name='Дата подписания')),
                ('director', models.CharField(max_length=255, null=True, verbose_name='ФИО Директора')),
                ('reason', models.CharField(max_length=255, null=True, verbose_name='На основании')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='agency', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Агентство',
                'verbose_name_plural': 'Агентства',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
