# Generated by Django 4.0.4 on 2022-09-16 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_alter_agency_email_alter_agency_sign_date_contract_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='email',
        ),
    ]
