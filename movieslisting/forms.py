from django import forms
from movieslisting.models import Actors,Movies
class ActorsForm(forms.ModelForm):
	genders=(('male','Male'),('female','Female'),('others','Others'))
	gender = forms.ChoiceField(choices=genders,widget=forms.RadioSelect)
	dob = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
	class Meta:
		model = Actors
		fields = ('actor_Name','gender','dob','bio',)
class MoviesForm(forms.ModelForm):
	
	class MyModelMultipleChoiceField(forms.ModelMultipleChoiceField):
		def label_from_instance(self, cast):
			return cast.actor_Name
		def to_field_name(self,cast):
			return cast.actor_Name
	
	cast = MyModelMultipleChoiceField(queryset=Actors.objects.distinct())
	class Meta:
		model = Movies
		fields = ('poster','movie_name','release_year','plot','cast',)
