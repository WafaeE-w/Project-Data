from django.db import models

# Create your models here

class FichierCSV(models.Model):
    fichier = models.FileField(upload_to='uploads/')  # Chemin où les fichiers sont stockés
    date_ajout = models.DateTimeField(auto_now_add=True)  # Date d'ajout du fichier

    def __str__(self):
        return self.fichier.name
