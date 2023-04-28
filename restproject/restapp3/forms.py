from django import forms
from .models import Food

class Foodforms(forms.ModelForm):
    class Meta:
        model=Food
        fields=['foodday','foodname','foodimg','fooddesc']