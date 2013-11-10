from django import forms
from project.models import MileStone


class AddMileStone(forms.ModelForm):
    start_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class':'jquery_date'}))
    end_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class':'jquery_date'}))
    class Meta:
        model= MileStone
        exclude = ('project','start_date', 'end_date')
