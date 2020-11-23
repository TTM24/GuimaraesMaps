import requests
from flask import Flask
import json
import requests
import pymysql
import math
from datetime import datetime

conn = pymysql.connect(host="localhost", user="root", passwd="BENFICA07", db="guimaraesmap")

def hospital():
# Rotunda Hospital Guimarães

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.44087577,-8.30463195&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    json_data_hospital = json.loads(response.text.encode('utf8'))

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#print(response.text.encode('utf8'))

    rotundaGuimarães = "Rotunda Hospital Guimaraes"
    velocidadeAtualHospital = json_data_hospital["flowSegmentData"]["currentSpeed"]
    velocidadeFreeHospital = json_data_hospital["flowSegmentData"]["freeFlowSpeed"]
    tempoviagemAtualHospital = json_data_hospital["flowSegmentData"]["currentTravelTime"]
    tempoviagemFreeHospital = json_data_hospital["flowSegmentData"]["freeFlowTravelTime"]

    myCursor = conn.cursor()

#myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree) VALUES ('Rotunda Hospital Guimaraes', 20, 30, 40, 50);")
    myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree, horaRegisto) VALUES (%s, %s, %s, %s, %s, %s)", (rotundaGuimarães, velocidadeAtualHospital, velocidadeFreeHospital, tempoviagemAtualHospital, tempoviagemFreeHospital, dt_string))
    print("> Dados inseridos! -> " + rotundaGuimarães + " " + dt_string)

    conn.commit()
    conn.rollback()
    #conn.close()   

    #potencia_ligeiro = 46 + 30*math.log10(30)
    #print(potencia_ligeiro)

    fluxo = 500
    pesados = 4
    EQ = 10 - 1

    if velocidadeAtualHospital > 30:
        velocidadeAtualHospital = velocidadeAtualHospital
        #potencia_ligeiro = 46 + 30*math.log10(velocidadeAtualHospital) + 2
        #print(potencia_ligeiro)
    else:
        velocidadeAtualHospital = 30
        #print(potencia_ligeiro)

    # C = 2 -- Rotunda
    potencia_ligeiro = 46 + 30*math.log10(velocidadeAtualHospital) + 2

    LW1 = (fluxo+fluxo*pesados*(EQ/100))/velocidadeAtualHospital
    #print(LW1)

    LW2 = potencia_ligeiro + 10*math.log10(LW1) - 30
    print(LW2)

    

hospital()


def circular():
# Circular Urbana Guimaraes

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.448880219871974,-8.307156223239609&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    now = datetime.now()
 

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#print(response.text.encode('utf8'))

    json_data_circular = json.loads(response.text.encode('utf8'))

    circularGuimarães = "Circular Urbana Guimaraes"
    velocidadeAtualCircular = json_data_circular["flowSegmentData"]["currentSpeed"]
    velocidadeFreeCircular = json_data_circular["flowSegmentData"]["freeFlowSpeed"]
    tempoviagemAtualCircular = json_data_circular["flowSegmentData"]["currentTravelTime"]
    tempoviagemFreeCircular = json_data_circular["flowSegmentData"]["freeFlowTravelTime"]

    myCursor = conn.cursor()

#myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree) VALUES ('Rotunda Hospital Guimaraes', 20, 30, 40, 50);")
    myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree, horaRegisto) VALUES (%s, %s, %s, %s, %s, %s)", (circularGuimarães, velocidadeAtualCircular, velocidadeFreeCircular, tempoviagemAtualCircular, tempoviagemFreeCircular, dt_string))
    print("> Dados inseridos! -> " + circularGuimarães + " " + dt_string)

    conn.commit()
    conn.rollback()
    conn.close() 

circular()

# WebService
# app=Flask(__name__)

# #jsonify(dados)
# @app.route("/tomtom")
# def hello():
#     return json_data

# if __name__ ==  '__main__':
#     app.run(debug=True)
