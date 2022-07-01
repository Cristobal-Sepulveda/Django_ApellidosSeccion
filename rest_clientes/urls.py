from django.urls import path 
from .views import lista_clientes
from rest_clientes.views import lista_clientes, detalle_cliente
from rest_clientes.viewslogin import login_api

urlpatterns = [ 
    path('lista_clientes', lista_clientes, name="lista_clientes"),
    path('detalle_cliente/<id>', detalle_cliente, name="detalle_cliente" ),
    path('login_api', login_api, name="login_api"),
]