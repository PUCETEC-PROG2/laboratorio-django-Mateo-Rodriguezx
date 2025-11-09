from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('pokedex.urls', 'pokedex'), namespace='pokedex')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
