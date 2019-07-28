from django.shortcuts import render, redirect
from django.http import HttpResponse 
from movieslisting import forms
from movieslisting.models import Actors,Movies
# Create your views here.

def addactor(request):
	add_actor=forms.ActorsForm
	if request.method=='POST':
		add_actor_data=forms.ActorsForm(request.POST)
		if add_actor_data.is_valid():
			add_actor_data.save(commit=True)
		add_actor=forms.ActorsForm
	actors_dict={'add':add_actor}
	return render(request,'movieslisting/add.html',actors_dict)
	

def createmovie(request):
	create_movie=forms.MoviesForm
	if request.method=='POST':
		create_movie_data=forms.MoviesForm(request.POST, request.FILES)
		if create_movie_data.is_valid():
			create_movie_data.save(commit=True)
			return redirect('success')
		else:
			print(create_movie_data.errors)
		create_movie=forms.MoviesForm
	create_movies_dict={'create':create_movie}
	return render(request,'movieslisting/add1.html',create_movies_dict)

def moviedisplay(request):
	movies_list=Movies.objects.all()
	movies_dict={'display':movies_list}
	print('hello')
	return render(request,'movieslisting/display.html',movies_dict)
	

def success(request): 
    return HttpResponse('successfuly uploaded')

def failed(request): 
    return HttpResponse('failed uploaded')