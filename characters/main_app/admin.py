from django.contrib import admin

# Register your models here.
from .models import Character, Action

admin.site.register(Character)
admin.site.register(Action)
