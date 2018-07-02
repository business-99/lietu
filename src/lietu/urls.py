from django.conf.urls import url
from .views import DogInfoViews, DogListView, DogGroupView

app_name = "lietu"
urlpatterns = [
    url(r'^$', DogListView.as_view(), name='index'),
    url(r'^trace/$', DogInfoViews.as_view(), name='trace'),
    url(r'^group/(?P<pk>\d+)/$', DogGroupView.as_view(), name='group')
]
