from django.conf.urls import url, include
from django.urls import path

from . import views
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()

app_name = 'movies'
router.register(r'movie_details', views.MovieDetails)

urlpatterns = [
    url(r'^', include(router.urls))
    # path('', api_movie_details, name='details')
]