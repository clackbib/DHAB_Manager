from django import forms
from project.models import Project, Requirements

ESTIMATION_TECHNIQUES = (('COCOMO I', 'COCOMO I'), ('COCOMO II', 'COCOMO II') )
REQUIREMENT_TYPES = (('Functional', 'Functional'),('Non-Functional', 'Non-Functional') )

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('creator',)

class AddRequirementForm(forms.ModelForm):
    technique = forms.ChoiceField(widget=forms.RadioSelect, choices= ESTIMATION_TECHNIQUES )
    requirement_type = forms.ChoiceField(widget= forms.RadioSelect, choices= REQUIREMENT_TYPES)
    class Meta:
        model = Requirements
        exclude = ('creator', 'project','technique','requirement_type',)