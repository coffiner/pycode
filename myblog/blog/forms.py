#_*_coding:utf-8_*_ 

from django import forms
from blog.models import Post, Category



class PostForm(forms.ModelForm):

	slug = forms.SlugField(max_length=50)
	class Meta:
		model = Post
		fields = ('title','slug','contents','category')

		widgets = {
			'contents':forms.Textarea(),
			# 'category':forms.ModelChoiceField(queryset=Category.objects.get())
		}