from django.contrib import admin
from .models import Project, ProjectPhase

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'client', 'status', 'budget_approved')
    search_fields = ('name',)

@admin.register(ProjectPhase)
class ProjectPhaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'order', 'status')
