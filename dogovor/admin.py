from django.contrib import admin
from .models import Dogovor, DogClients


# Register your models here.

class DogClientsAdmin(admin.StackedInline):
    model = DogClients


@admin.register(Dogovor)
class DogovorAdmin(admin.ModelAdmin):
    inlines = [DogClientsAdmin]
    list_display = ['id', 'created_by', 'tour', 'timestamp']
    search_fields = ['id', 'created_by', 'tour', 'client']

    class Meta:
        model = Dogovor


@admin.register(DogClients)
class DogClientsAdmin(admin.ModelAdmin):
    pass
