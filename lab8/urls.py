from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.urls import path, include
from oauth2_provider import urls as oauth2_urls


urlpatterns = [
    path('', include('pokedex.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('o/', include(oauth2_urls)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
