from django.shortcuts import render
from .models import Movie

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

def movies_detail(request, cat_id):
  movie = Movie.objects.get(id=movie_id)
  return render(request, 'movies/detail.html', { 'movie': movie })