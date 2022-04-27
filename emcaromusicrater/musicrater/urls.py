from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('search-artist/', views.searchArtist, name='search-artist'),
]