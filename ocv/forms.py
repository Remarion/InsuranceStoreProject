from django import forms
from django.forms import Select, TextInput
from .models import CalculationOCV


class CalculationOCVForm(forms.ModelForm):
    class Meta:
        model = CalculationOCV
        fields = ('setlCalc', 'catTypeSimpleCalc', 'carTypeLabelCalc', 'carTypeMTSBUCalc')
        widgets = {
            'setlCalc': Select(attrs={"class": "form-control", "type": "text", "placeholder": "Default input"}),
            'catTypeSimpleCalc': Select(attrs={"class": "form-control", "type": "text", "placeholder": "Default input"}),
            'carTypeMTSBUCalc': Select(attrs={"class": "form-control", "type": "text", "placeholder": "Default input"}),
        }