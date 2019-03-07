from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id=models.AutoField
    movie_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()