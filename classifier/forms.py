from django import forms
from . import models


class CreateImage(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ['image', 'side', 'stage']
