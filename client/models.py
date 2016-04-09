from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    mnemo = models.CharField(max_length=15, unique=True, verbose_name="Mnemonique")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    naissance = models.DateField(verbose_name="Date de naissance")
    mail = models.EmailField(unique=True)
    solde = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Solde")
    HOMME = 'HO'
    FEMME = 'FE'
    SEXE = (
        (HOMME, 'Homme'),
        (FEMME, 'Femme'),
    )
    sexe = models.CharField(max_length=2, choices=SEXE)

    MINI = 'MINI'
    NOVICE = 'NOVICE'
    TOP = 'TOP'
    NIVEAU = (
        (MINI, 'MINI'),
        (NOVICE, 'NOVICE'),
        (TOP, 'TOP'),
    )
    niveau = models.CharField(max_length=7, choices=NIVEAU)

    ADMIN = 'AD'
    USER = 'US'
    ROLE = (
        (ADMIN, 'Admin'),
        (USER, 'User'),
    )
    role = models.CharField(max_length=5,
                                      choices=ROLE)


    def __str__(self):
        return self.mnemo



