from django.urls import path
from mywatchlist.views import *

app_name = 'wishlist'

urlpatterns = [
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
]