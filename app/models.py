from django.db import models
from django.contrib.auth.models import User

class Colaborador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)  # Fecha de inicio de trabajo
    dias_vacaciones = models.IntegerField(null=True, blank=True)  # Días de vacaciones totales
    dias_vacaciones_disponibles = models.IntegerField(null=True, blank=True)  # Días de vacaciones disponibles
    cantidad_permisos = models.IntegerField(null=True, blank=True)  # Cantidad de permisos
    puesto = models.CharField(max_length=100, null=True, blank=True)  # Puesto del colaborador
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Salario del colaborador
    departamento = models.CharField(max_length=100, null=True, blank=True)  # Departamento del colaborador
    supervisor = models.CharField(max_length=100, null=True, blank=True)  # Supervisor del colaborador
    notas = models.TextField(null=True, blank=True)  # Notas adicionales
    creado_en = models.DateTimeField(auto_now_add=True)
    
    # Roles
    es_vendedor = models.BooleanField(default=False)
    es_administrativo = models.BooleanField(default=False)
    es_almacen = models.BooleanField(default=False)
    tiene_acceso_total = models.BooleanField(default=False)

    def __str__(self):
        return self.correo
