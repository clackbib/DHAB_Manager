from django import forms
from project.models import Project, Requirements

ESTIMATION_TECHNIQUES = (('Function Point', 'Function Point '), ('KLOC', 'KLOC') )
REQUIREMENT_TYPES = (('Functional', 'Functional'), ('Non-Functional', 'Non-Functional') )


class NewProjectForm(forms.ModelForm):
    start_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'jquery_date'}))
    end_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'jquery_date'}))

    class Meta:
        model = Project
        exclude = ('creator', 'start_date', 'end_date',)


class AddRequirementForm(forms.ModelForm):
    technique = forms.ChoiceField(widget=forms.RadioSelect, choices=ESTIMATION_TECHNIQUES)
    requirement_type = forms.ChoiceField(widget=forms.RadioSelect, choices=REQUIREMENT_TYPES)
    start_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'jquery_date'}))
    end_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'jquery_date'}))

    class Meta:
        model = Requirements
        exclude = (
        'creator', 'project', 'technique', 'requirement_type', 'end_date', 'current_completion', 'assignment')


class EditRequirement(forms.ModelForm):
    technique = forms.ChoiceField(widget=forms.RadioSelect, choices=ESTIMATION_TECHNIQUES)
    requirement_type = forms.ChoiceField(widget=forms.RadioSelect, choices=REQUIREMENT_TYPES)
    start_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'jquery_date'}))
    end_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'jquery_date'}))

    class Meta:
        model = Requirements
        exclude = ('creator', 'project', 'technique', 'requirement_type', 'end_date', 'assignment')


