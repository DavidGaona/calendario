from django.urls import path
from . import views

urlpatterns = [
    path('', views.actividades),
    path('actividades/', views.actividades, name="actividades"),
    path('crear-actividad/', views.crear_actividad, name="crear-actividad"),
    path('editar-actividad/<str:pk>/', views.editar_actividad, name="editar-actividad")
]
