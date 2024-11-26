from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import(inicio,
                   visualizacion_administrable,
                   logueo_usario,
                   visualizacion_libros,
                   formulario_libro,
                   busqueda_libro,
                   eliminar_libro,
)


urlpatterns =[
    path("",inicio, name="Inicio"),
    path("visualizacion_administrable",visualizacion_administrable, name="visualizacion_administrable"),
    path('login/', logueo_usario, name='login'),
    path('nuevo_libro/', formulario_libro, name='formulario_libro'),
    path('busqueda_libro/', busqueda_libro, name='busqueda_libro'),
    path('visualizacion_libros', visualizacion_libros, name='visualizacion_libros'),
    path('eliminar_libro', eliminar_libro, name='eliminar_libro')

]