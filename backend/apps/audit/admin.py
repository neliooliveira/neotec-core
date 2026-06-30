from django.contrib import admin
from .models import AuditLog
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'resource_type', 'resource_id', 'created_at')
    list_filter = ('action', 'resource_type')
    search_fields = ('resource_id',)
    readonly_fields = ('user', 'action', 'resource_type', 'resource_id', 'old_values', 'new_values', 'created_at')
