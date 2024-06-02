from django import forms
from .models import Inputemo

class EmoForm(forms.ModelForm):
    class Meta:
        model = Inputemo
        fields = ('emo_name', 'file')