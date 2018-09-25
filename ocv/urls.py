from .views import OCV_View
from django.conf.urls import url

urlpatterns = [
    url(r'^$', OCV_View.as_view(), name='ocvCalc')
]
