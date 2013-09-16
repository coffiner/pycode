#_*_coding:utf-8_*_ 

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
    url(r'^$', 'forum.views.index'),
    url(r'^index/$', 'forum.views.index'),
    url(r'^index/(?P<name>\w+)/$', 'forum.views.status'),
    url(r'^register/$', 'forum.views.register'),
    url(r'^login/$', 'forum.views.login_user'),
    url(r'^logout/$', 'forum.views.logout_user'),
    url(r'^search/$', 'forum.views.search'),
    url(r'^post/$', 'forum.views.post'),
    url(r'^post/(?P<id>\d+)/$', 'forum.views.reply'),
    url(r'^hot/$', 'forum.views.hot'),
    url(r'^field/(?P<id>\d+)/$', 'forum.views.field'),
    url(r'^topic/(?P<id>\d+)/$', 'forum.views.topic'),
    url(r'^newPasswd/(?P<id>\d+)/$', 'forum.views.newPasswd'),
)
