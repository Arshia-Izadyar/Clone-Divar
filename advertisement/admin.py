from django.contrib import admin

# Register your models here.
from .models import Advertisement, Category


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)