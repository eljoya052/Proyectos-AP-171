from cgitb import reset
from django.shortcuts import render
from persona_APP.models import persona, proyecto
from persona_APP.forms import FormProyecto

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

def agregarproyecto(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarproyecto.html', data)
