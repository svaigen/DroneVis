import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import util

def prepareData():
    allData,inscricao,validade,operador,tipo_pessoa,tipo_uso,fabricante,modelo,numero_serie,peso_maximo,cidade,estado,ramo = util.leituraDados()
    years = ["2020","2019","2018"]
    statesList = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
    
    pessoas = {}
    for op in operador:
        if(op in pessoas):
            pessoas[op] += 1
        else:
            pessoas[op] = 1

    pessoasMais = []
    for p in pessoas.keys():
        if(pessoas[p] > 30):
           # print(pessoas[p],p)
            pessoasMais.append((pessoas[p],p))

    pessoaEstado = []
    for o in pessoasMais:
        for a in allData:
            if(a[2] == o[1]):
                pessoaEstado.append((a[10],o[1],o[0]))
                break


    #print({k: v for k, v in sorted(pessoas.items(), key=lambda item: item[1])})
    estados = []
    pessoas = []
    drones = []
    cont = 0
    conts = []
    for p in pessoaEstado:
        estados.append(p[0])
        pessoas.append(p[1])
        drones.append(p[2])
        conts.append(cont)
        cont+=1
    d = {'':conts,'estado': estados, 'pessoa': pessoas, 'drones': drones}
    return pd.DataFrame(d)



df = pd.read_csv('../base_dados/treeMap.csv')

def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
        dfg = df.groupby(levels[i:]).sum()
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'total'
        df_tree['value'] = dfg[value_column]
        df_tree['color'] = dfg[color_columns[0]] / soma
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series(dict(id='total', parent='',
                              value=df[value_column].sum(),
                              color=df[color_columns[0]].sum() / soma))
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees



if __name__ == '__main__':
    df = prepareData()
    
    levels = ['pessoa', 'estado'] # levels used for the hierarchical chart
    color_columns = ['drones']
    value_column = 'drones'

    soma = 1974
    
    df_all_trees = build_hierarchical_dataframe(df, levels, value_column, color_columns)
    average_score = df['drones'].sum() / soma 

    pallete = util.colorViridis(1)

    rgbPallete = []
    for counter in range(len(pallete)):
        r = pallete[counter][0]
        g = pallete[counter][1]
        b = pallete[counter][2]
        color = "rgb({},{},{})".format(r, g, b)
        rgbPallete.append(color)

    fig = go.Figure()
    fig.add_trace(go.Treemap(
        labels=df_all_trees['id'],
        parents=df_all_trees['parent'],
        values=df_all_trees['value'],
        branchvalues='total',
        name="",
        marker=dict(
            colors=df_all_trees['color'],
            colorscale=rgbPallete,
            cmid=average_score),
        hovertemplate='<b>%{label} </b> <br> Número de drones: %{value}<br> Porcentagem do total: %{color:.2f}',
        maxdepth=2
        ))

    fig.update_layout(margin=dict(t=50, b=50, r=50, l=50), title="Proprietários com o maior número de drones cadastrados por estado",height=700)

    app = dash.Dash()
    app.layout = html.Div([
    dcc.Graph(id='rank1', figure=fig)])

    app.run_server(debug=False, use_reloader=True)