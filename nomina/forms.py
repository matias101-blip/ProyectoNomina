#!/usr/bin/env python3
from django.forms import CharField, ChoiceField, ModelForm, ModelChoiceField, DateField, DecimalField, NumberInput, Select, TextInput, DateInput
from .models import Cargo, Departamento, Empleado, Rol, TipoContrato

class RolPago(ModelForm):
    empleado = ModelChoiceField(
        queryset = Empleado.objects.all(),
        label = "Empleado",
        empty_label="Seleccione el empleado",
        widget=Select(attrs={'class':'form-select'})
    )
    aniomes = DateField(label="Anio y mes", widget=DateInput(attrs={'type':'date','class':'form-control'}))
    horas_extra = DecimalField(label="Horas extras",widget=NumberInput(attrs={'class':'form-control'}))
    bono = DecimalField(label="Bono",widget=NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = Rol
        fields = ["empleado","aniomes","horas_extra","bono"]

class EmpleadoForm(ModelForm):
    nombre = CharField(widget=TextInput(attrs={'class':'form-control'}))
    cedula = CharField(widget=TextInput(attrs={'class':'form-control'}))
    direccion = CharField(widget=TextInput(attrs={'class':'form-control'}))
    sexo = ChoiceField(
        choices=Empleado.SEXO_CHOICES,
        widget=Select(attrs={'class':'form-control'})
    )
    sueldo = DecimalField(widget=NumberInput(attrs={'class':'form-control'}))
    cargo = ModelChoiceField(
        queryset=Cargo.objects.all(),
        empty_label="Seleccione el cargo",
        widget=Select(attrs={'class':'form-select'})
    )

    departamento = ModelChoiceField(
        queryset=Departamento.objects.all(),
        empty_label="Seleccione su departamento",
        widget=Select(attrs={'class':'form-select'})
    )

    tipo_contrato = ModelChoiceField(
        queryset=TipoContrato.objects.all(),
        empty_label="Seleccione su tipo de contrato",
        widget=Select(attrs={'class':'form-select'})
    )

    class Meta:
        model = Empleado
        fields = ["nombre","cedula","direccion","sexo","sueldo","cargo","departamento","tipo_contrato"]

class FormDepartamento(ModelForm):
    descripcion = CharField(widget=TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Departamento
        fields = ['descripcion']

class FormCargo(ModelForm):
    descripcion = CharField(widget=TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Cargo
        fields = ['descripcion']

class FormContrato(ModelForm):
    descripcion = CharField(widget=TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = TipoContrato
        fields = ['descripcion']
