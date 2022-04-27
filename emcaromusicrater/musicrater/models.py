from django.db import models
from django.contrib.auth.models import User

class User (models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Song (models.Model):
    song=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    rating=models.IntegerField()

    def __str__ (self):
        return self.song

class UserRating (models.Model):
    username = models.CharField(max_length=100)
    song=models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    rating=models.IntegerField()

    def __str__ (self):
        return self.username







class Artist (models.Model):
    artist=models.CharField(max_length=100)
    song=models.CharField(max_length=100)
    album=models.CharField(max_length=100)

    def __str__ (self):
        return self.song

class Album (models.Model):
    album=models.CharField(max_length=100)
    yearPublished=models.IntegerField()
    artist=models.CharField(max_length=100)
    awards=models.CharField(max_length=200)
    genre=models.CharField(max_length=100)

    def __str__ (self):
        return self.album
