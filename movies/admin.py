from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year','imdb_rating', 'metascore', 'votes', 'type')


admin.site.register(Movie, MovieAdmin)
