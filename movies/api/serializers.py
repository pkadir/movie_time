from rest_framework import serializers
from movies.models import Movies


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['movie_name', 'director_name', 'popularity', 'image', 'genre', 'imdb_score']
