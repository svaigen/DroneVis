import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly

df = pd.read_csv('../base_dados/dadosPordia2.csv')
fig = make_subplots(6, 5,subplot_titles=('Acre (AC)','Alagoas (AL)','Amapá (AP)','Amazonas (AM)','Bahia (BA)','Ceará (CE)','Espírito Santo (ES)',
'Goiás (GO)','Maranhão (MA)','Mato Grosso (MT)','Mato Grosso do Sul (MS)','Minas Gerais (MG)','Pará (PA)','Paraíba (PB)', 
'Paraná (PR)','Pernambuco (PE)','Piauí (PI)','Rio de Janeiro (RJ)','Rio Grande Norte (RN)','Rio Grande Sul (RS)','Rondônia (RO)',
'Roraima (RR)','Santa Catarina (SC)','São Paulo (SP)','Sergipe (SE)','Tocantins (TO)'))
df_ordenado = df.sort_values(by='day')

cols=['rgb(35, 80, 105)']

df1 = df_ordenado.query("estado == 'AC'")
dff = df1.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines', name='Acre',marker=dict(color=cols[0])), 1, 1)

df2 = df.query("estado == 'AL'")
dff = df2.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines', name='Alagoas',marker=dict(color=cols[0])), 1, 2)

df3 = df.query("estado == 'AP'")
dff = df3.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines', name='Amapá',marker=dict(color=cols[0])), 1,3)

df4 = df.query("estado == 'AM'")
dff = df4.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 1,4)

df5 = df.query("estado == 'BA'")
dff = df5.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 1,5)

df6 = df.query("estado == 'CE'")
dff = df6.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 2,1)

df8 = df.query("estado == 'ES'")
dff = df8.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 2,2)

df9 = df.query("estado == 'GO'")
dff = df9.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 2,3)

df10 = df.query("estado == 'MA'")
dff = df10.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 2,4)

df11 = df.query("estado == 'MT'")
dff = df11.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 2,5)

df12 = df.query("estado == 'MS'")
dff = df12.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 3,1)

df13 = df.query("estado == 'MG'")
dff = df13.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 3,2)

df14 = df.query("estado == 'PA'")
dff = df14.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 3,3)

df15 = df.query("estado == 'PB'")
dff = df15.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 3,4)

df16 = df.query("estado == 'PR'")
dff = df16.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 3,5)

df17 = df.query("estado == 'PE'")
dff = df17.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 4,1)

df18 = df.query("estado == 'PI'")
dff = df18.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 4,2)

df19 = df.query("estado == 'RJ'")
dff = df19.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 4,3)

df20 = df.query("estado == 'RN'")
dff = df20.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 4,4)

df21 = df.query("estado == 'RS'")
dff = df21.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 4,5)

df22 = df.query("estado == 'RO'")
dff = df22.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 5,1)

df23 = df.query("estado == 'RR'")
dff = df23.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 5,2)

df24 = df.query("estado == 'SC'")
dff = df24.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 5,3)

df25 = df.query("estado == 'SP'")
dff = df25.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 5,4)

df26 = df.query("estado == 'SE'")
dff = df26.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 5,5)

df27 = df.query("estado == 'TO'")
dff = df27.set_index(["day","elemento"]).count(level='day')
fig.add_trace(go.Scatter(x=df_ordenado['day'].unique(), y=dff.estado, mode='lines',marker=dict(color=cols[0]) ), 6,1)






fig.update_xaxes(range=['2018-01-01','2020-01-07'],showgrid=False,visible=False)
fig.update_layout(showlegend=False,template=None, autosize=True, margin={'t' : 30})
fig.update_yaxes(range=[0,80],showgrid=False,visible=False)

plotly.io.write_html(fig, file="./../website/webviews/peqmul-drone.html", full_html=False, default_height="100%")