from django import forms
from django.forms import ModelForm


from .models import User, UserRating, Artist

class SignUpForm (ModelForm):
    class Meta:
        model=User
        fields=['username','password']


class FindRatingsForm (ModelForm):
    class Meta:
        model = UserRating
        fields=['username']

class FindArtistForm(ModelForm):
    class Meta:
        model=Artist
        fields=['artist']