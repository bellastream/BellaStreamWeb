from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from django.http import Http404
from blog.models import BlogsPost
import os.path

# Create your views here.

def archivePage(request):
	posts = BlogsPost.objects.all()
	t = loader.get_template("blog.html")
	c = Context({'posts':posts})
	return HttpResponse(t.render(c))

def detailPage(request, id = ''):
	try:
		post = BlogsPost.objects.get(id = int(id))
	except Blog.DoesNotExist:
		raise Http404
	t = loader.get_template("details.html")
	c = Context({'post':post})
	return HttpResponse(t.render(c))
