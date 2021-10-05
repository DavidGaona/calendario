from django.urls import path

from . import views

urlpatterns = [
    path('', views.actividades),
    path('actividades/', views.actividades, name="actividades"),
    path('crear-actividad/', views.crear_actividad, name="crear-actividad"),
    path('editar-actividad/<str:pk>/', views.editar_actividad, name="editar-actividad"),
    path('calendario/', views.calendario, name="calendario"),
    path('crear-calendario/', views.crear_calendario, name="crear-calendario"),
    path('editar-calendario/<str:pk>/', views.editar_calendario, name="editar-calendario"),
]
