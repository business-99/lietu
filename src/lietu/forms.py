from django import forms
from .models import DogInfo

class EventForms(forms.ModelForm):

    class Meta:
        model = DogInfo