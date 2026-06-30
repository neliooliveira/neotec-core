from rest_framework import serializers
from .models import Company, Team


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'slug', 'description', 'website', 'tax_id', 'email', 'is_active']
        read_only_fields = ['id']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'company', 'members']
        read_only_fields = ['id']
