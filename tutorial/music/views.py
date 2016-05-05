from django.shortcuts import render
from django.http import HttpResponse
from music.models import Singer, Album, Song
# Create your views here.

def main(request):
    return HttpResponse("Main")

def search(request, type):
    ctx={
        'type':type,
    }
    return render(request,'search.html',ctx)

def result(request):
    if 'q' in request.GET :
        keyword = request.GET['q']
    else :
        keyword = ""

    type = request.GET['type']
    if type=='singer':
        results = Singer.objects.filter(name__icontains=keyword)
    elif type=='album' :
        results = Album.objects.filter(name__icontains=keyword)
    else :
        results = Song.objects.filter(name__icontains=keyword)


    ctx={
            'results' : results,
            'keyword' : keyword,
            'type':type,
    }
    return render(request,'result.html',ctx)

def info(request, type, id):

    if type=='singer':
        result = Singer.objects.get(id=id)
    elif type=='album':
        result = Album.objects.get(id=id)
    else:
        result = Song.objects.get(id=id)

    ctx={
            'result' : result,
            'type' : type,
    }
    return render(request,'info.html',ctx)

