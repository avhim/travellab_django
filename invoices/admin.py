from django.contrib import admin
from .models import Invoices

# Register your models here.


class InvoicesAdmin(admin.ModelAdmin):
    list_display = ["slug", "timestamp", "agency", "paid"]
    list_display_links = ["slug"]
    list_filter = ['tour', 'paid', 'agency']


admin.site.register(Invoices, InvoicesAdmin)
