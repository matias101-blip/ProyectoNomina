from django.urls import path
from .views import Inicio, Lista
urlpatterns = [
    path("",Inicio, name="Inicio"),
    path("listado/",Lista, name="Lista"),
]
