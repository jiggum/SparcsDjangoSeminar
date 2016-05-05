from django.shortcuts import render
from review.models import Comment
from django.http import HttpResponseRedirect
# Create your views here.

def main(request):
    comments = Comment.objects.all()
    ctx = {
        'comments' : comments,
    }
    return render(request,'main.html',ctx)

def insert(request):
    return render(request,'insert.html')

def add(request):
    name = request.POST['name']
    comment = request.POST['comment']
    Comment(name=name, comment=comment).save()
    return HttpResponseRedirect('/review/insert')
