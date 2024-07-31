from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgregarNoticia, EliminarNoticia, ModificarNoticia, ListarNoticias
# NoticiaViewSet,

# router = DefaultRouter()
# router.register(r'noticias', NoticiaViewSet, basename='noticia')

urlpatterns = [
    # path('', include(router.urls)),
    path('noticias_agregar/', AgregarNoticia.as_view(), name='noticias-agregar'),
    path('noticias_eliminar/', EliminarNoticia.as_view(), name='noticias-eliminar'),
    path('noticias_modificar/', ModificarNoticia.as_view(),
         name='noticias-modificar'),
    path('noticias_listar/', ListarNoticias.as_view(), name='noticias-listar'),
]
