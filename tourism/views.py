# -*- coding: utf8 -*-
from django.shortcuts import render
from django.views import View
from ocv.models import CarTypeSimple, CarTypeLabel, CarTypeMTSBU, Settlement

# Create your views here.

class Tourism_View(View):
    def get(self, request):
        context = {'text': 'Hello'}
        return render(request, 'tourism/tourism.html', context)


