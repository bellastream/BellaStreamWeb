# -*- coding:utf-8 -*-
from django.template import loader, Context, RequestContext
from django.http import HttpResponse
from django.http import Http404
from django import forms
from django.core.paginator import Paginator
from blog.models import BlogPost, BlogComment, POST_TYPE
from blog.forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
import re

# Create your views here.

def archivePage(request):
	type = request.GET.get('type', '')
	if type in POST_TYPE:
		posts_list = BlogPost.objects.filter(type=type)
	else:
		posts_list = BlogPost.objects.all()

	pages = Paginator(posts_list, 5)
	page = int(request.GET.get('page', '1'))
	try:
		page_list = pages.page(page)
	except (EmptyPage, InvalidPage):
		page_list = pages.page(paginator.num_pages)

	t = loader.get_template("blog.html")
	c = Context({'posts': page_list})
	return HttpResponse(t.render(c))


def detailPage(request, id=''):
	try:
		post = BlogPost.objects.get(id=int(id))
	except BlogPost.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save_comment(post)

	form = CommentForm()
	comments = post.blogcomment_set.all()
	t = loader.get_template("details.html")
	c = RequestContext(request, {'post': post})
	c['comments'] = comments
	c['form'] = form
	return HttpResponse(t.render(c))


