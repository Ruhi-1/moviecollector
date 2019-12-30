from django.forms import ModelForm
from .models import Review, Watching

class WatchingForm(ModelForm):
  class Meta:
    model = Watching
    fields = ['date', 'time']

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['date', 'rating']