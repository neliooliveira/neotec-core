from rest_framework import serializers
from .models import Requirement, RequirementVersion

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'code', 'title', 'project', 'type', 'status', 'priority']
        read_only_fields = ['id']
