from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'requirements'
router = DefaultRouter()
router.register(r'', views.RequirementViewSet, basename='requirement')

urlpatterns = [path('', include(router.urls))]
