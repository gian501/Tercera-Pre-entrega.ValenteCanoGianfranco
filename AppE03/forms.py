from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Curso'}))
    comision = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Comision Nº: :4444'}))

class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
    apellido = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'})) 
    email = forms.EmailField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'})) 
    profesion = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Profesion'}))
class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
    apellido = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'})) 
    email = forms.EmailField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
    apellido = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'})) 
    email = forms.EmailField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    fechaEntrega = forms.DateTimeField(required=True, widget=forms.TextInput(attrs={'placeholder': '14-02-2023'}))
    entregado = forms.BooleanField()

