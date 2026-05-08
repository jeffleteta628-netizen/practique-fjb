import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = px.data.gapminder()
df_afrique = df[df['continent'] == 'Africa']
liste_pays = sorted(df_afrique['country'].unique())

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("🌍 Mon premier dashboard africain",
            style={'textAlign': 'center', 'color': '#2c3e50'}),
html.Label("Choisissez un pays :"),
    dcc.Dropdown(
        id='selection-pays',
        options=[{'label': pays, 'value': pays} for pays in liste_pays],
        value='Senegal'  # Valeur par défaut
    ),
    dcc.Graph(id='graphique-esperance-vie'),
 dcc.Graph(id='carte-afrique')
])


@app.callback(
    Output('graphique-esperance-vie', 'figure'),
    Input('selection-pays', 'value')
)
def mettre_a_jour_courbe(pays_choisi):
    # Filtrer les données pour le pays choisi
    donnees_pays = df_afrique[df_afrique['country'] == pays_choisi]

    # Créer le graphique
    fig = px.line(donnees_pays,
                  x='year',
                  y='lifeExp',
                  title=f'Espérance de vie au {pays_choisi}')

    return fig


@app.callback(
    Output('carte-afrique', 'figure'),
    Input('selection-pays', 'value')  # Même input, mais on pourrait en ajouter
)
def mettre_a_jour_carte(pays_choisi):
    # On prend l'année la plus récente
    annee_recente = df_afrique['year'].max()
    donnees_annee = df_afrique[df_afrique['year'] == annee_recente]

    # Créer la carte
    fig = px.choropleth(donnees_annee,
                        locations='iso_alpha',
                        color='lifeExp',
                        hover_name='country',
                        title=f'Espérance de vie en Afrique ({annee_recente})',
                        color_continuous_scale='Viridis')

    # Zoomer sur l'Afrique
    fig.update_geos(scope='africa')

    return fig
if __name__ == '__main__':
    app.run(debug=True)
