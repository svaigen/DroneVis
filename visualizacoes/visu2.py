import plotly.graph_objects as go
import util
import queue as q

time = ['Jan (2018)','Fev (2018)','Mar (2018)','Abr (2018)','Mai (2018)', 'Jun (2018)', 'Jul (2018)', 'Ago (2018)', 'Set (2018)',
        'Out (2018)','Nov (2018)','Dez (2018)','Jan (2019)','Fev (2019)','Mar (2019)', 'Abr (2019)', 'Mai (2019)', 'Jun (2019)', 
        'Jul (2019)', 'Ago (2019)', 'Set (2019)','Out (2019)','Nov (2019)','Dez (2019)','Jan (2020)','Fev (2020)','Mar (2020)', 
        'Abr (2020)', 'Mai (2020)', 'JUn (2020)', 'Jul (2020)', 'Ago (2020)', 'Set (2020)']

allData,inscricao,validade,operador,tipo_pessoa,tipo_uso,fabricante,modelo,numero_serie,peso_maximo,cidade,estado,ramo = util.leituraDados()

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
  #  print(d,len(dicModelo[d]))
  #  if(len(dicModelo[d]))
    filaModelo.put([len(dicModelo[d]),d])

while(not filaModelo.empty()):
    print(filaModelo.get())



fig = go.Figure()
fig.add_trace(go.Scatter(
    x=time, y=[40, 60, 40, 10],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(131, 90, 241)'),
    stackgroup='one' # define stack group
))
fig.add_trace(go.Scatter(
    x=time, y=[20, 10, 10, 60],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(111, 231, 219)'),
    stackgroup='one'
))
fig.add_trace(go.Scatter(
    x=time, y=[40, 30, 50, 30],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(184, 247, 212)'),
    stackgroup='one'
))

fig.update_layout(yaxis_range=(0, 100))
fig.show()