from django.contrib import admin
from app.models import Infos, ServicesModel, AboutModel


@admin.register(Infos)
class InfosAdmin(admin.ModelAdmin):
    list_display = ["company_name", "company_email", "phone_number"]



@admin.register(ServicesModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'service_description']


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['about_title', 'about_content']
