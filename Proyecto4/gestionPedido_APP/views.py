from http.client import HTTPResponse
from math import hypot
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedido_APP.models import Producto

# Create your views here.
def busqueda_producto(request):
    return render(request, "busqueda_producto.html")

def buscar(request):
    if request.GET["prd"]:
        #mensaje="Producto buscado: %r" %request.GET["prd"]
        produ = Producto.objects.filter(nombre__icontains=produ)
        return render(request, "resultados.html", {"productos":produ, "query":produ})
    else:
        mensaje="No has instroducido nada de nada"
    return HttpResponse(mensaje)