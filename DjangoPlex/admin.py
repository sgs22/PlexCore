from django.contrib import admin

from .models import MediaRequest


# Register your models here.
class MediaRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaRequest, MediaRequestAdmin)
