from django.contrib import admin
from .models import Document
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'type', 'state', 'revision', 'author')
    search_fields = ('title',)
