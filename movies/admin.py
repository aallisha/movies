from django.contrib import admin
from .models import Movie, MovieCast, MovieComment


admin.site.register(Movie)
admin.site.register(MovieCast)

# models can also be registered in this way
@admin.register(MovieComment)
class CommentAdmin(admin.ModelAdmin):
    """
    Class to customize the representation of data on the admin page
    """
    # how to display a specific comment
    list_display = ('name', 'body', 'movie', 'created_on', 'active')
    # how to filter the comments
    list_filter = ('active', 'created_on')
    # search the database based on parameters provided
    search_fields = ('name', 'email', 'body')
    # unapproved comments won't display on the movie's detail page
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        # Takes a queryset and updates the active boolean field to True
        queryset.update(active=True)
