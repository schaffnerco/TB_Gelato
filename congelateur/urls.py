from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    url(r'^accueil$', views.accueil, name='accueil'),
    url(r'^congelateur$', views.congelateur, name='congo'),
    url(r'^home$', views.home, name='home'),
    url(r'^produits$', views.produits, name='produit'),
    url(r'^about$', views.about, name='about')

]


