from django.urls import path
from AppE03 import views
# importando las funciones desde views


urlpatterns = [
    path('', views.inicio, name='Inicio'), # esta conectado con views
    path('cursos/', views.cursos, name='Cursos'),
    path('profesores/', views.profesores, name='Profesores'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('entregables/', views.entregables, name='Entregables'),
    path('busquedaComision', views.busquedaComision, name= "BusquedaComision"),
    path('buscar/', views.buscar),
]