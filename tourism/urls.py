from .views import Tourism_View
from tourism import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', Tourism_View.as_view(), name='tourismCalc'),
]
