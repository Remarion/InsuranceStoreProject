# -*- coding: utf8 -*-
from django.shortcuts import render
from django.views import View
from .forms import CalculationOCVForm


class Index(View):
    def get(self, request):
        context = {'text': 'Main page'}
        return render(request, 'basic.html', context)


class OCV_View(View):
    def get(self, request):
        if request.method == 'POST':
            form = CalculationOCVForm(request.POST)
        else:
            form = CalculationOCVForm()
        return render(request, 'ocv.html', {'form': form})