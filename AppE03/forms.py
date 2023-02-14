from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    comision = forms.IntegerField()

class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=40) #letras
    email = forms.EmailField() # tipo mail
    profesion = forms.CharField(max_length=30)

class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=40) #letras
    apellido = forms.CharField(max_length=40) #letras
    email = forms.EmailField() # tipo mail

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=40) #letras
    email = forms.EmailField() # tipo mail
    fechaEntrega = forms.DateField()
    entregado = forms.BooleanField()