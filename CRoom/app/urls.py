from django.conf.urls import patterns, url
 
from chat import views
 
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^(?P\d+)/$', views.chat_room, name='chat_room'),
)