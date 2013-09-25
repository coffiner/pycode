#_*_coding:utf-8_*_ 

from django.db import models
from django.db.models import permalink
from markdown import markdown

class Category(models.Model):
	#  分类表
	name = models.CharField(max_length=10,verbose_name=u"名称")
	slug = models.CharField(max_length=50, unique=True, verbose_name=u'Slug')

	def __unicode__(self):
		return self.name

	@permalink
	def get_absolute_url(self):
		return ('blog_category',None, {'slug':self.slug})

	class Meta:
		ordering = ['id']
		verbose_name_plural = verbose_name = u'分类'

class Post(models.Model):
	#  文章
	title = models.CharField(max_length=100,verbose_name=u'标题')
	slug = models.SlugField(max_length=50, unique=True, verbose_name=u'Slug')
	contents = models.TextField(verbose_name=u'内容')
	contents_html = models.TextField(blank=True, null=True)
	create_time = models.DateTimeField(auto_now=True,verbose_name=u"发表日期")
	allow_comment = models.BooleanField(default=False, verbose_name=u"允许评论")
	counts = models.IntegerField(default=0,verbose_name=u'点击数')

	category = models.ForeignKey(Category, verbose_name=u'分类')

	def __unicode__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('blog_article',None,{'slug':self.slug})

	def save(self):
		self.contents_html = markdown(self.contents, ['codehilite'])
		super(Post,self).save()

	class Meta:
		get_latest_by = 'create_time'
		ordering = ['-id']
		verbose_name_plural = verbose_name = u'文章'

class Link(models.Model):
	# friends Link 
	name = models.CharField(max_length=30, verbose_name=u"名称")
	link = models.URLField(max_length=100, verbose_name=u"链接")

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = verbose_name = u'链接'
