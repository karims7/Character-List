from django.forms import ModelForm
from .models import Action

class ActionForm(ModelForm):
    class Meta:
        model = Action
        fields = ["action", "reason", "action_type"]