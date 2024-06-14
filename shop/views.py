from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd
# FORMS
from .forms import ProductoForm, PedidoForm
# MODELS
from .models import Producto


#------------------------------------------
# -- PRODUCTOS --

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu producto se guardó correctamente.')
            return redirect('agregar_producto')
        else:
            messages.error(request, 'Hubo un error, no se guardó el producto. Intenta nuevamente o contacta a sistemas.')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

@login_required
def agregar_varios_productos(request):
    if request.method == 'POST' and 'submit_excel' in request.POST:
        excel_file = request.FILES['excel_file']
        try:
            df = pd.read_excel(excel_file)
            for _, row in df.iterrows():
                Producto.objects.create(
                    nombre=row['Nombre'],
                    descripcion=row.get('Descripción', ''),
                    marca=row.get('Marca', ''),
                    modelo=row.get('Modelo', ''),
                    anio=row.get('Año', None),
                    numero_parte=row['Número de Parte'],
                    costo_proveedor=row.get('Costo al Proveedor', 0),
                    precio_venta=row.get('Precio de Venta', 0),
                    stock=row.get('Stock', 0),
                    compatible_modelos=row.get('Modelos Compatibles', ''),
                )
            messages.success(request, 'Los productos se subieron correctamente.')
        except Exception as e:
            messages.error(request, f'Hubo un error al subir los productos: {str(e)}')
        return redirect('agregar_producto')
    return render(request, 'productos/agregar_producto.html')

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})



#------------------------------------------
# -- PEDIDOS --

@login_required
def agregar_pedido(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'El pedido se guardó correctamente.')
            except ValueError as e:
                messages.error(request, str(e))
            return redirect('agregar_pedido')
        else:
            messages.error(request, 'Hubo un error, por favor revise el formulario.')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/agregar_pedido.html', {'form': form, 'productos': productos})