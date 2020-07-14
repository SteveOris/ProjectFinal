from django.shortcuts import render
from .models import Album 
# Create your views here.

def index(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  context ={"albums": albums})