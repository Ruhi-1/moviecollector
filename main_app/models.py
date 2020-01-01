from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

TIMES = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('E', 'Evening')
)

RATINGS = (
  ('E', 'Exellent'),
  ('V', 'Very Good'),
  ('G', 'Good'),
  ('B', 'Bad')
)

class Review(models.Model):
  date = models.DateField()
  rating = models.CharField(
    max_length=1,
      choices=RATINGS,
      default=RATINGS[0][0]
  )

class Movie(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  reviews = models.ManyToManyField(Review)
  user = models.ForeignKey(User, on_delete=models.CASCADE)



  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'movie_id': self.id})

  # def review_for_today(self):
  #   return self.review_set.filter(date=date.today()).count() >= len(RATINGS)



class Photo(models.Model):
    url = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for movie_id: {self.movie_id} @{self.url}"

class Watching(models.Model):
  date = models.DateField('Watch Date')
  time = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
  )

  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_rating_display()} on {self.date}"
 
class Meta:
  ordering = ['-date']