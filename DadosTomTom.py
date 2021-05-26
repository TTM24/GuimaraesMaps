import requests
from flask import Flask
import json
import requests
import pymysql
import math
from datetime import datetime

conn = pymysql.connect(host="localhost", user="root", passwd="BENFICA07", db="guimaraesmap")

#VER CORREÇÃO DECLIVE E PAVIMENTO!!!!

#Definir hora registo e periodo do dia
now = datetime.now()

hora = now.hour

dt_string = now.strftime("%d/%m/%Y %H:%M")

if(hora >= 7) and (hora < 20):
    dia = "Diurno"
elif (hora >= 20) and (hora < 23):
    dia = "Entardecer"
elif (hora >= 23) or (hora < 7):
    dia = "Noturno"

print("Periodo do dia -> " + dia)

def P241():
# P24 - Rua da Liberdade

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.43839131,-8.30116439&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    json_data_liberdade = json.loads(response.text.encode('utf8'))

    ruaLiberdade = "Rua da Liberdade"
    velocidadeAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeRuaLiberdade= 41.43839131
    LongitudeRuaLiberdade= -8.30116439

    #Fluxo
    if (dia == "Diurno"):
        fluxo = 10 + 528 + 4
    elif (dia == "Entardecer"):
        fluxo = 23 + 425 + 1
    elif (dia == "Noturno"):
        fluxo = 4 + 78 + 0

    #Velocidade
    velocidade = velocidadeAtualLiberdade

    #Declive
    declive = 2
    
    #Pesados
    if (dia == "Diurno"):
        pesados = 1
    elif (dia == "Entardecer"):
        pesados = 0
    elif (dia == "Noturno"):
        pesados = 0
    
    #CRTN - Fluxo 
    FluxoP24 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Declive
    DecliveP24 = 0.3*declive
    
    #CRTN - Velocidade
    VelocidadeP24 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Total - Leq
    CRTNTotal24 = (FluxoP24 + VelocidadeP24 + DecliveP24) - 3

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data, PeriodoDia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ruaLiberdade, LatitudeRuaLiberdade, LongitudeRuaLiberdade, velocidadeAtualLiberdade, fluxo, CRTNTotal24, dt_string, dia))
    print("> Dados inseridos! -> " + ruaLiberdade + " " + dt_string)
    print (CRTNTotal24)

    conn.commit()
    conn.rollback()
    #conn.close() 

P241()

def P26():
# P26 - Avenida D.João IV

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.43555205,-8.29508543&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    json_data_djoao = json.loads(response.text.encode('utf8'))

    ruaDJoao = "Avenida D João IV - 1"
    velocidadeAtualDJoao = json_data_djoao["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeDJoao= 41.43555205
    LongitudeDJoao= -8.29508543

     #Fluxo
    if (dia == "Diurno"):
        fluxo = 6 + 1189 + 60
    elif (dia == "Entardecer"):
        fluxo = 14 + 957 + 11
    elif (dia == "Noturno"):
        fluxo = 2 + 176 + 5
    
    #Velocidade
    velocidade = velocidadeAtualDJoao

    #Declive
    declive = 2

    #Pesados
    if (dia == "Diurno"):
        pesados = 5
    elif (dia == "Entardecer"):
        pesados = 1
    elif (dia == "Noturno"):
        pesados = 3

    #CRTN - Fluxo
    FluxoP26 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Declive
    DecliveP26 = 0.3*declive

    #CRTN - Velocidade
    VelocidadeP26 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Total - Leq
    CRTNTotal26 = (FluxoP26 + VelocidadeP26 + DecliveP26) - 3

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data, PeriodoDia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ruaDJoao, LatitudeDJoao, LongitudeDJoao, velocidadeAtualDJoao, fluxo, CRTNTotal26, dt_string, dia))
    print("> Dados inseridos! -> " + ruaDJoao + " " + dt_string)
    print (CRTNTotal26)

    conn.commit()
    conn.rollback()
    #conn.close() 

P26()

def P261():
# P261 - Avenida D.João IV - 2

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.43919561,-8.29072416&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    json_data_djoao2 = json.loads(response.text.encode('utf8'))

    ruaDJoao2 = "Avenida D João IV - 2"
    velocidadeAtualDJoao2 = json_data_djoao2["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeDJoao2= 41.43919561
    LongitudeDJoao2= -8.29072416

    #Fluxo
    if (dia == "Diurno"):
        fluxo = 6 + 1189 + 60
    elif (dia == "Entardecer"):
        fluxo = 14 + 957 + 11
    elif (dia == "Noturno"):
        fluxo = 2 + 176 + 5

    #Velocidade
    velocidade = velocidadeAtualDJoao2

    #Declive
    declive = 2

    #Pesados
    if (dia == "Diurno"):
        pesados = 5
    elif (dia == "Entardecer"):
        pesados = 1
    elif (dia == "Noturno"):
        pesados = 3

    #CRTN - Fluxo
    FluxoP261 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Declive
    DecliveP261 = 0.3*declive

    #CRTN - Velocidade
    VelocidadeP261 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Total - Leq
    CRTNTotal261 = (FluxoP261 + VelocidadeP261 + DecliveP261) - 3

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data, PeriodoDia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ruaDJoao2, LatitudeDJoao2, LongitudeDJoao2, velocidadeAtualDJoao2, fluxo, CRTNTotal261, dt_string, dia))
    print("> Dados inseridos! -> " + ruaDJoao2 + " " + dt_string)
    print (CRTNTotal261)

    conn.commit()
    conn.rollback()
    #conn.close() 

P261()

def P25():
# P25 - Rua Antonio da Costa Guimarães

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.42868663,-8.29874396&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    json_data_ruaAntonio = json.loads(response.text.encode('utf8'))

    ruaAntonio = "Rua Antonio da Costa Guimaraes"
    velocidadeAtualAntonio = json_data_ruaAntonio["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeRuaAntonio= 41.42868663
    LongitudeRuaAntonio= -8.29874396

    #Fluxo
    if (dia == "Diurno"):
        fluxo = 5 + 759 + 52
    elif (dia == "Entardecer"):
        fluxo = 3 + 445 + 15
    elif (dia == "Noturno"):
        fluxo = 0 + 81 + 2

    #Velocidade
    velocidade = velocidadeAtualAntonio

    #Declive
    declive = 2
    
    #Pesados
    if (dia == "Diurno"):
        pesados = 6
    elif (dia == "Entardecer"):
        pesados = 3
    elif (dia == "Noturno"):
        pesados = 2

    #CRTN - Fluxo
    FluxoP25 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Declive
    DecliveP25 = 0.3*declive

    #CRTN - Velocidade
    VelocidadeP25 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Total - Leq
    CRTNTotal25 = (FluxoP25 + VelocidadeP25 + DecliveP25) - 3
    
    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data, PeriodoDia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ruaAntonio, LatitudeRuaAntonio, LongitudeRuaAntonio, velocidadeAtualAntonio, fluxo, CRTNTotal25, dt_string, dia))
    print("> Dados inseridos! -> " + ruaAntonio + " " + dt_string)
    print (CRTNTotal25)

    conn.commit()
    conn.rollback()
    #conn.close() 

P25()

def P22():
# P22 - Rua D.João I

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.44194625,-8.29893172&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    json_data_ruaDJoaoI = json.loads(response.text.encode('utf8'))

    ruaDJoaoI = "Rua D.João I"
    velocidadeAtualDJoaoI = json_data_ruaDJoaoI["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeRuaDJoaoI= 41.44194625
    LongitudeRuaDJoaoI= -8.29893172

    #Fluxo
    if (dia == "Diurno"):
        fluxo = 2 + 34 + 0
    elif (dia == "Entardecer"):
        fluxo = 4 + 27 + 0
    elif (dia == "Noturno"):
        fluxo = 1 + 5 + 0

    #Velocidade
    velocidade = velocidadeAtualDJoaoI

    #Declive
    declive = 2
    
    #Pesados
    if (dia == "Diurno"):
        pesados = 0
    elif (dia == "Entardecer"):
        pesados = 0
    elif (dia == "Noturno"):
        pesados = 0

    #CRTN - Fluxo
    FluxoP22 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Declive
    DecliveP22 = 0.3*declive

    #CRTN - Velocidade
    VelocidadeP22 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Pavimento
    PavimentoP22 = 4-0.03*pesados

    #CRTN - Total - Leq
    CRTNTotal22 = (FluxoP22 + VelocidadeP22 + PavimentoP22 + DecliveP22) - 3

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data, PeriodoDia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ruaDJoaoI, LatitudeRuaDJoaoI, LongitudeRuaDJoaoI, velocidadeAtualDJoaoI, fluxo, CRTNTotal22, dt_string, dia))
    print("> Dados inseridos! -> " + ruaDJoaoI + " " + dt_string)
    print (CRTNTotal22)

    conn.commit()
    conn.rollback()
    #conn.close() 

P22()

def P23():
# P23 - Rua de Camões

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.44110177,-8.29697371&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    json_data_ruaCamoes = json.loads(response.text.encode('utf8'))

    ruaCamoes = "Rua de Camões"
    velocidadeAtualCamoes = json_data_ruaCamoes["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeRuaCamoes= 41.44110177
    LongitudeRuaCamoes= -8.29697371

    #Fluxo
    if (dia == "Diurno"):
        fluxo = 4 + 176 + 2
    elif (dia == "Entardecer"):
        fluxo = 9 + 142 + 0
    elif (dia == "Noturno"):
        fluxo = 1 + 26 + 0
    
    #Velocidade
    velocidade = velocidadeAtualCamoes

    #Declive
    declive = 2

    #Pesados
    if (dia == "Diurno"):
        pesados = 1
    elif (dia == "Entardecer"):
        pesados = 0
    elif (dia == "Noturno"):
        pesados = 0

    #CRTN - Fluxo
    FluxoP23 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Declive
    DecliveP23 = 0.3*declive

    #CRTN - Velocidade
    VelocidadeP23 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Pavimento
    PavimentoP23 = 4-0.03*pesados

    #CRTN - Total - Leq
    CRTNTotal23 = (FluxoP23 + VelocidadeP23 + PavimentoP23 + DecliveP23) - 3
    
    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data, PeriodoDia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ruaCamoes, LatitudeRuaCamoes, LongitudeRuaCamoes, velocidadeAtualCamoes, fluxo, CRTNTotal23, dt_string, dia))
    print("> Dados inseridos! -> " + ruaCamoes + " " + dt_string)
    print (CRTNTotal23)

    conn.commit()
    conn.rollback()
    conn.close() 

P23()

