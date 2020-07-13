from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=250, null=False, blank=False)


class Movies(models.Model):
    movie_name = models.CharField(max_length=250, null=False, blank=False)
    genre = models.ManyToManyField(Genre)
    director_name = models.CharField(max_length=250, null=False, blank=False)
    popularity = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    imdb_score = models.IntegerField()

    def __str__(self):
        return self.movie_name
