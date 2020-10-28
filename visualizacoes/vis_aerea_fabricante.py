import plotly.graph_objects as go
import util
import queue as q
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

time = ['Jan (2018)','Fev (2018)','Mar (2018)','Abr (2018)','Mai (2018)', 'Jun (2018)', 'Jul (2018)', 'Ago (2018)', 'Set (2018)',
        'Out (2018)','Nov (2018)','Dez (2018)','Jan (2019)','Fev (2019)','Mar (2019)', 'Abr (2019)', 'Mai (2019)', 'Jun (2019)', 
        'Jul (2019)', 'Ago (2019)', 'Set (2019)','Out (2019)','Nov (2019)','Dez (2019)','Jan (2020)','Fev (2020)','Mar (2020)', 
        'Abr (2020)', 'Mai (2020)', 'JUn (2020)', 'Jul (2020)', 'Ago (2020)', 'Set (2020)']

allData,inscricao,validade,operador,tipo_pessoa,tipo_uso,fabricante,modelo,numero_serie,peso_maximo,cidade,estado,ramo = util.leituraDados()

allData = allData[1:]
inscricao = inscricao[1:]
validade = validade[1:]
operador = operador[1:]
tipo_pessoa = tipo_pessoa[1:]
tipo_uso = tipo_uso[1:]
fabricante = fabricante[1:]
modelo = modelo[1:]
numero_serie = numero_serie[1:]
peso_maximo = peso_maximo[1:]
cidade = cidade[1:]
estado = estado[1:]
ramo = ramo[1:]

named_colorscales = px.colors.named_colorscales()


dicModelo = {}
for m in fabricante:
    tx = m.strip()
    if(tx not in dicModelo):
        dicModelo[tx] = []
        dicModelo[tx].append(1)
    else:
        dicModelo[tx].append(1)

filaModelo = q.PriorityQueue()
for d in dicModelo.keys():
    filaModelo.put([len(dicModelo[d]),d])

modelos = []
while(not filaModelo.empty()):
    data = filaModelo.get()
    if(data[0]>=100):
        modelos.append(data[1])

fab = {}

for data in allData:
    txt = data[5].strip()
    if (txt not in modelos):
        txt = 'OUTROS'
    if (txt in fab):
        pos = util.geraPosicao(data[0])
        fab[txt][pos] = fab[txt][pos] + 1
    else:
        fab[txt] = [0] * 33
        pos = util.geraPosicao(data[0])
        fab[txt][pos] = fab[txt][pos] + 1

colors = []

for c in px.colors.cyclical.IceFire:
    colors.append(c)
for c in px.colors.cyclical.Phase:
    colors.append(c)


cont = 0
fig = go.Figure()
for f in fab.keys():
    fig.add_trace(go.Scatter(
        x=time, y=fab[f],
        hovertemplate='<b>%{x} </b> <br> Drones cadastrados %{y}',
        hoverinfo='x+y',
        mode='lines',
        name=f,
        text=f,
        line=dict(width=0.5, color = colors[cont]),
        stackgroup='one' # define stack group
    ))
    cont +=1


fig.update_layout(title="Relação parte todo entre quantidade de drones e fabricante",
                #xaxis_title='Month',
                yaxis_title='Número de drones cadastrados',height=700)
app = dash.Dash()
app.layout = html.Div([
dcc.Graph(id='rank1', figure=fig)])

app.run_server(debug=False, use_reloader=True)