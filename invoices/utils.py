import random
import string
from datetime import date
# from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator():
    # """
    # This is for a Django project and it assumes your instance
    # has a model with a slug field and a title character (char) field.
    # """
    # if new_slug is not None:
    #     slug = new_slug
    # else:
    #     slug = instance.slug
    #
    # Klass = instance.__class__
    # qs_exists = Klass.objects.filter(slug=slug).exists()
    # if qs_exists:
    new_slug = "{slug}-{randstr}".format(
               slug=date.today().strftime("%d-%m-%Y"),
               randstr=random_string_generator(size=4)
                )
    return new_slug
