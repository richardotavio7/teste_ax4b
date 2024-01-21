from django.db import models

class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Postagens(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    user_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()

# Create your models here.
