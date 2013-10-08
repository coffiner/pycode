#_*_coding:utf-8_*_ 

from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink

class ProUser(models.Model):
	user = models.OneToOneField(User)
	headimg = models.URLField(blank=True, null=True, verbose_name=u'headimg')
	attention = models.ForeignKey(User, related_name="attention")

	def __unicode__(self):
		return self.user.username

class Letter(models.Model):
	letter = models.CharField(max_length=400, verbose_name=u'letter')
	post_user = models.ForeignKey(User, related_name=u'post')
	recv_user = models.ForeignKey(User, related_name=u'recv')

class Group(models.Model):
	groupname = models.CharField(max_length=50, unique=True, verbose_name=u'groupname')
	master = models.OneToOneField(User, related_name=u'master')
	isPublic = models.BooleanField(default=False, verbose_name=u'xiaozuzhuangtai')
	# slug = models.SlugField(unique=True, verbose_name=u'slug')
	create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'createtime')
	description = models.TextField(verbose_name=u'description')

	members = models.ManyToManyField(User, related_name=u'member')

	@permalink
	def get_absolute_url(self):
		return ('blog_group',None, {'slug': self.slug})

	def __unicode__(self):
		return self.groupname
