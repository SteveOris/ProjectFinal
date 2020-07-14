from django.shortcuts import render
from .models import Album 
# Create your views here.

def list_contacts(request):
    album = Album.objects.all()
    return render(request, "albums/add_albums.html",
                  {"album": album})