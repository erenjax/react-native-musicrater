from rest_framework import serializers
from .models import User, UserRating, Song

class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model=User
         fields=("username", "password")

class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRating
        fields=("id","username", "song", "artist", "rating")



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=("song", "artist", "rating")