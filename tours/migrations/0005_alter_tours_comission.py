# Generated by Django 4.0.4 on 2022-09-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_alter_tours_num_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='comission',
            field=models.FloatField(blank=True, default=40, null=True, verbose_name='Комиссия'),
        ),
    ]