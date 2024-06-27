import uuid
from django import forms
from .models import Song
from .firebase_config import storage as firebase_storage 

class SongAdminForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'artist', 'file','user')  

    file = forms.FileField(label='Select a file', required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if 'file' in self.cleaned_data:
            file = self.cleaned_data['file']
            file_content = file.read()
            unique_id = uuid.uuid4()
            firebase_filename = f"songs/{unique_id}.mp3"
            firebase_storage.child(firebase_filename).put(file_content)
            instance.file = firebase_storage.child(firebase_filename).get_url(None)
        if commit:
            instance.save()
        return instance
