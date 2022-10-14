from django.db import models


# Create your models here.
class Post(models.Model):
    active = models.BooleanField(default=False, verbose_name='Активно')
    title = models.CharField(max_length=255, default='название поста', verbose_name='Название поста')
    image = models.ImageField(upload_to='images/blog/%Y/%m/%d')
    content = models.TextField(blank=True)
    head_keywords = models.TextField(null=True, blank=True, verbose_name="сео слова")
    head_description = models.TextField(null=True, blank=True, verbose_name="сео описание")

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
