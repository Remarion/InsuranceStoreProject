# -*- coding: utf8 -*-
from django.shortcuts import render
from django.views import View
from .forms import CalculationOCVForm

# Create your views here.

class Index(View):
    def get(self, request):
        context = {'text':'Main page'}
        return render(request, 'basic.html', context)

class OCV_View(View):
    def get(self, request):
        form = CalculationOCVForm(request.POST)
        return render(request, 'ocv.html', {'form': form})



