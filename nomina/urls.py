from django.urls import path
from .views import Inicio, Lista,Secion
urlpatterns = [
    path("",Inicio, name="Inicio"),
    path("listado/",Lista, name="Lista"),
    path("Secion/",Secion,name="Secion")
]
