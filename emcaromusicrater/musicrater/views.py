from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, FindRatingsForm, FindArtistForm
from django.contrib.auth import login
from django.contrib import messages
from .models import User, UserRating, Artist, Song
from django.db.models import Q,Avg
from django.views.generic import TemplateView, ListView
from django.template import RequestContext
from rest_framework import viewsets
from .serializers import UserSerializer, UserRatingSerializer, SongSerializer


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset=User.objects.all()

class UserRatingView (viewsets.ModelViewSet):
    serializer_class=UserRatingSerializer
    
    queryset=UserRating.objects.all()
    



class SongView(viewsets.ModelViewSet):
    serializer_class=SongSerializer
    
    queryset=Song.objects.all()
    


def index(request):
    return HttpResponse('Welcome to MusicRater')

# Create your views here.
def my_html_view(request, question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'templates/template.html',{'question':question})

def signup(request):
    form=SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ('You registered!'))
        
    context={'form':form}
    return render(request, 'musicrater/signup.html', context)
def search(request):
    if 'retrieve_rating' in request.POST:
        rating=FindRatingsForm(request.POST or None)
        ratings=[]
        if rating.is_valid():
            ratings=Rating.objects.filter(username=rating.cleaned_data["username"])
            if len(ratings)!=0:
                context={
                    'rating':rating,
                    'ratings':ratings,
                }
            else:
                context={
                    'rating':rating,
                    'ratings':-1,
                }
    else:
        context={'rating':FindRatingsForm(None)}
    return render(request, 'musicrater/search.html',context)

def searchArtist(request):
    if 'retrieve_artist' in request.POST:
        artist=FindArtistForm(request.POST or None)
        songs=[]
        if artist.is_valid():
            songs=Artist.objects.filter(artist=artist.cleaned_data["artist"])
            if len(songs)!=0:
                context={
                    'artist':artist,
                    'songs':songs,
                }
            else:
                context={
                    'artist':artist,
                    'songs':-1,
                }
    else:
        context={'artist':FindArtistForm(None)}
    return render(request, 'musicrater/search-artist.html',context)


    
    

        