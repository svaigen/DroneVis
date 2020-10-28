import plotly
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Load data
df = pd.read_csv('../base_dados/dadosPordia2.csv')


fig = go.Figure()
df_ordenado = df.sort_values(by='day')

dff = df_ordenado.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,line=dict(color="#000066"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="AC"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#3333cc"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="AL"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#666699"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="AP"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#6600cc"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="AM"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#cc00ff"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="BA"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#660066"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="CE"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#cc0099"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="DF"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#993366"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="ES"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#660033"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="GO"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#993333"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="MA"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#cc6600"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="MT"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#ff9900"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="MS"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#663300"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="MG"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#cc9900"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="PA"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#cccc00"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="PB"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#666633"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="PR"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#009900"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="PE"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#333300"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="PI"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#009933"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="RJ"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#003300"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="RN"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#00cc66"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="RS"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#009999"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="RO"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#336699"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="RR"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#006699"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="SC"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#00ccff"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="SP"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#3366cc"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="SE"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#000099"),name=""))

data_filtered = df_ordenado[df_ordenado.estado=="TO"]
dff = data_filtered.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(
    x=df_ordenado['day'].unique(), 
    y=dff.estado,visible=False,line=dict(color="#00ffff"),name=""))


# Set title
fig.update_layout(
    title_text="Número de drones cadastrados ao longo do tempo",height=700
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="2020",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1a",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=[{"visible": [True, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo"}],
                    label="All",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, True, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Acre"}],
                    label="AC",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, True, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado de Alagoas"}],
                    label="AL",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, True, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Amapá"}],
                    label="AP",
                    method="update"
                ),
                 dict(
                    args=[{"visible": [False, False, False, False, True,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Amazonas"}],
                    label="AM",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,True, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado da Bahia"}],
                    label="BA",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, True, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Ceará"}],
                    label="CE",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, True, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no Distrito Federal"}],
                    label="DF",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, True, False,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Espírito Santo"}],
                    label="ES",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, True,False, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado de Goiás"}],
                    label="GO",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,True, False, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Maranhão"}],
                    label="MA",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, True, False, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Mato Grosso"}],
                    label="MT",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, True, False, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Mato Grosso do Sul"}],
                    label="MS",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, True, False,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado de Minas Gerais"}],
                    label="MG",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, True,False, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Pará"}],
                    label="PA",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, True, False, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado da Paraíba"}],
                    label="PB",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, True, False, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Paraná"}],
                    label="PR",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, True, False, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado de Pernambuco"}],
                    label="PE",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, False, True, False,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Piauí"}],
                    label="PI",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, False, False, True,False, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Rio de Janeiro"}],
                    label="RJ",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, False, False, False,True, False, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Rio Grande do Norte"}],
                    label="RN",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, False, False, False,False, True, False, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Rio Grande do Sul"}],
                    label="RS",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, False, False, False,False, False, True, False, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado de Rondônia"}],
                    label="RO",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, False, False, False,False, False, False, True, False,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado de Roraima"}],
                    label="RR",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, False, False, False,False, False, False, False, True,False, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado de Santa Catarina"}],
                    label="SC",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, False, False, False,False, False, False, False, False,True, False, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado de São Paulo"}],
                    label="SP",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, False, False, False,False, False, False, False, False,False, True, False]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado de Sergipe"}],
                    label="SE",
                    method="update"
                ),
                dict(
                    args=[{"visible": [False, False, False, False, False,False, False, False, False, False,False, False, False, False, False, False, False, False, False, False,False, False, False, False, False,False, False, True]},
                           {"title": "Número de drones cadastrados ao longo do tempo no estado do Tocantins"}],
                    label="TO",
                    method="update"
                )
            ]),
            direction="down",
            pad={"l":1350},
            showactive=True,
         #   x=0.005,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

plotly.io.write_html(fig,"../website/webviews/vis_linha_qtd_drone.html",full_html=False)

# app = dash.Dash()
# app.layout = html.Div([
# dcc.Graph(id='rank1', figure=fig)])

# app.run_server(debug=False, use_reloader=True)