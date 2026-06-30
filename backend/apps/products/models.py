from django.db import models
from core.models import BaseModel

class Product(BaseModel):
    """Product model."""
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, related_name='products')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class ProductVersion(BaseModel):
    """Product versions."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    class Meta:
        unique_together = ('product', 'version_number')
    def __str__(self):
        return f"{self.product} - v{self.version_number}"
