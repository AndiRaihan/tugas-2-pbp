from django.shortcuts import render
from mywatchlist.models import WatchlistMovies
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_html(request):
    data = WatchlistMovies.objects.all()
    sum_watched_movies = 0
    half_of_movies = len(data)/2
    for movies in data.iterator():
        if movies.watched:
            sum_watched_movies +=1
        
    if sum_watched_movies >= half_of_movies:
        msg = "Selamat, kamu sudah banyak menonton!"
    else:
        msg = "Wah, kamu masih sedikit menonton!"
    context = {
        'list_film' : data,
        'nama' : 'Andi Muhamad Dzaky Raihan',
        'npm' : '2106631412',
        'Message' : msg,
    }
    return render(request, 'watchlist.html', context)
    

def show_xml(request):
    data = WatchlistMovies.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistMovies.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
