from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request,'Inicio.jinja')

def Lista(request):
    return render(request, 'lista_nominas.jinja')
