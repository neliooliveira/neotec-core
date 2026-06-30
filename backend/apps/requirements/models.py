from django.db import models
from core.models import BaseModel

class Requirement(BaseModel):
    """Living requirements model."""
    
    TYPE_CHOICES = [('functional', 'Functional'), ('non-functional', 'Non-Functional'), ('technical', 'Technical'), ('design', 'Design'), ('other', 'Other')]
    STATUS_CHOICES = [('draft', 'Draft'), ('submitted', 'Submitted'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('archived', 'Archived')]
    PRIORITY_CHOICES = [('critical', 'Critical'), ('high', 'High'), ('medium', 'Medium'), ('low', 'Low')]
    
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='requirements')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='functional')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='created_requirements')
    modified_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_requirements')
    
    class Meta:
        unique_together = ('project', 'code')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.code} - {self.title}"


class RequirementVersion(BaseModel):
    """Versioning for requirements."""
    
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='versions')
    version_number = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    cost_estimated = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cost_approved = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    reason_for_change = models.TextField(blank=True)
    approved_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_requirement_versions')
    approved_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='created_requirement_versions')
    
    class Meta:
        unique_together = ('requirement', 'version_number')
        ordering = ['version_number']
    
    def __str__(self):
        return f"{self.requirement} - v{self.version_number}"


class RequirementCost(BaseModel):
    """Cost tracking for requirements."""
    
    TYPE_CHOICES = [('estimated', 'Estimated'), ('approved', 'Approved'), ('actual', 'Actual')]
    
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='costs')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default='EUR')
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.requirement} - {self.type}"


class RequirementAttachment(BaseModel):
    """Attachments for requirements."""
    
    FILE_TYPE_CHOICES = [('image', 'Image'), ('video', 'Video'), ('document', 'Document')]
    
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='requirement_attachments/')
    file_size = models.PositiveIntegerField()
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES)
    uploaded_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='uploaded_attachments')
    
    def __str__(self):
        return f"{self.requirement} - {self.file.name}"


class RequirementComment(BaseModel):
    """Comments on requirements."""
    
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='requirement_comments')
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"Comment by {self.author} on {self.requirement}"
