#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import PostForm
from blog.models import Post, Category, Link




def common_response(reqeust):

	common = {
		'category_list' : Category.objects.all(),
		'link_list'		: Link.objects.all(),

	}
	return common

def index(request):
	post_list = Post.objects.all()

	paginator = Paginator(post_list,5)
	page = request.GET.get('page')

	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)

	data = {'contacts': contacts}
	data.update(common_response(request))

	return render(request,'index.html',data)

def category(request,slug):

	cur_category = get_object_or_404(Category,slug=slug)
	contacts = cur_category.post_set.all()
	data = {'contacts':contacts, 'category': cur_category}
	data.update(common_response(request))
	return render(request,'index.html',data)

def about(request):
	data = {'comments':True}
	data.update(common_response(request))
	return render_to_response('about.html', data)

def reply(request):
	data = {'comments':True}
	data.update(common_response(request))

	return render_to_response('reply.html', data)

def archives(request):
	post_list = Post.objects.order_by('-id').all()
	data = {'post_list':post_list}
	data.update(common_response(request))

	return render_to_response('archives.html', data)

def article(request,slug):

	post = Post.objects.get(slug=slug)
	data = {'post':post, 'comments':True}
	data.update(common_response(request))

	return render_to_response('article.html', data)

