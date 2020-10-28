import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv('../base_dados/dadosPordia2.csv')
fig = make_subplots(2, 3)
df_ordenado = df.sort_values(by='day')

df1 = df_ordenado.query("estado == 'SP'")
dff = df1.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines+text', text='São Paulo'), 1, 1)
fig.add_annotation(x=200, y=50,text="São Paulo",showarrow=False,yshift=10)

df2 = df.query("estado == 'RJ'")
dff = df2.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines', name='Rio de Janeiro',text='RJ'), 1, 2)

df3 = df.query("estado == 'MG'")
dff = df3.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines', name='Minas Gerais'), 1, 3)


df4 = df_ordenado.query("estado == 'AC'")
dff = df4.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines', name='Acre'), 2, 1)

df5 = df.query("estado == 'AL'")
dff = df5.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines', name='Alagoas'), 2, 2)

df6 = df.query("estado == 'AP'")
dff = df6.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines', name='Amapá'), 2,3)

fig.update_xaxes(range=['2018-01-01','2020-01-07'],showgrid=False,visible=False)
fig.update_layout(showlegend=False,template=None, height=400,title="Pequenos múltiplos da quantidade de drones cadastrados ao longo do tempo por estado")
fig.update_yaxes(range=[0,200],showgrid=False,visible=False)

app = dash.Dash()
app.layout = html.Div([
dcc.Graph(id='rank1', figure=fig)])

app.run_server(debug=False, use_reloader=True)