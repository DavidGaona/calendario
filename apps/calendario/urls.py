from django.urls import path
from django.urls.conf import re_path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('', views.actividades),
    path('actividades/', views.actividades, name="actividades"),
    path('crear-actividad/', views.crear_actividad, name="crear-actividad"),
    path('editar-actividad/<str:pk>/', views.editar_actividad, name="editar-actividad"),
    re_path(r'^swingtime/events/type/([^/]+)/$', views.event_type, name='karate-event'),
    path('swingtime/', include('swingtime.urls')),
    path('reportes/', views.reportes, name="reportes"),

]
