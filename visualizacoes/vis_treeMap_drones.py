import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv('../base_dados/treeMap.csv')

levels = ['cidade', 'estado', 'regiao'] # levels used for the hierarchical chart
color_columns = ['drones']
value_column = 'drones'

soma = 77812
def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
    """
    Build a hierarchy of levels for Sunburst or Treemap charts.

    Levels are given starting from the bottom to the top of the hierarchy,
    ie the last level corresponds to the root.
    """
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


df_all_trees = build_hierarchical_dataframe(df, levels, value_column, color_columns)
average_score = df['drones'].sum() / soma 

fig = go.Figure()
fig.add_trace(go.Treemap(
    labels=df_all_trees['id'],
    parents=df_all_trees['parent'],
    values=df_all_trees['value'],
    branchvalues='total',
    name="",
    marker=dict(
        colors=df_all_trees['color'],
        colorscale='IceFire',
        cmid=average_score),
    hovertemplate='<b>%{label} </b> <br> Número de drones: %{value}<br> Porcentagem do total: %{color:.2f}',
    maxdepth=2
    ))

fig.update_layout(margin=dict(t=50, b=50, r=50, l=50), title="Número de drones por região, estado e cidade",height=700)

app = dash.Dash()
app.layout = html.Div([
dcc.Graph(id='rank1', figure=fig)])

app.run_server(debug=False, use_reloader=True)