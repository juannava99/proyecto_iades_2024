from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from abm_libros.forms import LoginForm, FormularioLibro, FormularioBusquedaLibro
from abm_libros.models import Libros
from django.contrib.auth.decorators import login_required

def login_view(request):
    form = LoginForm(request.POST or None)
    print(f"metodo: {request.method}")
    if request.method == 'POST':
        print("Entro post")
        if form.is_valid():
            print("Valido formulario")
            usuario = form.cleaned_data['usuario']
            contarseña = form.cleaned_data['contraseña']
            user = authenticate(request, username=usuario, password=contarseña)
            if user is not None:
                login(request, user)
                print("valido usuario")
                return redirect('visualizacion_administrable')  # Redirige a la página principal después de iniciar sesión
            else:
                messages.error(request, 'Usuario Invalido o contraseña incorrecta')
    return render(request, 'login.html', {'form': form})

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
                messages.error(request, f"Ocurrió un error al guardar el libro: {e}")
                
        else:
            # Mensaje de error si el formulario no es válido
            messages.error(request, "El formulario contiene errores. Por favor, verifica los datos.")
    formulario = FormularioLibro()
    return render(request,"formulario_libro.html",{"formulario": formulario})

def busqueda_libro(request):
    # Guardar la URL de referencia (de dónde vino el usuario)
    if not request.session.get('previous_url'):
        request.session['previous_url'] = request.META.get('HTTP_REFERER', '/')

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

    return render(request, 'busqueda_libro.html', {"formulario": formulario, "resultados": resultados})


def visualizacion_libros(request):
    if not request.session.get('previous_url'):
        request.session['previous_url'] = request.META.get('HTTP_REFERER', '/')

    libros = Libros.objects.all()
    return render(request, 'visualizacion_libros.html', {'libros': libros})


def inicio(request):
    return render(request,'inicio.html')
