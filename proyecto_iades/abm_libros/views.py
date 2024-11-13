from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from abm_libros.forms import LoginForm, FormularioLibro
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
        print("Entre post")
        formulario = FormularioLibro(request.POST)
        isbn = formulario.cleaned_data['isbn']
        
        print(isbn)
        if formulario.is_valid():
            print("valido que si")
            datos = formulario.cleaned_data
            libro_new = Libros(nombre = datos ["nombre"],autor = datos ["autor"],precio = datos ["precio"],stock = datos ["stock"],ISBN = datos ["isbn"])
            libro_new.save()
            return HttpResponseRedirect("/abm_libros/visualizacion_administrable")
        else:
            print("error")
            messages.error(request, 'Usuario Invalido o contraseña incorrecta')
    formulario = FormularioLibro()
    return render(request,"formulario_libro.html",{"formulario": formulario})

    
def visualizacion_libros(request):
    return render(request,'visualizacion_libros.html')

def inicio(request):
    return render(request,'inicio.html')
