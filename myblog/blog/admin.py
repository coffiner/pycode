#_*_coding:utf-8_*_ 

from django.contrib import admin
from blog.models import Category, Post, Link

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']
	prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
	list_display = ['title','slug','counts','category','create_time']
	list_filter = ['title'] 
	prepopulated_fields = {'slug':('title',)}
	# yu tianchong

class LinkAdmin(admin.ModelAdmin):
	list_display = ['name','link']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Link,LinkAdmin)

