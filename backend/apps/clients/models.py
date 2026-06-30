from django.db import models
from core.models import BaseModel

class Client(BaseModel):
    """Client/Customer model."""
    
    STATUS_CHOICES = [('active', 'Active'), ('inactive', 'Inactive'), ('archived', 'Archived')]
    
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, related_name='clients')
    client_company = models.ForeignKey(
        'companies.Company',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='client_relationships'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    contact_person = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    tax_id = models.CharField(max_length=50, blank=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='created_clients')
    modified_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_clients')
    
    class Meta:
        unique_together = ('company', 'slug')
        ordering = ['name']
    
    def __str__(self):
        return self.name
