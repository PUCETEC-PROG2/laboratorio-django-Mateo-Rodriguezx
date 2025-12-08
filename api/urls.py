from django.urls import path, include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register(r'pokemons', views.PokemonViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]