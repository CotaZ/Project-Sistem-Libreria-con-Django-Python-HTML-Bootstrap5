from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libreria.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #En el archivo urls.py, agrega las siguientes líneas al comienzo del archivo para que los archivos multimedia se sirvan correctamente en modo de desarrollo:
