from django import forms
from movies.models import Movie
class Movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"