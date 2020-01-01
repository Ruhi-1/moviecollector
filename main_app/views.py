from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Movie, Review, Photo
from .forms import ReviewForm, WatchingForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'moviecollector'

class MovieCreate(LoginRequiredMixin, CreateView):
  model = Movie
  fields = '__all__'

@login_required
def form_valid(self, form):
  form.instance.user = self.request.user  
  return super().form_valid(form)


class MovieUpdate(UpdateView):
  model = Movie
  fields = ['description']

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'


# Define the home view
@login_required
def home(request):
  return render(request, 'home.html')

@login_required
def about(request):
  return render(request, 'about.html')


@login_required
def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

@login_required
def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  review_form = ReviewForm()
  watching_form = WatchingForm()
  return render(request, 'movies/detail.html', { 
    'movie': movie, 'watching_form': watching_form,
    'review_form': review_form
  })

@login_required
def add_watching(request, movie_id):
  form = WatchingForm(request.POST)
  if form.is_valid():
    new_watching = form.save(commit=False)
    new_watching.movie_id = movie_id
    new_watching.save()
  return redirect('detail', movie_id=movie_id)

@login_required
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

@login_required
def add_photo(request, movie_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, movie_id=movie_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', movie_id=movie_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


