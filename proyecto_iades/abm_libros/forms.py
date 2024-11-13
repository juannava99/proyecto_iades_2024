# forms.py
from django import forms
from .models import Libros
class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Usuario', 'required': 'required'
    }))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Contraseña', 'required': 'required'
    }))

class FormularioLibro(forms.Form):
    nombre = forms.CharField()
    autor = forms.CharField()
    precio = forms.IntegerField()
    stock = forms.IntegerField()
    isbn = forms.IntegerField()

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        print("pase isbn")
        if Libros.objects.filter(isbn=isbn).exists():  # Validación para asegurarse de que no exista el ISBN
            raise forms.ValidationError("Este ISBN ya está registrado.")
        return isbn