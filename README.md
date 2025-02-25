# Data Analysis Project

## Description

Le projet **Data Analysis** permet d'importer, analyser et visualiser des fichiers CSV à l'aide de l'interface web Django. L'utilisateur peut télécharger un fichier CSV, explorer ses données, effectuer des analyses statistiques de base et générer des visualisations graphiques. Ce projet est conçu pour faciliter la gestion et l'analyse de données à l'aide de bibliothèques Python telles que Pandas, Matplotlib et Seaborn.

---

## Fonctionnalités

- **Téléchargement de fichiers CSV** : Permet à l'utilisateur de télécharger un fichier CSV sur le serveur.
- **Affichage des données** : Permet à l'utilisateur de voir les données contenues dans le fichier CSV, avec la possibilité d'afficher une ligne ou une colonne spécifique.
- **Analyse statistique** : Calcule et affiche des statistiques descriptives (moyenne, médiane, écart type, etc.) pour une colonne sélectionnée du fichier CSV.
- **Visualisation des données** : Permet de générer différents types de graphiques à partir des données du fichier CSV (diagramme en dispersion, ligne, barre, histogramme).

---

## Prérequis

Assurez-vous d'avoir installé les outils et bibliothèques suivants :

- Python 3.15
- Django 3.15 
- Pandas
- Matplotlib
- Seaborn

Vous pouvez installer les dépendances nécessaires en exécutant la commande suivante dans votre terminal :

```bash
pip install -r requirements.txt

python -m venv venv
source venv\Scripts\activate
python manage.py migrate
python manage.py runserver
```

---

## Structure du Projet

```plaintext
data-analysis-project/
│
├── data_analysis/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       ├── base.html
│       ├── upload.html
│       ├── analyse.html
│       ├── indexation.html
│       └── visualisation.html
├── static/
│   ├── css/
│   ├── images/
│   └── js/
├── manage.py
├── Pipfile
├── Pipfile.lock
└── db.sqlite3
```

- **data_analysis/** : Contient les fichiers de l'application Django (modèles, vues, formulaires, etc.).
- **templates/** : Contient les fichiers HTML pour l'interface utilisateur.
- **static/** : Contient les fichiers CSS, JS et images pour le design.
- **manage.py** : Outil de gestion Django.
- **requirements.txt** : Liste des dépendances du projet.
- **db.sqlite3** : Base de données SQLite utilisée par défaut.

---

## Utilisation

### 1. Téléchargement d’un fichier CSV
- Rendez-vous sur la page "Upload CSV".
- Sélectionnez et téléchargez un fichier CSV depuis votre ordinateur. Les données seront enregistrées dans la base de données pour une utilisation ultérieure.

### 2. Affichage des données
- Consultez le contenu du fichier CSV sous forme de tableau.
- Filtrez les données en affichant des lignes ou colonnes spécifiques.

### 3. Analyse des données
- Obtenez des statistiques descriptives sur vos données.
- Sélectionnez une colonne pour afficher des métriques comme la moyenne, la médiane, et l’écart-type.

### 4. Visualisation des données
- Créez des graphiques personnalisés :
  - **Scatter plot** (nuage de points)
  - **Histogram** (histogramme)
  - **Bar chart** (graphique en barre)
  - **Line chart** (graphique linéaire)

---

## Technologies utilisées

### Backend
- **Django** : Framework web Python pour la gestion des données et la logique serveur.
- **Pandas** : Manipulation et analyse des données.

### Frontend
- **Bootstrap** : Framework CSS et JavaScript pour la structure et le design de l’interface.
- **Matplotlib** et **Seaborn** : Génération de visualisations graphiques.

---

## Auteur

- **Wafae El Baghdadi**
  - **Email** : [wa.elbaghdadi@edu.umi.ac.ma](mailto:wa.elbaghdadi@edu.umi.ac.ma)
  - **GitHub** : [WafaeE-w](https://github.com/WafaeE-w)
  - **LinkedIn** : [WafaeElbaghdadi](https://www.linkedin.com/in/WafaeElbaghdadi)

---

## Remerciements

- À l'équipe Django pour son framework puissant.
- À Pandas, Matplotlib et Seaborn pour leurs outils exceptionnels d’analyse et de visualisation.

