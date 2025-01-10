# Importation du module forms de Django
from django import forms
# Importation du modèle FichierCSV
from .models import FichierCSV

# Définition du formulaire pour le modèle FichierCSV
class FichierCSVForm(forms.ModelForm):
    # Classe Meta utilisée pour configurer les options du formulaire
    class Meta:
        model = FichierCSV  # Spécifie le modèle associé à ce formulaire
        fields = ['fichier']  # Indique les champs du modèle à inclure dans le formulaire
