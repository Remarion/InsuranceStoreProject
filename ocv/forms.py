from django import forms
from .models import CalculationOCV

class CalculationOCVForm(forms.ModelForm):
    class Meta:
        model = CalculationOCV
        fields = ('setlCalc', 'catTypeCalc', 'price', )