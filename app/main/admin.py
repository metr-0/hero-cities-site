from django.contrib import admin

from main import models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    """city admin model"""

    list_display = (
        models.City.name.field.name,
        models.City.lantitude.field.name,
        models.City.longtitude.field.name,
        models.City.text.field.name,
    )

    list_display_links = (
        models.City.name.field.name,
    )
