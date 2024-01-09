from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Animale(models.Model):
    Nom=models.CharField(max_length=250)
    Age=models.IntegerField()
    statut_vaccial=models.CharField(max_length=250)
    sterillisation=models.CharField(max_length=250)
    type=models.CharField(max_length=20)
    

class client:
    Fullname=models.CharField(max_length=10)
    age=models.IntegerField()
    phoneNumber=models.IntegerField()
    adress=models.CharField(max_length=250)    

class Adoption(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cin = models.CharField(max_length=100)
    salaire_mensuel = models.DecimalField(max_digits=10, decimal_places=2)
    logement_avec_jardin = models.BooleanField(default=False)
    situation_familiale = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)

  