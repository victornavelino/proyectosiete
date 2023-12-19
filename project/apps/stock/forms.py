
from django import forms
from dal import autocomplete
from queryset_sequence import QuerySetSequence
from articulo.models import Articulo
from empleado.models import Sucursal
from stock.models import Deposito, MovimientoArticulo
from usuario.models import Usuario



class MovimientoArticuloForm(autocomplete.FutureModelForm):
    content_object= autocomplete.Select2GenericForeignKeyModelField(
        queryset=QuerySetSequence(Deposito.objects.all(), Sucursal.objects.all()),
        label='Lugar',
        required=False,
    )

    class Meta:
        model = MovimientoArticulo
        fields = ['content_object', 'cantidad','usuario', 'tipo']