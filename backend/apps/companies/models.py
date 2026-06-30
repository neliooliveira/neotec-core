from django.db import models
from core.models import BaseModel


class Company(BaseModel):
    """Company/Organization model."""
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    website = models.URLField(blank=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    tax_id = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Team(BaseModel):
    """Teams within a company."""
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='teams')
    members = models.ManyToManyField(
        'users.User',
        related_name='teams',
        blank=True
    )
    
    class Meta:
        unique_together = ('name', 'company')
    
    def __str__(self):
        return f"{self.name} ({self.company})"
