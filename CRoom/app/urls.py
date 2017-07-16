from django.conf.urls import patterns, url

from app.views import *

urlpatterns = patterns(
        url(r'^login$', UserLogin.as_view(), name='login'),
        url(r'^logout$', UserLogout.as_view(), name='logout'),
        url(r'^register$',UserReg.as_view(), name='register'),
        url(r'^profile$',.as_view(),name='profile'),
        url(r'^chatrooms$',.as_view(),name='manage_rooms'),
        url(r'^members$',.as_view(),name='manage_members'),
        url(r'^$',.as_view(),name='Chatroom'),
)