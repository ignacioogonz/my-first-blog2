from django.conf.urls import include, url
from . import views
from django.contrib import admin
from blog.views import post_list, mascota_view, mascota_list, mascota_edit, mascota_delete,registroUsuario

app_name = "mascota"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list, name='index'),
    url(r'^nuevo$', mascota_view, name='mascota_crear'),
    url(r'^listar$', mascota_list, name='mascota_listar'),  
    url(r'^editar/(?P<id_mascota>\d+)$', mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)$', mascota_delete, name='mascota_eliminar'),
    url(r'^RegistroUsuario/$', views.registroUsuario, name='registroUsuario'),
]
