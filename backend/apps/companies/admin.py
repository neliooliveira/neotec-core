from django.contrib import admin
from .models import Company, Team

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'tax_id', 'email', 'is_active')
    search_fields = ('name', 'tax_id')
    list_filter = ('is_active',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ('name',)
    list_filter = ('company',)
