from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'status', 'contact_email')
    search_fields = ('name', 'contact_email')
