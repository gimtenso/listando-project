from djongo import models
from django.contrib.auth import get_user_model


class Stats(models.Model):
    user = models.CharField(max_length=100, primary_key=True)

    listas_completas = models.IntegerField(default=0)
    questoes_completas = models.IntegerField(default=0)
