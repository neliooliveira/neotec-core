from django.contrib import admin
from .models import Engineering
@admin.register(Engineering)
class EngineeringAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
