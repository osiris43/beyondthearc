from django.conf.urls import patterns, url
from statistics import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<nba_game_id>\d+)/$', views.show, name='show'))
