# Generated by Django 4.0.4 on 2022-11-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Активно')),
                ('title', models.CharField(default='название поста', max_length=255, verbose_name='Название поста')),
                ('slug', models.SlugField(blank=True, default='blog-slug', null=True)),
                ('image', models.ImageField(upload_to='images/blog/%Y/%m/%d')),
                ('content', models.TextField(blank=True)),
                ('head_keywords', models.TextField(blank=True, null=True, verbose_name='сео слова')),
                ('head_description', models.TextField(blank=True, null=True, verbose_name='сео описание')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
