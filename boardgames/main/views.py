from django.shortcuts import render
from .models import Boardgames
# Create your views here.


def index(request):
    boardgames = Boardgames.objects.all()[:10]

    context = {
        'boardgames':boardgames
    }
    return render(request, 'index.html', context)

def details(request, id):
    boardgames = Boardgames.objects.get(id=id)

    context = {
        'boardgame': boardgames
    }
    return render(request, 'details.html', context)
