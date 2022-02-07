from django.shortcuts import render

# Create your views here.
def curso (request):
    return render (request, 'AppCoder/curso.html')

def inicio (request):
    return render (request, 'AppCoder/index.html')

def estudiantes (request):
    return render (request, 'AppCoder/estudiantes.html')

def profesores (request):
    return render (request, 'AppCoder/profesores.html')

def entregas (request):
    return render (request, 'AppCoder/entregas.html')