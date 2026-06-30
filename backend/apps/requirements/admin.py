from django.contrib import admin
from .models import Requirement, RequirementVersion, RequirementCost

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'project', 'type', 'status', 'priority')
    search_fields = ('code', 'title')
    list_filter = ('status', 'priority', 'type')

@admin.register(RequirementVersion)
class RequirementVersionAdmin(admin.ModelAdmin):
    list_display = ('requirement', 'version_number', 'cost_estimated', 'cost_approved')

@admin.register(RequirementCost)
class RequirementCostAdmin(admin.ModelAdmin):
    list_display = ('requirement', 'type', 'amount', 'currency')
