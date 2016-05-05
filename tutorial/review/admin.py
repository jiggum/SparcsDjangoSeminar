from django.contrib import admin
from review.models import Comment

class CommentAdmin(admin.ModelAdmin):
     list_display = ('name',)

admin.site.register(Comment,CommentAdmin)
# Register your models here.
