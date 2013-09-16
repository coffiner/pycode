#_*_coding:utf-8_*_ 

from django.contrib import admin
from forum.models import User, Category, Post, Reply

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Reply)