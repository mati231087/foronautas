from django.urls import path
from . import views

app_name = 'foro'

urlpatterns = [
    path('crear_tema/', views.crear_tema, name='crear_tema'),
    path('editar_tema/<int:tema_id>/', views.editar_tema, name='editar_tema'),
    path('eliminar_tema/<int:tema_id>/', views.eliminar_tema, name='eliminar_tema'),
    path('detalle_tema/<int:tema_id>/', views.detalle_tema, name='detalle_tema'),
    path('editar_comentario/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    path('eliminar_comentario/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario'),
    path('obtener_temas', views.obtener_temas, name='obtener_temas'),
]
