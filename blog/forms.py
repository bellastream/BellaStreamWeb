# coding=utf-8
#forms.py
from django import forms


class CommentForm(forms.Form):
	name = forms.CharField(max_length=30, label='Name')
	email = forms.EmailField(required=False, label='Email')
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
