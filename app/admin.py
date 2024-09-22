from django.contrib import admin
from .models import image


@admin.register(image)
class image_admin(admin.ModelAdmin):
    list_display = ["id","photo","date"]