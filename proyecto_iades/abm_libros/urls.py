from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import(inicio,
                   visualizacion_administrable,
                   login_view,
                   visualizacion_libros,
                   formulario_libro,
)


urlpatterns =[
    path("",inicio, name="Inicio"),
    path("visualizacion_administrable",visualizacion_administrable, name="visualizacion_administrable"),
    path('login/', login_view, name='login'),
    path('nuevo_libro/', formulario_libro, name='formulario_libro'),
    path('visualizacion_libros', visualizacion_libros, name='visualizacion_libros')

]