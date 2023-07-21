from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "user", "created_date")
    list_filter = ("type", "status")
    search_fields = ("id", "user__username")
