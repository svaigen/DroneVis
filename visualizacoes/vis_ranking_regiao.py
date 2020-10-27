import plotly.express as px
import plotly.graph_objects as go
import plotly
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import csv


if __name__ == '__main__':
    data = pd.read_csv('../base_dados/treeMap.csv')
    dataRegiao = {}
    dataEstado = {}
    dataCidade = {}
    for i, row in data.iterrows():
        if row['estado'] == '-':
            continue
        if row['regiao'] not in dataRegiao:
            dataRegiao[row['regiao']] = int(row['drones'])
        else:
            dataRegiao[row['regiao']] = dataRegiao[row['regiao']] + int(row['drones'])        

        if row['regiao'] not in dataEstado:
            dataEstado[row['regiao']] = {}            
        if row['estado'] not in dataEstado[row['regiao']]:
                dataEstado[row['regiao']][row['estado']] = int(row['drones'])
        else:
            dataEstado[row['regiao']][row['estado']] = dataEstado[row['regiao']][row['estado']] + int(row['drones'])

        if row['regiao'] not in dataCidade:
            dataCidade[row['regiao']] = {}            
        if row['estado'] not in dataCidade[row['regiao']]:
            dataCidade[row['regiao']][row['estado']] = {}
        if row['cidade'] not in dataCidade[row['regiao']][row['estado']]:
            dataCidade[row['regiao']][row['estado']][row['cidade']] = int(row['drones'])
        else :
            dataCidade[row['regiao']][row['estado']][row['cidade']] = dataCidade[row['regiao']][row['estado']][row['cidade']] + int(row['drones'])
    
    estadoMatriz = []
    cidadeMatriz = []
    for regiao in dataEstado:
        for estado in dataEstado[regiao]:
            estadoMatriz.append([regiao,estado,dataEstado[regiao][estado]])
            for cidade in dataCidade[regiao][estado]:
                cidadeMatriz.append([regiao,estado,cidade,dataCidade[regiao][estado][cidade]])

    regiaoDf = pd.DataFrame.from_dict(dataRegiao, orient='index', columns = ['drones'])
    
    estadoDf = pd.DataFrame.from_dict(estadoMatriz)
    estadoDf = estadoDf.rename(columns={0: 'regiao',1: 'estado', 2:'drones'})

    cidadeDf = pd.DataFrame.from_dict(cidadeMatriz)
    cidadeDf = cidadeDf.rename(columns={0: 'regiao',1: 'estado', 2:'cidade', 3: 'drones'})

    fig = go.Figure(go.Bar(x= regiaoDf['drones'], y= regiaoDf.index, name="Drones por região", orientation='h', marker=dict(color="#095256"), hovertemplate = "Drones cadastrados: %{hovertext}<extra></extra>", hovertext = regiaoDf['drones']))
    fig.update_layout(title='Total de drones cadastrados por região', yaxis={'categoryorder':'sum ascending', 'title' : 'Região'}, xaxis={'title' : 'Drones cadastrados'})
    plotly.io.write_html(fig,"../website/webviews/vis_ranking_regiao.html",full_html=False)

    for regiao in dataEstado:
        data_filtered_state = estadoDf[estadoDf.regiao == regiao]
        fig = go.Figure(go.Bar(x= data_filtered_state['drones'], y= data_filtered_state['estado'], name="Drones por estado da região {}".format(regiao), orientation='h', marker=dict(color="#095256"), hovertemplate = "Drones cadastrados: %{hovertext}<extra></extra>", hovertext = data_filtered_state['drones']))
        fig.update_layout(title='Total de drones cadastrados por estado da região {}'.format(regiao), yaxis={'categoryorder':'sum ascending', 'title' : 'Estado'}, xaxis={'title' : 'Drones cadastrados'})
        plotly.io.write_html(fig,"../website/webviews/vis_ranking_{}.html".format(regiao.lower()),full_html=False)

        for estado in dataEstado[regiao]:
            data_filtered_cidade = cidadeDf[cidadeDf.regiao == regiao]
            data_filtered_cidade = cidadeDf[cidadeDf.estado == estado]
            data_filtered_cidade.sort_values(by=['drones'])
            data_filtered_cidade = data_filtered_cidade[0:10]
            fig = go.Figure(go.Bar(x = data_filtered_cidade['drones'], y = data_filtered_cidade['cidade'], name="Drones por cidade do estado {}".format(estado), orientation='h', marker=dict(color="#095256"), hovertemplate = "Drones cadastrados: %{hovertext}<extra></extra>", hovertext = data_filtered_cidade['drones']))
            fig.update_layout(title='Número de drones cadastrados nas 10 cidades com mais registros no estado {}'.format(estado), yaxis={'categoryorder':'sum ascending', 'title' : 'Cidade'}, xaxis={'title' : 'Drones cadastrados'})
            plotly.io.write_html(fig,"../website/webviews/vis_ranking_{}_{}.html".format(regiao.lower(), estado.lower()),full_html=False)

    # data_filtered = cidadeDf[cidadeDf.regiao == "Norte"]
    # data_filtered = data_filtered[data_filtered.estado == 'RR']
    # data_filtered.sort_values(by=['drones'])
    # data_filtered = data_filtered[0:10]
    # fig = go.Figure(go.Bar(x= data_filtered['drones'], y= data_filtered['cidade'], name="Drones por região", orientation='h', marker=dict(color="#095256")))
    # data_filtered = data[data.Ano == "2019"]
    # fig.add_trace(go.Bar(x= data_filtered['Drones cadastrados'], y= data['Estado'].unique(), name="2019", orientation='h', marker=dict(color="#5AAA95"), hovertemplate = "drones cadastrados: %{hovertext}<extra></extra>", hovertext = data_filtered['Drones cadastrados']))
    # data_filtered = data[data.Ano == "2020"]
    # fig.add_trace(go.Bar(x= data_filtered['Drones cadastrados'], y= data['Estado'].unique(), name="2020", orientation='h', marker=dict(color="#BB9F06"), hovertemplate = "drones cadastrados: %{hovertext}<extra></extra>", hovertext = data_filtered['Drones cadastrados']))
    # fig.update_layout(title='Total de drones cadastrados por região', yaxis={'categoryorder':'sum ascending', 'title' : 'Região'}, xaxis={'title' : 'Drones cadastrados'}, height=700)
    # fig.update_xaxes(range=[0,27000])

    # app = dash.Dash()
    # app.layout = html.Div([
    #     dcc.Graph(id='rank1', figure=fig)
    # ]
    # )

    # app.run_server(debug=False, use_reloader=True)