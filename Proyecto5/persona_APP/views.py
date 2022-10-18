from django.shortcuts import render
from persona_APP.models import persona, proyecto
# Create your views here.

def personadata(request):
    personas = persona.objects.all()
    data = {'personas' : personas}
    return render(request, 'empleados.html', data)

def index(request):
    return render(request, 'index.html')

def listadoproyectos(request):
    proyectos = proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request, 'proyectos.html', data)

