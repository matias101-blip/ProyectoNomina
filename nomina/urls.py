from django.urls import path
from .views import Inicio,Empleados,Departamentos,Cargos,Contrato,Nominas,Secion,singout,signin
urlpatterns = [
    path("",Inicio, name="Inicio"),
    path("listado/",Empleados, name="Lista"),
    path("departamento_listado/",Departamentos, name='ListadoDepartamento'),
    path("cargo_listado/",Cargos, name='ListadoCargo'),
    path("contrato_listado/",Contrato, name='ListadoContrato'),
    path("nominas_listado/",Nominas, name='ListadoNominas'),
    path("Secion/",Secion,name="Secion"),
    path("singout/",singout,name="singout"),
    path("signin/",signin,name="signin"),
]
