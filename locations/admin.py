from django.contrib import admin

from .models import District, Province, City, Location


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "province")
    search_fields = ("name",)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name", "city")
    search_fields = ("name",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("province", "city", "district")
    search_fields = ("province",)
