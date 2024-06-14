from django.urls import path
from . import views

urlpatterns = [
    # --- PRODUCTOS ---
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('agregar_varios/', views.agregar_varios_productos, name='agregar_varios_productos'),
    # --- PEDIDOS ---
    path('agregar_pedido/', views.agregar_pedido, name='agregar_pedido'),
]
