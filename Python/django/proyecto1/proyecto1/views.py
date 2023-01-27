from django.http import HttpResponse
import datetime

def saludo(request): # primera vista
    
    documento = """
    <html>
        <body>
            <h1> Hola mundo. Primera pagina con django. </h1>
        </body>
    </html>"""
    
    
    return HttpResponse(documento)  # Esto no es lo mejor pero es para editar el texto. 


def despedida(request):
    return HttpResponse("Ya largate perro. ")

    
def hora(request):
    fecha = datetime.datetime.now()
    
    fecha1 = f"""
    <html>
        <body>
            <h1> Fecha y hora actuales {fecha} </h1>
        </body>
    </html>"""
    
    return HttpResponse(fecha1)

def calcula_edad(request, edad, agno): # Esta funcion es para que pongas un parametro en la url pero casi no es muy usada pero es bueno saber. 
    # edadActual = 24
    
    periodo = agno - 2022
    edadfutura = edad + periodo
    
    documento = f"""
    <html>
        <body>
            <h1> En el año {agno} tendras {edadfutura} años </h1>
        </body>
    </html>"""
    
    return HttpResponse(documento)