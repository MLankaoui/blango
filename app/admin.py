from django.contrib import admin
from app.models import Infos, ServicesModel


@admin.register(Infos)
class InfosAdmin(admin.ModelAdmin):
    list_display = ["company_name", "company_email", "phone_number"]



@admin.register(ServicesModel)
class InfosAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'service_description']
