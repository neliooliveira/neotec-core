from django.db import models
from core.models import BaseModel

class Document(BaseModel):
    """Technical documents."""
    TYPE_CHOICES = [('design', 'Design'), ('specification', 'Specification'), ('manual', 'Manual'), ('datasheet', 'Datasheet'), ('schematic', 'Schematic'), ('other', 'Other')]
    STATE_CHOICES = [('draft', 'Draft'), ('review', 'Review'), ('approved', 'Approved'), ('archived', 'Archived')]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='documents', null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='draft')
    revision = models.CharField(max_length=50, default='1.0')
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='authored_documents')
    file = models.FileField(upload_to='documents/')
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
