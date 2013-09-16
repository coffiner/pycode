#_*_coding:utf-8_*_ 

from django.db import models

class User(models.Model):
	email = models.EmailField(max_length=50, unique=True, verbose_name=u"Email")
	username = models.CharField(max_length=30, verbose_name=u"name")
	passwd = models.CharField(max_length=150,verbose_name=u"password")
	create_time = models.DateField(auto_now=True)
	headimg = models.FileField(upload_to="./headimg/",blank=True, null=True, verbose_name=u"headImg")

	def __unicode__(self):
		return self.email 

class Category(models.Model):
	name = models.CharField(max_length=50, unique=True, verbose_name=u"kongjian")
	description = models.TextField(verbose_name=u"miaoshu")
	logo = models.FileField(upload_to="./logo/", blank=True, null=True, verbose_name=u"logo")
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name=u"title")
	content = models.TextField(verbose_name=u"content")
	img = models.FileField(upload_to="./img/", blank=True, null=True, verbose_name=u"img")
	count = models.IntegerField(default=0,verbose_name=u"dianjishu")
	create_time = models.DateTimeField(auto_now=True)
	allow_comment = models.BooleanField(default=True)

	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)

	def __unicode__(self):
		return self.title
    

class Reply(models.Model):
	content = models.TextField(verbose_name=u"content")
	img = models.FileField(upload_to="./img/")
	create_time = models.DateTimeField(auto_now=True)

	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)

	
