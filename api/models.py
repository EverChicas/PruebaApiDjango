from django.db import models

# Create your models here.
class Credencial(models.Model):
    nombre = models.CharField(max_length=100)
    token = models.CharField(max_length=300)