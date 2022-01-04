from django.db import models


class Game(models.Model):

    class Meta:
        app_label = 'simple_app'

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
