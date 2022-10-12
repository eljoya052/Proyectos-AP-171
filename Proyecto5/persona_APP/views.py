from django.shortcuts import render
from persona_APP.models import persona
# Create your views here.

def personadata(request):
    personas = persona.objects.all()
    data = {'personas' : personas}
    return render(request, 'empleados.html', data)
