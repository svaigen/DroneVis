import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import util
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
    
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
    dataByRamo = {}
    ramos = list(set(ramo[1:]))

    for year in years:
        dataByRamo[year] = {}   
    
    for year in years:
        for ramo in ramos:
            dataByRamo[year][ramo] = list(filter(lambda d: ramo == d[-1] and year == d[0].split("/")[-1], allData))

    ramoByYear = {}
    for year in years:
        ramoByYear[year] = {}

    for year in years:
        for ramo in dataByRamo[year]:
            ramoByYear[year][ramo] = len(dataByRamo[year][ramo])    
    anos = []
    ramos = []
    numDrones = []
    for key in ramoByYear:
        for key2 in ramoByYear[key]:
            if(key2 !='Não Informado'):
                anos.append(key)
                ramos.append(key2)
                numDrones.append(ramoByYear[key][key2])
    d = {'Ano': anos, 'Ramo': ramos, 'Drones cadastrados': numDrones}
    return pd.DataFrame(d)

if __name__ == '__main__':
    data = prepareData()
    data_filtered = data[data.Ano == "2018"]
    fig = go.Figure(go.Bar(x= data_filtered['Drones cadastrados'], y= data['Ramo'].unique(), name="2018", orientation='h', marker=dict(color="#095256"), hovertemplate = "drones cadastrados: %{hovertext}<extra></extra>", hovertext = data_filtered['Drones cadastrados']))
    data_filtered = data[data.Ano == "2019"]
    fig.add_trace(go.Bar(x= data_filtered['Drones cadastrados'], y= data['Ramo'].unique(), name="2019", orientation='h', marker=dict(color="#5AAA95"), hovertemplate = "drones cadastrados: %{hovertext}<extra></extra>", hovertext = data_filtered['Drones cadastrados']))
    data_filtered = data[data.Ano == "2020"]
    fig.add_trace(go.Bar(x= data_filtered['Drones cadastrados'], y= data['Ramo'].unique(), name="2020", orientation='h',marker=dict(color="#BB9F06"), hovertemplate = "drones cadastrados: %{hovertext}<extra></extra>", hovertext = data_filtered['Drones cadastrados']))
    fig.update_layout(barmode='stack', yaxis={'categoryorder':'sum ascending', 'title' : 'Ramo'}, xaxis={'title': 'Drones Cadastrados'}, autosize=True, margin={'t' : 15})
    fig.update_xaxes(range=[0,9000])

    plotly.io.write_html(fig, file="./../website/webviews/rank-ramo.html", full_html=False, default_height="80%")