
from django import forms
from dal import autocomplete

from articulo.models import Articulo
from empleado.models import Sucursal
from stock.models import Deposito, MovimientoArticulo
from usuario.models import Usuario


class MovimientoArticuloForm(forms.ModelForm):
    articulo_foraneo = forms.ModelChoiceField(
        queryset=Articulo.objects.all(),
        label="Articulo",
        widget=forms.Select()
    )
    deposito_foraneo = forms.ModelChoiceField(
        queryset=Deposito.objects.all(),
        label="Deposito",
        widget=forms.Select()
    )
    sucursal_foraneo = forms.ModelChoiceField(
        queryset=Sucursal.objects.all(),
        label="Sucursal",
        widget=forms.Select()
    )


    class Meta:
        model = MovimientoArticulo
        fields = ['articulo_foraneo', 'deposito_foraneo', 'cantidad', 'sucursal_foraneo','usuario', 'tipo']
    
    def _init_(self, *args, **kwargs):
        super(MovimientoArticuloForm, self)._init_(*args, **kwargs)
        self.fields['articulo_foraneo'].autocomplete=False


class MovimientoStockForm(autocomplete.FutureModelForm):
    content_object= autocomplete