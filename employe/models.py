from django.db import models

# Create your models here.
class Employe(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    poste = models.CharField(max_length=150)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom
    