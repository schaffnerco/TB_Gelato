from django.shortcuts import render
from congelateur.models import Glace, Congelateur, Tiroir
from django.db.models import Sum
from django.db import connection
from django.views.generic import ListView, DetailView

# Create your views here.


def accueil(request):
    return render(request, 'congelateur/accueil.html', locals())

def about(request):
    return render(request, 'congelateur/about.html')

def discover(request):
    return render(request, 'congelateur/discover.html', locals())

def dashboard(request):
    return render(request, 'congelateur/dashboard.html', locals())

def home(request):
    return render(request, 'congelateur/home.html')


class CongelateurListView(ListView):
    queryset = Congelateur.objects.select_related()

    def get_context_data(self, **kwargs):
        context = super(CongelateurListView, self).get_context_data(**kwargs)
        return context

class CongelateurDetailView(DetailView):
    model = Congelateur
    def get_context_data(self, **kwargs):
        context = super(CongelateurDetailView, self).get_context_data(**kwargs)
        return context

class GlaceListView(ListView):
    queryset = Glace.objects.select_related()

    def get_context_data(self, **kwargs):
        context = super(GlaceListView, self).get_context_data(**kwargs)
        return context

