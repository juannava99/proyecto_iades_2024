# forms.py
from django import forms
from .models import Libros
class FormularioLogueo(forms.Form):
    usuario = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Usuario', 'required': 'required'
    }))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Contraseña', 'required': 'required'
    }))

class FormularioLibro(forms.Form):
    nombre = forms.CharField()
    autor = forms.CharField()
    precio = forms.DecimalField()
    stock = forms.IntegerField()
    isbn = forms.CharField()
    
class FormularioBusquedaLibro(forms.Form):
    nombre = forms.CharField(required=False)
    isbn = forms.IntegerField(required=False)