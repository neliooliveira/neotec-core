from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'company', 'status', 'contact_person', 'contact_email', 'tax_id']
        read_only_fields = ['id']
