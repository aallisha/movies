from django.urls import path
from .views import (MovieListView, MovieDetailView,
                    MovieSearchView, MovieGenreView,
                    MovieCastView)

app_name = 'movies_app'

urlpatterns = [
    # movie_list.html
    path('', MovieListView.as_view(), name='movies_list'),

    # movie_detail.html
    path('<slug:slug>/', MovieDetailView.as_view(), name='movies_detail'),

    path('search/',MovieSearchView.as_view(), name='search'),

    path('genre/<str:genre>', MovieGenreView.as_view(), name='movies_genre'),

    path('cast/<slug:actor_slug>', MovieCastView.as_view(), name='movies_cast'),
]
