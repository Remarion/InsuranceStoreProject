from .views import OCV_View
from django.conf.urls import url
from ocv import views

urlpatterns = [
    url(r'^$', OCV_View.as_view(), name='ocvCalc'),
    url(r'^(?P<cartype_id>[0-9]+)/$', views.index, name='ocvCalcFull'),
    url(r'^prices/$', views.prices, name='getPrices'),
]
