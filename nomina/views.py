from django.http import HttpResponse
from django.shortcuts import render

from nomina.models import Empleado

# Create your views here.
def Inicio(request):
    return render(request,'Inicio.jinja')

def Lista(request):
    empleados = Empleado.objects.all()
    return render(request, 'lista_nominas.jinja',{"empleados":empleados})

# Lolis
