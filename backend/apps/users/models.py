from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel


class User(AbstractUser):
    """Extended User model."""
    
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.get_full_name() or self.username


class Role(BaseModel):
    """User roles."""
    
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('manager', 'Manager'),
        ('engineer', 'Engineer'),
        ('finance', 'Finance'),
        ('client', 'Client'),
        ('support', 'Support'),
    ]
    
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)
    description = models.TextField(blank=True)
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='roles'
    )
    
    class Meta:
        unique_together = ('name', 'company')
    
    def __str__(self):
        return f"{self.get_name_display()} ({self.company})"


class Permission(BaseModel):
    """Permissions for roles."""
    
    codename = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'
    
    def __str__(self):
        return self.name


class UserRole(BaseModel):
    """M2M between User and Role."""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')
    
    class Meta:
        unique_together = ('user', 'role')
    
    def __str__(self):
        return f"{self.user} - {self.role}"


class RolePermission(BaseModel):
    """M2M between Role and Permission."""
    
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='permissions')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('role', 'permission')
    
    def __str__(self):
        return f"{self.role} - {self.permission}"
