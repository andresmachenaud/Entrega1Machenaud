from django import forms  

class libroformulario(forms.Form):
    
    titulo = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=100)
    año = forms.IntegerField()
    editorial = forms.CharField(max_length=100)

class clienteformulario(forms.Form):
    
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()

class empleadoformulario(forms.Form):
    
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()