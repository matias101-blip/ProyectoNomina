from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from nomina.models import Cargo, Departamento, Empleado, Rol, TipoContrato

# Create your views here.
def Inicio(request):
    return render(request,'Inicio.jinja')

def Empleados(request):
    empleados=Empleado.objects.all()
    empleados_dict = [{"Nombre":emp.nombre, "Cedula":emp.cedula,"Direccion":emp.direccion,"Sexo":emp.sexo,"Sueldo":emp.sueldo,"Cargo":emp.cargo.descripcion,"Departamento":emp.departamento.descripcion,"Contrato":emp.tipo_contrato.descripcion} for emp in empleados]
    return render(request, 'lista_nominas.jinja',{"table_body":empleados_dict})

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

def singout(request):
    logout(request)
    return HttpResponseRedirect('/')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.jinja',{'form':AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'signin.jinja',
                          {'form':AuthenticationForm,
                           'error':"Tu usuario o contrasena  esta incorrecta"})
        else:
            login(request,user)
            return redirect('Lista')




def Departamentos(request):
    departamentos = Departamento.objects.all()
    departamentos_dict = [{
        "id":dep.pk,"Descripcion":dep.descripcion
    } for dep in departamentos]
    return render(request,'departamentos.jinja',{"table_body":departamentos_dict})

def Cargos(request):
    cargos = Cargo.objects.all()
    cargos_dict = [{
        "id":dep.pk,"Descripcion":dep.descripcion
    } for dep in cargos]
    return render(request,'cargos.jinja',{"table_body":cargos_dict})

def Contrato(request):
    contratos = TipoContrato.objects.all()
    contratos_dict = [{
        "id":dep.pk,"Descripcion":dep.descripcion
    } for dep in contratos]
    return render(request,'contrato.jinja',{"table_body":contratos_dict})

def Nominas(request):
    nominas = Rol.objects.all()
    nominas_dict = [{
        "Empleado":rol.empleado.nombre, "Anio Mes":rol.aniomes, "sueldo":rol.sueldo,
        "Horas Extra":rol.horas_extra,"Bono":rol.bono,"Iess":rol.iess,"Total":rol.tot_ing,
        "Descuento":rol.tot_des, "Neto":rol.neto
    } for rol in nominas]
    return render(request,'nominas.jinja',{"table_body":nominas_dict})
