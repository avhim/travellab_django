from django.contrib import admin
from .models import Agency


# Register your models here.

class AgencyAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "active"]
    list_display_links = ["title"]
    list_editable = ["active"]
    list_filter = ["active"]
    search_fields = ('title',)

    class Meta:
        model = Agency


admin.site.register(Agency, AgencyAdmin)
