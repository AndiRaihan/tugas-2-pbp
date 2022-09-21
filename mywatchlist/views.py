from django.shortcuts import render
from mywatchlist.models import WatchlistMovies
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_html(request):
    data = WatchlistMovies.objects.all()
    context = {
        'list_film' : data,
        'nama' : 'Andi Muhamad Dzaky Raihan',
        'npm' : '2106631412',
    }
    return render(request, 'watchlist.html', context)
    

def show_xml(request):
    data = WatchlistMovies.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistMovies.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
