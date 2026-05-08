from django.contrib import admin

from .models import CardOwner, ScanRecord


@admin.register(CardOwner)
class CardOwnerAdmin(admin.ModelAdmin):
    list_display = ("card_uid", "employee_id", "employee_name", "department")
    search_fields = ("card_uid", "employee_id", "employee_name", "department")


@admin.register(ScanRecord)
class ScanRecordAdmin(admin.ModelAdmin):
    list_display = ("card_uid", "employee_id", "employee_name", "department", "time_in", "time_out")
    search_fields = ("card_uid", "employee_id", "employee_name", "department")
    list_filter = ("department", "time_in", "time_out")
