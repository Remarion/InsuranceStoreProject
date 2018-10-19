# -*- coding: utf8 -*-

from django.shortcuts import render
from django.views import View
from .models import CarTypeSimple, CarTypeLabel, CarTypeMTSBU, Settlement
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .api import getUniPrice


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
    data = []
    if cartype_id != '100':
        cartypemtsbu = CarTypeMTSBU.objects.filter(carTypeSimple__id=cartype_id)
        cartypelabel = CarTypeLabel.objects.get(carTypeSimple__id=cartype_id)
        for cartype in cartypemtsbu:
            data.append({'id': cartype.id, 'carTypeKind': cartype.carTypeKind})
        response = {'item_list': data, 'cartypelabel': cartypelabel.carTypeLabel}
        return HttpResponse(json.dumps(response))
    else:
        return HttpResponse(json.dumps({'item_list': data}))

@csrf_exempt
def prices(request):
    if request.method == 'POST':
        setl = Settlement.objects.get(pk=int(request.POST['setl']))
        carType = CarTypeMTSBU.objects.get(pk=int(request.POST['group']))
        price = getUniPrice(setl=setl.settlementMTSBUCode, carType=carType.carTypeMTSBU)
        return HttpResponse(json.dumps({'price': price}))
    return HttpResponse(json.dumps({'price': '0'}))
