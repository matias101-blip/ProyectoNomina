from django.http import HttpResponse
from django.shortcuts import render

from nomina.models import Cargo, Departamento, Empleado, Rol, TipoContrato

# Create your views here.
def Inicio(request):
    return render(request,'Inicio.jinja')

def Empleados(request):
    empleados = Empleado.objects.all()
    empleados_dict = [{"Nombre":emp.nombre, "Cedula":emp.cedula,"Direccion":emp.direccion,"Sexo":emp.sexo,"Sueldo":emp.sueldo,"Cargo":emp.cargo.descripcion,"Departamento":emp.departamento.descripcion,"Contrato":emp.tipo_contrato.descripcion} for emp in empleados]
    return render(request, 'lista_nominas.jinja',{"table_body":empleados_dict})

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
