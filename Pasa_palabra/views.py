from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
"""este código es provisorio y va a cambiar"""

def menu_inicio (request):
    temas=("Anime","Cine","Videojuegos","Ciencia","Tecnología","Historia","Mitología","Literatura","Arte","testeo","Deportes","Manga",)
    externo=loader.get_template("index.html")
    """plt=Template(externo.read("F:\inform\pip\proyecto_final\Pasa_palabra\Pasa_palabra\Templates\index.html"))
    externo.close
    ctx=Context({"Temas":temas})
    documento=externo.render(ctx)"""
    documento=externo.render({"Temas":temas})
    return HttpResponse(documento)

#clase pregunta temporal hasta haber base de datos
class Pregunta(object):
    def __init__(self, pregunta, respuesta, letra):
        self.pregunta=pregunta
        self.respuesta=respuesta
        self.letra=letra

"""def normalizar(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s"""

def preparar_preguntas(abecedario):
    preguntas=[]
    for letra in abecedario:
        preguntas.append(Pregunta("Pregunta de prueba, la respuesta es 'probando'.","probando",letra))
    return preguntas

def comprobar_rptas(pregunta, rpta):
    """pregunta_normalizada=normalizar(pregunta.pregunta)
    rpta=normalizar(rpta)"""
    acierto=False
    if pregunta == rpta:
        acierto=True
    return acierto
     
    


def juego_visual(request, letra):
    abecedario=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
    
    preguntas=preparar_preguntas(abecedario)
    externo=open("F:\inform\pip\proyecto_final\Pasa_palabra\Pasa_palabra\Templates\juego.html")
    plt=Template(externo.read())
    externo.close
    i=abecedario.index(letra)
    pregunta=preguntas[i]

    ctx=Context({"pregunta":pregunta, "abecedario":abecedario})
    documento=plt.render(ctx)
    return HttpResponse(documento)


