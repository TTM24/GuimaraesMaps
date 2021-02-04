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

    ruaLiberdade1 = "Rua da Liberdade - 1"
    velocidadeAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentSpeed"]
    velocidadeFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowSpeed"]
    tempoviagemAtualLiberdade = json_data_liberdade["flowSegmentData"]["currentTravelTime"]
    tempoviagemFreeLiberdade = json_data_liberdade["flowSegmentData"]["freeFlowTravelTime"]

    myCursor = conn.cursor()

#myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree) VALUES ('Rotunda Hospital Guimaraes', 20, 30, 40, 50);")
    myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree, horaRegisto) VALUES (%s, %s, %s, %s, %s, %s)", (ruaLiberdade1, velocidadeAtualLiberdade, velocidadeFreeLiberdade, tempoviagemAtualLiberdade, tempoviagemFreeLiberdade, dt_string))
    print("> Dados inseridos! -> " + ruaLiberdade1 + " " + dt_string)

    conn.commit()
    conn.rollback()
    conn.close() 

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
    CRTNTotal = FluxoP241 + VelocidadeP241 
    print (CRTNTotal)

P241()
