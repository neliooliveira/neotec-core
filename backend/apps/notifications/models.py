from django.db import models
from core.models import BaseModel

class Notification(BaseModel):
    """User notifications."""
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
