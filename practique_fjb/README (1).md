# Visualisation de données avec Python

**Module :** Visualisation & Analyse de données  
**Formation :** Développement Web Full Stack — LocalHost Academy  
**Étudiant :** Jeff K.

---

## Contenu du dépôt

```
visualisation_data/
├── td/
│   └── TD_visualisation.ipynb    # Réponses aux exercices du TD
├── tp/
│   ├── dashboard.py              # Application Dash interactive
│   └── analyse.md                # Mini-analyse des données africaines
├── screenshots/
│   └── dashboard_preview.png     # Aperçu du dashboard
├── requirements.txt              # Dépendances Python
└── README.md                     # Ce fichier
```

---

## Aperçu du Dashboard

![Dashboard Preview](screenshots/dashboard_preview.png)

---

## Comment exécuter le projet

### Prérequis

- Python 3.8 ou supérieur
- pip

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Lancer le dashboard (TP)

```bash
cd tp
python dashboard.py
```

Puis ouvrez votre navigateur à l'adresse : **http://127.0.0.1:8050**

### Voir les exercices TD (Jupyter Notebook)

```bash
cd td
jupyter notebook TD_visualisation.ipynb
```

---

## Fonctionnalités du Dashboard

- **Sélection de pays** : menu déroulant pour choisir un pays africain
- **Slider d'année** : choisir l'année affichée sur la carte (1952–2007)
- **Graphique 1** : Évolution de l'espérance de vie pour le pays sélectionné
- **Graphique 2** : Relation PIB / Espérance de vie pour l'année sélectionnée
- **Carte choroplèthe** : Vue géographique de l'espérance de vie en Afrique

---

## Technologies utilisées

| Outil | Usage |
|-------|-------|
| Python 3 | Langage principal |
| Dash | Framework web pour le dashboard |
| Plotly Express | Graphiques interactifs |
| Pandas | Manipulation des données |
| Matplotlib | Graphiques statiques (TD) |
| Seaborn | Graphiques statistiques (TD) |
| Jupyter Notebook | Exercices interactifs |

---

## Compatibilité

| Environnement | Statut |
|---------------|--------|
| PyCharm | ✅ Compatible |
| Visual Studio Code | ✅ Compatible |
| Jupyter Notebook | ✅ Compatible (TD uniquement) |
| Terminal / cmd | ✅ Compatible |

---

## Source des données

- **Gapminder** via Plotly Express (`px.data.gapminder()`)
- **mpg dataset** via Seaborn (`sns.load_dataset('mpg')`)
