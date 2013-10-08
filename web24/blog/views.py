#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User 
from blog.models  import Letter, Group 
from django.contrib.auth import login, logout, authenticate
import hashlib


def index(request):
	group_list = Group.objects.all()
	if request.user.is_authenticated():
		user = request.user 
		letter = user.recv.all()
		if letter:
			ishave = True
	return render(request,'index.html',{'group_list': group_list, 
				'user':request.user, 'ishave':ishave})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['passwd']
		password = hashlib.sha1(username + password).hexdigest()
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/index/')
		else:
			# return HttpResponse('%s,%s' % (username, password))
			return HttpResponse(user) 

	return render(request,'login.html',{})

def sign_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['passwd']
		password = hashlib.sha1(username + password).hexdigest()
		user = User.objects.create_user(username=username,email=email, 
						password=password)
		user.set_password(password)
		user.save()
		return HttpResponseRedirect('/index/')
		
	return render_to_response('regist.html',{},
				context_instance=RequestContext(request))

def create_group(request):
	if request.method == 'POST':
		if request.user.is_authenticated():
			user = request.user
			isPublic = request.POST.get('ispub')
			if isPublic == 'True':
				is_done = True
			else:
				is_done = False
			groupname = request.POST.get('groupname')
			groupdesc = request.POST.get('groupdesc')
			group = Group.objects.create(groupname=groupname,master=user,
				isPublic=is_done ,description=groupdesc)
			group.members.add(user)
			group.save()
			return HttpResponseRedirect('/index/')
	return render(request,'create_group.html',{'user':request.user})

def apply_add(request, id):
	group = Group.objects.get(id=id)
	if request.user.is_authenticated():
		user = request.user
		if user not in group.members.all():
			group.members.add(user)
			group.save()
			return HttpResponse('ok')
		return HttpResponse('this user is group master or group member')
	return HttpResponse('please login')

# def add_member(request, id):


def about_group(request, id):
	group = Group.objects.get(id=id)

	return render(request, 'about_group.html',{'group':group})


def blog_me(request, id):
	user = User.objects.get(id=id)

	return render(request, 'blog.html', {'me': request, 'user':user})

def letter(request, id):
	if request.user.is_authenticated():
		me = request.user
	user = User.objects.get(id=id)
	if request.method == 'POST':
		content = request.POST.get('letter')
		Letter.objects.create(letter=content,post_user=me, recv_user=user)
		return HttpResponse(' post done')
	return render(request, 'letter.html',{'user':user, 'me':me})

def logout_user(request):
	request.session.clear()
	return HttpResponseRedirect('/index/')