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
        return False
     
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
    list_display = ('lugar_descripcion', 'articulo', 'cantidad', 'fecha', 'tipo', 'usuario')
    search_fields = ('articulo',)
    list_per_page = 30

    def lugar_descripcion(self, obj):
        content_type_deposito = ContentType.objects.get_for_model(Deposito)
        content_type_sucursal = ContentType.objects.get_for_model(Sucursal)

        obj = content_type_sucursal.get_object_for_this_type(id=obj.lugar_id)
        print(obj)
        return obj


