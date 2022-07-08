from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):
    mensaje = """
    <h1>Universidad Nacional Tecnológica de Lima Sur</h1>
    <h1>EP Ingeniería de Sistemas</h1>
    <h1>Bienvenidos</h1>
    """
    return HttpResponse(mensaje)


def uc3(request):
    mensaje = """
    <h1>Lenguaje de Programación III</h1>
    <h2>Evaluación de la Unidad de Competencia 3</h2>
    <h2>Docente: Mg. Flor Elizabeth Cerdán León</h2>
    <h2>Integrantes:</h2>
    <ul>
        <li>Gomez Huamani Steve</li>
    </ul>
    
    """
    return HttpResponse(mensaje)


def noticia(request):
    mensaje = """
    <h1>Fiscalía incluyó a Norma Sánchez, esposa de Juan Silva, en investigación preliminar contra Zamir Villaverde por presunto lavado de activos</h1>
    <p>La fiscal Luz Taquire incluyó a Norma Sánchez Cordova, esposa del exministro de Transportes y Comunicaciones, Juan Silva, en la investigación preliminar seguida al empresario Zamir Villaverde y otros por presunto lavado de activos </p>  
    """
    return HttpResponse(mensaje)
