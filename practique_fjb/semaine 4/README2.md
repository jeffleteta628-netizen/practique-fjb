# Semaine 4 — EDA : Analyse des Prix Alimentaires au Cameroun

**Étudiant :** Jeff K.  
**Formation :** Développement Web Full Stack — LocalHost Academy  
**Module :** Analyse exploratoire de données (EDA)

---

## Aperçu du projet

Ce notebook réalise une analyse exploratoire complète (EDA) sur un dataset de prix alimentaires relevés dans les marchés de Douala, Yaoundé et Bafoussam.

| Étape | Description | Points |
|-------|-------------|--------|
| Tâche 1 | Audit complet : shape, types, NaN, doublons, outliers | 3 pts |
| Tâche 2 | Nettoyage justifié : NaN → médiane, outliers ÷ 10, doublons supprimés | 3 pts |
| Tâche 3 | Analyse univariée : distributions, skewness, stats | 3 pts |
| Tâche 4 | Analyse bivariée : corrélations, boxplots, évolution mensuelle | 3 pts |
| Tâche 5 | Analyse multivariée : pairplot, heatmaps | 3 pts |
| Tâche 6 | 4 features créées : prix_par_quantite, est_saison_haute, tranche_prix, volume_marche | 3 pts |
| Tâche 7 | Rapport EDA + 5 hypothèses ML | 2 pts |

---

## Résultats clés

- **Dataset brut** : 615 lignes (20 NaN + 15 doublons + 5 outliers détectés et corrigés)
- **Dataset final** : 600 lignes × 12 colonnes (8 originales + 4 features)
- **Le produit** est le principal déterminant du prix (r ≈ 0.80)
- **Effet saisonnier** confirmé : Avr/Mai = +8% de prix en moyenne
- **Yaoundé** légèrement plus cher que Douala (+14% en moyenne)

---

## Figures générées

| Fichier | Contenu |
|---------|---------|
| `figures/fig1_univariee.png` | Distributions des 6 variables |
| `figures/fig2_bivariee.png` | Boxplots, prix par produit, évolution mensuelle |
| `figures/fig3_multivariee.png` | Heatmaps produit×mois et corrélations |
| `figures/fig4_pairplot.png` | Pairplot variables numériques |
| `figures/fig5_features.png` | Visualisation des features engineerées |

---

## Comment exécuter

```bash
# 1. Installer les dépendances
pip install pandas numpy matplotlib seaborn scipy jupyter

# 2. Lancer le notebook
jupyter notebook EDA_JEFF.ipynb
```

Compatible : **PyCharm** | **VS Code** | **Jupyter Notebook** | **GitHub** (rendu automatique)

---

## Structure du dossier

```
semaine-4/
├── EDA_JEFF.ipynb                      ← Notebook principal (livrable)
├── prix_alimentaires_cameroun.csv      ← Dataset brut généré
├── prix_alimentaires_clean.csv         ← Dataset après nettoyage
├── prix_alimentaires_features.csv      ← Dataset avec features engineerées
├── figures/
│   ├── fig1_univariee.png
│   ├── fig2_bivariee.png
│   ├── fig3_multivariee.png
│   ├── fig4_pairplot.png
│   └── fig5_features.png
└── README.md
```

---

*Source des données : dataset simulé avec `numpy.random.seed(2024)` pour reproductibilité*
