import requests
from flask import Flask
import json
import requests
import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="BENFICA07", db="guimaraesmap")

def hospital():
# Rotunda Hospital Guimarães

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.44159398,-8.30343568&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    json_data = json.loads(response.text.encode('utf8'))

#print(response.text.encode('utf8'))

    rotundaGuimarães = "Rotunda Hospital Guimaraes"
    velocidadeAtual = json_data["flowSegmentData"]["currentSpeed"]
    velocidadeFree = json_data["flowSegmentData"]["freeFlowSpeed"]
    tempoviagemAtual = json_data["flowSegmentData"]["currentTravelTime"]
    tempoviagemFree = json_data["flowSegmentData"]["freeFlowTravelTime"]

    myCursor = conn.cursor()

#myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree) VALUES ('Rotunda Hospital Guimaraes', 20, 30, 40, 50);")
    myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree) VALUES (%s, %s, %s, %s, %s)", (rotundaGuimarães, velocidadeAtual, velocidadeFree, tempoviagemAtual, tempoviagemFree))
    print("> Dados inseridos! -> " + rotundaGuimarães)

    conn.commit()
    conn.rollback()
    #conn.close()   

hospital()


def circular():
# Circular Urbana Guimaraes

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=41.448880219871974,-8.307156223239609&key=WJgVtZpI5Q5lGFGbqNK1PU3J2N6OvDJY"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

#print(response.text.encode('utf8'))

    json_data_circular = json.loads(response.text.encode('utf8'))

    circularGuimarães = "Circular Urbana Guimaraes"
    velocidadeAtualC = json_data_circular["flowSegmentData"]["currentSpeed"]
    velocidadeFreeC = json_data_circular["flowSegmentData"]["freeFlowSpeed"]
    tempoviagemAtualC = json_data_circular["flowSegmentData"]["currentTravelTime"]
    tempoviagemFreeC = json_data_circular["flowSegmentData"]["freeFlowTravelTime"]

    myCursor = conn.cursor()

#myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree) VALUES ('Rotunda Hospital Guimaraes', 20, 30, 40, 50);")
    myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeAtual, VelocidadeFree, tempoviagemAtual, tempoviagemFree) VALUES (%s, %s, %s, %s, %s)", (circularGuimarães, velocidadeAtualC, velocidadeFreeC, tempoviagemAtualC, tempoviagemFreeC))
    print("> Dados inseridos! -> " + circularGuimarães)

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
