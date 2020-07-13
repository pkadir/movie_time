from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from movies.models import Movies
from movies.api.serializers import MovieSerializer
from rest_framework import viewsets


class MovieDetails(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movies.objects.all()
