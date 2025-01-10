
# Create your views here.

from django.urls import reverse
import pandas as pd
from django.shortcuts import render, redirect
from .models import FichierCSV
from .forms import FichierCSVForm
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return HttpResponse("<h1>Bienvenue sur le projet Data Analysis!</h1>")

# Fonction pour gérer l'upload de fichiers CSV

def upload_file(request):
    # Si la requête est un POST (formulaire envoyé)

    if request.method == 'POST':
        form = FichierCSVForm(request.POST, request.FILES)

        # Si le formulaire est valide
        if form.is_valid():
            form.save()
            return render(request, 'upload.html', {'form': form, 'success': 'Dataset uploaded successfully!'})
        else:
            return render(request, 'upload.html', {'form': form, 'error': 'There was an error uploading the dataset. Please try again with a csv file.'})
    else:
        form = FichierCSVForm()      # Création d'un formulaire vide si la requête n'est pas un POST
    return render(request, 'upload.html', {'form': form})

# Fonction pour afficher les données d'un fichier CSV uploadé

def afficher_donnees(request):
    fichier = FichierCSV.objects.last()  # Dernier fichier uploadé
    if not fichier:
        return render(request, 'indexation.html', {'resultat': 'Aucun fichier trouvé.'})
    
    df = pd.read_csv(fichier.fichier.path)   # Chargement du fichier CSV dans un DataFrame pandas
    ligne = request.GET.get('ligne')   # Récupère le numéro de ligne de la requête
    colonne = request.GET.get('colonne')   # Récupère le nom de la colonne de la requête
    resultat = None    # Initialisation de la variable de résultat
    # Si une ligne est spécifiée, tente de récupérer la ligne demandée

    if ligne:
        try:
            resultat = df.iloc[int(ligne)].to_dict()   # Convertit la ligne en dictionnaire
        except IndexError:
            resultat = 'Index de ligne invalide.'      # Si l'index est incorrect
    elif colonne:     # Si une colonne est spécifiée, tente de récupérer la colonne demandée

        try:
            resultat = df[colonne].to_list()   # Convertit la colonne en liste
        except KeyError:
            resultat = 'Nom de colonne invalide.'  # Si le nom de la colonne est incorrect

    return render(request, 'indexation.html', {'resultat': resultat})

# Fonction pour analyser des statistiques sur une colonne d'un fichier CSV

def analyse_statistique(request):
    fichier = FichierCSV.objects.last()  # Récupère le dernier fichier uploadé
    if not fichier:
        return render(request, 'analyse.html', {'resultat': 'Aucun fichier trouvé.'})

    df = pd.read_csv(fichier.fichier.path)  # Chargement du fichier CSV dans un DataFrame pandas
    colonne = request.GET.get('colonne')  # Récupère le nom de la colonne de la requête
    stats = None  # Initialisation de la variable de statistiques

    # Si une colonne est spécifiée, tente de calculer les statistiques
    if colonne:
        try:
            data = df[colonne]  # Sélectionne la colonne demandée
            stats = {
                'Moyenne': data.mean(),  # Calcule la moyenne
                'Médiane': data.median(),  # Calcule la médiane
                'Écart type': data.std(),  # Calcule l'écart type
                'Valeur minimale': data.min(),  # Calcule la valeur minimale
                'Valeur maximale': data.max(),  # Calcule la valeur maximale
            }
        except KeyError:
            stats = 'Nom de colonne invalide.'  # Si le nom de la colonne est incorrect

    return render(request, 'analyse.html', {'colonne': colonne, 'stats': stats})

# Fonction pour visualiser les données sous forme de graphiques

def visualisation_donnees(request):
    fichier = FichierCSV.objects.last()
    if not fichier:
        return render(request, 'visualisation.html', {'image': None, 'error': 'Aucun fichier trouvé.'})

    df = pd.read_csv(fichier.fichier.path)
    graph_type = request.GET.get('graph_type', 'scatter')
    colonne_x = request.GET.get('colonne_x')
    colonne_y = request.GET.get('colonne_y')
    image = None
    error = None

    try:
        plt.figure(figsize=(8, 6))
        if graph_type == 'scatter':
            sns.scatterplot(data=df, x=colonne_x, y=colonne_y)
        elif graph_type == 'line':
            sns.lineplot(data=df, x=colonne_x, y=colonne_y)
        elif graph_type == 'bar':
            sns.barplot(data=df, x=colonne_x, y=colonne_y)
        elif graph_type == 'hist':
            df[colonne_x].hist(bins=30, alpha=0.7, label=colonne_x)
            plt.legend()
        elif graph_type == 'heatmap':
            numeric_df = df.select_dtypes(include=['number'])  # Filtrer uniquement les colonnes numériques
            if numeric_df.empty:
                error = "Aucune donnée numérique disponible pour tracer une heatmap."
            else:
                sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
                plt.title('Heatmap des corrélations')

        elif graph_type == 'pie':
            if colonne_x:
                df[colonne_x].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
                plt.ylabel('')
                plt.title(f'Diagramme en secteurs : {colonne_x}')
        elif graph_type == 'boxplot':
            sns.boxplot(data=df, x=colonne_x, y=colonne_y)
        elif graph_type == 'pairplot':
            sns.pairplot(df)
            plt.close()  # Seaborn crée directement des figures, on peut les fermer ici
        else:
            error = 'Type de graphique invalide.'

        if graph_type != 'pairplot':  # Les pairplots ne nécessitent pas de sauvegarde directe
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()
            image = base64.b64encode(image_png).decode('utf-8')
            plt.close()

    except KeyError:
        error = 'Nom de colonne invalide ou données non disponibles.'
    except ValueError as ve:
        error = f'Erreur dans les données : {str(ve)}'

    return render(request, 'visualisation.html', {'image': image, 'error': error})

# Fonction pour afficher le tableau de bord (template de base)
def dashboard(request):
    return render(request, 'base.html')