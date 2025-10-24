from django.contrib import admin

from .models import Place, Photo 


class PhotoInline(admin.TabularInline):
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии'
    model = Photo


# Register your models here.
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    inlines = (PhotoInline,)
