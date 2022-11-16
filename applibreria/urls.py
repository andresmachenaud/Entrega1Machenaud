from django.urls import path
from applibreria.views import *

urlpatterns = [
    path("", inicio, name="libreria-inicio"),
    path("tienda/", tienda, name="libreria-tienda"),
    path("clientes/", clientes, name="libreria-clientes"),
    path("clientes/crear", crear_cliente, name="libreria-clientes-crear"),
    path("empleados/", empleados, name="libreria-empleados"),
    path("empleados/crear", crear_empleado, name="libreria-empleados-crear"),
    path("tienda/crear/", crear_libro, name="libreria-libros-crear"),
    path("tienda/buscar/", buscar_libro, name="libreria-libros-buscar"),
    path("tienda/buscar/resultados/", resultados_buscar_libros, name="libreria-libros-buscar-resultados"),
]