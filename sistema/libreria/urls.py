from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'), #Se elimina directamente el libro marcando el ID que corresponda
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('registros_usuarios/', views.registro_usuarios, name='registro_usuarios'),
    path('registros_usuarios/', views.registro_usuarios, name='registro_usuarios'), 
    path('ingreso_usuarios/', views.ingreso_usuarios, name='ingreso_usuarios'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
