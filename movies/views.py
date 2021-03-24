from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie, MovieLinks, MovieCast
from django.views.generic.edit import FormView
from .forms import CommentForm


class HomeView(ListView):
    model = Movie
    template_name = 'movies/movie_home.html'

    def get_context_data(self, **kwargs):
        """
        Returns the context object list to which we're adding the movie genres
        """
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_viewed'] = Movie.objects.filter(status='MV')
        context['recently_added'] = Movie.objects.filter(status='RA')
        return context

    
class MovieListView(ListView):
    # Render the template against a context containing a variable called object_list that contains all the movie objects.
    model = Movie
    paginate_by = 1

class MovieDetailView(DetailView):
    model = Movie
    paginate_by = 1

    def get_context_data(self, **kwargs):
        """
        Retrieves the movie links for our movie object and adds it to our context
        """
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        # retrieving the single movie object
        movie_object = super(MovieDetailView, self).get_object()
        # we'll use this 'link' variable in our templates
        context['link'] = MovieLinks.objects.filter(movie=self.get_object())
        # include only the approved comments
        context['comments'] = movie_object.comments.filter(active=True)
        # for displaying the related movies based on the genre
        context['related_movies'] = Movie.objects.filter(genre=self.get_object().genre)
        # get all of the actors that a movie object has and pass it to the context
        context['actors'] = movie_object.cast.all()
        # increment the views count every time the object is retrieved
        movie_object.views +=1
        movie_object.save()
        return context

class MovieCastView(ListView):
    model = Movie

    def get_queryset(self):
        """
        Returns the queryset that will be used to retrieve the object that this view will display,
        in this case, movies based on cast
        """
        # get the cast using the actor_slug value in the url
        self.cast = MovieCast.objects.get(actor_slug=self.kwargs.get('actor_slug'))
        # return all of the movies that related to the cast instance
        return Movie.objects.filter(cast=self.cast)

    def get_context_data(self, **kwargs):
        """
        Returns the context object list to which we're adding the movie casts
        """
        context = super(MovieCastView, self).get_context_data(**kwargs)
        movies = Movie.objects.filter(cast=self.cast)
        # filter movies based on the cast and include it in the context
        context['movies_of_actor'] = movies
        # also include the cast object in the context
        context['movie_cast'] = self.cast
        return context

class MovieGenreView(ListView):
    model = Movie
    paginate_by = 1

    def get_queryset(self):
       """
       Returns the queryset that will be used to retrieve the object that this view will display,
       in this case, movies based on genre
       """
       self.genre = self.kwargs['genre']
       # we're using this to filter the movie based on which genre is available in the url
       return Movie.objects.filter(genre=self.genre)

    def get_context_data(self, **kwargs):
        """
        Returns the context object list to which we're adding the movie genres
        """
        context = super(MovieGenreView, self).get_context_data(**kwargs)
        context['movie_genre'] = self.genre
        return context

class MovieSearchView(ListView):
    model = Movie
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = Movie.objects.filter(title__icontains=query)
        else:
            object_list = Movie.objects.all()
        return object_list

class MovieCommentFormView(FormView):
    form_class = CommentForm
    template_name = 'movies/movie_comment_form.html'


class MovieYearView(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'produced_date'
    make_object_list = True
    allow_future = True
    template_name = "movies/year.html"
