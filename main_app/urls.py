from django.urls import path
# Add the include function to the import
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('movies/', views.movies_index, name='index'),
  path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
  path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
  path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
  path('movies/<int:pk>/delete', views.MovieDelete.as_view(), name='movies_delete'),
  path('movies/<int:movie_id>/add_watching/', views.add_watching, name='add_watching'),
  path('movies/<int:movie_id>/add_photo/', views.add_photo, name='add_photo'),
  path('movies/<int:movie_id>/add_review', views.add_review, name='add_review'),
  path('accounts/signup/', views.signup, name='signup'),

  
] 
