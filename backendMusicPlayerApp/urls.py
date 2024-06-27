from django.urls import path,include
from .views import SongListView,SongDeleteView,UserCreateView,UserDetailView,DefaultSongView,create_song, SongUpdateView#SongPatchView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
urlpatterns = [
 
    path('register',UserCreateView.as_view(),name = 'user-create'),
    path('token/access', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('songs/', SongListView.as_view(), name='song-list'),
    path('songUpdate/<int:pk>/',SongUpdateView.as_view(),name ='song-update'),
    path('songDelete/<int:pk>/',SongDeleteView.as_view(),name = 'song-delete'),
    path('user',UserDetailView.as_view(),name= 'user-detail'),
    path('defaultsong',DefaultSongView.as_view(),name = 'default-song'),
    path('songs/create',create_song,name='create-song'),
]
