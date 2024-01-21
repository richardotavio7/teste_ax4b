from django.db import models

class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Postagens(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    user_id = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True)
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title


class Comentarios(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    body = models.TextField()
    post_id = models.ForeignKey(Postagens, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_id



# Create your models here.
