from django.conf.urls import patterns, include, url
from blog.feeds import RSSFeed

urlpatterns = patterns('',
	
	url(r'^$','blog.views.index'),
	url(r'^index/$','blog.views.index', name="blog_index"),
	url(r'^about/$', 'blog.views.about'),
	url(r'^reply/$', 'blog.views.reply'),
	url(r'^category/(?P<slug>[\w]+)/$', 'blog.views.category', name="blog_category"),
	# url(r'^post/(?P<title>[\w]+)/$','blog.views.post'),
	url(r'^archives/$', 'blog.views.archives', name="blog_archives"),
	url(r'^article/(?P<slug>[-\w]+)/$', 'blog.views.article', name= "blog_article"),


)

urlpatterns += patterns('',
    url(r'^feeds/$', RSSFeed(), name='blog_feed'),
)