import uuid

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

from .fields import WEBPField
# Create your models here.

def image_folder(instance, filename):
    return f'webp/gallery/{instance}-{filename}-{uuid.uuid4().hex}-travellab.webp'


class Gallery(models.Model):
    image = WEBPField(verbose_name=_('Image'), upload_to=image_folder, blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
