from django.db import models

# Create your models here.
class Singer(models.Model):
    image = models.CharField(max_length=10000)
    name = models.CharField(max_length=100)
    debut_year = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.name
class Album(models.Model):
    image = models.CharField(max_length=10000)
    name = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    genre = models.CharField(max_length=400)
    singer = models.ManyToManyField('Singer',related_name='album')
    def __unicode__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ManyToManyField('Album',related_name='song')
    def __unicode__(self):
        return self.name

