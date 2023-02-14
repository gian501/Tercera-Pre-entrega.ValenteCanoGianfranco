from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Curso'}))
    comision = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Curso'}))

class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
    apellido = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'})) 
    email = forms.EmailField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'})) 
    profesion = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
    apellido = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'})) 
    email = forms.EmailField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
    apellido = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'})) 
    email = forms.EmailField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    fechaEntrega = forms.DateTimeField()
    entregado = forms.BooleanField()

