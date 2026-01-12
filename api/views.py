from rest_framework import viewsets
from pokedex.models import Pokemon, Trainer
from .serializes import PokemonSerializer, TrainerSerializer
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from rest_framework.permissions import IsAuthenticated, AllowAny

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated(), TokenHasScope()]


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']

    def get_permissions(self):
            if self.request.method == 'GET':
                return [AllowAny()]
            return [IsAuthenticated(), TokenHasScope()]