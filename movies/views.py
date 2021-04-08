from django.views.generic import ListView, DetailView
from .models import Movie, MovieCast
from .forms import CommentForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib import messages


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
    """
    Render the template against a context containing a variable called object_list that contains all the movie objects.
    """
    model = Movie
    paginate_by = 1
    order_by = 'created_date'


class MovieDetailView(FormMixin, DetailView):
    model = Movie
    paginate_by = 1
    form_class = CommentForm

    def get_success_url(self):
        return reverse('movies_main:movies_detail', kwargs = {'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        """
        Retrieves the movie links for our movie object and adds it to our context
        """
        context = super(MovieDetailView, self).get_context_data(**kwargs)

        # retrieve the single movie object
        movie_object = super(MovieDetailView, self).get_object()

        # pass the comment form to context
        context['comment_form'] = CommentForm(initial={'movie': self.object})

        # get all the approved comments 
        context['comments'] = movie_object.comments.filter(active=True)

        # get all of the actors that a movie object has and pass it to the context
        context['actors'] = movie_object.cast.all()

        # for displaying the related movies based on the genre
        context['related_movies'] = Movie.objects.filter(genre=self.get_object().genre)

        # increment the views count every time the object is retrieved
        movie_object.views +=1
        movie_object.save()

        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        # this message will be available in the context
        messages.success(self.request, 'Please wait, your comment will be displayed after the admin approves of it.')
        return super(MovieDetailView, self).form_valid(form)

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
