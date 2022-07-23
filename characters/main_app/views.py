from django.shortcuts import render
from django.http import HttpResponse

class Character:
  def __init__(self, name, media_name, movie_format, description, role, goal, obstacle):
    self.name = name
    self.media_name = media_name
    self.movie_format = movie_format
    self.description = description
    self.role = role
    self.goal = goal
    self.obstacle = obstacle

characters = [
  Character("Rustin Cohle", "True Detective", False, "One of two detectives who hunts a serial killer in Louisiana for 17 years", "Protagonist", "Finding the killer", "Complex murder case"),
  Character("Tony Soprano", "The Sopranos", False, "Mob boss Tony Soprano deals with personal and professional issues in his home and business life that affect his mental state.", "Main character", "Becoming a varsity athlete", "Crime life and family life."),
  Character("Creed Bratton", "The Office", False, "An old clueless dude working at an office full of clashes, inappropriate behavior and tedium", "Supporting character", "Scuba", "Asthma")
]

# Create your views here.

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, "about.html")

def characters_index(request):
    return render(request, "characters/index.html", { "characters": characters })