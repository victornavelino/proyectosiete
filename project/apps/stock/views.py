from django.http import HttpResponse
from django.shortcuts import render
import json
from django.core import serializers
from stock.models import ArticuloDeposito

# Create your views here.
def get_articulos_deposito(request, id_deposito):
    if request.user.is_authenticated:
        print("id deposito que viene del front")
        print(id_deposito)
        articulosdeposito = ArticuloDeposito.objects.filter(pk=id_deposito)
        if len(articulosdeposito) > 0:
            results = []
            for articulo in articulosdeposito:
                json_valores = {
                    "id_articulo": str(articulo.pk),
                    "nombre": articulo.nombre,
                    "deposito": articulo.deposito
                    }
                results.append(json_valores)
            data = json.dumps(results)
        else:
            json_valores = {'error': 'El Deposito No tiene articulos'}
            data = json.dumps(json_valores)
        
    else:
        valores = {}
        data = serializers.serialize('json', valores)
    return HttpResponse(data, content_type="application/json")

