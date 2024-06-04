from django.contrib import admin
from django.contrib import admin
from .models import Application, ApplicationInstance

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'sub_type', 'is_active']
    search_fields = ['title', 'type', 'sub_type']
    list_filter = ['is_active']

@admin.register(ApplicationInstance)
class ApplicationInstanceAdmin(admin.ModelAdmin):
    list_display = ['title', 'application', 'is_active', 'last_connected_at']
    search_fields = ['title', 'application__title']
    list_filter = ['is_active']
