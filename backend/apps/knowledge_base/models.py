from django.db import models
from core.models import BaseModel

class KnowledgeArticle(BaseModel):
    """Knowledge base articles."""
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='knowledge_articles')
    is_published = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
