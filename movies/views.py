from django.shortcuts import render
from .models import Movie
from django.core.paginator import Paginator


def index(request):
    movies = Movie.objects.all()

    paginator = Paginator(movies, 15)

    page = request.GET.get('page')

    movies = paginator.get_page(page)

    return render(request, 'index.html', {'movies': movies})
