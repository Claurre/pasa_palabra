from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from juegoBD.models import Pregunta
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

def preparar_preguntas():

    lista_preguntas=[]
    abecedario=[]
        
    items=preguntas.objects.all()
    for item in items:
        pregunta=item.texto
        respuesta=item.respuesta
        letra=item.letra
        abecedario.append(item.letra)
        lista_preguntas.append(pregunta(preg,respuesta,letra))

    return [lista_preguntas,abecedario]

def comprobar_rptas(pregunta, rpta):
    """pregunta_normalizada=normalizar(pregunta.pregunta)
    rpta=normalizar(rpta)"""
    acierto=False
    if pregunta == rpta:
        acierto=True
    return acierto
     
    


def juego_visual(request, letra):
    #abecedario=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
    
    preg=preparar_preguntas()
    preguntas=preg[0]
    abecedario=preg[1]
    """externo=open("F:\inform\pip\proyecto_final\Pasa_palabra\Pasa_palabra\Templates\juego.html")"""
    externo=loader.get_template("juego.html")
    #plt=Template(externo.read())
    #externo.close
    
    i=abecedario.index(letra)
    pregunta=preguntas[i]

    """ctx=Context({"pregunta":pregunta, "abecedario":abecedario})"""
    #documento=plt.render(ctx)
    documento=externo.render({"pregunta":pregunta, "abecedario":abecedario})
    return HttpResponse(documento)




def juego_inicio(request):
    #abecedario=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
    preg=preparar_preguntas()
    preguntas=preg[0]
    abecedario=preg[1]
    
    """try
        respuesta=request.GET
        
        pregunta=preguntas[1]
        

    except
        pregunta=preguntas[0]"""

    
    
    externo=open("F:\inform\pip\proyecto_final\Pasa_palabra\Pasa_palabra\Templates\juego.html")
    plt=Template(externo.read())
    externo.close
    pregunta=preguntas[0]

    ctx=Context({"pregunta":pregunta, "abecedario":abecedario})
    documento=plt.render(ctx)
    return HttpResponse(documento)

   


