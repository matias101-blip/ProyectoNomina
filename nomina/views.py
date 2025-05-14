from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
from nomina.models import Empleado

# Create your views here.
def Inicio(request):
    return render(request,'Inicio.jinja')

def Lista(request):
    empleados = Empleado.objects.all()
    return render(request, 'lista_nominas.jinja',{"empleados":empleados})
def Secion(request):
    if request.method == "GET":
        return render(request,'singup.jinja',{
        'form':UserCreationForm
        })
    else:
        if request.POST['password1']== request.POST['password2']:
            try:
                # Resgistra usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return HttpResponseRedirect('/listado/')


            except IntegrityError:
                return render(request,'singup.jinja',{
                    'form':UserCreationForm,
                'error':'El usuario ya existe'})

        return render(request,'singup.jinja',{
                'form':UserCreationForm,
                'error':'Las contrase;as no coinciden'
                })



# Lolis
