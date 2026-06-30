from rest_framework import serializers
from .models import Project, ProjectPhase

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'company', 'client', 'status', 'budget_estimated', 'budget_approved', 'margin']
        read_only_fields = ['id']
