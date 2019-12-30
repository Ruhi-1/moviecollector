from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Movie, Review
from .forms import ReviewForm, WatchingForm

class MovieCreate(CreateView):
  model = Movie
  fields = '__all__'

class MovieUpdate(UpdateView):
  model = Movie
  fields = ['description']

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  review_form = ReviewForm()
  watching_form = WatchingForm()
  return render(request, 'movies/detail.html', { 
    'movie': movie, 'watching_form': watching_form,
    'review_form': review_form
  })

def add_watching(request, movie_id):
  form = WatchingForm(request.POST)
  if form.is_valid():
    new_watching = form.save(commit=False)
    new_watching.movie_id = movie_id
    new_watching.save()
  return redirect('detail', movie_id=movie_id)

def add_review(request, movie_id):
	# create the ModelForm using the data in request.POST
  form = ReviewForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_review = form.save(commit=False)
    new_review.cat_id = movie_id
    new_review.save()
  return redirect('detail', movie_id=movie_id)


