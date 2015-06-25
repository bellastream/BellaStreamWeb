# coding=utf-8
#forms.py
from django import forms
from models import BlogComment


class CommentForm(forms.Form):
	name = forms.CharField(max_length=30, label='Name')
	email = forms.EmailField(required=False, label='Email')
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '8'}))

	def save_comment(self, post, is_owner=False):
		BlogComment.objects.create(post=post, author=self.cleaned_data['name'], email=self.cleaned_data['email'],
							   content=self.cleaned_data['content'], is_owner=is_owner)
