from django.db import models
from django.urls import reverse

# Create your models here.


class Album(models.Model):
    album_title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album_jacket = models.ImageField(upload_to='img/')
    audio_file = models.FileField(upload_to='audio/', null=True, blank=True)
    song_lyric = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist
