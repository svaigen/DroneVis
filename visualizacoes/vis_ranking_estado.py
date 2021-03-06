import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import util
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly

class StatePerDrone:
    def __init__(self, sigla = None, totalDrones = None):
        self.sigla = sigla
        self.totalDrones = totalDrones
    
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

def getPorcentagem(data):
    porcentagem = []
    for d in data:
        porcentagem.append(d.porcentagem)
    return porcentagem

def prepareData():
    allData,inscricao,validade,operador,tipo_pessoa,tipo_uso,fabricante,modelo,numero_serie,peso_maximo,cidade,estado,ramo = util.leituraDados()
    years = ["2020","2019","2018"]
    statesList = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
    dataByState = {}

    for year in years:
        dataByState[year] = {}   
    
    for year in years:
        for state in statesList:
            dataByState[year][state] = list(filter(lambda d: state == d[10] and year == d[0].split("/")[-1], allData))

    stateByYear = {}
    for year in years:
        stateByYear[year] = {}

    for year in years:
        for state in dataByState[year]:
            stateByYear[year][state] = len(dataByState[year][state])    
    anos = []
    estados = []
    numDrones = []
    for key in stateByYear:
        for key2 in stateByYear[key]:
            anos.append(key)
            estados.append(key2)
            numDrones.append(stateByYear[key][key2])
    d = {'Ano': anos, 'Estado': estados, 'Drones cadastrados': numDrones}
    return pd.DataFrame(d)

if __name__ == '__main__':
    data = prepareData()
    data_filtered = data[data.Ano == "2018"]
    fig = go.Figure(go.Bar(x= data_filtered['Drones cadastrados'], y= data['Estado'].unique(), name="2018", orientation='h', marker=dict(color="#095256"), hovertemplate = "drones cadastrados: %{hovertext}<extra></extra>", hovertext = data_filtered['Drones cadastrados']))
    data_filtered = data[data.Ano == "2019"]
    fig.add_trace(go.Bar(x= data_filtered['Drones cadastrados'], y= data['Estado'].unique(), name="2019", orientation='h', marker=dict(color="#5AAA95"), hovertemplate = "drones cadastrados: %{hovertext}<extra></extra>", hovertext = data_filtered['Drones cadastrados']))
    data_filtered = data[data.Ano == "2020"]
    fig.add_trace(go.Bar(x= data_filtered['Drones cadastrados'], y= data['Estado'].unique(), name="2020", orientation='h', marker=dict(color="#BB9F06"), hovertemplate = "drones cadastrados: %{hovertext}<extra></extra>", hovertext = data_filtered['Drones cadastrados']))
    fig.update_layout(barmode='stack', yaxis={'categoryorder':'sum ascending', 'title' : 'Estado'}, xaxis={'title' : 'Drones cadastrados'}, autosize=True, margin={'t' : 15})
    fig.update_xaxes(range=[0,27000])

    plotly.io.write_html(fig, file="./../website/webviews/rank-drone-estado-acumulado.html", full_html=False, default_height="80%")