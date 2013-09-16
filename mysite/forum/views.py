#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from forum.models import User, Category, Post, Reply
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
import hashlib 
import json

nav = 1

def index(request):
	category = Category.objects.all()
	post_list = Post.objects.order_by('-id').all()

	p = Paginator(post_list, 2) 
	page = request.GET.get('page')
	try:
		contacts = p.page(page)
	except PageNotAnInteger:
		contacts = p.page(1)
	except EmptyPage:
		contacts = p.page(p.num_pages)

	if request.session.get('user'):
		user = request.session['user']
	else:
		user = ''
	
	return render(request, 'index.html', {'post_list': post_list,
				'user': user,'category':category, 'contacts': contacts})	

def register(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		username = request.POST.get('username')
		passwd = request.POST.get('passwd')
		passwd = hashlib.sha1(email + passwd).hexdigest()
		headImg = request.FILES['headImg']
		user = User.objects.create(email=email, username=username, passwd=passwd, headimg=headImg)

		request.session['user'] = user
		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('register.html', {})

def login_user(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		passwd = request.POST.get('passwd')
		passwd = hashlib.sha1(email + passwd).hexdigest()
		try:
			user = User.objects.get(email=email, passwd=passwd)
			request.session['user'] = user
		except ObjectDoesNotExist:
			return HttpResponse('login.html',{})

		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('login.html',{})

def logout_user(request):
	request.session.clear()

	return HttpResponseRedirect('/index/')

def search(request):

	sear = request.GET.get('search')
	print 3
	post_list = Post.objects.filter(title__contains=sear)
	
	if post_list:
		return render(request, 'index.html',{'contacts':post_list,'user':request.session.get('user')})
	return HttpResponse('error')

def post(request):

	if request.session.get('user'):
		user = request.session['user']
		if request.method == 'POST':
			title = request.POST.get('title')
			content = request.POST.get('content')
			
			category = Category.objects.get(id=nav)
			try:
				Post.objects.create(title=title, content=content,user=user,category=category)
				return HttpResponseRedirect('/index/')
			except:
				return HttpResponse('post error')
	else:
		return HttpResponseRedirect('/login/')
	return render(request,'post.html',{'user': user})

def reply(request, id):
	
	post = Post.objects.get(id=id)
	post.count += 1
	post.save()
	if request.session.get('user'):
		user = request.session['user']
		if request.method == 'POST':
			content = request.POST['content']
			reply = post.reply_set.create(content=content, user=request.session['user'])
	else:
		user = ''
	reply_list = post.reply_set.all()
	return render(request, 'index.html', {'cur_post': post, 'reply_list': reply_list,
						"user": user})

def status(request, name):
	global nav
	nav = name
	category = Category.objects.get(id=nav)
	post_list = Post.objects.filter(category=name)

	p = Paginator(post_list, 2) 
	page = request.GET.get('page')
	try:
		contacts = p.page(page)
	except PageNotAnInteger:
		contacts = p.page(1)
	except EmptyPage:
		contacts = p.page(p.num_pages)


	return render(request, 'index.html', {'post_list':post_list, 'nav':category.name,'contacts':contacts,
					'user': request.session.get('user')})

def hot(request):
	hot = True
	post_list = Post.objects.order_by('-count').all()

	p = Paginator(post_list, 2) 
	page = request.GET.get('page')
	try:
		contacts = p.page(page)
	except PageNotAnInteger:
		contacts = p.page(1)
	except EmptyPage:
		contacts = p.page(p.num_pages)


	return render(request, 'index.html', {'post_list': post_list, 'user': request.session.get('user'),
	 					'hot':hot,'contacts':contacts})	

def field(request, id):
	isInfo = True

	return render(request, 'index.html', {'isInfo':isInfo,'user':request.session.get('user')})

def topic(request, id):
	isInfo = True
	isTopic = True
	user = User.objects.get(id=id)
	post_list = user.post_set.all()

	return render(request, 'index.html', {'isTopic':isTopic, 'isInfo':isInfo,'user':request.session.get('user'),
					'self_list':post_list})

def newPasswd(request, id):
	isInfo = True
	newPasswd = True
	user = User.objects.get(id=id)
	if request.method == 'POST':
		new = request.POST['npasswd']
		passwd = hashlib.sha1(user.email + new).hexdigest()
		user.passwd = passwd
		user.save()
		return HttpResponseRedirect('/index/')	
	return render(request,'index.html',{ 'isInfo':isInfo,'newPasswd':newPasswd,
					'user':request.session.get('user')})


