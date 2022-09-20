from django.db import models

#modele pour la classe voiture
class Voiture(models.Model):
    marque = models.fields.CharField(max_length=100)
    couleur = models.fields.CharField(max_length=50)
    annee = models.IntegerField()
    porte = models.IntegerField()
    climatiser = models.fields.CharField(max_length=5)
    energie = models.fields.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True) #pour date de création de chaque entité
    def __str__(self):
        return self.marque


 #modele pour classe client
class Client(models.Model):
    nom = models.fields.CharField(max_length=100)
    prenoms = models.fields.CharField(max_length=100)
    sexe = models.fields.CharField(max_length=15)
    profession = models.fields.CharField(max_length=150)
    credible = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)


#classe association

class Location(models.Model):
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    #les clés étrangères
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date_debut