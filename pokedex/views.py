from django.shortcuts import render, redirect
from .models import Pokemon, Trainer
from .forms import PokemonForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views import View


def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    return render(request, 'index.html', {
        'pokemons': pokemons,
        'trainers': trainers
    })


def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'display_pokemon.html', {
        'pokemon': pokemon
    })


def trainer_details(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    return render(request, 'display_trainer.html', {
        'trainer': trainer
    })


@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()

    return render(request, 'pokemon_form.html', {'form': form})


@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    form = PokemonForm(request.POST or None, request.FILES or None, instance=pokemon)

    if form.is_valid():
        form.save()
        return redirect('pokedex:index')

    return render(request, 'pokemon_form.html', {'form': form})


@login_required
def delete_pokemon(request, pokemon_id):
    Pokemon.objects.get(id=pokemon_id).delete()
    return redirect('pokedex:index')


class CustomLoginView(View):
    def get(self, request):
        return render(request, 'login_form.html')

    def post(self, request):
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )

        if user:
            login(request, user)
            return redirect('pokedex:index')

        return render(request, 'login_form.html', {
            'error': 'Usuario o contraseña incorrectos'
        })
