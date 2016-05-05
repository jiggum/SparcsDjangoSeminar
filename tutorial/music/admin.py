from django.contrib import admin
from music.models import Singer, Album, Song

class SingerAdmin(admin.ModelAdmin):
     list_display = ('name','debut_year')
     list_filter = ('name',)

class AlbumAdmin(admin.ModelAdmin):
     list_display = ('name','release_date')
     list_filter = ('release_date',)

class SongAdmin(admin.ModelAdmin):
     list_display = ('name',)
     list_filter = ('name',)

admin.site.register(Singer,SingerAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Song,SongAdmin)

# Register your models here.
