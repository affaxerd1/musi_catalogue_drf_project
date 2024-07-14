from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(null=True, blank=True, help_text="Give some info about the artist")
    song_total = models.IntegerField(blank=True, null=True)
    choices = models.TextField(choices=[('1', 'Choice 1'), ('2', 'Choice 2')], blank=True, null=False)
    favorite = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)


class Album(models.Model):
    title = models.CharField(max_length=1000)
    released_on = models.DateTimeField(blank=True)
    artists = models.ManyToManyField('Artist')


class Song(models.Model):
    title = models.CharField(max_length=100)
    Album = models.ForeignKey('Album', on_delete=models.CASCADE)
