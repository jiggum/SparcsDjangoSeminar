from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=65536)
