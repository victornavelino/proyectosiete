
from django import forms
from dal import autocomplete
from queryset_sequence import QuerySetSequence
from django.core.exceptions import ValidationError
from articulo.models import Articulo
from empleado.models import Sucursal
from stock.models import Deposito, MovimientoArticulo
from usuario.models import Usuario
from django.contrib.contenttypes.models import ContentType


class MovimientoArticuloForm(autocomplete.FutureModelForm):

    origen= autocomplete.Select2GenericForeignKeyModelField(
        queryset=QuerySetSequence(Deposito.objects.all(), Sucursal.objects.all()),
        label='Origen',
        required=False,
    )   

    destino= autocomplete.Select2GenericForeignKeyModelField(
        queryset=QuerySetSequence(Deposito.objects.all(), Sucursal.objects.all()),
        label='Destino',
        required=True,
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
        fields = ['origen','destino', 'articulo_foraneo', 'cantidad','usuario_foraneo', 'observaciones']

    def clean(self):
        cleaned_data = super().clean()
        origen = cleaned_data.get('origen')
        destino = cleaned_data.get('destino')

        # Validar que al menos uno de los campos de ContentType no esté vacío
        print('IMPRIMO VALIDACION CLEAN DE FORMULARIO')
        print(origen)
        print(destino)
        if not origen and not destino:
            print('ENTRO IF')
            raise ValidationError("Debes seleccionar al menos un contenido.")
        return cleaned_data

    def clean_origen(self):
        origen = self.cleaned_data['origen']
        print('imprimo validacion origen')
        #print(origen)
        if not origen:
            origen = 'Externo'
            #raise ValidationError("Campo origen de ContentType no puede estar vacío.")
        return origen  
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['origen'].label_from_instance = self.label_from_instance
        self.fields['destino'].label_from_instance = self.label_from_instance

    def label_from_instance(self, obj):
        # Personaliza cómo se muestra cada objeto en el campo queryset_sequence
        if isinstance(obj, Deposito):
            return f'DEPOSITO - {obj.nombre}'
        elif isinstance(obj, Sucursal):
            return f'SUCURSAL - {obj.nombre}'
        return str(obj)
    