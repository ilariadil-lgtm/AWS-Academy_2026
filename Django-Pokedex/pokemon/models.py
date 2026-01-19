from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    salute = models.PositiveIntegerField(default=50)
    attacco = models.PositiveIntegerField(default=50)
    difesa = models.PositiveIntegerField(default=50)
    attacco_speciale = models.PositiveIntegerField(default=50)
    difesa_speciale = models.PositiveIntegerField(default=50)
    velocita = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.nome
