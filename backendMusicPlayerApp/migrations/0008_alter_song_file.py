# Generated by Django 5.0.6 on 2024-06-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendMusicPlayerApp', '0007_alter_song_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
