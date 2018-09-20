from django import forms
from django.forms import Select, TextInput
from .models import CalculationOCV


class CalculationOCVForm(forms.ModelForm):
    class Meta:
        model = CalculationOCV
        fields = ('setlCalc', 'catTypeCalc', 'price')
        widgets = {
            'setlCalc': Select(attrs={"class": "form-control", "type": "text", "placeholder": "Default input"}),
            'catTypeCalc': Select(attrs={"class": "form-control", "type": "text", "placeholder": "Default input"}),
            'price': TextInput(attrs={"class": "form-control", "type": "text"})
        }
