from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            'activity',
            'to_do_date',
        ]

class RawActivityForm(forms.Form):
    activity   = forms.CharField(max_length=50)
    to_do_date  = forms.DateTimeField()