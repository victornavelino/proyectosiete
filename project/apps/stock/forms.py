
from django import forms
from dal import autocomplete

from articulo.models import Articulo
from empleado.models import Sucursal
from stock.models import Deposito, MovimientoArticulo
from usuario.models import Usuario



class MovimientoArticuloForm(autocomplete.FutureModelForm):
    content_object= autocomplete.Select2GenericForeignKeyModelField(
        model_choice=[(Deposito, 'nombre')],
        widget=autocomplete.QuerySetSequenceSelect2,
    )

    class Meta:
        model = MovimientoArticulo
        fields = ['content_object', 'cantidad','usuario', 'tipo']