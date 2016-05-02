from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=100)
    debut_year = models.IntegerField(default = 0)
    genre = models.CharField(max_length=400)

class Album(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.IntegerField(default = 0)
    introduction = models.CharField(max_length=4000)
    singer = models.ManyToManyField('Singer',related_name='album')

class Song(models.Model):
    name = models.CharField(max_length=100)
    tracknumber = models.IntegerField(default = 0)
    lyrics = models.CharField(max_length=65536)
    album = models.ManyToManyField('Album',related_name='song')


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=65536)
