from django.contrib import admin
from .models import User, Role, Permission, UserRole


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'company', 'is_active')
    search_fields = ('username', 'email', 'first_name')
    list_filter = ('is_active', 'company')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ('name',)
    list_filter = ('company',)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('codename', 'name')
    search_fields = ('codename', 'name')


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role__name')
