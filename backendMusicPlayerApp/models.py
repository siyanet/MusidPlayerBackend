from django.db import models
from django.contrib.auth.models import User
from .firebase_config import storage as firebase_storage
class Song(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    file = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return self.title

   