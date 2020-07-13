from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'movies'


urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('details/<pk>/', views.show_details, name='details'),
    path('logout/', views.logout, name='logout'),
    path('movies/', views.all_movies, name='movies'),
    path('add_movie/', views.AddMovie.as_view(), name='add_movie'),
    path('delete/<pk>/', views.delete_movie, name='delete'),
    path('edit/<pk>/', views.edit_movie, name='edit'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)