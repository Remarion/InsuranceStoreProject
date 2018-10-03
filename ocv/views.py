# -*- coding: utf8 -*-
import simplejson as simplejson
from django.shortcuts import render
from django.views import View
from .models import CarTypeSimple, CarTypeLabel, CarTypeMTSBU, Settlement
from django.core import serializers
from django.http import HttpResponse
import json


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


"""def index(request, cartype_id, setl_id):
    setl = Settlement.objects.all()
    cartypes = CarTypeSimple.objects.all()
    typeDefault = CarTypeSimple.objects.get(pk=cartype_id)
    cartypelabel = CarTypeLabel.objects.get(carTypeSimple__id=cartype_id)
    cartypemtsbu = CarTypeMTSBU.objects.filter(carTypeSimple__id=cartype_id)
    if setl_id != '0':
        setlDefault = Settlement.objects.get(pk=setl_id)
        data = {'setl': setl, 'cartypes': cartypes, 'cartypelabel': cartypelabel, 'cartypemtsbu': cartypemtsbu,
                'typeDefault': typeDefault, 'setlDefault': setlDefault}
    else:
        data = {'setl': setl, 'cartypes': cartypes, 'cartypelabel': cartypelabel, 'cartypemtsbu': cartypemtsbu,
                'typeDefault': typeDefault}
    return render(request, 'ocv/ocv_calc.html', data)"""


def index(request, cartype_id, setl_id):
    cartypemtsbu = CarTypeMTSBU.objects.filter(carTypeSimple__id=cartype_id)
    cartypelabel = CarTypeLabel.objects.get(carTypeSimple__id=cartype_id)
    data = []
    for cartype in cartypemtsbu:
        data.append({'id': cartype.id, 'carTypeKind': cartype.carTypeKind})
    response = {'item_list': data, 'cartypelabel': cartypelabel.carTypeLabel}
    return HttpResponse(json.dumps(response))
