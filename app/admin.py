from django.contrib import admin
from app.models import Infos


@admin.register(Infos)
class InfosAdmin(admin.ModelAdmin):
    list_display = ["company_name", "company_email", "phone_number"]
