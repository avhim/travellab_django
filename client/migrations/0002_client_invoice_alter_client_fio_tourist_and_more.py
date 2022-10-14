# Generated by Django 4.0.4 on 2022-09-26 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0006_remove_invoices_client'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='invoice',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoices.invoices', verbose_name='счета'),
        ),
        migrations.AlterField(
            model_name='client',
            name='fio_tourist',
            field=models.CharField(default='Иванов Иван Иванович', max_length=255, verbose_name='ФИО туриста'),
        ),
        migrations.AlterField(
            model_name='client',
            name='fio_tourist_lat',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО туриста латиницей'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.CharField(max_length=15, verbose_name='Паспорт'),
        ),
    ]
