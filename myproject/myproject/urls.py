# myproject/myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')), # Inclui as URLs do seu aplicativo core
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')), # Rotas de autenticação do DRF
]
