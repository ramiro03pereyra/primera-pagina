from django.urls import path, include
from .views import inicio, lista_productos_template, cargar_producto, lista_proveedores, crear_proveedor, lista_pedidos, crear_pedido
urlpatterns = [
    path('', inicio, name = "inicio" ),
  
    path('lista-productos/', lista_productos_template, name="lista-productos/"), 
    path('cargar-producto/', cargar_producto, name='cargar_producto/'),
  
    path('lista-proveedores/', lista_proveedores , name='lista_proveedores'),
    path("proveedores/crear/", crear_proveedor, name="crear_proveedor"), 
   
    path("pedidos/", lista_pedidos, name="lista_pedidos"),#tengo que modificarlos
    path("pedidos/crear/", crear_pedido, name="crear_pedido"),#no se ve nada
]
    