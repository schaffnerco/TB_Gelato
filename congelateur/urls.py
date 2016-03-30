from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    url(r'^accueil$', views.accueil),
    url(r'^congelateur$', views.congelateur),
    url(r'^home$', views.home),
    url(r'^produits$', views.produits),
    url(r'^about$', views.about)

]


