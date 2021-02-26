import requests
from flask import Flask
import json
import requests
import pymysql
import math
from datetime import datetime

conn = pymysql.connect(host="localhost", user="root", passwd="BENFICA07", db="guimaraesmap")

#VER CORREÇÃO DECLIVE E PAVIMENTO!!!!

def P241():
# P24 - Rua da Liberdade

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.43839131,-8.30116439&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    now = datetime.now()
 

    dt_string = now.strftime("%d/%m/%Y %H:%M")

#print(response.text.encode('utf8'))

    json_data_liberdade = json.loads(response.text.encode('utf8'))

    ruaLiberdade = "Rua da Liberdade"
    velocidadeAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeRuaLiberdade= 41.43839131
    LongitudeRuaLiberdade= -8.30116439


    myCursor = conn.cursor()

    #Fluxo
    fluxo = 10 + 528 + 4
    #Velocidade
    velocidade = velocidadeAtualLiberdade
    #Pesados
    pesados = 1

    #CRTN - Fluxo
    FluxoP24 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Velocidade
    VelocidadeP24 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Total
    CRTNTotal24 = FluxoP24 + VelocidadeP24
    print (CRTNTotal24)

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data) VALUES (%s, %s, %s, %s, %s, %s, %s)", (ruaLiberdade, LatitudeRuaLiberdade, LongitudeRuaLiberdade, velocidadeAtualLiberdade, fluxo, CRTNTotal24, dt_string))
    print("> Dados inseridos! -> " + ruaLiberdade + " " + dt_string)

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

    now = datetime.now()
 

    dt_string = now.strftime("%d/%m/%Y %H:%M")

#print(response.text.encode('utf8'))

    json_data_djoao = json.loads(response.text.encode('utf8'))

    ruaDJoao = "Avenida D João IV - 1"
    velocidadeAtualDJoao = json_data_djoao["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeDJoao= 41.43555205
    LongitudeDJoao= -8.29508543


    myCursor = conn.cursor()

    #Fluxo
    fluxo = 6 + 1189 + 60
    #Velocidade
    velocidade = velocidadeAtualDJoao
    #Pesados
    pesados = 5

    #CRTN - Fluxo
    FluxoP26 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Velocidade
    VelocidadeP26 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Total
    CRTNTotal26 = FluxoP26 + VelocidadeP26
    print (CRTNTotal26)

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data) VALUES (%s, %s, %s, %s, %s, %s, %s)", (ruaDJoao, LatitudeDJoao, LongitudeDJoao, velocidadeAtualDJoao, fluxo, CRTNTotal26, dt_string))
    print("> Dados inseridos! -> " + ruaDJoao + " " + dt_string)

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

    now = datetime.now()
 

    dt_string = now.strftime("%d/%m/%Y %H:%M")

#print(response.text.encode('utf8'))

    json_data_djoao2 = json.loads(response.text.encode('utf8'))

    ruaDJoao2 = "Avenida D João IV - 2"
    velocidadeAtualDJoao2 = json_data_djoao2["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeDJoao2= 41.43919561
    LongitudeDJoao2= -8.29072416


    myCursor = conn.cursor()

    #Fluxo
    fluxo = 6 + 1189 + 60
    #Velocidade
    velocidade = velocidadeAtualDJoao2
    #Pesados
    pesados = 5

    #CRTN - Fluxo
    FluxoP261 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Velocidade
    VelocidadeP261 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Total
    CRTNTotal261 = FluxoP261 + VelocidadeP261
    print (CRTNTotal261)

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data) VALUES (%s, %s, %s, %s, %s, %s, %s)", (ruaDJoao2, LatitudeDJoao2, LongitudeDJoao2, velocidadeAtualDJoao2, fluxo, CRTNTotal261, dt_string))
    print("> Dados inseridos! -> " + ruaDJoao2 + " " + dt_string)

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

    now = datetime.now()
 

    dt_string = now.strftime("%d/%m/%Y %H:%M")

#print(response.text.encode('utf8'))

    json_data_ruaAntonio = json.loads(response.text.encode('utf8'))

    ruaAntonio = "Rua Antonio da Costa Guimaraes"
    velocidadeAtualAntonio = json_data_ruaAntonio["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeRuaAntonio= 41.42868663
    LongitudeRuaAntonio= -8.29874396


    myCursor = conn.cursor()

    #Fluxo
    fluxo = 5 + 759 + 52
    #Velocidade
    velocidade = velocidadeAtualAntonio
    #Pesados
    pesados = 6

    #CRTN - Fluxo
    FluxoP25 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Velocidade
    VelocidadeP25 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Total
    CRTNTotal25 = FluxoP25 + VelocidadeP25
    print (CRTNTotal25)

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data) VALUES (%s, %s, %s, %s, %s, %s, %s)", (ruaAntonio, LatitudeRuaAntonio, LongitudeRuaAntonio, velocidadeAtualAntonio, fluxo, CRTNTotal25, dt_string))
    print("> Dados inseridos! -> " + ruaAntonio + " " + dt_string)

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

    now = datetime.now()
 

    dt_string = now.strftime("%d/%m/%Y %H:%M")

#print(response.text.encode('utf8'))

    json_data_ruaDJoaoI = json.loads(response.text.encode('utf8'))

    ruaDJoaoI = "Rua D.João I"
    velocidadeAtualDJoaoI = json_data_ruaDJoaoI["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeRuaDJoaoI= 41.44194625
    LongitudeRuaDJoaoI= -8.29893172


    myCursor = conn.cursor()

    #Fluxo
    fluxo = 2 + 34 + 0
    #Velocidade
    velocidade = velocidadeAtualDJoaoI
    #Pesados
    pesados = 0

    #CRTN - Fluxo
    FluxoP22 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Velocidade
    VelocidadeP22 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Pavimento
    PavimentoP22 = 4-0.03*pesados

    #CRTN - Total
    CRTNTotal22 = FluxoP22 + VelocidadeP22 + PavimentoP22
    print (CRTNTotal22)

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data) VALUES (%s, %s, %s, %s, %s, %s, %s)", (ruaDJoaoI, LatitudeRuaDJoaoI, LongitudeRuaDJoaoI, velocidadeAtualDJoaoI, fluxo, CRTNTotal22, dt_string))
    print("> Dados inseridos! -> " + ruaDJoaoI + " " + dt_string)

    conn.commit()
    conn.rollback()
    conn.close() 

P22()



