# --- ÉTAPE 1 : IMPORTER LES BIBLIOTHÈQUES ---
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# --- ÉTAPE 2 : CHARGER LES DONNÉES ---
# Gapminder contient des données sur les pays (PIB, espérance de vie, population)
df = px.data.gapminder()

# On garde uniquement les pays d'Afrique
df_afrique = df[df['continent'] == 'Africa']

# On récupère la liste des pays africains
liste_pays = sorted(df_afrique['country'].unique())

# Liste des années disponibles
liste_annees = sorted(df_afrique['year'].unique())

# --- ÉTAPE 3 : CRÉER L'APPLICATION ---
app = dash.Dash(__name__)

# Titre de la page dans le navigateur
app.title = "Dashboard Afrique — Analyse des données"

# --- ÉTAPE 4 : CONSTRUIRE L'INTERFACE (LAYOUT) ---
app.layout = html.Div(style={'backgroundColor': '#f8f9fa', 'fontFamily': 'Arial, sans-serif', 'padding': '20px'}, children=[

    # En-tête
    html.Div(style={'backgroundColor': '#1a1a2e', 'padding': '20px', 'borderRadius': '10px', 'marginBottom': '20px'}, children=[
        html.H1("🌍 Dashboard — Données Africaines",
                style={'textAlign': 'center', 'color': '#e6c97e', 'margin': '0', 'fontSize': '28px'}),
        html.P("Gapminder Dataset — Espérance de vie, PIB et Population (1952–2007)",
               style={'textAlign': 'center', 'color': '#aaaaaa', 'margin': '5px 0 0 0', 'fontSize': '14px'})
    ]),

    # Ligne de contrôles
    html.Div(style={'display': 'flex', 'gap': '30px', 'marginBottom': '20px', 'alignItems': 'flex-end'}, children=[

        # Sélection du pays
        html.Div(style={'flex': '1'}, children=[
            html.Label("🗺️ Choisissez un pays :", style={'fontWeight': 'bold', 'color': '#333', 'display': 'block', 'marginBottom': '5px'}),
            dcc.Dropdown(
                id='selection-pays',
                options=[{'label': pays, 'value': pays} for pays in liste_pays],
                value='Senegal',
                clearable=False,
                style={'borderRadius': '8px'}
            )
        ]),

        # Sélection de l'année (Tâche 1 : slider)
        html.Div(style={'flex': '2'}, children=[
            html.Label("📅 Année pour la carte :", style={'fontWeight': 'bold', 'color': '#333', 'display': 'block', 'marginBottom': '5px'}),
            dcc.Slider(
                id='slider-annee',
                min=min(liste_annees),
                max=max(liste_annees),
                step=5,
                value=max(liste_annees),
                marks={str(a): str(a) for a in liste_annees},
                tooltip={"placement": "bottom", "always_visible": False}
            )
        ])
    ]),

    # Ligne graphiques 1 et 2
    html.Div(style={'display': 'flex', 'gap': '15px', 'marginBottom': '15px'}, children=[

        # Graphique 1 : Évolution espérance de vie
        html.Div(style={'flex': '1', 'backgroundColor': 'white', 'borderRadius': '10px',
                        'padding': '15px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'}, children=[
            dcc.Graph(id='graphique-esperance-vie', style={'height': '350px'})
        ]),

        # Graphique 3 (Tâche 2) : Scatter PIB / Espérance de vie
        html.Div(style={'flex': '1', 'backgroundColor': 'white', 'borderRadius': '10px',
                        'padding': '15px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'}, children=[
            dcc.Graph(id='graphique-pib-vie', style={'height': '350px'})
        ])
    ]),

    # Graphique 2 : Carte de l'Afrique (pleine largeur)
    html.Div(style={'backgroundColor': 'white', 'borderRadius': '10px',
                    'padding': '15px', 'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'marginBottom': '15px'}, children=[
        dcc.Graph(id='carte-afrique', style={'height': '450px'})
    ]),

    # Pied de page
    html.Div(style={'textAlign': 'center', 'color': '#999', 'fontSize': '12px', 'marginTop': '10px'}, children=[
        html.P("Source des données : Gapminder — Visualisation réalisée avec Dash & Plotly")
    ])
])


# --- ÉTAPE 5 : AJOUTER L'INTERACTIVITÉ (CALLBACKS) ---

# Callback pour le graphique en courbe — espérance de vie
@app.callback(
    Output('graphique-esperance-vie', 'figure'),
    Input('selection-pays', 'value')
)
def mettre_a_jour_courbe(pays_choisi):
    donnees_pays = df_afrique[df_afrique['country'] == pays_choisi]

    fig = px.line(donnees_pays,
                  x='year',
                  y='lifeExp',
                  markers=True,
                  title=f'📈 Espérance de vie — {pays_choisi}',
                  labels={'year': 'Année', 'lifeExp': 'Espérance de vie (ans)'})

    fig.update_traces(line_color='#e6c97e', line_width=3, marker_color='#1a1a2e', marker_size=8)
    fig.update_layout(plot_bgcolor='#fafafa', paper_bgcolor='white',
                      font_color='#333', title_font_size=14)
    return fig


# Callback pour la carte choroplèthe — avec slider d'année (Tâche 1)
@app.callback(
    Output('carte-afrique', 'figure'),
    Input('selection-pays', 'value'),
    Input('slider-annee', 'value')
)
def mettre_a_jour_carte(pays_choisi, annee_choisie):
    donnees_annee = df_afrique[df_afrique['year'] == annee_choisie]

    fig = px.choropleth(donnees_annee,
                        locations='iso_alpha',
                        color='lifeExp',
                        hover_name='country',
                        hover_data={'pop': ':,.0f', 'gdpPercap': ':,.0f'},
                        title=f'🗺️ Espérance de vie en Afrique — {annee_choisie}',
                        color_continuous_scale='YlOrRd',
                        labels={'lifeExp': 'Espérance de vie'})

    fig.update_geos(scope='africa', bgcolor='#f0f0f0', landcolor='#e8e8e8',
                    showframe=False, showcoastlines=True)
    fig.update_layout(paper_bgcolor='white', font_color='#333',
                      title_font_size=14, margin={"r": 0, "t": 40, "l": 0, "b": 0})
    return fig


# Callback pour le scatter PIB / Espérance de vie (Tâche 2)
@app.callback(
    Output('graphique-pib-vie', 'figure'),
    Input('slider-annee', 'value')
)
def mettre_a_jour_scatter(annee_choisie):
    donnees_annee = df_afrique[df_afrique['year'] == annee_choisie]

    fig = px.scatter(donnees_annee,
                     x='gdpPercap',
                     y='lifeExp',
                     size='pop',
                     hover_name='country',
                     title=f'💰 PIB vs Espérance de vie — {annee_choisie}',
                     labels={'gdpPercap': 'PIB par habitant (USD)', 'lifeExp': 'Espérance de vie (ans)', 'pop': 'Population'},
                     color='lifeExp',
                     color_continuous_scale='Blues')

    fig.update_layout(plot_bgcolor='#fafafa', paper_bgcolor='white',
                      font_color='#333', title_font_size=14,
                      showlegend=False)
    return fig


# --- ÉTAPE 6 : LANCER L'APPLICATION ---
if __name__ == '__main__':
    app.run(debug=True)
