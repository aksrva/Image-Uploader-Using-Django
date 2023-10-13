from django.contrib import admin
from imageuploaderapp.models import ImageUploader

# Register your models here.


class ImageUploaderAdmin(admin.ModelAdmin):
    list_display = ("image", "created_at")


admin.site.register(ImageUploader, ImageUploaderAdmin)
