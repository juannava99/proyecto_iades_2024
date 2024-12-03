from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from abm_libros.forms import FormularioLogueo, FormularioLibro, FormularioBusquedaLibro
from abm_libros.models import Libros
from django.contrib.auth.decorators import login_required

def logueo_usario(request):
    formulario_logueo = FormularioLogueo(request.POST or None)
    print(f"metodo: {request.method}")
    if request.method == 'POST':
        print("Entro post")
        if formulario_logueo.is_valid():
            print("Valido formulario")
            usuario = formulario_logueo.cleaned_data['usuario']
            contarseña = formulario_logueo.cleaned_data['contraseña']
            user = authenticate(request, username=usuario, password=contarseña)
            if user is not None:
                login(request, user)
                print("valido usuario")
                return redirect('visualizacion_administrable')  # Redirige a la página principal después de iniciar sesión
            else:
                messages.error(request, 'Usuario Invalido o contraseña incorrecta')
    return render(request, 'login.html', {'form': formulario_logueo})

@login_required
def visualizacion_administrable(request):
    return render(request,'visualizacion_administrable.html')

@login_required
def formulario_libro(request):
    if request.method == 'POST':
        formulario = FormularioLibro(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            try:
                libro_new = Libros(nombre = datos ["nombre"],autor = datos ["autor"],precio = datos ["precio"],stock = datos ["stock"],isbn = datos ["isbn"])
                libro_new.save()
                messages.success(request,"El libro ha sido guardado correctamente")
                return HttpResponseRedirect("/abm_libros/visualizacion_administrable")
            except Exception as e:
                # Si ocurre algún error durante el guardado
                messages.error(request, f"El ISBN del libro ingresado ya existe")
            return redirect('formulario_libro')    
        else:
            # Mensaje de error si el formulario no es válido
            messages.error(request, "El formulario contiene errores. Por favor, verifica los datos.")
    formulario = FormularioLibro()
    return render(request,"formulario_libro.html",{"formulario": formulario,"url_regreso": 'visualizacion_administrable' })

def busqueda_libro(request):
    origen = request.GET.get('next', 'default')
    if origen == 'html1':
        url_regreso = reverse('visualizacion_administrable')
    else:
        url_regreso = reverse('Inicio')
    formulario = FormularioBusquedaLibro(request.GET)
    resultados = None
    if formulario.is_valid():
        isbn_busqueda = formulario.cleaned_data.get('isbn', '')
        nombre_busqueda = formulario.cleaned_data.get('nombre', '')
        if isbn_busqueda and nombre_busqueda:
            resultados = Libros.objects.filter(isbn=isbn_busqueda, nombre__icontains=nombre_busqueda)
        elif isbn_busqueda:
            resultados = Libros.objects.filter(isbn=isbn_busqueda)
        elif nombre_busqueda:
            resultados = Libros.objects.filter(nombre__icontains=nombre_busqueda)

    return render(request, 'busqueda_libro.html', {"formulario": formulario, "resultados": resultados, "url_regreso": url_regreso})

@login_required
def eliminar_libro(request):
    if request.method == "POST":
        isbn = request.POST.get('isbn', None)
        if isbn:
            try:
                libro = get_object_or_404(Libros, isbn=isbn)
                libro.delete()
                messages.success(request, f"El libro con ISBN {isbn} ha sido eliminado correctamente.")
                return HttpResponseRedirect("/abm_libros/visualizacion_administrable")
            
            except Http404  as e:
                messages.error(request, f"No se encontró un libro con el ISBN {isbn}.")

            except Exception as e:
                print(f"error       {e}")
                messages.error(request, f"No se pudo eliminar el libro con el ISBN: {str(isbn)}")
        return redirect('eliminar_libro')
    
    return render(request, 'eliminar_libro.html',{"url_regreso": 'visualizacion_administrable' })


def visualizacion_libros(request):
    origen = request.GET.get('next', 'default')
    if origen == 'html1':
        url_regreso = reverse('visualizacion_administrable')
    else:
        url_regreso = reverse('Inicio')

    libros = Libros.objects.all()
    return render(request, 'visualizacion_libros.html', {'libros': libros,"url_regreso": url_regreso})


def inicio(request):
    return render(request,'inicio.html')
