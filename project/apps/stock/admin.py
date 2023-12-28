from typing import Any
from django.contrib import admin, messages
from django.contrib.contenttypes.models import ContentType
from empleado.models import Sucursal
from stock.utils import calcular_stock
from stock.forms import MovimientoArticuloForm
from stock.models import Deposito, ArticuloSucursal, MovimientoArticulo, ArticuloDeposito


@admin.register(Deposito)
class DepositoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'domicilio',)
    search_fields = ('nombre',)
    list_per_page = 30


@admin.register(ArticuloSucursal)
class ArticuloSucursalAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'sucursal','cantidad')
    search_fields = ('articulo',)
    list_per_page = 30

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True
     
    def save_model(self, request, obj, form, change):
        messages.error(request, 'No Puede modificar movimientos desde este panel')
        return False


@admin.register(ArticuloDeposito)
class ArticuloDepositoAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'deposito','cantidad')
    search_fields = ('articulo',)
    list_per_page = 30


@admin.register(MovimientoArticulo)
class MovimientoArticuloAdmin(admin.ModelAdmin):
    form = MovimientoArticuloForm
    list_display = ('lugar', 'articulo', 'cantidad', 'fecha', 'tipo')
    search_fields = ('articulo',)
    list_per_page = 30

    def lugar(self, obj):
        from django.contrib.contenttypes.models import ContentType
        ct = ContentType.objects.get_for_id(obj.lugar_type.id)
        print('imprimo contentype')
        print(ct.model_class)
        obj_get = ct.get_object_for_this_type(pk=obj.lugar_object_id)
        return obj_get.nombre

    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        
        if form.cleaned_data["articulo_foraneo"]:
            obj.articulo = form.cleaned_data["articulo_foraneo"].nombre
        if form.cleaned_data["usuario_foraneo"]:
            obj.usuario = form.cleaned_data["usuario_foraneo"]
        if isinstance(obj.lugar, Sucursal):
            print('Sucursalaaaaaaaaaaaa')
            try:

                articulo_sucursal=ArticuloSucursal.objects.get(articulo=form.cleaned_data["articulo_foraneo"],
                                                         sucursal=form.cleaned_data["lugar"])
                if obj.tipo=='ingreso':                                        
                    articulo_sucursal.cantidad+=obj.cantidad
                else:
                    articulo_sucursal.cantidad-=obj.cantidad
                articulo_sucursal.save()
            except:
                ArticuloSucursal.objects.create(articulo=form.cleaned_data["articulo_foraneo"],
                                            sucursal=form.cleaned_data["lugar"],
                                            cantidad=obj.cantidad)
        if isinstance(obj.lugar, Deposito):
            print('Depositooooooooooooooo')
            try:
                articulo_deposito=ArticuloDeposito.objects.get(articulo=form.cleaned_data["articulo_foraneo"],
                                                         deposito=form.cleaned_data["lugar"])
                if obj.tipo=='ingreso': 
                    articulo_deposito.cantidad+=obj.cantidad
                else:
                    articulo_deposito.cantidad-=obj.cantidad
                articulo_deposito.save()
            except:
                ArticuloDeposito.objects.create(articulo=form.cleaned_data["articulo_foraneo"],
                                            deposito=form.cleaned_data["lugar"],
                                            cantidad=obj.cantidad)
        
        obj.save()
    
