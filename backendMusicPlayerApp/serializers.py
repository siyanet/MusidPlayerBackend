from rest_framework import serializers
from .models import Song
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {"password": {"write_only": True}} 
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user   




