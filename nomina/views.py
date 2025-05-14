from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from nomina.forms import EmpleadoForm, FormCargo, FormContrato, FormDepartamento, RolPago
from nomina.models import Cargo, Departamento, Empleado, Rol, TipoContrato

# Create your views here.

# Vistas para presentar
def Inicio(request):
    return render(request,'Inicio.jinja')

def Empleados(request):
    empleados = Empleado.objects.all()
    empleados_dict = [{"id":emp.pk,"Nombre":emp.nombre, "Cedula":emp.cedula,"Direccion":emp.direccion,"Sexo":emp.sexo,"Sueldo":emp.sueldo,"Cargo":emp.cargo.descripcion,"Departamento":emp.departamento.descripcion,"Contrato":emp.tipo_contrato.descripcion} for emp in empleados]
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
        "id":rol.pk,"Empleado":rol.empleado.nombre, "Anio Mes":rol.aniomes, "sueldo":rol.sueldo,
        "Horas Extra":rol.horas_extra,"Bono":rol.bono,"Iess":rol.iess,"Total":rol.tot_ing,
        "Descuento":rol.tot_des, "Neto":rol.neto
    } for rol in nominas]
    return render(request,'nominas.jinja',{"table_body":nominas_dict})

# Vistas de crear
def CrearEmpleado(request):
    if request.method == "POST":
        print("Hoyeee")
        formulario = EmpleadoForm(request.POST);
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            sueldo = formulario.cleaned_data['sueldo']
            cedula = formulario.cleaned_data['cedula']
            direccion = formulario.cleaned_data['direccion']
            sexo_choice = dict(Empleado.SEXO_CHOICES)
            sexo = sexo_choice[formulario.cleaned_data['sexo']]
            cargo = Cargo.objects.get(descripcion=formulario.cleaned_data['cargo'])
            departamento = Departamento.objects.get(descripcion=formulario.cleaned_data['departamento'])
            tipo_contrato = TipoContrato.objects.get(descripcion=formulario.cleaned_data['tipo_contrato'])
            empleado = Empleado(
                nombre=nombre, cedula=cedula, direccion=direccion,sexo=sexo,
                cargo=cargo, departamento=departamento,tipo_contrato=tipo_contrato, sueldo = sueldo
            )
            empleado.save()
            return redirect("Lista")
        else:
            return HttpResponse(formulario.errors.as_json())
    else:
        formulario = EmpleadoForm()
    return render(request,'crear_empleado.jinja',{'formulario':formulario})

def CrearNominas(request):
    if request.method == "POST":
        formulario = RolPago(request.POST);
        if formulario.is_valid():
            empleado = Empleado.objects.get(nombre=formulario.cleaned_data["empleado"])
            aniomes = formulario.cleaned_data["aniomes"]
            horas_extra = formulario.cleaned_data['horas_extra']
            bono = float(formulario.cleaned_data['bono'])
            sueldo = float(empleado.sueldo)
            iess = 0.0945
            tot_ing= sueldo + float(horas_extra) + bono
            tot_des = iess * sueldo
            neto = tot_ing - tot_des
            Nomina = Rol(empleado=empleado, aniomes=aniomes, horas_extra=int(horas_extra), bono=bono,
                         sueldo=sueldo,iess=iess * float(100),tot_ing=tot_ing,tot_des=tot_des,neto=neto)
            Nomina.save()
            return redirect("Lista")
    else:
        formulario = RolPago()
    return render(request,'crear_nominas.jinja',{'formulario':formulario})

def CrearCargo(request):
    if request.method == "POST":
        formulario = FormCargo(request.POST);
        if formulario.is_valid():
            descripcion = formulario.cleaned_data['descripcion']
            cargo = Cargo(descripcion=descripcion)
            cargo.save()
            return redirect("Lista")
    else:
        formulario = FormCargo()
    return render(request,'crear_cargo.jinja',{'formulario':formulario,"tipo":"Cargo","name":"Crear_Cargo"})

def CrearDepartamento(request):
    if request.method == "POST":
        formulario = FormDepartamento(request.POST);
        if formulario.is_valid():
            descripcion = formulario.cleaned_data['descripcion']
            departamento = Departamento(descripcion=descripcion)
            departamento.save()
            return redirect("Lista")
    else:
        formulario = FormDepartamento()
    return render(request,'crear_cargo.jinja',{'formulario':formulario, "tipo":"Departamento","name":"Crear_Departamento"})

def CrearContrato(request):
    if request.method == "POST":
        formulario = FormContrato(request.POST);
        if formulario.is_valid():
            descripcion = formulario.cleaned_data['descripcion']
            contrato = TipoContrato(descripcion=descripcion)
            contrato.save()
            return redirect("Lista")
    else:
        formulario = FormCargo()
    return render(request,'crear_cargo.jinja',{'formulario':formulario, "tipo":"Contrato","name":"Crear_Contrato"})
# Vistas de actulizar
def UpdateEmpleado(request,id):
    if request.method == "POST":
        formulario = EmpleadoForm(request.POST,instance=Empleado.objects.get(pk=id))
        if formulario.is_valid():
            empleado = formulario.save(commit=False)
            SEXO_CHOICES = dict(Empleado.SEXO_CHOICES)
            sexo = SEXO_CHOICES[formulario.cleaned_data['sexo']]
            empleado.sexo = sexo
            empleado.save()
            return HttpResponseRedirect("/listado/")
    else:
        empleado = Empleado.objects.get(pk=id)
        formulario = EmpleadoForm(instance=empleado)
    return render(request,'update_empleado.jinja',{"formulario":formulario, 'id':id})

def UpdateNomina(request,id):
    if request.method == "POST":
        formulario = RolPago(request.POST,instance=Rol.objects.get(pk=id))
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/listado/")
    else:
        empleado = Rol.objects.get(pk=id)
        formulario = RolPago(instance=empleado)
    return render(request,'update_nomina.jinja',{"formulario":formulario, 'id':id})

def UpdateDepartamento(request,id):
    if request.method == "POST":
        formulario = FormDepartamento(request.POST,instance=Departamento.objects.get(pk=id))
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/listado/")
    else:
        departamento = Departamento.objects.get(pk=id)
        formulario = FormDepartamento(instance=departamento)

    return render(request,'update_cargo.jinja',{'formulario':formulario, "tipo":"Departamento","name":"Update_Departamento",'id':id})


def UpdateCargo(request,id):
    if request.method == "POST":
        formulario = FormCargo(request.POST,instance=Cargo.objects.get(pk=id))
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/listado/")
    else:
        cargo = Cargo.objects.get(pk=id)
        formulario = FormCargo(instance=cargo)
    return render(request,'update_cargo.jinja',{'formulario':formulario, "tipo":"Cargo","name":"Update_Cargo",'id':id})

def UpdateContrato(request,id):
    if request.method == "POST":
        formulario = FormContrato(request.POST,instance=TipoContrato.objects.get(pk=id))
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/listado/")
    else:
        contrato = TipoContrato.objects.get(pk=id)
        formulario = FormCargo(instance=contrato)
    return render(request,'update_cargo.jinja',{'formulario':formulario, "tipo":"Contrato","name":"Update_Contrato",'id':id})

# Delate
def Eliminar(request,id,modelo):
    if modelo == "Empleado":
        modelo = Empleado.objects.get(pk=id)
    elif modelo == "Nomina":
        modelo = Rol.objects.get(pk=id)
    elif modelo == "Cargo":
        modelo = Cargo.objects.get(pk=id)
    elif modelo == "Departamento":
        modelo = Departamento.objects.get(pk=id)
    elif modelo == "Contrato":
        modelo = TipoContrato.objects.get(pk=id)
    modelo.delete()
    return HttpResponseRedirect("/listado/")
