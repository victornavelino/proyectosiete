
from stock.models import ArticuloSucursal


def calcular_stock(form):
    if form.cleaned_data["articulo_foraneo"]:
        articulo_mov = form.cleaned_data["articulo_foraneo"]
        articulo_sucursal = ArticuloSucursal.objects.get(articulo=articulo_mov)