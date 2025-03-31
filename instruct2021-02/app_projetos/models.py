from django.db import models

class Colecao(models.Model):
        nome = models.CharField(max_length=150)
        pacotes = models.CharField(max_length=150)
        versao = models.CharField(max_length=150)

        def __str__(self):
            return self.nome
