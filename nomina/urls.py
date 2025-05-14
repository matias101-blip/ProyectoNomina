from django.urls import path
from .views import *
urlpatterns = [
    path("",Inicio, name="Inicio"),
    path("listado/",Empleados, name="Lista"),
    path("departamento_listado/",Departamentos, name='ListadoDepartamento'),
    path("cargo_listado/",Cargos, name='ListadoCargo'),
    path("contrato_listado/",Contrato, name='ListadoContrato'),
    path("nominas_listado/",Nominas, name='ListadoNominas'),
]
