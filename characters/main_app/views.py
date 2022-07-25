from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from .models import Character

# Create your views here.

class CharacterCreate(CreateView):
  model = Character
  fields = "__all__"
  #success_url gives error

class CharacterUpdate(UpdateView):
  model = Character
  fields = ["media_name", "year_created", "description", "role", "goal", "obstacle"]
  #success_url gives error


class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters/'


def home(request):
  return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def characters_index(request):
  characters = Character.objects.all()
  return render(request, "characters/index.html", { "characters": characters })

def characters_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  return render(request, "characters/detail.html", { "character": character })
