
from django import forms
from dal import autocomplete
from queryset_sequence import QuerySetSequence
from articulo.models import Articulo
from empleado.models import Sucursal
from stock.models import Deposito, MovimientoArticulo
from usuario.models import Usuario



class MovimientoArticuloForm(autocomplete.FutureModelForm):

    origen= autocomplete.Select2GenericForeignKeyModelField(
        queryset=QuerySetSequence(Deposito.objects.all(), Sucursal.objects.all()),
        label='Origen',
        required=False,
    )

    destino= autocomplete.Select2GenericForeignKeyModelField(
        queryset=QuerySetSequence(Deposito.objects.all(), Sucursal.objects.all()),
        label='Destino',
        required=False,
    )

    articulo_foraneo = forms.ModelChoiceField(
        queryset=Articulo.objects.all(),
        label="Articulo",
        widget=forms.Select()
    )

    usuario_foraneo = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        label="Usuario",
        widget=forms.Select()
    )

    class Meta:
        model = MovimientoArticulo
        fields = ['origen','destino', 'articulo_foraneo', 'cantidad','usuario_foraneo']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['origen'].label_from_instance = self.label_from_instance
        self.fields['destino'].label_from_instance = self.label_from_instance

    def label_from_instance(self, obj):
        # Personaliza cómo se muestra cada objeto en el campo queryset_sequence
        if isinstance(obj, Deposito):
            return f'DEPOSITO: {obj.nombre}'
        elif isinstance(obj, Sucursal):
            return f'SUCURSAL: {obj.nombre}'
        return str(obj)