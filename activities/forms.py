from django import forms
from .models import Activitie

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activitie
        fields = [
            'activitie',
            'to_do_date',
        ]