from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from applibreria.forms import *
from applibreria.models import *

# Create your views here.

def inicio(request):
    return render(request, "applibreria/inicio.html")

def tienda(request):
    libros = Libro.objects.all()
    lista_libros = []
    for libro in libros:
        lista_libros.append((libro.titulo, libro.autor, libro.año, libro.editorial))
    datos = {"listado_libros": lista_libros}
    plantilla = loader.get_template("tienda.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def crear_libro(request):
    if request.method == "POST":
        miFormulario = libroformulario(request.POST)
        if miFormulario.is_valid():
            miLibro = Libro(titulo = miFormulario.cleaned_data["titulo"], autor = miFormulario.cleaned_data["autor"], año = miFormulario.cleaned_data["año"], editorial = miFormulario.cleaned_data["editorial"])
            miLibro.save()
    miFormulario = libroformulario() #cuando crea el nuevo profesor le pasa al template un formulario vacío para que se vacíen los campos
    contexto = {"formulario": miFormulario}
    return render(request, "applibreria/libros_formulario.html", contexto)

def buscar_libro(request):
    return render(request, "applibreria/busqueda_libros.html")

def resultados_buscar_libros(request):
    titulo_libro = request.GET["titulo_libro"]
    nombre_autor = request.GET["nombre_autor"]
    libros = Libro.objects.filter(titulo__icontains=titulo_libro,autor__icontains=nombre_autor)
    return render(request, "applibreria/resultados_busqueda_libros.html", {"libros": libros})

def empleados(request):
    return render(request, "applibreria/empleados.html")

def crear_empleado(request):
    if request.method == "POST":
        miFormulario = empleadoformulario(request.POST)
        if miFormulario.is_valid():
            miEmpleado = Empleado(nombre = miFormulario.cleaned_data["nombre"], apellido = miFormulario.cleaned_data["apellido"], email = miFormulario.cleaned_data["email"])
            miEmpleado.save()
    miFormulario = empleadoformulario() #cuando crea el nuevo profesor le pasa al template un formulario vacío para que se vacíen los campos
    contexto = {"formulario": miFormulario}
    return render(request, "applibreria/empleados_formulario.html", contexto)

def clientes(request):
    return render(request, "applibreria/clientes.html")

def crear_cliente(request):
    if request.method == "POST":
        miFormulario = clienteformulario(request.POST)
        if miFormulario.is_valid():
            miCliente = Cliente(nombre = miFormulario.cleaned_data["nombre"], apellido = miFormulario.cleaned_data["apellido"], email = miFormulario.cleaned_data["email"])
            miCliente.save()
    miFormulario = clienteformulario() #cuando crea el nuevo profesor le pasa al template un formulario vacío para que se vacíen los campos
    contexto = {"formulario": miFormulario}
    return render(request, "applibreria/clientes_formulario.html", contexto)