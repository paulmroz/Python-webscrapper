from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})
