from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^index/$', 'blog.views.index'),
    url(r'^login/$', 'blog.views.login_user'),
    url(r'^logout/$', 'blog.views.logout_user'),
    url(r'^regist/$', 'blog.views.sign_user'),
    url(r'^create_group/$', 'blog.views.create_group'),
    url(r'^add_group/(?P<id>\d+)/$', 'blog.views.apply_add'),
    url(r'^add_member/(?P<id>\d+)/$', 'blog.views.add_member'),
    url(r'^group/(?P<id>\d+)/$', 'blog.views.about_group'),
    url(r'^blog/(?P<id>\d+)/$', 'blog.views.blog_me'),
    url(r'^letter/(?P<id>\d+)/$', 'blog.views.letter'),
)
