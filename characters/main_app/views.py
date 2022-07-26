from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from .models import Character
from .forms import ActionForm 

# Create your views here.

class CharacterCreate(CreateView):
  model = Character
  fields = "__all__"


class CharacterUpdate(UpdateView):
  model = Character
  fields = ["media_name", "year_created", "description", "role", "goal", "obstacle"]


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
  action_form = ActionForm()
  return render(request, "characters/detail.html", { "character": character, "action_form": action_form } )

def add_action (request, character_id):
  form = ActionForm(request.POST)
  if form.is_valid():
    new_action = form.save(commit=False)
    new_action.character_id = character_id
    new_action.save()
  return redirect('detail', character_id=character_id)