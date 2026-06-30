from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API routes
    path('api/auth/', include('apps.users.urls', namespace='auth')),
    path('api/users/', include('apps.users.urls', namespace='users')),
    path('api/companies/', include('apps.companies.urls', namespace='companies')),
    path('api/clients/', include('apps.clients.urls', namespace='clients')),
    path('api/projects/', include('apps.projects.urls', namespace='projects')),
    path('api/requirements/', include('apps.requirements.urls', namespace='requirements')),
    path('api/engineering/', include('apps.engineering.urls', namespace='engineering')),
    path('api/products/', include('apps.products.urls', namespace='products')),
    path('api/production/', include('apps.production.urls', namespace='production')),
    path('api/billing/', include('apps.billing.urls', namespace='billing')),
    path('api/documents/', include('apps.documents.urls', namespace='documents')),
    path('api/notifications/', include('apps.notifications.urls', namespace='notifications')),
    path('api/audit/', include('apps.audit.urls', namespace='audit')),
    path('api/knowledge/', include('apps.knowledge_base.urls', namespace='knowledge_base')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
