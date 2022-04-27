from django.contrib import admin

from .models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=("username",)

from .models import UserRating
@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):
    list_display=("username",)


from .models import Song
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=("song",)


from .models import Artist
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display=("artist",)

from .models import Album
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=("album",)




