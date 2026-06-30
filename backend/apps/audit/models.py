from django.db import models
from core.models import BaseModel

class AuditLog(BaseModel):
    """Audit trail for all operations."""
    ACTION_CHOICES = [('create', 'Create'), ('update', 'Update'), ('delete', 'Delete'), ('approve', 'Approve')]
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='audit_logs')
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    resource_type = models.CharField(max_length=100)
    resource_id = models.CharField(max_length=100)
    old_values = models.JSONField(default=dict, blank=True)
    new_values = models.JSONField(default=dict, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.user} - {self.action} - {self.resource_type}"
