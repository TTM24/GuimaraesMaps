import requests
import json
from flask import Flask
from flask import jsonify
import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="BENFICA07", db="guimaraesmap")

myCursor = conn.cursor()

myCursor.execute("INSERT INTO heremap(NomeEstrada, VelocidadeLimite, VelocidadeNaoLimite, VelocidadeFree, Congestionamento) VALUES ('Rua Antonio', 20, 30, 40, 50);")
print("> Dados inseridos!")

conn.commit()
conn.rollback()
conn.close()    

url = "https://traffic.cit.api.here.com/traffic/6.1/flow.json?prox=41.4137,-8.3063,4928"

payload = {}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzUxMiIsImN0eSI6IkpXVCIsImlzcyI6IkhFUkUiLCJhaWQiOiJkTk8xc1NRMHhyWlRRRFdTN01VSyIsImlhdCI6MTU5OTQxNDkxMCwiZXhwIjoxNTk5NTAxMzEwLCJraWQiOiJqMSJ9.ZXlKaGJHY2lPaUprYVhJaUxDSmxibU1pT2lKQk1qVTJRMEpETFVoVE5URXlJbjAuLlNKWmthc3kxMUh3VFFSampyYmdISlEuQjNVSzhGWUNDSmc0a1JGa25fNFBKVk1LMm4ySkRtQ0F2c0ZEY3R0TC0tanJBMXFMMW51Wi1BVGZRWXZPbk5ucF92dVN0bi1QSzVHMGNCaG9ZQ0k0V3Jyd1RXYjZOZlZoc0ozWkNCaXNBUGZEOFZGenVwTFVYeTB1TFBMd1BOZ25lX3ZDb0p6ZmxaOXZtLXc0akxTV05BLmI0bXJuT1RsaHFuNml3RG5pWWhaVUUxNUFPMVV1YmdKUDFhV3lmcTRucFE.YNehqAnUTlAwIGQ4e0Vt6pb6erek0zbeDUdYzQ1cxd2DT-QHQ0-wTuza6yI6lwDvoKh5eTFo4ovMN1nGyJtbxXi1cnGnYK0eksdwVvJM-uNK7Bh-aAbyI0c6sJ3bl_fTgtSb3s5z7TocjeqcImTYrNo9KntWUn-mn1Wrh_aO4CBwIg2pLKDBG50XAOL9vuVQDwDXynjoOqxHH4le-W9zVebQdeeNyyMobS-BkmfCsV007mmSXfNPOEgKtYCa3BJZ22JTPHLI7ZwXNLLYgzLodJb9ImWqYXCUUjs1O_In6iF6m-UwnUqvTLfl12IqIBRyJd0RExoI1BApnrDvcciaeA'
}

response = requests.request("GET", url, headers=headers, data = payload)

json_data = json.loads(response.text.encode('utf8'))

dados1 = json_data['RWS'][0]

#dados = json_data['RWS'][0]['RW']

#estradas
estradas = []
for item in dados1['RW']: 
    print (item['DE'])
    estradas.append(item['DE'])

#estrada = json_data['RWS'][0]['RW'][0]['DE']

#WebService
app=Flask(__name__)

#jsonify(dados)
@app.route("/here")
def hello():
    return  jsonify(estradas)

if __name__ ==  '__main__':
    app.run(debug=True)

