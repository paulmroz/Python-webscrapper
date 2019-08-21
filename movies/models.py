from django.db import models


# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    imdb_rating = models.IntegerField()
    metascore = models.IntegerField()
    votes = models.IntegerField()
    description = models.CharField(max_length=2000)
    type = models.CharField(max_length=255)
