from django.db import models


class motivos(models.Model):
    BICONDICIONAL = [('Y', 'SIM'), ('N', 'NÃO')]
    OPTIONS = [
        ("B", "Bastante"),
        ("M", "mais ou menos"),
        ("P", "Pouco"),
    ]
    title = models.CharField(max_length=100)
    mecanica = models.CharField(max_length=70)
    concorda = models.CharField(max_length=1, choices=OPTIONS, default='')
    ja_jogou = models.CharField(max_length=1, choices=BICONDICIONAL)


class sensações(models.Model):
    BICONDICIONAL = [('Y', 'SIM'), ('N', 'NÃO')]
    RANKING = [
        ("H", "high"),
        ("M", "Medium,"),
        ("L", "low"),
    ]
    title = models.CharField(max_length=100)
    dificuldade = models.CharField(max_length=1, choices=RANKING)
    fez = models.CharField(max_length=1, choices=BICONDICIONAL)
    prazer = models.CharField(max_length=1, choices=RANKING)

class MinhaTabela(models.Model):
    tittle = models.CharField(max_length=100)
    so = models.CharField(max_length=100)
    processadsor = models.CharField(max_length=100)
    memoria = models.CharField(max_length=100)
    placa_de_video= models.CharField(max_length=100)
    directx = models.CharField(max_length=100)