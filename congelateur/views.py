from django.shortcuts import render
from congelateur.models import Glace

from django.views.generic import ListView

# Create your views here.


def accueil(request):
    return render(request, 'accueil.html')
def about(request):
    return render(request, 'about.html')


def congelateur(request):
    return render(request, 'congelateur.html')

def home(request):
    return render(request, 'home.html')

def produits(request):
    listeGlaces = Glace.objects.all()
    #return render(request, 'products.html')
    return render(request, 'products.html', {'glaces': listeGlaces})


