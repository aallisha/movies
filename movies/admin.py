from django.contrib import admin
from .models import Movie, MovieLinks, MovieCast


admin.site.register(Movie)
admin.site.register(MovieLinks)
admin.site.register(MovieCast)
