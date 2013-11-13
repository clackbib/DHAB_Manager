from django import forms
from project.models import MileStone,Assignment


class AddMileStone(forms.ModelForm):
    start_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class':'jquery_date'}))
    end_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class':'jquery_date'}))
    class Meta:
        model= MileStone
        exclude = ('project','start_date', 'end_date')

class EditMileStone(forms.ModelForm):
    start_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class':'jquery_date'}))
    end_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class':'jquery_date'}))
    class Meta:
        model= MileStone
        exclude = ('project','start_date', 'end_date')

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ('project',)