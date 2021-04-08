from django.db import models
from django.utils.text import slugify
from django.utils import timezone


STATUS_CHOICES = (
        ('TR', 'Top Rated'),
        ('RA', 'Recently Added'),
        ('MV', 'Most Viewed')
)

GENRE_CHOICES = (
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('History', 'History'),
        ('Romance', 'Romance')
)

RATING = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)


class MovieCast(models.Model):
    """
    Contains the actors in a movie
    """
    actor_name = models.CharField(max_length=100)
    actor_slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ 
        Override the default save function to extend its functionality 
        """
        # if there's no slug provided then assign a slug using the actor's name
        if not self.actor_slug:
            self.actor_slug = slugify(self.actor_name)
        super(MovieCast, self).save(*args, **kwargs)

    def __str__(self):
        return self.actor_name

class Movie(models.Model):
    """ 
    Base class for the properties our movies will have 
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie_images')
    description = models.TextField(max_length=1000)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=10)
    cast = models.ManyToManyField(MovieCast, related_name='movies')
    poster = models.ImageField(upload_to='movie_posters')
    created_date = models.DateTimeField(default=timezone.now)
    produced_date = models.DateTimeField()
    slug = models.SlugField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    trailer_link = models.URLField()
    views = models.IntegerField(default=0)
    rating = models.IntegerField(choices=RATING, default=2)

    def save(self, *args, **kwargs):
        """ 
        Override the default save function to extend its functionality 
        """
        # if there's no slug provided then assign a slug using the title of movie
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class MovieComment(models.Model):
    """
    Model for the comments on each movie
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
