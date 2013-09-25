#coding:utf8
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import Post

class RSSFeed(Feed):
	title = "danpy5 news"
	link = "/"
	description = "Update on changes"

	def items(self):
		return Post.objects.order_by('-create_time')[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.contents_html




