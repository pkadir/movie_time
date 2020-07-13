from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib import messages

from .models import Movies


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect('/movies')
                elif user:
                    return redirect('/movies')

                else:
                    messages.warning(request, 'You are not authorized to access this page.')
                    return render(request, 'login.html')
            else:
                messages.warning(request, 'Username or Password Incorrect.')
                return render(request, 'login.html')
        else:
            messages.warning(request, 'Please enter username and password.')
            return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def show_details(request, pk):
    try:
        movie = Movies.objects.get(pk=pk)
        return render(request, 'details.html', {'movie': movie})
    except Exception as e:
        messages.warning(request, "Some   Error Occurred... Please Try Again" + str(e))
        return redirect('/movies')


class AddMovie(View):
    def get(self, request):
        return render(request, 'add_movie.html')

    def post(self, request):
        if request.method == "POST":
            try:
                movie_name = request.POST.get('movie_name')
                director = request.POST.get('director')
                popularity = request.POST.get('popularity')
                imdb_score = request.POST.get('imdb_score')
                all_genre = request.POST.get('all_genre')
                print(all_genre.split(','))
                image = request.POST.get('image')
                print('Image url', image)

                movie = Movies.objects.create(movie_name=movie_name, director_name=director, popularity=int(popularity),
                                              imdb_score=int(imdb_score), image=image)
                movie.save()
                for genre in all_genre.split(','):
                    movie.genre.create(genre=genre)
                    movie.save()
                return redirect('/movies')
            except Exception as e:
                messages.warning(request, "Some   Error Occurred... Please Try Again" + str(e))
                return redirect('/movies')
        else:
            messages.warning(request, "Some   Error Occurred... Please Try Again" + str(e))
            return redirect('/movies')


def all_movies(request):
    movies = Movies.objects.all()
    return render(request, 'movies.html', {'movies': movies})


def delete_movie(request, pk):
    movie = Movies.objects.get(pk=pk)
    movie.delete()
    return redirect('/movies')


def edit_movie(request, pk):
    movie = Movies.objects.get(pk=pk)
    return render(request, 'edit_movie.html', {'movie': movie})


def update_movie(request, pk):
    if request.method == "POST":
        try:
            movie_name = request.POST.get('movie_name')
            director = request.POST.get('director')
            popularity = request.POST.get('popularity')
            imdb_score = request.POST.get('imdb_score')
            all_genre = request.POST.get('all_genre')
            print(all_genre.split(','))
            image = request.POST.get('image')

            movie = Movies.objects.filter(pk=pk).update(movie_name=movie_name, director_name=director,
                                                        popularity=int(popularity),
                                                        imdb_score=int(imdb_score), image=image)
            for genre in all_genre.split(','):
                movie.genre.create(genre=genre)
                movie.save()
            return redirect('/movies')
        except Exception as e:
            messages.warning(request, "Some   Error Occurred... Please Try Again" + str(e))
            return redirect('/movies')
    else:
        messages.warning(request, "Some   Error Occurred... Please Try Again" + str(e))
        return redirect('/movies')
