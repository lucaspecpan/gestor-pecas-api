import dash
from dash import dcc, html, Output, Input
import plotly.express as px
import requests
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
API_URL = os.getenv("API_URL")

app = dash.Dash(__name__)

def get_data():
    response = requests.get(f"{API_URL}/pecas/")
    return pd.DataFrame(response.json())

app.layout = html.Div(className='container', children=[
    html.H1('Gestor de Peças', className='titulo'),
    dcc.Graph(id='estoque-graph'),
    dcc.Interval(id='interval-update', interval=60000, n_intervals=0),
])

@app.callback(
    Output('estoque-graph', 'figure'),
    Input('interval-update', 'n_intervals')
)
def update_graph(n):
    df = get_data()
    fig = px.bar(df, x='modelo', y='quantidade', color='montadora',
                 title='Estoque Atual por Modelo')
    fig.update_layout(template='plotly_white')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)