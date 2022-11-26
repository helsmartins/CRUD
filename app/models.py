from django.db import models

# Create your models here.

#classe produto
class Oculos(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    cor = models.CharField(max_length=30)

#classe cliente
class Clientes(models.Model):
    nome = models.CharField(max_length=150)
    logradouro = models.CharField(max_length=150)
    telefone = models.CharField(max_length=50)
    cpf = models.CharField(max_length=30)
    
