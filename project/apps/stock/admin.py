from django.contrib import admin

from stock.models import Deposito, ArticuloSucursal

# Register your models here.
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