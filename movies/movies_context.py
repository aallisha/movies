from .models import Movie

def movies_slider(request):
    """
    Adds a context to every template of our movies which contains the recently added movies
    """
    recent_movies = Movie.objects.all().order_by('created_date')[0:1]
    # this should be added to our settings context processors with the format <app>.<this filename>.<this function>
    return { 'movies_slider': recent_movies }

