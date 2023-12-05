from django.contrib import admin
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


@admin.register(ArticuloDeposito)
class ArticuloDepositoAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'deposito','cantidad')
    search_fields = ('articulo',)
    list_per_page = 30


@admin.register(MovimientoArticulo)
class MovimientoArticuloAdmin(admin.ModelAdmin):
    form = MovimientoArticuloForm
    list_display = ('articulo', 'deposito','sucursal','cantidad', 'fecha', 'tipo', 'usuario')
    search_fields = ('articulo', 'deposito',)
    list_per_page = 30

    def save_model(self, request, obj, form, change):
        # Al guardar, copiar el contenido del campo_texto de la instancia relacionada
        if form.cleaned_data["articulo_foraneo"]:
            obj.articulo = form.cleaned_data["articulo_foraneo"].nombre
        if form.cleaned_data["deposito_foraneo"]:
            obj.deposito = form.cleaned_data["deposito_foraneo"].nombre
        if form.cleaned_data["sucursal_foraneo"]:
            obj.sucursal = form.cleaned_data["sucursal_foraneo"].nombre
        if form.cleaned_data["usuario_foraneo"]:
            obj.usuario = form.cleaned_data["usuario_foraneo"]
        obj.save()
    