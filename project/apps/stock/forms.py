
from django import forms

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
    usuario_foraneo = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        label="Usuario",
        widget=forms.Select()
    )

    class Meta:
        model = MovimientoArticulo
        fields = ['articulo_foraneo', 'deposito_foraneo', 'cantidad', 'sucursal_foraneo','usuario_foraneo']