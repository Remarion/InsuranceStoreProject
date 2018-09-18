# -*- coding: utf8 -*-
from django.shortcuts import render
from django.views import View

# Create your views here.

class Tourism_View(View):
    def get(self, request):
        context = {'text':'Main page'}
        return render(request, 'tourism.html', context)