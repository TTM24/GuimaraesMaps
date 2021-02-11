import requests
from flask import Flask
import json
import requests
import pymysql
import math
from datetime import datetime

conn = pymysql.connect(host="localhost", user="root", passwd="BENFICA07", db="guimaraesmap")

def P241():
# P24 - Rua da Liberdade 1

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.43955272,-8.29848433&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    now = datetime.now()
 

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#print(response.text.encode('utf8'))

    json_data_liberdade = json.loads(response.text.encode('utf8'))

    ruaLiberdade = "Rua da Liberdade - 1"
    velocidadeAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentSpeed"]
    #velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    #tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    #tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]
    LatitudeRuaLiberdade= 41.43955272
    LongitudeRuaLiberdade= -8.29848433


    myCursor = conn.cursor()

    #Fluxo
    fluxo = 10 + 528 + 4
    #Velocidade
    velocidade = velocidadeAtualLiberdade
    #Pesados
    pesados = 1

    #CRTN - Fluxo
    FluxoP241 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Velocidade
    VelocidadeP241 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Total
    CRTNTotal241 = FluxoP241 + VelocidadeP241 
    print (CRTNTotal241)

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO ruido_guimaraes(NomeEstrada, Latitude, Longitude, VelocidadeAtual, Fluxo, Ruido, Data) VALUES (%s, %s, %s, %s, %s, %s, %s)", (ruaLiberdade, LatitudeRuaLiberdade, LongitudeRuaLiberdade, velocidadeAtualLiberdade, fluxo, CRTNTotal241, dt_string))
    print("> Dados inseridos! -> " + ruaLiberdade + " " + dt_string)

    conn.commit()
    conn.rollback()

P241()

def P242():
# P24 - Rua da Liberdade 2

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.43839131,-8.30116439&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    now = datetime.now()
 

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#print(response.text.encode('utf8'))

    json_data_liberdade2 = json.loads(response.text.encode('utf8'))

    ruaLiberdade2 = "Rua da Liberdade - 2"
    velocidadeAtualLiberdade2 = json_data_liberdade2["flowSegmentData"]["currentSpeed"]
    velocidadeFreeLiberdade2 = json_data_liberdade2["flowSegmentData"]["freeFlowSpeed"]
    tempoviagemAtualLiberdade2 = json_data_liberdade2["flowSegmentData"]["currentTravelTime"]
    tempoviagemFreeLiberdade2 = json_data_liberdade2["flowSegmentData"]["freeFlowTravelTime"]

    myCursor = conn.cursor()

#myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree) VALUES ('Rotunda Hospital Guimaraes', 20, 30, 40, 50);")
    myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree, horaRegisto) VALUES (%s, %s, %s, %s, %s, %s)", (ruaLiberdade2, velocidadeAtualLiberdade2, velocidadeFreeLiberdade2, tempoviagemAtualLiberdade2, tempoviagemFreeLiberdade2, dt_string))
    print("> Dados inseridos! -> " + ruaLiberdade2 + " " + dt_string)

    conn.commit()
    conn.rollback()
    conn.close() 

    #Fluxo
    fluxo = 10 + 528 + 4
    #Velocidade
    velocidade = velocidadeAtualLiberdade2
    #Pesados
    pesados = 1

    #CRTN - Fluxo
    FluxoP242 = 42.2 + 10*math.log10(fluxo)

    #CRTN - Velocidade
    VelocidadeP242 = 33*math.log10(velocidade + 40 + (500/velocidade)) + 10*math.log10(1 + (5*pesados/velocidade)) - 68.8

    #CRTN - Total
    CRTNTotal = FluxoP242 + VelocidadeP242
    print (CRTNTotal)

P242()
