from django.contrib import admin
from .models import Client


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ["fio_tourist", "date_created"]
    search_fields = ["fio_tourist"]


admin.site.register(Client, ClientAdmin)
