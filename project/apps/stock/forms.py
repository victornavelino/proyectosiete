
from django import forms

from articulo.models import Articulo
from stock.models import MovimientoArticulo


class MovimientoArticuloForm(forms.ModelForm):
    articulo_foraneo = forms.ModelChoiceField(
        queryset=Articulo.objects.all(),
        label="Articulo",
        widget=forms.Select()
    )

    class Meta:
        model = MovimientoArticulo
        fields = ['articulo_foraneo', 'cantidad']