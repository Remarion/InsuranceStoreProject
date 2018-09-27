# -*- coding: utf8 -*-
from django.shortcuts import render
from django.views import View
from .forms import CalculationOCVForm
from .models import CarTypeSimple, CarTypeLabel, CarTypeMTSBU, Settlement


class Index(View):
    def get(self, request):
        context = {'text': 'Main page'}
        return render(request, 'basic.html', context)

class OCV_View(View):
    def get(self, request):
        setl = Settlement.objects.all()
        cartypes = CarTypeSimple.objects.all()
        context = {'setl': setl, 'cartypes': cartypes}
        return render(request, 'ocv/ocv_calc.html', context)


def index(request, cartype_id):
    setl = Settlement.objects.all()
    cartypes = CarTypeSimple.objects.all()
    cartypelabel = CarTypeLabel.objects.get(carTypeSimple__id=cartype_id)
    cartypemtsbu = CarTypeMTSBU.objects.filter(carTypeSimple__id=cartype_id)
    context = {'setl': setl, 'cartypes': cartypes, 'cartypelabel': cartypelabel, 'cartypemtsbu': cartypemtsbu}
    return render(request, 'ocv/ocv_calc.html', context)