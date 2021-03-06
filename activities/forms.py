from django import forms
from .models import Activity
from django.contrib.admin.widgets import AdminDateWidget
from bootstrap_datepicker_plus import DateTimePickerInput

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            'activity',
            'to_do_date',
        ]
        labels = {
            'activity': 'Aktywność',
            'to_do_date': 'Data aktywności'
        }
        help_texts = {
            'activity': 'Podaj nazwę aktywności do zrobienia.',
            'to_do_date': 'Podaj date aktywność w odpowiednim formacie np. 2020-02-25 18:00'
        }
        widgets = {
            'to_do_date': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
        }

class RawActivityForm(forms.Form):
    activity   = forms.CharField(max_length=50)
    to_do_date  = forms.DateTimeField()