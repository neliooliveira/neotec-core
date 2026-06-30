from django.contrib import admin
from .models import KnowledgeArticle
@admin.register(KnowledgeArticle)
class KnowledgeArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    search_fields = ('title', 'slug')
    list_filter = ('is_published',)
