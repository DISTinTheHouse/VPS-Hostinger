from django.db import models

#------------------------------------------
# -- PRODUCTO --

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    anio = models.PositiveIntegerField(blank=True, null=True)
    numero_parte = models.CharField(max_length=100, unique=True)
    costo_proveedor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/img/', blank=True, null=True)
    compatible_modelos = models.TextField(blank=True, null=True, help_text="Lista de modelos compatibles")

    def __str__(self):
        return f"{self.nombre} ({self.numero_parte})"

    @property
    def margen(self):
        if self.costo_proveedor and self.precio_venta:
            return self.precio_venta - self.costo_proveedor
        return None

    @property
    def disponible(self):
        return self.stock > 0 if self.stock is not None else False



#------------------------------------------
# -- PEDIDOS --

class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=255)
    direccion_envio = models.TextField()

    def __str__(self):
        return f'Pedido #{self.id} - {self.producto.nombre}'

    def save(self, *args, **kwargs):
        producto = self.producto
        if producto.stock >= self.cantidad:
            producto.stock -= self.cantidad
            producto.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError('No hay suficiente stock para este pedido')
