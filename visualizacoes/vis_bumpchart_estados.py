import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import util
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime
import random

def dataByPeriodo(data):
  for d in data[1:]:
    date = datetime.strptime(d[0],'%d/%m/%Y')
    if (date < datetime.strptime("01/04/2018",'%d/%m/%Y')):
      d[0] = "1/2018"
    elif (date < datetime.strptime("01/07/2018",'%d/%m/%Y')):
      d[0] = "2/2018"
    elif (date < datetime.strptime("01/10/2018",'%d/%m/%Y')):
      d[0] = "3/2018"
    elif (date < datetime.strptime("01/01/2019",'%d/%m/%Y')):
      d[0] = "4/2018"
    elif (date < datetime.strptime("01/04/2019",'%d/%m/%Y')):
      d[0] = "1/2019"
    elif (date < datetime.strptime("01/07/2019",'%d/%m/%Y')):
      d[0] = "2/2019"
    elif (date < datetime.strptime("01/10/2019",'%d/%m/%Y')):
      d[0] = "3/2019"
    elif (date < datetime.strptime("01/01/2020",'%d/%m/%Y')):
      d[0] = "4/2019"
    elif (date < datetime.strptime("01/04/2020",'%d/%m/%Y')):
      d[0] = "1/2020"
    elif (date < datetime.strptime("01/07/2020",'%d/%m/%Y')):
      d[0] = "2/2020"
    elif (date < datetime.strptime("01/10/2020",'%d/%m/%Y')):
      d[0] = "3/2020"

def prepareData():
    allData,inscricao,validade,operador,tipo_pessoa,tipo_uso,fabricante,modelo,numero_serie,peso_maximo,cidade,estado,ramo = util.leituraDados()
    periodos = ["1/2018","2/2018","3/2018","4/2018","1/2019","2/2019","3/2019","4/2019","1/2020","2/2020","3/2020"]
    dataByPeriodo(allData)
    d = pd.DataFrame(allData[1:], columns=allData[0])
    estadosList = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
    orderEstadosRet = []

    dictEstadosPeriodos = {}
    for estado in estadosList:
      dictEstadosPeriodos[estado] = {} 
      for periodo in periodos:
        valInsc = d[d.inscrição == periodo]
        valEst = valInsc[valInsc.estado == estado]
        dictEstadosPeriodos[estado][periodo] = [0,len(valEst)]
    
    firstPeriodo = True #para calcular e retornar a lista ordenada dos estados pelo primeiro trimestre
    for periodo in periodos:
      listToOrder = []
      for estado in estadosList:
        listToOrder.append([estado, dictEstadosPeriodos[estado][periodo]])
      listToOrder.sort(key=lambda listToOrder: listToOrder[1][1], reverse=True)
      i = 1
      for data in listToOrder:
        dictEstadosPeriodos[data[0]][periodo][0] = i if i > 9 else "0{}".format(i)
        if firstPeriodo:
          orderEstadosRet.append(data[0])
        i += 1
      firstPeriodo = False

    pCols = []
    eCols = []
    oCols = []
    dCols = []
    for periodo in periodos:
      for estado in estadosList:
        pCols.append(periodo)
        eCols.append(estado)
        oCols.append(dictEstadosPeriodos[estado][periodo][0])
        dCols.append(dictEstadosPeriodos[estado][periodo][1])

    d = {'Periodo': pCols, 'Estado': eCols, 'Ranking': oCols, '# drones': dCols}
    return orderEstadosRet, pd.DataFrame(d)

if __name__ == '__main__':
    estados, data = prepareData()
    fig = go.Figure()
    pallete = util.colorViridis(8)
    counter = 0
    for estado in estados:
      r = pallete[counter][0]
      g = pallete[counter][1]
      b = pallete[counter][2]
      color = "rgb({},{},{})".format(r, g, b)
      data_filtered = data[data.Estado == estado]
      fig.add_trace(go.Scatter(
                      x = data_filtered['Periodo'],
                      y = data_filtered['Ranking'],
                      mode = 'lines+markers+text',
                      name = estado,
                      marker = {"size": 20, 'color' : color},
                      line = {"color": color},
                      hovertemplate = "# de drones: %{hovertext}<extra></extra>",
                      hovertext = data_filtered['# drones'],
                      text = estado,
                      textfont = dict(color = "{}".format("#000000" if (r*0.299 + g*0.587 + b*0.114) > 150 else "#ffffff"))
                    ))
      counter += 1
    fig.update_yaxes(type='category')
    fig.update_layout(title='Ranking dos estados ao longo dos trimestres baseado no número de drones cadastrados',
                      yaxis={'categoryorder':'category descending', 'title' : 'Posição no ranking'},
                      xaxis={'title' : 'trimestre/ano'},
                      height=800,
                      showlegend = False,
                      plot_bgcolor = "#ffffff",
                      paper_bgcolor = "#ffffff"
                     )
    
    app = dash.Dash()
    app.layout = html.Div([
        dcc.Graph(id='rank1', figure=fig)
    ]
    )

    app.run_server(debug=False, use_reloader=True)
