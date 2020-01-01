from django.contrib import admin
from .models import Movie, Review, Watching, Photo

# Register your models here.
admin.site.register(Movie)
admin.site.register(Watching)
admin.site.register(Review)
admin.site.register(Photo)
