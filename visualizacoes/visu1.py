import plotly.graph_objects as go
import util


def geraTextoData(data):
    mes = int(data[3:5])
    ano = int(data[6:])

    if(ano == 2018):
        if(mes == 1):
            return "Jan (2018)"
        if(mes == 2):
            return "Fev (2018)"
        if(mes == 3):
            return "Mar (2018)"
        if(mes == 4):
            return "Abr (2018)"
        if(mes == 5):
            return "Mai (2018)"
        if(mes == 6):
            return "Jun (2018)"
        if(mes == 7):
            return "Jul (2018)"
        if(mes == 8):
            return "Ago (2018)"
        if(mes == 9):
            return "Set (2018)"
        if(mes == 10):
            return "Out (2018)"
        if(mes == 11):
            return "Nov (2018)"
        if(mes == 12):
            return "Dec (2018)"
    if(ano == 2019):
        if(mes == 1):
            return "Jan (2019)"
        if(mes == 2):
            return "Fev (2019)"
        if(mes == 3):
            return "Mar (2019)"
        if(mes == 4):
            return "Abr (2019)"
        if(mes == 5):
            return "Mai (2019)"
        if(mes == 6):
            return "Jun (2019)"
        if(mes == 7):
            return "Jul (2019)"
        if(mes == 8):
            return "Ago (2019)"
        if(mes == 9):
            return "Set (2019)"
        if(mes == 10):
            return "Out (2019)"
        if(mes == 11):
            return "Nov (2019)"
        if(mes == 12):
            return "Dec (2019)"
    if(ano == 2020):
        if(mes == 1):
            return "Jan (2020)"
        if(mes == 2):
            return "Fev (2020)"
        if(mes == 3):
            return "Mar (2020)"
        if(mes == 4):
            return "Abr (2020)"
        if(mes == 5):
            return "Mai (2020)"
        if(mes == 6):
            return "Jun (2020)"
        if(mes == 7):
            return "Jul (2020)"
        if(mes == 8):
            return "Ago (2020)"
        if(mes == 9):
            return "Set (2020)"
        if(mes == 10):
            return "Out (2020)"
        if(mes == 11):
            return "Nov (2020)"
        if(mes == 12):
            return "Dec (2020)"

def modeloCor(modelo):
    modelo = modelo.strip(" ")
    if(modelo == 'Mavic'):
        return "#4169E1"
    elif(modelo == 'Phantom 3'):
        return "#2E8B57"
    elif(modelo == 'Phantom 4'):
        return "#DB7093"
    elif(modelo == 'MK Okto XL 6S12'):
        return "#B8860B"
    elif(modelo == 'Phantom 2'):
        return "#BA55D3"
    else:
        print(modelo)
        return("#000000")
    

def processaDados(allData):
    newDataInscricao = []
    newDataDia = []
    cores = []

    firstRow = True
    for row in allData:
        if(not firstRow):
            texto = geraTextoData(row[0])
            newDataInscricao.append(texto)
            newDataDia.append(int(row[0][0:2]))
            cores.append(modeloCor(row[6]))

        firstRow = False
    return newDataInscricao, newDataDia,cores


allData,inscricao,validade,operador,tipo_pessoa,tipo_uso,fabricante,modelo,numero_serie,peso_maximo,cidade,estado,ramo = util.leituraDados()

newDataInscricao, newDataDia,cores = processaDados(allData)




fig = go.Figure(data=go.Scatter(x=newDataDia,
                                y=newDataInscricao,
                                mode='markers',
                                marker_color=cores,
                                text=fabricante)) # hover text goes here

fig.update_layout(title='Population of USA States')
fig.show()

#time = [ 'Ago (2020)','Jul (2020)', 'Jun (2020)', 'Mai (2020)', 'Abr (2020)', 'Mar (2020)', 'Fev (2020)', 'Jan (2020)',
#           'Dec (2019)','Nov (2019)','Out (2019)','Set (2019)','Ago (2019)','Jul (2019)', 'Jun (2019)', 'Mai (2019)', 'Abr (2019)', 'Mar (2019)', 'Fev (2019)', 'Jan (2019)',
#           'Dec (2018)','Nov (2018)','Out (2018)','Set (2018)','Ago (2018)','Jul (2018)', 'Jun (2018)', 'Mai (2018)', 'Abr (2018)', 'Mar (2018)', 'Fev (2018)', 'Jan (2018)']
#voting_pop = [40, 45.7, 52, 53.6, 54.1, 54.2, 54.5, 54.7, 55.1, 56.6]
#reg_voters = [49.1, 42, 52.7, 84.3, 51.7, 61.1, 55.3, 64.2, 91.1, 58.9]

#fig = go.Figure()

#fig.add_trace(go.Scatter(
#    x=voting_pop,
#    y=time,
#    name='Percent of estimated voting age population',
#    marker=dict(
#        color='rgba(156, 165, 196, 0.95)',
#        line_color='rgba(156, 165, 196, 1.0)',
#    )
#))
#fig.add_trace(go.Scatter(
#    x=reg_voters, y=time,
#    name='Percent of estimated registered voters',
#    marker=dict(
#        color='rgba(204, 204, 204, 0.95)',
#        line_color='rgba(217, 217, 217, 1.0)'
#    )
#))

#fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=16))

#fig.update_layout(
#    title="Modelos de drones cadastrados ao longo do tempo",
#    xaxis=dict(
#        showgrid=False,
#        showline=False,
      #  linecolor='rgb(102, 102, 102)',
      #  tickfont_color='rgb(102, 102, 102)',
#        showticklabels=False,
      #  dtick=10,
      #  ticks='outside',
      #  tickcolor='rgb(102, 102, 102)',
#    ),
#    margin=dict(l=140, r=40, b=50, t=80),
#    legend=dict(
#        font_size=10,
#        yanchor='middle',
#        xanchor='right',
#    ),
#    width=800,
#    height=600,
#    paper_bgcolor='white',
#    plot_bgcolor='white',
#    hovermode='closest',
#)
#fig.show()