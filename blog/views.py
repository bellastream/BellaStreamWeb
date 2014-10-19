from django.shortcuts import render
from django.template import loader, Context,RequestContext
from django.http import HttpResponse
from django.http import Http404
from django import forms
from blog.models import BlogPost
from blog.models import BlogComment
from blog.forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
import os.path
import time

# Create your views here.

def archivePage(request):
	posts = BlogPost.objects.all()
	t = loader.get_template("blog.html")
	c = Context({'posts':posts})
	return HttpResponse(t.render(c))

def detailPage(request, id = ''):
	try:
		post = BlogPost.objects.get(id = int(id))
	except Blog.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():	  
			addComment(post,form, id)
	else:
		form = CommentForm()
	comments = post.blogcomment_set.all()
	t = loader.get_template("details.html")
	c = RequestContext(request,{'post':post})
	c['comments'] = comments
	c['form'] = form
	return HttpResponse(t.render(c))

def getTime():
	return time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
def addComment(post, form, id = ''):
		comment=BlogComment(post=post,author=form.cleaned_data['name'], email=form.cleaned_data['email'],body=form.cleaned_data['message'],timestamp=getTime())
		comment.save()
