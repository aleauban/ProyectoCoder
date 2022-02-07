from django.urls import path
from AppCoder.views import curso, entregas, inicio, estudiantes, profesores

urlpatterns = [
    path('curso/', curso, name="AppCoderCurso"),
    path('inicio/', inicio, name="AppCoderInicio"),
    path('estudiantes/', estudiantes, name="AppCoderEstudiantes"),
    path('profesores/', profesores, name="AppCoderProfesores"),
    path('entregas/', entregas, name="AppCoderEntregas"),
]