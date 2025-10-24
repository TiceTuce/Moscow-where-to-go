from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminBase, SortableTabularInline

from .models import Place, Photo 


class PhotoInline(SortableTabularInline):
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии'
    model = Photo
    
    fields = ['image', 'preview', 'position']
    
    readonly_fields = ['preview']
    
    def preview(self, obj):
        return mark_safe(f'<img src="{settings.MEDIA_URL+str(obj.image)}" style="max-height: 200px; max-width: 200px">')
        # return mark_safe(f'<img src="{}">')
    


# Register your models here.
@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    inlines = [PhotoInline]
