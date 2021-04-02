from django.urls import path
from .views import (MovieListView, MovieDetailView,
                    MovieSearchView, MovieGenreView,
                    MovieCastView)

from . import views

app_name = 'movies_app'

urlpatterns = [
    # movie_list.html
    path('', MovieListView.as_view(), name='movie_list'),

    # movie_detail.html
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),

    path('search/',MovieSearchView.as_view(), name='search'),

    path('genre/<str:genre>', MovieGenreView.as_view(), name='movie_genre'),

    path('cast/<slug:actor_slug>', MovieCastView.as_view(), name='movie_cast'),
]
