from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    data = {"nombre" : "Pedro", "apellido":"Gaete"}
    return render(request, 'templatesApp/miplantilla.html', data)

