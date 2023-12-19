from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from articulo.models import Articulo

from empleado.models import Sucursal
from usuario.models import Usuario

# Create your models here.
class Deposito(models.Model):
    class Meta:
        verbose_name = 'Deposito'
        verbose_name_plural = 'Depositos'
        ordering = ['-id']

    nombre = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    domicilio = models.CharField(max_length=100, verbose_name='Domicilio', unique=True)

    def __str__(self):
        return f'{self.nombre}'
    
    @staticmethod
    def autocomplete_search_fields():
        return 'nombre',

    

class ArticuloSucursal(models.Model):
    class Meta:
        verbose_name =  'Articulo Sucursal'
        verbose_name_plural = 'Articulos Sucursal'

    def __str__(self):
        return self.name
    
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name='Articulo')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, verbose_name='Sucursal')
    cantidad = models.PositiveIntegerField(null=False, verbose_name='Cantidad')

    def __str__(self):
        return f'{self.sucursal}'


class ArticuloDeposito(models.Model):
    class Meta:
        verbose_name =  'Articulo Deposito'
        verbose_name_plural = 'Articulos Deposito'

    def __str__(self):
        return self.name
    
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name='Articulo')
    deposito = models.ForeignKey(Deposito, on_delete=models.CASCADE, verbose_name='Deposito')
    cantidad = models.PositiveIntegerField(null=False, verbose_name='Cantidad')

    def __str__(self):
        return f'{self.articulo}, {self.deposito}'


class MovimientoArticulo(models.Model):
    class Meta:
        verbose_name = 'Movimiento de articulo'
        verbose_name_plural = 'Movimientos de articulos'
    
    # Objeto genérico
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    # Fin Objeto generico ajaja
    articulo = models.CharField(max_length=100, default='', verbose_name='Articulo') 
    cantidad = models.IntegerField(null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    usuario = models.CharField(max_length=50, default='', verbose_name='Usuario')

    def __str__(self):
        return f"{self.tipo} de {self.cantidad} unidades de {self.articulo} el {self.fecha}"
    

class MovimientoStock(models.Model):
    class Meta:
        verbose_name = 'Movimiento de Stock'
        verbose_name_plural = 'Movimientos de Stock'
    

    cantidad = models.IntegerField(null=False)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    usuario = models.CharField(max_length=50, default='', verbose_name='Usuario')
