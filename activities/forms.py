from django import forms
from .models import Activitie

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activitie
        fields = [
            'activitie',
            'to_do_date',
        ]

class RawActivityForm(forms.Form):
    activitie   = forms.CharField(max_length=50)
    to_do_date  = forms.DateTimeField()