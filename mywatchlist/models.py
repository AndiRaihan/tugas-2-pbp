from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class WatchlistMovies(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating_validator = [MaxValueValidator(5), MinValueValidator(1)]
    rating = models.IntegerField(rating_validator)
    release_date = models.DateField()
    review = models.TextField(default='-')
    
