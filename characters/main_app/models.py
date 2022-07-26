from statistics import mode
from django.db import models
from django.urls import reverse


ACTION_TYPE = (
    ("G", "Good"),
    ("B", "Bad"),
    ("N", "Necessary/Neutral"),
    ("S", "Subjective") 
)
# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    media_name = models.CharField(max_length=100)
    movie_format = models.BooleanField()
    year_created = models.IntegerField()
    description = models.TextField(max_length=500)
    role = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    obstacle = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs = {"character_id": self.id})

class Action(models.Model):
    action = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    action_type = models.CharField(
        "Type of action",
        max_length=1,
        choices=ACTION_TYPE,
        default=ACTION_TYPE[2][0]
    )
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.action} was {self.get_action_type_display()}"
