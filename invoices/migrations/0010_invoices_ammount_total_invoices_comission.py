# Generated by Django 4.0.4 on 2022-10-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0009_remove_invoices_tourists_qouta_invoices_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='ammount_total',
            field=models.FloatField(blank=True, null=True, verbose_name='Итого'),
        ),
        migrations.AddField(
            model_name='invoices',
            name='comission',
            field=models.FloatField(blank=True, null=True, verbose_name='Комиссия'),
        ),
    ]