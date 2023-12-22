
from django import forms
from dal import autocomplete
from queryset_sequence import QuerySetSequence
from articulo.models import Articulo
from empleado.models import Sucursal
from stock.models import Deposito, MovimientoArticulo
from usuario.models import Usuario



class MovimientoArticuloForm(autocomplete.FutureModelForm):
    lugar= autocomplete.Select2GenericForeignKeyModelField(
        queryset=QuerySetSequence(Deposito.objects.all(), Sucursal.objects.all()),
        label='Lugar',
        required=False,
    )

    class Meta:
        model = MovimientoArticulo
        fields = ['lugar', 'cantidad','usuario', 'tipo']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lugar'].label_from_instance = self.label_from_instance

    def label_from_instance(self, obj):
        # Personaliza cómo se muestra cada objeto en el campo queryset_sequence
        if isinstance(obj, Deposito):
            return f'DEPOSITO: {obj.nombre}'
        elif isinstance(obj, Sucursal):
            return f'SUCURSAL: {obj.nombre}'
        return str(obj)