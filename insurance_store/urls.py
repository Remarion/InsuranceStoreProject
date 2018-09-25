# -*- coding: utf8 -*-

from django.contrib import admin
from django.conf.urls import url, include
from ocv.views import Index
#from django.urls import include, path


urlpatterns = [
     url(r'admin/', admin.site.urls),
     url(r'^$', Index.as_view(), name='mainPage'),
     url(r'^ocv/', include('ocv.urls')),
     url(r'^tourism/', include('tourism.urls'))
]
