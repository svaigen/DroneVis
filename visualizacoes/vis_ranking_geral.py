import plotly.express as px
import geopandas as pd
import util

class StatePerDrone:
    def __init__(self, sigla, totalDrones):
        self.sigla = sigla
        self.totalDrones = totalDrones
    
    def getTotalDrones(self):
        return self.totalDrones
    
def getNumDrones(data):
    numDrones = []
    for d in data:
        numDrones.append(d.totalDrones)
    return numDrones

def getSiglas(data):
    siglas = []
    for d in data:
        siglas.append(d.sigla)
    return siglas



allData,inscricao,validade,operador,tipo_pessoa,tipo_uso,fabricante,modelo,numero_serie,peso_maximo,cidade,estado,ramo = util.leituraDados()
statesList = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
dataByState = {}

for state in statesList:
    dataByState[state] = list(filter(lambda d: state == d[10], allData))

stateByNumberOfDrones = []
for state in dataByState:
    stateByNumberOfDrones.append(StatePerDrone(state,len(dataByState[state])))

stateByNumberOfDrones.sort(key = StatePerDrone.getTotalDrones, reverse = True)

for drone in stateByNumberOfDrones:
    print({}{})

d = {'# drones': getNumDrones(stateByNumberOfDrones), 'estado': getSiglas(stateByNumberOfDrones)}

fig = px.bar(d, x="# drones", y="estado", orientation='h', title='Número de drones por estado')

fig.show()