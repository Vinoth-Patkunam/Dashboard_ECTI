from django.contrib import admin
from django.urls import path, include  # ← on ajoute include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Branche toutes les routes du router DRF sous /api/
    path('api/', include('api.urls')),
]
