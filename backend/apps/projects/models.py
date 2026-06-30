from django.db import models
from core.models import BaseModel

class Project(BaseModel):
    """Project model."""
    
    STATUS_CHOICES = [('planning', 'Planning'), ('active', 'Active'), ('on_hold', 'On Hold'), ('completed', 'Completed'), ('archived', 'Archived')]
    
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, related_name='projects')
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='projects')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    budget_estimated = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    budget_approved = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    budget_used = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    budget_remaining = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    margin = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text='Percentage')
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='created_projects')
    modified_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_projects')
    
    class Meta:
        unique_together = ('company', 'slug')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name


class ProjectPhase(BaseModel):
    """Project phases/milestones."""
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='phases')
    order = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default='pending')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = ('project', 'order')
        ordering = ['order']
    
    def __str__(self):
        return f"{self.project} - {self.name}"
