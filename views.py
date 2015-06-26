from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse

# Create your views here.

def home_view(request):
	t = loader.get_template("index.html")
	c = Context({})
	return HttpResponse(t.render(c))


def music_view(request):
	t = loader.get_template("music.html")
	c = Context({})
	return HttpResponse(t.render(c))


def about_view(request):
	t = loader.get_template("about.html")
	c = Context({})
	return HttpResponse(t.render(c))
