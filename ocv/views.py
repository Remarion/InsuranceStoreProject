# -*- coding: utf8 -*-
from django.shortcuts import render
from django.views import View
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


def index(request, cartype_id , setl_id):
    setl = Settlement.objects.all()
    cartypes = CarTypeSimple.objects.all()
    typeDefault = CarTypeSimple.objects.get(pk=cartype_id)
    cartypelabel = CarTypeLabel.objects.get(carTypeSimple__id=cartype_id)
    cartypemtsbu = CarTypeMTSBU.objects.filter(carTypeSimple__id=cartype_id)
    if setl_id != '0':
        setlDefault = Settlement.objects.get(pk=setl_id)
        context = {'setl': setl, 'cartypes': cartypes, 'cartypelabel': cartypelabel, 'cartypemtsbu': cartypemtsbu,
                   'typeDefault': typeDefault, 'setlDefault': setlDefault}
    else:
        context = {'setl': setl, 'cartypes': cartypes, 'cartypelabel': cartypelabel, 'cartypemtsbu': cartypemtsbu,
               'typeDefault': typeDefault}
    return render(request, 'ocv/ocv_calc.html', context)