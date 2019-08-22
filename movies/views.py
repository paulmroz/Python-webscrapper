from django.shortcuts import render
from .models import Movie
from django.core.paginator import Paginator


def index(request):
    movies = Movie.objects.all()

    paginator = Paginator(movies, 15)

    page = request.GET.get('page')

    movies = paginator.get_page(page)

    return render(request, 'index.html', {'movies': movies})


def search(request):

    title = request.GET.get('title')

    movies = Movie.objects.filter(name__icontains=title)

    paginator = Paginator(movies, 15)

    page = request.GET.get('page')

    movies = paginator.get_page(page)

    return render(request, 'index.html', {'movies': movies})