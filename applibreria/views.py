from django.shortcuts import render
from django.http import HttpResponse
from applibreria.forms import *
from applibreria.models import *

# Create your views here.

def inicio(request):
    return render(request, "applibreria/inicio.html")