from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Role, Permission
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        # Filter by company
        if self.request.user.company:
            return User.objects.filter(company=self.request.user.company)
        return User.objects.all()


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    
    def get_queryset(self):
        if self.request.user.company:
            return Role.objects.filter(company=self.request.user.company)
        return Role.objects.all()


class LoginView(APIView):
    def post(self, request):
        # Placeholder - implement JWT authentication
        return Response({'message': 'Login endpoint'})


class LogoutView(APIView):
    def post(self, request):
        # Placeholder
        return Response({'message': 'Logout endpoint'})
