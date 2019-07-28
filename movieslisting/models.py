from django.db import models
from django import forms

# Create your models here.
class Actors(models.Model):
	actor_Name = models.CharField(primary_key=True,max_length=50)
	gender = models.CharField(max_length=6)
	dob = models.DateField()
	bio = models.CharField(max_length=200)
	def __str__(self):
		return u'{0}'.format(self.actor_Name)


class Movies(models.Model):
	poster = models.ImageField(upload_to='images/')
	movie_name = models.CharField(max_length=50)
	release_year = models.IntegerField(default=2000)
	plot = models.CharField(max_length=200)
	cast = models.CharField(max_length=5000)	
