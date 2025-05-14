from django.urls import path
from .views import *
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
    # Urls de creacion
    path("crear_empleado",CrearEmpleado, name="Crear_Empleado"),
    path("crear_nominas/",CrearNominas,name="Crear_Nomina"),
    path("crear_cargo/",CrearCargo,name="Crear_Cargo"),
    path("crear_departamento/",CrearDepartamento,name="Crear_Departamento"),
    path("crear_contrato/",CrearContrato,name="Crear_Contrato"),
    # Urls de Update
    path("update_empleado/<int:id>/",UpdateEmpleado,name="Update_Empleado"),
    path("update_nomina/<int:id>/",UpdateNomina,name="Update_Nomina"),
    path("update_cargo/<int:id>/",UpdateCargo,name="Update_Cargo"),
    path("update_departamento/<int:id>/",UpdateDepartamento,name="Update_Departamento"),
    path("update_contrato/<int:id>/",UpdateContrato,name="Update_Contrato"),
    path('delate/<str:modelo>/<int:id>',Eliminar,name="Eliminar")
]
