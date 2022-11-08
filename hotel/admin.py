from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
# Register your models here.

from .models import Hotel, Badges, RoomType
from gallery.models import Gallery


class HotelImageAdmin(GenericStackedInline):
    model = Gallery
    extra = 1


class RoomTypeAdmin(admin.StackedInline):
    model = RoomType
    extra = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageAdmin, RoomTypeAdmin, ]
    list_display = ["active", "title", "updated"]
    list_editable = ["active"]
    list_display_links = ["title"]
    list_filter = ["active"]
    search_fields = ('title',)

    class Meta:
        model = Hotel

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    inlines = [HotelImageAdmin, ]


admin.site.register(Badges)
