import requests
from flask import Flask
import json
import requests
import pymysql
import math
from datetime import datetime

conn = pymysql.connect(host="localhost", user="root", passwd="BENFICA07", db="guimaraesmap")

def P241():
# P24 - Rua da Liberdade

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.43839131,-8.30116439&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    now = datetime.now()
 

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

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
 

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

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
    conn.close() 

P26()



