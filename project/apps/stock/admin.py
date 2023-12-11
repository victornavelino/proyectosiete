from django.contrib import admin, messages
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
        if form.cleaned_data["usuario"]:
            obj.usuario = form.cleaned_data["usuario"]

        try:

            articulo_sucursal=ArticuloSucursal.objects.get(articulo=form.cleaned_data["articulo_foraneo"],
                                                         sucursal=form.cleaned_data["sucursal_foraneo"])
            articulo_sucursal.cantidad+=obj.cantidad
            articulo_sucursal.save()
        except:
            ArticuloSucursal.objects.create(articulo=form.cleaned_data["articulo_foraneo"],
                                            sucursal=form.cleaned_data["sucursal_foraneo"],
                                            cantidad=obj.cantidad)
        obj.save()

        




    def get_form(self, request, obj=None, *args, **kwargs):
        form = super(MovimientoArticuloAdmin, self).get_form(request, *args, **kwargs)
        print(request.user.username)
        if obj is None:
            form.base_fields['usuario'].initial = str(request.user.username)
        else:
            form.base_fields['usuario'].initial = obj.usuario
        form.base_fields['usuario'].disabled = True
        return form
"""   
    def has_add_permission(self, form):
        self.readonly_fields=['usuario',]
        return True
    
    def has_change_permission(self, request, obj=None):
        self.readonly_fields=['usuario',]
        return True
"""

    