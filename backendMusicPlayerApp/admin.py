from django.contrib.auth.models import User
from django.contrib import admin
from .models import Song
from .forms import SongAdminForm

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    form = SongAdminForm
    list_display = ('title', 'artist', 'file')  
