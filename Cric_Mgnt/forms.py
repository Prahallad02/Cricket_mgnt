from django import forms
from .models import CoachModel,PlayersModel


class CoachForm(forms.ModelForm):
    class Meta:
        model = CoachModel
        fields = '__all__'


class PlayersForm(forms.ModelForm):
    class Meta:
        model = PlayersModel
        fields = '__all__'
