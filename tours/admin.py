from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import Tours, TourImage, TourDays, TourDayQuota, CategoryTour
from gallery.models import Gallery


# Register your models here.
class TourImageAdmin(GenericStackedInline):
    model = Gallery
    extra = 1


class TourDaysAdmin(admin.StackedInline):
    model = TourDays
    extra = 1


class TourDayQuotaAdmin(admin.TabularInline):
    model = TourDayQuota
    extra = 1

@admin.register(Tours)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageAdmin, TourDaysAdmin, TourDayQuotaAdmin]
    list_display = ["active", "name", "updated"]
    list_editable = ["active"]
    list_display_links = ["name"]
    list_filter = ["active"]
    search_fields = ('name',)

    class Meta:
        model = Tours


@admin.register(TourDays)
class TourDaysAdmin(admin.ModelAdmin):
    pass


@admin.register(TourDayQuota)
class TourDayQuotaAdmin(admin.ModelAdmin):
    pass


class CategoryTourAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(CategoryTour, CategoryTourAdmin)
# admin.site.register(Tours)
