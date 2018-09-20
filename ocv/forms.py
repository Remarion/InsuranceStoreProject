from django import forms
from .models import CalculationOCV

class CalculationOCVForm(forms.ModelForm):
    class Meta:
        model = CalculationOCV
        fields = '__all__'
        labels = {'setlCalc': 'Місце реєстрації авто', 'catTypeCalc': 'Тип транспортного засобу', 'price': 'Вартість '
                                                                                                           'полісу'}