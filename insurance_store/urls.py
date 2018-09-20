# -*- coding: utf8 -*-
"""insurance_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from ocv.views import Index, OCV_View
from ocv import views
from tourism.views import Tourism_View

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name = 'main'),
    url(r'^ocv/', OCV_View.as_view(), name = 'calcOCV_new'),
    url(r'^tourism/', Tourism_View.as_view(), name = 'tourism'),
]
