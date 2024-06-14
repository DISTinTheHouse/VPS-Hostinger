from django import forms
from .models import Producto, Pedido

# - PRODUCTO -
#-----------------

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'marca', 'modelo', 'anio', 'numero_parte', 'costo_proveedor', 'precio_venta', 'stock', 'imagen', 'compatible_modelos']


# - PEDIDOS -
#------------------

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['producto', 'cantidad', 'cliente', 'direccion_envio']
