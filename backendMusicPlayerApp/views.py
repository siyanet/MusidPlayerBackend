from django.shortcuts import render
import pyrebase
import uuid
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import SongSerializer,UserSerializer
from .models import Song
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from .firebase_config import storage as firebase_storage 
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from django.http import Http404 

class SongListView(generics.ListAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Song.objects.filter(user = self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_song(request):
   

    file = request.FILES.get('file')

    if not file:
        return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

    try:
       
        unique_id = uuid.uuid4()
        filename = f"{unique_id}.mp3"
        firebase_storage.child("songs/" + filename).put(file)

    
        download_url = firebase_storage.child("songs/" + filename).get_url(None)

        serializer = SongSerializer(data={
            'file': download_url, 
            'title': request.data.get('title'),  
            'artist': request.data.get('artist'),
            'user': request.user.id  
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
       
        return Response({"error": "Failed to upload file"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class SongUpdateView(generics.UpdateAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Song.objects.filter(user = self.request.user)

class SongDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        
        try:
            song = Song.objects.get(pk=pk, user=request.user)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            song.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": "Failed to delete file"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
class DefaultSongView(generics.ListAPIView):
    serializer_class = SongSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        admin_user = User.objects.filter(is_superuser = True)
        return Song.objects.filter(user__in = admin_user) 



