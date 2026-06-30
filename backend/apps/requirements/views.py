from rest_framework import viewsets
from .models import Requirement
from .serializers import RequirementSerializer

class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
